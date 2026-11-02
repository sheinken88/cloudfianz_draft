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
    revianz_name, revianz_description = revianz[0].split(': ', 1)
    revianz_title = f'<span class="service-case-name">{revianz_name}</span>{revianz_description[0].upper()}{revianz_description[1:]}'
    approach_title, approach = section('Del problema')
    approach_intro, steps = subsections(approach)
    approach_steps = ''.join(f'<li><div class="approach-step-title"><span aria-hidden="true">{i:02}</span><h3>{title}</h3></div><div class="approach-step-copy">{copy}</div></li>' for i, (title, copy) in enumerate(steps, 1))
    stages_title, stages = section('Cómo podés')
    stages_intro, stages = subsections(stages)
    offers = ''.join(f'<article><h3>{title}</h3>{copy}</article>' for title, copy in stages)
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
    <article class="revianz-preview" id="proyecto-revianz" aria-labelledby="revianz-service-title">
      <div class="service-case-overview">
        <h3 id="revianz-service-title">{revianz_title}</h3>
      </div>
      <div class="service-case-details">
        <div class="revianz-preview-copy">{revianz_copy}</div>
        <div class="service-case-actions"><a class="button button-dark" href="{routes['caso-revianz']}">Conocé el caso REVIANZ</a><a class="text-link" href="https://revianz.com/" target="_blank" rel="noopener noreferrer" aria-label="Visitar revianz.com (nueva pestaña)">Visitar revianz.com</a></div>
      </div>
      {mockup('scope', 'Vista ilustrativa de REVIANZ: servicios, importes y margen de un proyecto.')}
    </article>
    <article class="service-project-secondary" aria-labelledby="photonix-service-title">
      <figure><img src="/assets/brand/photonix-ethos-official.jpg" alt="Equipo de radioterapia Ethos, en una imagen institucional publicada por Photonix." width="1920" height="1080" loading="lazy" decoding="async"><figcaption>Equipamiento de radioterapia. Imagen institucional de Photonix.</figcaption></figure>
      <div class="service-project-copy"><h3 id="photonix-service-title">{photonix[0]}</h3>{photonix[1]}</div>
    </article>
    <div class="service-portfolio-link"><a class="text-link" href="#indice-casos" data-content="indice-casos">Ver todos los casos</a></div>
  </div>
</section>
<section class="container page-section service-approach" id="como-abordamos" aria-labelledby="approach-heading">
  <div class="service-section-intro"><h2 id="approach-heading">{approach_title}</h2>{approach_intro}</div>
  <ol class="service-approach-steps">{approach_steps}</ol>
</section>
<section class="container page-section service-engagement" aria-labelledby="engagement-heading"><div class="service-section-intro"><h2 id="engagement-heading">{stages_title}</h2>{stages_intro}</div><div class="service-offers">{offers}</div></section>
<section class="service-backing" id="respaldo" aria-labelledby="backing-heading"><div class="container"><div class="service-backing-brand"><img src="/assets/brand/digifianz-official.svg" alt="Digifianz" width="226" height="80" loading="lazy"><p class="service-backing-credential">Elite Partner de HubSpot</p><a class="text-link light-link" href="https://www.digifianz.com/es/" target="_blank" rel="noopener noreferrer" aria-label="Conocé la empresa: Digifianz (nueva pestaña)">Conocé la empresa</a></div><div class="service-backing-copy"><h2 id="backing-heading">{backing_title}</h2>{backing}</div></div></section>
<section class="container faq page-section" aria-labelledby="questions-heading"><div class="section-intro"><h2 id="questions-heading">{faq_title}</h2></div><div class="faq-list">{faqs}</div></section>
<section class="page-contact" aria-labelledby="next-title"><div class="container page-contact-inner"><div><h2 id="next-title">{cta_title}</h2>{cta}</div><div class="page-contact-actions"><a class="button button-dark" href="/es#contacto">Hablemos de tu negocio</a><a class="text-link" href="/es#consulta">Prefiero enviar una consulta</a></div></div></section>
'''
