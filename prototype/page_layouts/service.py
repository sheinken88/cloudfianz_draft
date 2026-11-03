"""One service architecture, with capability-specific copy and project evidence."""
import re
from page_layouts.service_cases import BRANDS, case_media
from page_layouts.service_heroes import hero_media

SERVICES = {
    'servicio-desarrollo-software': {
        'name': 'Desarrollo de software a medida',
        'application_icons': ['custom-quotes', 'custom-operations', 'custom-portals'],
        'cases': [('despegar', 'Desarrollo a medida · Cotización comercial'), ('revianz', 'Desarrollo a medida · Para Digifianz')],
    },
    'servicio-integracion-sistemas': {
        'name': 'Integración de sistemas',
        'cases': [('properix', 'Integración · HubSpot y Odoo'), ('escala24x7', 'Integración · Operación comercial')],
    },
    'servicio-automatizacion-procesos': {
        'name': 'Automatización de procesos',
        'cases': [('properix', 'Automatización · Facturación'), ('despegar', 'Automatización · Documentos comerciales')],
    },
}


def build_service(key, meta, intro, sections):
    service = SERVICES[key]

    def section(prefix):
        return next((title, copy) for title, copy in sections.items() if title.startswith(prefix))

    def paragraphs(copy):
        return re.findall(r'<p>.*?</p>', copy, re.S)

    def subsections(copy):
        parts = re.split(r'<h3>(.*?)</h3>', copy)
        return parts[0], [(parts[i], parts[i + 1]) for i in range(1, len(parts), 2)]

    needs_title, needs = section('Qué podemos')
    needs_intro, applications = subsections(needs)
    application_icons = service.get('application_icons', [])
    if application_icons and len(application_icons) != len(applications):
        raise ValueError(f'Application copy and icons differ for {key}')
    needs_class = ' service-needs--illustrated' if application_icons else ''
    application_columns = []
    for index, (title, copy) in enumerate(applications):
        description, example = paragraphs(copy)
        example = example.removeprefix('<p><strong>Ejemplo:</strong> ').removesuffix('</p>')
        heading = f'<h3>{title}</h3>'
        if application_icons:
            icon = application_icons[index]
            heading = f'<div class="application-heading"><img class="application-icon" src="/assets/icons/{icon}.svg" alt="" aria-hidden="true" width="64" height="64" loading="lazy" decoding="async">{heading}</div>'
        application_columns.append(f'<article class="service-application">{heading}<div class="application-description">{description}</div><div class="application-example"><p class="application-example-label">Por ejemplo</p><p>{example}</p></div></article>')

    projects_title, projects = section('Casos reales')
    projects_intro, projects = subsections(projects)
    if len(projects) != len(service['cases']):
        raise ValueError(f'Project copy and visual configuration differ for {key}')
    case_cards = []
    for (heading, copy), (case, category) in zip(projects, service['cases']):
        parts = paragraphs(copy)
        description = ''.join(parts[:-1])
        title = heading.split(': ', 1)[1]
        title = title[0].upper() + title[1:]
        link = re.search(r'<a [^>]+>.*?</a>', parts[-1]).group(0)
        link = link.replace('<a ', '<a class="case-button" ', 1)
        case_cards.append(f'''<article class="service-case" id="proyecto-{case}" aria-labelledby="{case}-service-title">
        <div class="service-case-copy">
          <div class="service-case-brandline">{BRANDS[case]}<p class="service-case-category">{category}</p></div>
          <h3 id="{case}-service-title">{title}</h3>
          <div class="service-case-description">{description}</div>
          <div class="service-case-actions">{link}</div>
        </div>
        {case_media(case)}
      </article>''')

    approach_title, approach = section('Cómo trabajamos')
    approach_intro, offers = subsections(approach)
    hints = ['Evaluar las alternativas', 'Definir el alcance', 'Construir y poner en uso', 'Acompañar la operación']
    approach_tabs, approach_panels = [], []
    for i, ((label, copy), hint) in enumerate(zip(offers, hints), 1):
        offer_parts = paragraphs(copy)
        title = re.sub(r'</?(?:p|strong)>', '', offer_parts[0])
        description = ''.join(offer_parts[1:-1])
        delivery = re.fullmatch(r'<p><strong>(.*?):</strong> (.*?)</p>', offer_parts[-1], re.S)
        delivery_label, delivery_copy = delivery.groups()
        delivery_copy = delivery_copy[0].upper() + delivery_copy[1:]
        approach_tabs.append(f'<button type="button" role="tab" id="approach-tab-{i}" aria-controls="approach-panel-{i}" aria-selected="{str(i == 1).lower()}" tabindex="{0 if i == 1 else -1}"><span class="approach-tab-name">{label}</span><span class="approach-tab-hint">{hint}</span></button>')
        approach_panels.append(f'<div class="approach-panel" id="approach-panel-{i}" role="tabpanel" aria-labelledby="approach-tab-{i}" tabindex="0"><h3>{title}</h3><div class="approach-panel-body"><div class="approach-step-copy">{description}</div><aside class="approach-delivery" aria-labelledby="approach-delivery-{i}"><h4 id="approach-delivery-{i}">{delivery_label}</h4><p>{delivery_copy}</p></aside></div></div>')

    faq_title, faq = section('Preguntas frecuentes')
    _, questions = subsections(faq)
    faqs = ''.join(f'<details name="service-questions"{" open" if i == 0 else ""}><summary>{question}<span class="plus" aria-hidden="true"></span></summary>{answer}</details>' for i, (question, answer) in enumerate(questions))
    cta_title, cta = section('Hablemos')
    cta_context, cta_reassurance = paragraphs(cta)
    hero_project = hero_media(key)
    return f'''
<section class="service-hero">
  <div class="container">
    <nav class="breadcrumbs" aria-label="Ubicación"><ol><li><a href="/es">Inicio</a></li><li><a href="/es#soluciones">Soluciones</a></li><li aria-current="page">{service['name']}</li></ol></nav>
    <div class="service-hero-grid service-hero-grid--project">
      <div class="service-hero-copy"><h1>{meta['H1']}</h1></div>{hero_project}
      <div class="service-hero-intro">{paragraphs(intro)[0]}<div class="page-actions"><a class="button button-dark" href="/es/contacto">Contanos qué necesitás</a><a class="text-link" href="#proyectos">Ver proyectos reales</a></div></div>
    </div>
  </div>
</section>
<section class="container service-needs page-section{needs_class}" aria-labelledby="needs-heading">
  <div class="service-section-intro"><h2 id="needs-heading">{needs_title}</h2>{needs_intro}</div>
  <div class="service-applications">{''.join(application_columns)}</div>
</section>
<section class="service-projects page-section" id="proyectos" aria-labelledby="projects-heading">
  <div class="container">
    <div class="service-section-intro service-projects-intro"><h2 id="projects-heading">{projects_title}</h2>{projects_intro}</div>
    <div class="service-case-list">{''.join(case_cards)}</div>
    <div class="service-portfolio-link"><a class="text-link" href="#indice-casos" data-content="indice-casos">Ver todos los casos</a></div>
  </div>
</section>
<section class="container page-section service-approach" id="como-abordamos" aria-labelledby="approach-heading">
  <div class="service-section-intro"><h2 id="approach-heading">{approach_title}</h2>{approach_intro}</div>
  <div class="service-process" data-tabs data-progressive-tabs>
    <div class="approach-tabs" role="tablist" aria-label="Modalidades de trabajo" hidden>{''.join(approach_tabs)}</div>
    <div class="approach-panels">{''.join(approach_panels)}</div>
  </div>
</section>
<section class="container faq service-faq page-section" id="preguntas-frecuentes" aria-labelledby="questions-heading"><div class="section-intro"><h2 id="questions-heading">{faq_title}</h2></div><div class="faq-list">{faqs}</div></section>
<section class="page-contact service-closing" id="conversemos" aria-labelledby="next-title"><div class="container service-closing-inner"><div class="service-closing-heading"><h2 id="next-title">{cta_title}</h2><div class="service-closing-reassurance">{cta_reassurance}</div></div><div class="service-closing-action">{cta_context}<a class="button" href="/es/contacto">Contanos qué necesitás</a></div></div></section>
'''
