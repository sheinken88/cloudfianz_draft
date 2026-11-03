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
    solution_title, solution = _section(sections, 'La solución')
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
        <div class="billing-identity"><img src="/assets/brand/consorcio-abierto-official.svg" alt="ConsorcioAbierto" width="156" height="20"><p>Integración y automatización de procesos</p></div>
        <h1 id="billing-title">{html.escape(meta['H1'])}</h1>
        <div class="billing-lead">{opening[0]}</div>
      </div>
      <figure class="billing-flow">
        <p class="billing-flow-title">Del acuerdo comercial a la factura</p>
        <ol class="billing-flow-steps" aria-label="Flujo de facturación">
          <li><div class="billing-flow-brand"><img class="billing-hubspot" src="/assets/brand/hubspot-official.svg" alt="HubSpot" width="1256" height="356" decoding="async"></div><div class="billing-flow-copy"><strong>Membresías</strong><span>Acuerdos, productos y condiciones comerciales</span></div></li>
          <li><div class="billing-flow-brand"><img class="billing-aws" src="/assets/aws/aws-logo-color.svg" alt="AWS" width="304" height="182" decoding="async"></div><div class="billing-flow-copy"><strong>Reglas de facturación</strong><span>Step Functions y Lambda aplican las condiciones de cada contrato</span></div></li>
          <li><div class="billing-flow-brand"><img class="billing-odoo" src="/assets/brand/odoo-official.svg" alt="Odoo" width="919" height="495" decoding="async"></div><div class="billing-flow-copy"><strong>Facturas</strong><span>Importes según período, descuentos y país</span></div></li>
        </ol>
        <figcaption>Esquema de la integración desarrollada para ConsorcioAbierto.</figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="container billing-challenge" id="problema" aria-labelledby="billing-problem-title">
  <aside class="billing-client" aria-labelledby="billing-client-title"><h2 id="billing-client-title">El cliente</h2>{opening[1]}</aside>
  <div class="billing-challenge-copy"><p class="billing-section-label">El desafío</p><h2 id="billing-problem-title">{_short_title(problem_title)}</h2><div class="page-prose">{problem}</div></div>
</section>

<section class="billing-approach" id="enfoque" aria-labelledby="billing-approach-title"><div class="container billing-approach-grid">
  <div><p class="billing-section-label">El enfoque</p><h2 id="billing-approach-title">{approach_title}</h2></div>
  <div class="page-prose">{approach}</div>
</div></section>

<section class="container billing-solution" id="solucion" aria-labelledby="billing-solution-title">
  <div class="billing-solution-heading"><p class="billing-section-label">La solución</p><h2 id="billing-solution-title">{_short_title(solution_title)}</h2></div>
  <ol class="billing-rules">{rules}</ol>
  <div class="billing-delivery"><p class="billing-section-label">Implementación</p><div class="page-prose">{''.join(_paragraphs(solution))}</div></div>
</section>

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
  <div class="page-contact-actions"><a class="button button-dark" href="/es#consulta">Contanos qué necesitás</a><a class="text-link" href="/es/casos">Ver todos los casos</a></div>
</div></section>
'''
