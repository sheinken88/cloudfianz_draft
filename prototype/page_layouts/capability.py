"""Native integration and automation pages, using the approved service copy."""
import re


def build_capability(key, meta, intro, sections):
    integration = key == 'servicio-integracion-sistemas'
    name = 'Integración de sistemas' if integration else 'Automatización de procesos'

    def section(prefix):
        return next((title, copy) for title, copy in sections.items() if title.startswith(prefix))

    def paragraphs(copy):
        return re.findall(r'<p>.*?</p>', copy, re.S)

    def parts(copy):
        chunks = re.split(r'<h3>(.*?)</h3>', copy)
        return chunks[0], [(chunks[i], chunks[i+1]) for i in range(1, len(chunks), 2)]

    needs_title, needs = section('Cuando cada' if integration else 'Qué puede mejorar')
    needs_intro, needs_items = parts(needs)
    needs_html = ''.join(f'<article><h3>{title}</h3>{copy}</article>' for title, copy in needs_items)
    principle_title, principle = section('La conexión' if integration else 'Empezamos por')
    controls_title, controls = section('Qué definimos' if integration else 'Controles y')
    offers_title, offers = section('Un alcance' if integration else 'Podés avanzar')
    faq_title, faq = section('Antes de conectar' if integration else 'Antes de automatizar')
    _, questions = parts(faq)
    faqs = ''.join(f'<details name="capability-faq"><summary>{question}<span class="plus" aria-hidden="true"></span></summary>{answer}</details>' for question, answer in questions)
    backing_title, backing = section('Una unidad' if integration else 'El respaldo')
    cta_title, cta = list(sections.items())[-1]

    if integration:
        case_title, case_copy = section('ConsorcioAbierto:')
        secondary_title, secondary_copy = section('Escala24x7:')
        proof = f'''<article class="capability-feature"><div><img src="/assets/brand/consorcio-abierto-white.png" alt="ConsorcioAbierto" width="250" height="70" loading="lazy"><h3>Más de 15.000 facturas mensuales.</h3><p>HubSpot y Odoo, conectados.</p></div><div>{case_copy}</div></article><article class="capability-secondary"><h3>{secondary_title}</h3><div>{secondary_copy}</div></article>'''
        diagram = '''<div class="capability-flow" aria-label="Ejemplo de integración: de una membresía en HubSpot a su facturación en Odoo"><p class="capability-flow-caption">Un recorrido real: ConsorcioAbierto</p><ol><li><span>HubSpot</span><strong>Membresías y condiciones comerciales</strong></li><li><span>Reglas de integración</span><strong>Períodos, descuentos y país</strong></li><li><span>Odoo</span><strong>Facturación conectada con la venta</strong></li></ol><a class="text-link" href="#caso-properix" data-content="caso-properix">Conocé el caso</a></div>'''
        measurement = ''
    else:
        _, examples = section('Ejemplos de aplicación')
        _, stories = parts(examples)
        proof = '<div class="capability-examples">' + ''.join(f'<article><h3>{title}</h3>{copy}</article>' for title, copy in stories) + '</div>'
        diagram = '''<div class="capability-flow" aria-label="Esquema de un proceso automatizado con revisión humana"><p class="capability-flow-caption">Cada paso, con una regla y un responsable</p><ol><li><span>Un evento inicia el proceso</span><strong>Una venta, una solicitud o un cambio</strong></li><li><span>Se aplican las reglas acordadas</span><strong>Datos, acciones y validaciones</strong></li><li><span>El equipo interviene donde hace falta</span><strong>Revisión, aprobación y seguimiento</strong></li></ol><a class="text-link" href="#proyectos">Ver ejemplos reales</a></div>'''
        measure_title, measure_copy = section('Una mejora que')
        measurement = f'<div class="capability-measure"><h3>{measure_title}</h3><div>{measure_copy}</div></div>'

    return f'''
<section class="capability-opening"><div class="container">
  <nav class="breadcrumbs" aria-label="Ubicación"><ol><li><a href="/es">Inicio</a></li><li><a href="/es#soluciones">Soluciones</a></li><li aria-current="page">{name}</li></ol></nav>
  <div class="capability-hero"><div><h1>{meta['H1']}</h1>{paragraphs(intro)[0]}<div class="page-actions"><a class="button button-dark" href="/es#consulta">Contanos qué necesitás</a><a class="text-link" href="#proyectos">Ver proyectos reales</a></div></div>{diagram}</div>
</div></section>
<section class="container page-section capability-needs" aria-labelledby="needs-title"><div class="capability-intro"><h2 id="needs-title">{needs_title}</h2><div>{needs_intro}</div></div><div class="capability-needs-grid">{needs_html}</div></section>
<section class="capability-proof page-section" id="proyectos" aria-labelledby="proof-title"><div class="container"><h2 id="proof-title">Así funciona en negocios reales.</h2>{proof}</div></section>
<section class="container page-section capability-approach" aria-labelledby="approach-title"><div class="capability-method"><div><h2 id="approach-title">{principle_title}</h2><div class="page-prose">{principle}</div></div><div class="capability-controls"><h3>{controls_title}</h3><div class="page-prose">{controls}</div></div></div>{measurement}<div class="capability-engagement"><h3>{offers_title}</h3><div class="page-prose">{offers}</div></div></section>
<section class="capability-backing"><div class="container"><img src="/assets/brand/digifianz-official.svg" alt="Digifianz" width="226" height="80" loading="lazy"><div><h2>Experiencia de negocio detrás de la tecnología.</h2>{backing}<a class="text-link light-link" href="https://www.digifianz.com/es/" target="_blank" rel="noopener noreferrer">Conocé la empresa</a></div></div></section>
<section class="container page-section capability-faq" id="preguntas-frecuentes" aria-labelledby="faq-title"><h2 id="faq-title">{faq_title}</h2><div class="faq-list">{faqs}</div></section>
<section class="capability-closing" id="conversemos" aria-labelledby="closing-title"><div class="container"><h2 id="closing-title">{cta_title}</h2><div>{cta}<a class="button" href="/es#consulta">Contanos qué necesitás</a></div></div></section>
'''
