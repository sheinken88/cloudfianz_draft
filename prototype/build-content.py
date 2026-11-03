"""Prepare the approved copy for the prototype's plain content reader.

Usage: python3 prototype/build-content.py [path/to/content]
This does not generate or style the future service and case pages.
"""
import html
import json
from pathlib import Path
import re
import sys

default_source = Path(__file__).resolve().parent / "content"
source = Path(sys.argv[1]) if len(sys.argv) > 1 else default_source
files = sorted(source.glob("servicio-*.md")) + sorted(source.glob("caso-*.md")) + [source / "indice-casos.md"] + sorted(source.glob("pagina-*.md"))
known = {path.stem for path in files}
routes = json.loads((Path(__file__).resolve().parent / "page-routes.json").read_text())


def inline(text):
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)

    def link(match):
        label, target = match.groups()
        key = Path(target).stem
        if key in routes:
            return f'<a href="{routes[key]}">{label}</a>'
        if key in known:
            return f'<a href="#{key}" data-content="{key}">{label}</a>'
        if target.startswith("https://"):
            return f'<a href="{target}" target="_blank" rel="noopener noreferrer">{label}</a>'
        return label

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, text)


contents = {}
for path in files:
    text = path.read_text()
    title = re.search(r"^\*\*H1:\*\*\s*(.+)$", text, re.M)
    title = title.group(1) if title else text.splitlines()[0].removeprefix("# ")
    text = text.split("## Apertura", 1)[-1].split("## Notas para diseño", 1)[0]
    blocks = [f'<h1 id="reader-title">{html.escape(title)}</h1>']
    for paragraph in re.split(r"\n\s*\n", text.strip()):
        paragraph = paragraph.strip()
        if not paragraph or paragraph.startswith(("**H1:", "**Botón", "**CTA", "**Enlace", "**Alternativa", "**URL", "**Title", "**Meta", "Versión ")):
            continue
        if paragraph.startswith("**Texto de contexto:"):
            blocks.insert(0, '<p class="reader-context">' + inline(paragraph.split("**", 2)[-1].strip()) + "</p>")
        elif paragraph.startswith("**Título:"):
            blocks.append("<h3>" + inline(paragraph.split("**", 2)[-1].strip()) + "</h3>")
        elif paragraph.startswith("### "):
            blocks.append("<h3>" + inline(paragraph[4:]) + "</h3>")
        elif paragraph.startswith("## "):
            blocks.append("<h2>" + inline(paragraph[3:]) + "</h2>")
        elif paragraph.startswith("- "):
            blocks.append("<ul>" + "".join("<li>" + inline(line[2:]) + "</li>" for line in paragraph.splitlines() if line.startswith("- ")) + "</ul>")
        else:
            blocks.append("<p>" + inline(paragraph.replace("\n", " ")) + "</p>")
    blocks.append('<div class="reader-bottom"><a class="button" href="/es/contacto">Hablemos de tu negocio </a></div>')
    contents[path.stem] = "\n".join(blocks)

target = Path(__file__).resolve().parent / "dist/content.json"
target.write_text(json.dumps(contents, ensure_ascii=False, indent=2) + "\n")
print(f"Prepared {len(contents)} approved texts in {target}")
