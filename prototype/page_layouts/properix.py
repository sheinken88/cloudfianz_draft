"""ConsorcioAbierto: contract rules, a documented integration, and billing at scale."""
import html
import re


def _section(sections, prefix):
    return next((title, copy) for title, copy in sections.items() if title.startswith(prefix))


def _paragraphs(copy):
    return re.findall(r'<p>.*?</p>', copy, re.S)


def _items(copy):
    return re.findall(r'<li>(.*?)</li>', copy, re.S)


def _short_title(title):
    text = title.split(': ', 1)[-1]
    return text[0].upper() + text[1:]


def _feature(item):
    heading = re.search(r'<strong>(.*?)</strong>', item, re.S)
    title = heading.group(1).rstrip('.')
    return f'<h3>{title}</h3><p>{item[heading.end():].strip()}</p>'


def build_properix(meta, intro, sections, routes):
    opening = _paragraphs(intro)
    problem_title, problem = _section(sections, 'El problema')
    approach_title, approach = _section(sections, 'Una arquitectura')
    approach_copy = _paragraphs(approach)
    solution_title, solution = _section(sections, 'La solución')
    solution_copy = _paragraphs(solution)
    results_title, results = _section(sections, 'Resultados')
    result_copy = _paragraphs(results)
    contact_title, contact = _section(sections, '¿Tu facturación')
    rules = ''.join(f'<li>{_feature(item)}</li>' for item in _items(solution))
    outcomes = ''.join(f'<li>{_feature(item)}</li>' for item in _items(results))
    return f'''
<section class="billing-hero" aria-labelledby="billing-title">
  <div class="container">
    <nav class="breadcrumbs" aria-label="Ubicación"><ol><li><a href="/es">Inicio</a></li><li><a href="/es/casos">Casos</a></li><li aria-current="page">ConsorcioAbierto</li></ol></nav>
    <div class="billing-hero-grid">
      <div class="billing-hero-copy">
        <div class="billing-identity"><div class="billing-client-logo"><img src="/assets/brand/consorcio-abierto-official.svg" alt="ConsorcioAbierto" width="156" height="20"></div><p>Integración y automatización de procesos</p></div>
        <h1 id="billing-title">{html.escape(meta['H1'])}</h1>
        <div class="billing-lead">{opening[0]}</div>
      </div>
      <figure class="billing-product">
        <div class="billing-product-image"><img src="/assets/projects/consorcioabierto-plataforma-usuario.png" alt="Plataforma de ConsorcioAbierto: resumen de fondos, pagos, reclamos y agenda de una administración." width="610" height="253" fetchpriority="high" decoding="async"></div>
        <figcaption>Plataforma de ConsorcioAbierto. Imagen de contexto del cliente.</figcaption>
      </figure>
    </div>
    <dl class="billing-project-facts"><div><dt>Trabajo de Cloudfianz</dt><dd>Integración y automatización de la facturación</dd></div><div><dt>Plataformas conectadas</dt><dd>HubSpot, AWS y Odoo</dd></div><div><dt>Alcance</dt><dd>Argentina, Uruguay, Paraguay y Colombia</dd></div></dl>
  </div>
</section>

<section class="container billing-challenge" id="problema" aria-labelledby="billing-problem-title">
  <aside class="billing-client" aria-labelledby="billing-client-title"><h2 id="billing-client-title">El cliente</h2>{opening[1]}</aside>
  <div class="billing-challenge-copy"><p class="billing-section-label">El desafío</p><h2 id="billing-problem-title">{_short_title(problem_title)}</h2><div class="page-prose">{problem}</div></div>
</section>

<section class="billing-approach" id="enfoque" aria-labelledby="billing-approach-title"><div class="container">
  <div class="billing-approach-heading"><p class="billing-section-label">La decisión técnica</p><h2 id="billing-approach-title">{approach_title}</h2></div>
  <div class="billing-decision"><div><h3>Lo que evaluamos</h3><div class="page-prose">{approach_copy[0]}</div></div><div><h3>Cómo lo resolvimos</h3><div class="page-prose">{''.join(approach_copy[1:])}</div></div></div>
</div></section>

<section class="billing-solution" id="solucion" aria-labelledby="billing-solution-title"><div class="container">
  <div class="billing-solution-heading"><div><p class="billing-section-label">La solución</p><h2 id="billing-solution-title">{_short_title(solution_title)}</h2></div><div class="page-prose">{solution_copy[0]}</div></div>
  <figure class="billing-flow">
    <ol class="billing-flow-steps" aria-label="Flujo de facturación">
      <li><div class="billing-flow-brand"><img class="billing-hubspot" src="/assets/brand/hubspot-official.svg" alt="HubSpot" width="1256" height="356" loading="lazy" decoding="async"></div><div class="billing-flow-copy"><strong>Membresías y productos</strong><span>Acuerdos y condiciones comerciales</span></div></li>
      <li><div class="billing-flow-brand"><img class="billing-aws" src="/assets/aws/aws-logo-color.svg" alt="AWS" width="304" height="182" loading="lazy" decoding="async"></div><div class="billing-flow-copy"><strong>Reglas de cada contrato</strong><span>Step Functions y Lambda</span></div></li>
      <li><div class="billing-flow-brand"><img class="billing-odoo" src="/assets/brand/odoo-official.svg" alt="Odoo" width="919" height="495" loading="lazy" decoding="async"></div><div class="billing-flow-copy"><strong>Facturas generadas</strong><span>Importes según período y país</span></div></li>
    </ol>
    <figcaption>Esquema de la integración desarrollada por Cloudfianz.</figcaption>
  </figure>
  <ol class="billing-rules">{rules}</ol>
  <div class="billing-delivery"><h3>Ordenar las reglas también fue parte del proyecto.</h3><div class="page-prose">{''.join(solution_copy[1:])}</div></div>
</div></section>

<section class="billing-results" id="resultados" aria-labelledby="billing-results-title"><div class="container">
  <p class="billing-section-label">Los resultados</p>
  <div class="billing-results-lead">
    <div class="billing-volume"><p>Más de <strong>15.000</strong><span>facturas mensuales</span></p><p class="billing-volume-detail">En cuestión de horas</p></div>
    <div class="billing-results-copy"><h2 id="billing-results-title">{_short_title(results_title)}</h2>{result_copy[0]}</div>
  </div>
  <div class="billing-outcomes-intro">{result_copy[1]}</div>
  <ul class="billing-outcomes">{outcomes}</ul>
  <div class="billing-results-note">{''.join(result_copy[2:])}</div>
</div></section>

<section class="page-contact billing-contact" aria-labelledby="billing-contact-title"><div class="container page-contact-inner">
  <h2 id="billing-contact-title">{contact_title}</h2>
  {contact}
  <div class="page-contact-actions"><a class="button button-dark" href="/es/contacto">Contanos qué necesitás</a><a class="text-link" href="/es/casos">Ver todos los casos</a></div>
</div></section>
'''
