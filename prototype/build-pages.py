"""Build the local homepage and standalone pages from current copy."""
import html
import json
from pathlib import Path
import re
import runpy

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'
runpy.run_path(str(ROOT / 'build-content.py'))
contents = json.loads((DIST / 'content.json').read_text())
routes = json.loads((ROOT / 'page-routes.json').read_text())
from page_layouts.revianz_mockups import mockup

home = (ROOT / 'templates/home.html').read_text()
home = home.replace('<!-- REVIANZ_HOME_PREVIEW -->', mockup(
    'margin', 'Vista ilustrativa del producto. Datos de ejemplo.',
    'home-case-media home-rv-preview',
))


def absolute_assets(text):
    return re.sub(r'((?:src|href)=")((?:assets/|styles\.css|app\.js)[^"]*)', r'\1/\2', text)


def native_links(text):
    for key, route in routes.items():
        text = text.replace(f'href="#{key}" data-content="{key}"', f'href="{route}"')
    return text


home = native_links(absolute_assets(home))
home = home.replace('</head>', '<link rel="canonical" href="https://cloudfianz.com/es">\n</head>')
(DIST / 'index.html').write_text(home)
header = re.search(r'<header class="site-header">.*?</header>', home, re.S).group()
footer = re.search(r'<footer class="site-footer">.*?</footer>', home, re.S).group()
dialogs = re.search(r'<dialog id="reader-dialog".*?</dialog>\s*<dialog id="info-dialog".*?</dialog>', home, re.S).group()


def home_links(text):
    return re.sub(r'href="#(inicio|soluciones|casos|como-trabajamos|contacto)"', r'href="/es#\1"', text)


header, footer = home_links(header), home_links(footer)


def document(key):
    source = (ROOT / 'content' / f'{key}.md').read_text()
    meta = {name: re.search(rf'^\*\*{name}:\*\*\s*(.+)$', source, re.M).group(1).strip()
            for name in ['Title', 'Meta description', 'H1']}
    rendered = contents[key].split('<div class="reader-bottom">')[0]
    rendered = re.sub(r'^.*?</h1>\s*', '', rendered, count=1, flags=re.S)
    pieces = re.split(r'<h2>(.*?)</h2>', rendered)
    sections = {pieces[i]: pieces[i+1].strip() for i in range(1, len(pieces), 2)}
    return meta, pieces[0].strip(), sections


def page(key, body, kind):
    meta, _, _ = document(key)
    title, description = html.escape(meta['Title'], quote=True), html.escape(meta['Meta description'], quote=True)
    canonical = 'https://cloudfianz.com' + routes[key]
    page_styles = {'case-page': 'case-page.css', 'service-page': 'service-page.css', 'revianz-page': 'revianz-page.css'}
    extra_css = f'<link rel="stylesheet" href="/{page_styles[kind]}">'
    if kind == 'revianz-page' or key == 'servicio-desarrollo-software':
        extra_css += '<link rel="stylesheet" href="/revianz-mockups.css">'
    return f'''<!doctype html>
<html lang="es-AR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex, nofollow"><meta name="theme-color" content="#0B1D3A">
<title>{title}</title><meta name="description" content="{description}"><link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{description}"><meta property="og:type" content="website"><meta property="og:url" content="{canonical}"><meta property="og:locale" content="es_AR">
<link rel="icon" href="/assets/brand/cloudfianz-symbol.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;450;500;550;600;650;700&family=Manrope:wght@400;500;600;650;700;750;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css"><link rel="stylesheet" href="/pages.css">{extra_css}<script src="/app.js" defer></script></head>
<body class="inner-page {kind}"><a class="skip-link" href="#principal">Ir al contenido</a>{header}<main id="principal">{body}</main>{footer}{dialogs}</body></html>'''


from page_layouts.service import build_service

from page_layouts.case import build_case

meta, intro, sections = document('caso-despegar')
case_body = build_case(meta, intro, sections, routes)

from page_layouts.revianz import build_revianz

meta, intro, sections = document('caso-revianz')
revianz_body = build_revianz(meta, intro, sections, routes)

pages = [('caso-despegar', case_body, 'case-page'), ('caso-revianz', revianz_body, 'revianz-page')]
for key in ['servicio-desarrollo-software', 'servicio-integracion-sistemas', 'servicio-automatizacion-procesos']:
    meta, intro, sections = document(key)
    pages.append((key, build_service(key, meta, intro, sections), 'service-page'))

for key, body, kind in pages:
    output = DIST / routes[key].lstrip('/') / 'index.html'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(page(key, body, kind))
print(f'Built homepage and {len(pages)} standalone pages.')
