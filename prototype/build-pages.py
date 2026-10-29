"""Build the local homepage and the first two standalone pages from current copy."""
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
home = (ROOT / 'templates/home.html').read_text()


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


def section(sections, prefix):
    return next((name, text) for name, text in sections.items() if name.startswith(prefix))


def paragraph_list(fragment):
    return re.findall(r'<p>.*?</p>', fragment, re.S)


def breadcrumbs(label, parent='Soluciones', target='/es#soluciones'):
    return f'<nav class="breadcrumbs" aria-label="Ubicación"><ol><li><a href="/es">Inicio</a></li><li><a href="{target}">{parent}</a></li><li aria-current="page">{label}</li></ol></nav>'


def contact(title, body):
    return f'''<section class="page-contact" aria-labelledby="next-title"><div class="container page-contact-inner"><div><h2 id="next-title">{title}</h2>{body}</div><div class="page-contact-actions"><a class="button button-dark" href="/es#contacto">Hablemos de tu negocio</a><a class="text-link" href="/es#consulta">Prefiero enviar una consulta</a></div></div></section>'''


def page(key, body, kind):
    meta, _, _ = document(key)
    title, description = html.escape(meta['Title'], quote=True), html.escape(meta['Meta description'], quote=True)
    canonical = 'https://cloudfianz.com' + routes[key]
    return f'''<!doctype html>
<html lang="es-AR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex, nofollow"><meta name="theme-color" content="#0B1D3A">
<title>{title}</title><meta name="description" content="{description}"><link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{description}"><meta property="og:type" content="website"><meta property="og:url" content="{canonical}"><meta property="og:locale" content="es_AR">
<link rel="icon" href="/assets/brand/cloudfianz-symbol.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;450;500;550;600;650;700&family=Manrope:wght@400;500;600;650;700;750;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css"><link rel="stylesheet" href="/pages.css"><script src="/app.js" defer></script></head>
<body class="inner-page {kind}"><a class="skip-link" href="#principal">Ir al contenido</a>{header}<main id="principal">{body}</main>{footer}{dialogs}</body></html>'''


meta, intro, sections = document('servicio-desarrollo-software')
needs_title, needs = section(sections, 'Cuando tus herramientas')
needs_parts = re.split(r'<h3>(.*?)</h3>', needs)
need_rows = ''.join(f'<article><h3>{needs_parts[i]}</h3><div>{needs_parts[i+1]}</div></article>' for i in range(1, len(needs_parts), 2))
choice_title, choice = section(sections, 'Elegimos')
delivery_title, delivery = section(sections, 'Una primera')
stages_title, stages = section(sections, 'Podés empezar')
stage_paragraphs = paragraph_list(stages)
stage_tabs, stage_panels = [], []
for i, entry in enumerate(stage_paragraphs[:4]):
    name, description = re.match(r'<p><strong>(.*?)\.</strong>\s*(.*?)</p>', entry, re.S).groups()
    stage_tabs.append(f'<button id="service-tab-{i}" role="tab" aria-selected="{str(i == 0).lower()}" aria-controls="service-stage-{i}" tabindex="{0 if i == 0 else -1}">{name}</button>')
    stage_panels.append(f'<div id="service-stage-{i}" class="service-stage-panel" role="tabpanel" aria-labelledby="service-tab-{i}" tabindex="0" {"hidden" if i else ""}><h3>{name}</h3><p>{description}</p></div>')
faq_title, faq = section(sections, 'Antes de empezar')
faq_parts = re.split(r'<h3>(.*?)</h3>', faq)
faqs = ''.join(f'<details><summary>{faq_parts[i]}<span class="plus" aria-hidden="true"></span></summary>{faq_parts[i+1]}</details>' for i in range(1, len(faq_parts), 2))
_, backing = section(sections, 'El respaldo')
cta_title, cta = section(sections, '¿Qué necesita')
projects_title, projects = section(sections, 'Proyectos')
project_parts = re.split(r'<h3>(.*?)</h3>', projects)
project_copy = [(project_parts[i], project_parts[i+1]) for i in range(1, len(project_parts), 2)]
other_projects = ''.join(f'<article><h3>{title}</h3>{copy}</article>' for title, copy in project_copy[1:])

service_body = f'''
<section class="service-opening"><div class="container">{breadcrumbs('Desarrollo de software a medida')}<div class="service-opening-grid"><div class="opening-copy"><p class="page-kicker">Desarrollo de software a medida</p><h1>{meta['H1']}</h1>{paragraph_list(intro)[0]}<div class="page-actions"><a class="button button-dark" href="/es#contacto">Hablemos de tu negocio</a><a class="text-link" href="#proyectos">Ver proyectos reales</a></div></div><figure class="service-visual"><div class="service-visual-head"><img src="/assets/brand/despegar-digifianz.png" alt="Despegar" width="180" height="52"><span>Software en uso</span></div><div class="service-screen"><img src="/assets/projects/despegar-cotizador.png" alt="Cotizador real de Despegar con las reglas de presupuesto, marcas y países integradas." width="1600" height="869" fetchpriority="high"></div><figcaption>Un cotizador con las reglas de Despegar, conectado con HubSpot.</figcaption><a class="text-link" href="{routes['caso-despegar']}">Conocé el proyecto</a></figure></div></div></section>
<section class="container service-needs page-section" aria-labelledby="needs-heading"><div class="service-section-intro"><h2 id="needs-heading">{needs_title}</h2>{needs_parts[0]}</div><div class="application-rows">{need_rows}</div></section>
<section class="service-projects page-section" id="proyectos" aria-labelledby="projects-heading"><div class="container"><h2 id="projects-heading">{projects_title}</h2><article class="service-feature"><figure><img src="/assets/projects/despegar-distribucion.png" alt="Distribución del presupuesto en el cotizador de Despegar." width="1600" height="775" loading="lazy"><figcaption>Captura del proyecto publicada por Digifianz.</figcaption></figure><div><img class="service-feature-logo" src="/assets/brand/despegar-digifianz.png" alt="Despegar" width="180" height="52" loading="lazy"><h3>{project_copy[0][0]}</h3>{project_copy[0][1]}</div></article><div class="related-projects">{other_projects}</div></div></section>
<section class="container page-section decision-section"><div><h2>{choice_title}</h2></div><div class="page-prose">{choice}</div></section>
<section class="delivery-section page-section"><div class="container delivery-grid"><h2>{delivery_title}</h2><div class="page-prose">{delivery}</div></div></section>
<section class="container page-section service-engagement" data-tabs aria-labelledby="engagement-heading"><div class="service-section-intro"><h2 id="engagement-heading">{stages_title}</h2>{stage_paragraphs[-1]}</div><div class="stage-tabs" role="tablist" aria-label="Formas de contratar el servicio">{''.join(stage_tabs)}</div>{''.join(stage_panels)}</section>
<section class="container faq page-section" aria-labelledby="questions-heading"><div class="section-intro"><h2 id="questions-heading">{faq_title}</h2></div><div class="faq-list">{faqs}</div></section>
<section class="service-backing"><div class="container"><img src="/assets/brand/digifianz-official.svg" alt="Digifianz" width="226" height="80" loading="lazy"><div>{backing}</div></div></section>
{contact(cta_title, cta)}'''

meta, intro, sections = document('caso-despegar')
case_sections = [('problema', 'El problema'), ('diseno', 'Diseñar'), ('solucion', 'La solución'), ('resultados', 'Resultados'), ('evolucion', 'Evolución')]
case_nav = [('problema', 'El desafío'), ('diseno', 'El enfoque'), ('solucion', 'La solución'), ('resultados', 'Los resultados')]
story = []
for slug, prefix in case_sections:
    title, copy = section(sections, prefix)
    if slug == 'solucion':
        copy += '<figure class="case-detail-image"><a href="/assets/projects/despegar-distribucion.png" target="_blank" rel="noopener" aria-label="Abrir captura del cotizador en tamaño completo"><img src="/assets/projects/despegar-distribucion.png" alt="Cotizador de Despegar: distribución del presupuesto por marca y país y selección de productos." width="1600" height="775" loading="lazy"></a><figcaption>La distribución del presupuesto y el catálogo se reúnen en una misma herramienta. <a href="/assets/projects/despegar-distribucion.png" target="_blank" rel="noopener">Ver captura completa</a></figcaption></figure>'
    story.append(f'<section class="case-story-section" id="{slug}" aria-labelledby="{slug}-title"><h2 id="{slug}-title">{title}</h2><div class="page-prose">{copy}</div></section>')
cta_title, cta = section(sections, '¿Tus cotizaciones')
case_body = f'''
<section class="case-opening container">{breadcrumbs('Despegar Ads', 'Casos', '/es#casos')}<img class="case-opening-logo" src="/assets/brand/despegar-digifianz.png" alt="Despegar" width="180" height="52"><h1>{meta['H1']}</h1><div class="case-intro-grid"><div class="case-opening-summary">{paragraph_list(intro)[0]}</div><dl class="case-facts"><div><dt>El negocio</dt><dd>Publicidad digital en Latinoamérica</dd></div><div><dt>La solución</dt><dd>Cotizador a medida conectado a HubSpot</dd></div><div><dt>El cambio</dt><dd>De horas de preparación a cotizaciones en minutos</dd></div></dl></div><figure class="case-cover"><div><img src="/assets/projects/despegar-cotizador.png" alt="Vista real del cotizador de Despegar con presupuesto y selección de productos para la propuesta comercial." width="1600" height="869" fetchpriority="high"></div><figcaption>Captura real del proyecto, publicada por Digifianz. Los campos difuminados pertenecen a la imagen original.</figcaption></figure></section>
<nav class="case-index" aria-label="En este caso"><div class="container"><span>En este caso</span>{''.join(f'<a href="#{slug}">{name}</a>' for slug,name in case_nav)}</div></nav>
<div class="container case-story"><div class="case-context"><h2>El contexto de Despegar Ads</h2><div class="page-prose">{paragraph_list(intro)[1]}</div></div>{''.join(story)}</div>
{contact(cta_title, cta)}'''

for key, body, kind in [('servicio-desarrollo-software', service_body, 'service-page'), ('caso-despegar', case_body, 'case-page')]:
    output = DIST / routes[key].lstrip('/') / 'index.html'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(page(key, body, kind))
print('Built homepage and 2 standalone pages.')
