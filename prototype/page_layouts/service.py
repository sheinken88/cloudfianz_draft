"""Service composition: business applications, real projects and independent offers."""
import re


def build_service(meta, intro, sections, routes):
    def section(prefix):
        return next((title, copy) for title, copy in sections.items() if title.startswith(prefix))

    def paragraphs(copy):
        return re.findall(r'<p>.*?</p>', copy, re.S)

    needs_title, needs = section('Cuando tus herramientas')
    parts = re.split(r'<h3>(.*?)</h3>', needs)
    needs_intro = parts[0]
    applications = [(parts[i], parts[i + 1]) for i in range(1, len(parts), 2)]
    lead_title, lead_copy = applications[0]
    supporting = ''.join(f'<article><h3>{title}</h3>{copy}</article>' for title, copy in applications[1:])
    projects_title, projects = section('Proyectos')
    parts = re.split(r'<h3>(.*?)</h3>', projects)
    projects = [(parts[i], parts[i + 1]) for i in range(1, len(parts), 2)]
    despegar, photonix, ads = projects
    ads_title = ads[0].replace('más de 50 cotizaciones diarias', '<span>más de 50 cotizaciones diarias</span>')
    choice_title, choice = section('Elegimos')
    delivery_title, delivery = section('Una primera')
    stages_title, stages = section('Podés empezar')
    stage_paragraphs = paragraphs(stages)
    offers = []
    for entry in stage_paragraphs[:4]:
        title, copy = re.match(r'<p><strong>(.*?)\.</strong>\s*(.*?)</p>', entry, re.S).groups()
        offers.append(f'<article><h3>{title}</h3><p>{copy}</p></article>')
    faq_title, faq = section('Antes de empezar')
    parts = re.split(r'<h3>(.*?)</h3>', faq)
    faqs = ''.join(f'<details><summary>{parts[i]}<span class="plus" aria-hidden="true"></span></summary>{parts[i + 1]}</details>' for i in range(1, len(parts), 2))
    _, backing = section('El respaldo')
    cta_title, cta = section('¿Qué necesita')
    return f'''
<section class="service-opening">
  <div class="container">
    <nav class="breadcrumbs" aria-label="Ubicación"><ol><li><a href="/es">Inicio</a></li><li><a href="/es#soluciones">Soluciones</a></li><li aria-current="page">Desarrollo de software a medida</li></ol></nav>
    <div class="service-opening-grid">
      <div class="opening-copy">
        <h1>{meta['H1']}</h1>
        {paragraphs(intro)[0]}
        <div class="page-actions"><a class="button button-dark" href="/es#contacto">Hablemos de tu negocio</a><a class="text-link" href="#proyectos">Ver proyectos reales</a></div>
      </div>
      <figure class="service-visual">
        <div class="service-screen"><img src="/assets/projects/despegar-cotizador.png" alt="Cotizador real de Despegar con las reglas de presupuesto, marcas y países integradas." width="1600" height="869" fetchpriority="high"></div>
        <figcaption><img src="/assets/brand/despegar-digifianz.png" alt="Despegar" width="180" height="52"><div><p>Un cotizador con las reglas de Despegar, conectado con HubSpot.</p><a class="text-link" href="{routes['caso-despegar']}">Conocé el proyecto</a></div></figcaption>
      </figure>
    </div>
  </div>
</section>
<section class="container service-needs page-section" aria-labelledby="needs-heading">
  <div class="service-section-intro"><h2 id="needs-heading">{needs_title}</h2>{needs_intro}</div>
  <article class="application-lead"><h3>{lead_title}</h3><div>{lead_copy}</div></article>
  <div class="application-pair">{supporting}</div>
</section>
<section class="service-projects page-section" id="proyectos" aria-labelledby="projects-heading">
  <div class="container">
    <h2 id="projects-heading">{projects_title}</h2>
    <article class="service-feature">
      <figure><img src="/assets/projects/despegar-distribucion.png" alt="Distribución del presupuesto en el cotizador de Despegar." width="1600" height="775" loading="lazy"><figcaption>Captura del proyecto publicada por Digifianz.</figcaption></figure>
      <div class="service-feature-copy"><img class="service-feature-logo" src="/assets/brand/despegar-digifianz.png" alt="Despegar" width="180" height="52" loading="lazy"><h3>{despegar[0]}</h3>{despegar[1]}</div>
    </article>
    <div class="project-companions">
      <article class="project-photonix-story"><figure><img src="/assets/brand/photonix-ethos-official.jpg" alt="Equipo de radioterapia Ethos, en una imagen institucional publicada por Photonix." width="1920" height="1080" loading="lazy"><figcaption>Equipamiento de radioterapia. Imagen institucional de Photonix.</figcaption></figure><div><h3>{photonix[0]}</h3>{photonix[1]}</div></article>
      <article class="project-ads-story"><h3>{ads_title}</h3>{ads[1]}</article>
    </div>
  </div>
</section>
<section class="container page-section decision-section"><div class="decision-copy"><h2>{choice_title}</h2><div class="page-prose">{choice}</div></div></section>
<section class="delivery-section page-section"><div class="container"><h2>{delivery_title}</h2><div class="delivery-copy">{delivery}</div></div></section>
<section class="container page-section service-engagement" aria-labelledby="engagement-heading"><div class="service-section-intro"><h2 id="engagement-heading">{stages_title}</h2>{stage_paragraphs[-1]}</div><div class="service-offers">{''.join(offers)}</div></section>
<section class="container faq page-section" aria-labelledby="questions-heading"><div class="section-intro"><h2 id="questions-heading">{faq_title}</h2></div><div class="faq-list">{faqs}</div></section>
<section class="service-backing"><div class="container"><img src="/assets/brand/digifianz-official.svg" alt="Digifianz" width="226" height="80" loading="lazy"><div>{backing}</div></div></section>
<section class="page-contact" aria-labelledby="next-title"><div class="container page-contact-inner"><div><h2 id="next-title">{cta_title}</h2>{cta}</div><div class="page-contact-actions"><a class="button button-dark" href="/es#contacto">Hablemos de tu negocio</a><a class="text-link" href="/es#consulta">Prefiero enviar una consulta</a></div></div></section>
'''
