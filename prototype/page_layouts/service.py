"""A concise service journey: business needs, evidence, decisions and contact."""
import html
import re


def _paragraphs(copy):
    return re.findall(r'<p>.*?</p>', copy, re.S)


def _subsections(copy):
    parts = re.split(r'<h3>(.*?)</h3>', copy)
    return parts[0], [(parts[i], parts[i + 1]) for i in range(1, len(parts), 2)]


def build_service(meta, intro, sections, routes):
    def section(prefix):
        return next((title, copy) for title, copy in sections.items() if title.startswith(prefix))

    needs_title, needs = section('Tres situaciones')
    _, applications = _subsections(needs)
    needs_html = ''.join(
        f'<article><h3>{title}</h3>{_paragraphs(copy)[0]}'
        f'<div class="service-example">{_paragraphs(copy)[1]}</div></article>'
        for title, copy in applications
    )
    projects_title, projects = section('Proyectos')
    _, project_entries = _subsections(projects)
    despegar, *other_projects = project_entries
    projects_html = ''
    for title, copy in other_projects:
        client, outcome = title.split(': ', 1)
        outcome = outcome[0].upper() + outcome[1:]
        projects_html += (
            f'<article><p class="service-client">{client}</p>'
            f'<h3>{outcome}</h3><div class="service-project-copy">{copy}</div></article>'
        )

    method_title, method = section('Tu operación')
    method_intro, steps = _subsections(method)
    process = ''.join(f'<li><h3>{title}</h3>{copy}</li>' for title, copy in steps)
    offers_title, offers_copy = section('Empezá por')
    offer_paragraphs = _paragraphs(offers_copy)
    offers = []
    for entry in offer_paragraphs[1:]:
        title, copy = re.match(r'<p><strong>(.*?)\.</strong>\s*(.*?)</p>', entry, re.S).groups()
        offers.append(f'<article><h3>{title}</h3><p>{copy}</p></article>')

    faq_title, faq = section('Antes de empezar')
    _, questions = _subsections(faq)
    faqs = ''.join(
        f'<details name="service-questions"><summary>{title}<span aria-hidden="true"></span></summary>'
        f'<div class="service-answer">{copy}</div></details>'
        for title, copy in questions
    )
    _, backing = section('El respaldo')
    cta_title, cta = section('¿Qué necesitás')

    return f'''
<section class="service-hero" aria-labelledby="service-title">
  <div class="container">
    <nav class="breadcrumbs" aria-label="Ubicación"><ol><li><a href="/es">Inicio</a></li><li><a href="/es#soluciones">Soluciones</a></li><li aria-current="page">Desarrollo de software a medida</li></ol></nav>
    <div class="service-hero-grid">
      <div class="service-hero-copy">
        <h1 id="service-title">{html.escape(meta['H1'])}</h1>
        {_paragraphs(intro)[0]}
        <div class="page-actions"><a class="button button-dark" href="/es#contacto">Hablemos de tu negocio</a><a class="text-link" href="#proyectos">Ver proyectos reales</a></div>
      </div>
      <figure class="service-product">
        <a class="service-product-image" href="/assets/projects/despegar-cotizador-original.png" target="_blank" rel="noopener" aria-label="Ampliar captura original del cotizador de Despegar (nueva pestaña)"><img src="/assets/projects/despegar-cotizador-original.png" alt="Cotizador de Despegar con presupuesto, distribución por marca y país y paneles de productos en una campaña de prueba." width="1633" height="887" fetchpriority="high" decoding="async"></a>
        <figcaption><img src="/assets/brand/despegar-digifianz.png" alt="Despegar" width="180" height="52"><div>{despegar[1]}</div></figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="service-problems container" aria-labelledby="needs-heading">
  <h2 id="needs-heading">{needs_title}</h2>
  <div class="service-problem-grid">{needs_html}</div>
</section>

<section class="service-evidence" id="proyectos" aria-labelledby="projects-heading">
  <div class="container"><h2 id="projects-heading">{projects_title}</h2><div class="service-case-pair">{projects_html}</div></div>
</section>

<section class="service-method" id="metodo" aria-labelledby="method-heading">
  <div class="container">
    <div class="service-method-intro"><h2 id="method-heading">{method_title}</h2><div>{method_intro}</div></div>
    <ol class="service-process">{process}</ol>
    <div class="service-method-backing"><img src="/assets/brand/digifianz-official.svg" alt="Digifianz" width="226" height="80" loading="lazy"><div>{backing}</div></div>
  </div>
</section>

<section class="service-contracts container" aria-labelledby="engagement-heading">
  <div class="service-contracts-intro"><h2 id="engagement-heading">{offers_title}</h2>{offer_paragraphs[0]}</div>
  <div class="service-contract-grid">{''.join(offers)}</div>
</section>

<section class="service-close" aria-labelledby="next-title">
  <div class="container service-close-grid">
    <div class="service-next"><h2 id="next-title">{cta_title}</h2>{cta}<div class="service-next-actions"><a class="button button-dark" href="/es#contacto">Hablemos de tu negocio</a><a class="text-link" href="/es#consulta">Prefiero enviar una consulta</a></div></div>
    <div class="service-questions"><h3>{faq_title}</h3>{faqs}</div>
  </div>
</section>
'''
