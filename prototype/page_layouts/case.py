"""Editorial layout for the Despegar case, using the approved content verbatim."""
import html
import re


def _section(sections, prefix):
    return next((title, copy) for title, copy in sections.items() if title.startswith(prefix))


def _paragraphs(copy):
    return re.findall(r'<p>.*?</p>', copy, re.S)


def _list(copy):
    return re.search(r'<ul>(.*?)</ul>', copy, re.S).group(1)


def build_case(meta, intro, sections, routes):
    """Return the main content only; the site builder supplies shared chrome."""
    opening = _paragraphs(intro)
    problem_title, problem = _section(sections, 'El problema')
    approach_title, approach = _section(sections, 'Diseñar')
    approach_copy = _paragraphs(approach)
    solution_title, solution = _section(sections, 'La solución')
    solution_intro = ''.join(_paragraphs(solution))
    results_title, results = _section(sections, 'Resultados')
    result_copy = _paragraphs(results)
    evolution_title, evolution = _section(sections, 'Evolución')
    contact_title, contact_copy = _section(sections, '¿Tus cotizaciones')

    return f'''
<section class="case-hero" aria-labelledby="case-title">
  <div class="container">
    <nav class="breadcrumbs" aria-label="Ubicación"><ol><li><a href="/es">Inicio</a></li><li><a href="/es#casos">Casos</a></li><li aria-current="page">Despegar Ads</li></ol></nav>
    <div class="case-identity">
      <div class="case-client-logo"><img src="/assets/brand/despegar-digifianz.png" alt="Despegar" width="180" height="52"></div>
      <p>Desarrollo a medida e integración</p>
    </div>
    <div class="case-hero-copy">
      <h1 id="case-title">{html.escape(meta['H1'])}</h1>
      <div class="case-hero-summary">{opening[0]}</div>
    </div>
    <figure class="case-hero-media">
      <a href="/assets/projects/despegar-cotizador.png" target="_blank" rel="noopener" aria-label="Abrir vista del cotizador de Despegar en tamaño completo"><img src="/assets/projects/despegar-cotizador.png" alt="Vista real del cotizador de Despegar con presupuesto y selección de productos para la propuesta comercial." width="1600" height="869" fetchpriority="high"></a>
      <figcaption><span>Captura real del proyecto, publicada por Digifianz. Los campos difuminados pertenecen a la imagen original.</span><a href="/assets/projects/despegar-cotizador.png" target="_blank" rel="noopener">Ver captura completa</a></figcaption>
    </figure>
  </div>
</section>

<div class="case-project-facts container">
  <dl>
    <div><dt>El negocio</dt><dd>Publicidad digital en Latinoamérica</dd></div>
    <div><dt>La solución</dt><dd>Cotizador a medida conectado a HubSpot</dd></div>
    <div><dt>El cambio</dt><dd>De horas de preparación a cotizaciones en minutos</dd></div>
  </dl>
</div>

<nav class="story-navigation" aria-label="En este caso"><div class="container"><span>En este caso</span><a href="#problema">El desafío</a><a href="#diseno">El enfoque</a><a href="#solucion">La solución</a><a href="#resultados">Los resultados</a></div></nav>

<section class="story-challenge container" id="problema" aria-labelledby="problema-title">
  <aside class="story-context"><h2>El contexto de Despegar Ads</h2><div class="page-prose">{opening[1]}</div></aside>
  <div class="story-challenge-copy"><h2 id="problema-title">{problem_title}</h2><div class="page-prose">{problem}</div></div>
</section>

<section class="story-approach container" id="diseno" aria-labelledby="diseno-title">
  <h2 id="diseno-title">{approach_title}</h2>
  <div class="story-approach-intro page-prose">{approach_copy[0]}</div>
  <div class="story-approach-decisions"><div class="page-prose">{approach_copy[1]}</div><div class="story-approach-principle">{''.join(approach_copy[2:])}</div></div>
</section>

<section class="story-solution" id="solucion" aria-labelledby="solucion-title">
  <div class="container">
    <div class="story-solution-heading"><h2 id="solucion-title">{solution_title}</h2><div class="page-prose">{solution_intro}</div></div>
    <figure class="story-product-evidence"><a href="/assets/projects/despegar-distribucion.png" target="_blank" rel="noopener" aria-label="Abrir captura de distribución del presupuesto en tamaño completo"><img src="/assets/projects/despegar-distribucion.png" alt="Cotizador de Despegar: distribución del presupuesto por marca y país y selección de productos." width="1600" height="775" loading="lazy"></a><figcaption><span>La distribución del presupuesto y el catálogo se reúnen en una misma herramienta.</span><a href="/assets/projects/despegar-distribucion.png" target="_blank" rel="noopener">Ver captura completa</a></figcaption></figure>
    <ul class="story-capabilities">{_list(solution)}</ul>
  </div>
</section>

<section class="story-results" id="resultados" aria-labelledby="resultados-title">
  <div class="container">
    <div class="story-results-heading"><h2 id="resultados-title">{results_title}</h2><p class="story-result-change">De horas<br>a minutos.</p></div>
    <div class="story-results-intro">{result_copy[0]}</div>
    <ul class="story-outcomes">{_list(results)}</ul>
    <div class="story-results-continuity">{''.join(result_copy[1:])}</div>
  </div>
</section>

<section class="story-evolution container" id="evolucion" aria-labelledby="evolucion-title"><h2 id="evolucion-title">{evolution_title}</h2><div class="page-prose">{evolution}</div></section>

<section class="page-contact" aria-labelledby="next-title"><div class="container page-contact-inner"><div><h2 id="next-title">{contact_title}</h2>{contact_copy}</div><div class="page-contact-actions"><a class="button button-dark" href="/es#contacto">Hablemos de tu negocio</a><a class="text-link" href="/es#consulta">Prefiero enviar una consulta</a></div></div></section>
'''
