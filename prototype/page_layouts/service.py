"""Service journey: value, fit, evidence, approach, offers and confidence."""
import re
from page_layouts.revianz_mockups import mockup


def build_service(meta, intro, sections, routes):
    def section(prefix):
        return next((title, copy) for title, copy in sections.items() if title.startswith(prefix))

    def paragraphs(copy):
        return re.findall(r'<p>.*?</p>', copy, re.S)

    def subsections(copy):
        parts = re.split(r'<h3>(.*?)</h3>', copy)
        return parts[0], [(parts[i], parts[i + 1]) for i in range(1, len(parts), 2)]

    needs_title, needs = section('Cuando tus herramientas')
    parts = re.split(r'<h3>(.*?)</h3>', needs)
    needs_intro = parts[0]
    applications = [(parts[i], parts[i + 1]) for i in range(1, len(parts), 2)]
    application_columns = []
    for title, copy in applications:
        description, example = paragraphs(copy)
        example = example.removeprefix('<p><strong>Ejemplo:</strong> ').removesuffix('</p>')
        application_columns.append(f'<article class="service-application"><h3>{title}</h3><div class="application-description">{description}</div><div class="application-example"><p class="application-example-label">Por ejemplo</p><p>{example}</p></div></article>')
    projects_title, projects = section('Nuestro trabajo')
    projects_intro, projects = subsections(projects)
    revianz, photonix = projects
    revianz_paragraphs = paragraphs(revianz[1])
    revianz_copy = ''.join(revianz_paragraphs[:-1])
    _, revianz_description = revianz[0].split(': ', 1)
    revianz_title = revianz_description[0].upper() + revianz_description[1:]
    photonix_paragraphs = paragraphs(photonix[1])
    photonix_copy = ''.join(photonix_paragraphs[:-1])
    _, photonix_description = photonix[0].split(': ', 1)
    photonix_title = photonix_description[0].upper() + photonix_description[1:]
    photonix_link = re.search(r'<a ([^>]+)>(.*?)</a>', photonix_paragraphs[-1]).group(0)
    photonix_link = photonix_link.replace('<a ', '<a class="case-button" ', 1)
    approach_title, approach = section('Cómo podés')
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
    faq_title, faq = section('Antes de empezar')
    parts = re.split(r'<h3>(.*?)</h3>', faq)
    faqs = ''.join(f'<details name="service-questions"{" open" if i == 1 else ""}><summary>{parts[i]}<span class="plus" aria-hidden="true"></span></summary>{parts[i + 1]}</details>' for i in range(1, len(parts), 2))
    backing_title, backing = section('Experiencia de negocio')
    cta_title, cta = section('Hablemos de lo que')
    cta_context, cta_reassurance = paragraphs(cta)
    return f'''
<section class="service-hero">
  <div class="container">
    <nav class="breadcrumbs" aria-label="Ubicación"><ol><li><a href="/es">Inicio</a></li><li><a href="/es#soluciones">Soluciones</a></li><li aria-current="page">Desarrollo de software a medida</li></ol></nav>
    <div class="service-hero-grid">
      <div class="service-hero-copy">
        <h1>{meta['H1']}</h1>
        {paragraphs(intro)[0]}
        <div class="page-actions"><a class="button button-dark" href="/es#contacto">Hablemos de tu negocio</a><a class="text-link" href="#proyectos">Ver proyectos reales</a></div>
      </div>
      <figure class="service-product">
        <a class="service-product-image" href="/assets/projects/despegar-cotizador-original.png" target="_blank" rel="noopener" aria-label="Ampliar captura original del cotizador de Despegar (nueva pestaña)"><img src="/assets/projects/despegar-cotizador-original.png" alt="Cotizador de Despegar con presupuesto, distribución por marca y país y paneles de productos en una campaña de prueba." width="1633" height="887" fetchpriority="high" decoding="async"></a>
        <figcaption><img src="/assets/brand/despegar-digifianz.png" alt="Despegar" width="180" height="52"><div><p>Cotizador a medida integrado con HubSpot.</p><a class="text-link" href="{routes['caso-despegar']}">Conocé el caso Despegar</a></div></figcaption>
      </figure>
    </div>
  </div>
</section>
<section class="container service-needs page-section" aria-labelledby="needs-heading">
  <div class="service-section-intro"><h2 id="needs-heading">{needs_title}</h2>{needs_intro}</div>
  <div class="service-applications">{''.join(application_columns)}</div>
</section>
<section class="service-projects page-section" id="proyectos" aria-labelledby="projects-heading">
  <div class="container">
    <div class="service-section-intro service-projects-intro"><h2 id="projects-heading">{projects_title}</h2>{projects_intro}</div>
    <div class="service-case-list">
      <article class="service-case" id="proyecto-revianz" aria-labelledby="revianz-service-title">
        <div class="service-case-copy">
          <div class="service-case-brandline">
            <span class="service-rv-logo" role="img" aria-label="Revianz"><span class="service-rv-logo-symbol" aria-hidden="true">RZ</span><span class="service-rv-logo-wordmark" aria-hidden="true">Revianz</span></span>
            <p class="service-case-category">Desarrollo a medida · Para Digifianz</p>
          </div>
          <h3 id="revianz-service-title">{revianz_title}</h3>
          <div class="service-case-description">{revianz_copy}</div>
          <div class="service-case-actions"><a class="case-button" href="{routes['caso-revianz']}">Conocé el caso REVIANZ</a><a class="text-link" href="https://revianz.com/" target="_blank" rel="noopener noreferrer" aria-label="Visitar revianz.com (nueva pestaña)">Visitar revianz.com</a></div>
        </div>
        {mockup('scope', 'Vista ilustrativa de REVIANZ: servicios, importes y margen de un proyecto.', 'service-case-media service-case-mockup')}
      </article>
      <article class="service-case" aria-labelledby="photonix-service-title">
        <div class="service-case-copy">
          <div class="service-case-brandline">
            <img class="service-case-logo-photonix" src="/assets/brand/photonix-official.svg" alt="Photonix" width="170" height="54" loading="lazy">
            <p class="service-case-category">Desarrollo a medida · Servicio técnico</p>
          </div>
          <h3 id="photonix-service-title">{photonix_title}</h3>
          <div class="service-case-description">{photonix_copy}</div>
          <div class="service-case-actions">{photonix_link}</div>
        </div>
        <figure class="service-case-media">
          <div class="service-case-stage"><img src="/assets/brand/photonix-ethos-official.jpg" alt="Equipo de radioterapia Ethos, en una imagen institucional publicada por Photonix." width="1920" height="1080" loading="lazy" decoding="async"></div>
          <figcaption>Equipamiento de radioterapia. Imagen institucional de Photonix.</figcaption>
        </figure>
      </article>
    </div>
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
<section class="service-backing" id="respaldo" aria-labelledby="backing-heading"><div class="container"><div class="service-backing-brand"><img src="/assets/brand/digifianz-official.svg" alt="Digifianz" width="226" height="80" loading="lazy"><p class="service-backing-credential">Elite Partner de HubSpot</p><a class="text-link light-link" href="https://www.digifianz.com/es/" target="_blank" rel="noopener noreferrer" aria-label="Conocé la empresa: Digifianz (nueva pestaña)">Conocé la empresa</a></div><div class="service-backing-copy"><h2 id="backing-heading">{backing_title}</h2>{backing}</div></div></section>
<section class="container faq service-faq page-section" id="preguntas-frecuentes" aria-labelledby="questions-heading"><div class="section-intro"><h2 id="questions-heading">{faq_title}</h2></div><div class="faq-list">{faqs}</div></section>
<section class="page-contact service-closing" id="conversemos" aria-labelledby="next-title"><div class="container service-closing-inner"><div class="service-closing-heading"><h2 id="next-title">{cta_title}</h2><div class="service-closing-reassurance">{cta_reassurance}</div></div><div class="service-closing-action">{cta_context}<a class="button" href="/es#consulta">Contanos qué necesitás</a></div></div></section>
'''
