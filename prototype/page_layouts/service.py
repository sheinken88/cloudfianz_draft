"""Service composition: business applications, real projects and independent offers."""
import re
from page_layouts.revianz_mockups import mockup


def build_service(meta, intro, sections, routes):
    def section(prefix):
        return next((title, copy) for title, copy in sections.items() if title.startswith(prefix))

    def paragraphs(copy):
        return re.findall(r'<p>.*?</p>', copy, re.S)

    needs_title, needs = section('Cuando tus herramientas')
    parts = re.split(r'<h3>(.*?)</h3>', needs)
    needs_intro = parts[0]
    applications = [(parts[i], parts[i + 1]) for i in range(1, len(parts), 2)]
    application_columns = []
    for title, copy in applications:
        description, example = paragraphs(copy)
        example = example.removeprefix('<p><strong>Ejemplo:</strong> ').removesuffix('</p>')
        application_columns.append(f'<article class="service-application"><h3>{title}</h3><div class="application-description">{description}</div><div class="application-example"><p class="application-example-label">Por ejemplo</p><p>{example}</p></div></article>')
    projects_title, projects = section('Proyectos')
    parts = re.split(r'<h3>(.*?)</h3>', projects)
    projects = [(parts[i], parts[i + 1]) for i in range(1, len(parts), 2)]
    despegar, revianz, photonix, ads = projects
    revianz_copy = re.sub(r'<p>(<a [^>]+>Conocé el caso REVIANZ</a>)\.</p>', r'<div class="revianz-preview-actions">\1<a href="https://revianz.com/" target="_blank" rel="noopener noreferrer" aria-label="Visitar revianz.com (nueva pestaña)">Visitar revianz.com</a></div>', revianz[1])
    ads_title = ads[0].replace('más de 50 cotizaciones diarias', '<span>más de 50 cotizaciones diarias</span>')
    choice_title, choice = section('Elegimos')
    delivery_title, delivery = section('Una primera')
    stages_title, stages = section('Modalidades')
    stage_paragraphs = paragraphs(stages)
    offers = []
    for entry in stage_paragraphs[:4]:
        title, copy = re.match(r'<p><strong>(.*?)\.</strong>\s*(.*?)</p>', entry, re.S).groups()
        offers.append(f'<article><h3>{title}</h3><p>{copy}</p></article>')
    faq_title, faq = section('Antes de empezar')
    parts = re.split(r'<h3>(.*?)</h3>', faq)
    faqs = ''.join(f'<details name="service-questions"><summary>{parts[i]}<span class="plus" aria-hidden="true"></span></summary>{parts[i + 1]}</details>' for i in range(1, len(parts), 2))
    backing_title, backing = section('Experiencia de negocio')
    cta_title, cta = section('¿Qué necesita')
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
        <figcaption><img src="/assets/brand/despegar-digifianz.png" alt="Despegar" width="180" height="52"><div><p>Cotizador a medida integrado con HubSpot.</p><a class="text-link" href="#proyecto-despegar">Ver el proyecto</a></div></figcaption>
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
    <h2 id="projects-heading">{projects_title}</h2>
    <article class="service-feature" id="proyecto-despegar">
      <figure><a href="/assets/projects/despegar-catalogo-original.png" target="_blank" rel="noopener" aria-label="Ampliar captura original del catálogo de Despegar (nueva pestaña)"><img src="/assets/projects/despegar-catalogo-original.png" alt="Catálogo de productos para Despegar Brasil dentro del cotizador, con buscador, formatos y precios unitarios." width="1641" height="883" loading="lazy" decoding="async"></a><figcaption>Catálogo del cotizador de Despegar. <a href="/assets/projects/despegar-catalogo-original.png" target="_blank" rel="noopener" aria-label="Ver captura completa del catálogo (nueva pestaña)">Ampliar captura</a></figcaption></figure>
      <div class="service-feature-copy"><img class="service-feature-logo" src="/assets/brand/despegar-digifianz.png" alt="Despegar" width="180" height="52" loading="lazy"><h3>{despegar[0]}</h3>{despegar[1]}</div>
    </article>
    <article class="revianz-preview" id="proyecto-revianz" aria-labelledby="revianz-service-title">
      <div class="revianz-preview-heading"><div><p class="revianz-project-context">Desarrollo de software a medida</p><h3 id="revianz-service-title">{revianz[0]}</h3></div><div class="revianz-preview-copy">{revianz_copy}</div></div>
      {mockup('scope', 'Vista ilustrativa de REVIANZ: servicios, importes y margen de un proyecto.')}
    </article>
    <div class="project-companions">
      <article class="project-photonix-story"><figure><img src="/assets/brand/photonix-ethos-official.jpg" alt="Equipo de radioterapia Ethos, en una imagen institucional publicada por Photonix." width="1920" height="1080" loading="lazy"><figcaption>Equipamiento de radioterapia. Imagen institucional de Photonix.</figcaption></figure><div><h3>{photonix[0]}</h3>{photonix[1]}</div></article>
      <article class="project-ads-story"><h3>{ads_title}</h3>{ads[1]}</article>
    </div>
  </div>
</section>
<section class="container page-section decision-section" id="criterio"><div class="decision-copy"><h2>{choice_title}</h2><div class="page-prose">{choice}</div></div></section>
<section class="delivery-section page-section" id="alcance"><div class="container"><h2>{delivery_title}</h2><div class="delivery-copy">{delivery}</div></div></section>
<section class="container page-section service-engagement" aria-labelledby="engagement-heading"><div class="service-section-intro"><h2 id="engagement-heading">{stages_title}</h2>{stage_paragraphs[-1]}</div><div class="service-offers">{''.join(offers)}</div></section>
<section class="container faq page-section" aria-labelledby="questions-heading"><div class="section-intro"><h2 id="questions-heading">{faq_title}</h2></div><div class="faq-list">{faqs}</div></section>
<section class="service-backing" id="respaldo" aria-labelledby="backing-heading"><div class="container"><div class="service-backing-brand"><img src="/assets/brand/digifianz-official.svg" alt="Digifianz" width="226" height="80" loading="lazy"><p class="service-backing-credential">Elite Partner de HubSpot</p><a class="text-link light-link" href="https://www.digifianz.com/es/" target="_blank" rel="noopener noreferrer" aria-label="Conocé la empresa: Digifianz (nueva pestaña)">Conocé la empresa</a></div><div class="service-backing-copy"><h2 id="backing-heading">{backing_title}</h2>{backing}</div></div></section>
<section class="page-contact" aria-labelledby="next-title"><div class="container page-contact-inner"><div><h2 id="next-title">{cta_title}</h2>{cta}</div><div class="page-contact-actions"><a class="button button-dark" href="/es#contacto">Hablemos de tu negocio</a><a class="text-link" href="/es#consulta">Prefiero enviar una consulta</a></div></div></section>
'''
