"""Product-led Despegar case: approved facts, original captures, editorial reading."""
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
    return f'<h3>{heading.group(1)}</h3><p>{item[heading.end():].strip()}</p>'


def build_case(meta, intro, sections, routes):
    opening = _paragraphs(intro)
    problem_title, problem = _section(sections, 'El problema')
    approach_title, approach = _section(sections, 'Diseñar')
    approach_copy = _paragraphs(approach)
    solution_title, solution = _section(sections, 'La solución')
    solution_copy = _paragraphs(solution)
    features = _items(solution)
    results_title, results = _section(sections, 'Resultados')
    result_copy = _paragraphs(results)
    evolution_title, evolution = _section(sections, 'Evolución')
    contact_title, contact_copy = _section(sections, '¿Tus cotizaciones')
    steps = [
        ('Relevar el negocio', 'Marcas, países y reglas de cálculo'),
        ('Validar con el equipo', 'Diagramas, plan y prototipo'),
        ('Integrar la solución', 'El cotizador conectado a HubSpot'),
    ]
    process = ''.join(
        f'<li><span class="case-process-number" aria-hidden="true">{i+1}</span>'
        f'<h3>{title}</h3><p class="case-process-output">{output}</p>'
        f'<div class="case-process-description">{copy}</div></li>'
        for i, ((title, output), copy) in enumerate(zip(steps, approach_copy))
    )

    return f'''
<section class="case-hero" aria-labelledby="case-title">
  <div class="container">
    <nav class="breadcrumbs" aria-label="Ubicación"><ol><li><a href="/es">Inicio</a></li><li><a href="/es#casos">Casos</a></li><li aria-current="page">Despegar Ads</li></ol></nav>
    <div class="case-hero-layout">
      <div class="case-hero-copy">
        <div class="case-identity"><div class="case-client-logo"><img src="/assets/brand/despegar-digifianz.png" alt="Despegar" width="180" height="52"></div><p>Desarrollo a medida e integración</p></div>
        <h1 id="case-title">{html.escape(meta['H1'])}</h1>
        <div class="case-hero-summary">{opening[0]}</div>
      </div>
      <figure class="case-hero-product">
        <a class="case-hero-capture" href="/assets/projects/despegar-cotizador-original.png" target="_blank" rel="noopener" aria-label="Ampliar vista del cotizador en el hero (nueva pestaña)"><img src="/assets/projects/despegar-cotizador-original.png" alt="Cotizador de Despegar: presupuesto, distribución por marca y país y selección de productos en una campaña de prueba." width="1633" height="887" fetchpriority="high" decoding="async"></a>
        <figcaption><a href="/assets/projects/despegar-cotizador-original.png" target="_blank" rel="noopener" aria-label="Ver captura del hero a tamaño completo (nueva pestaña)">Ampliar captura</a></figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="case-challenge container" id="problema" aria-labelledby="problema-title">
  <p class="case-section-label">El desafío</p>
  <div class="case-challenge-copy" id="resumen">
    <h2 id="problema-title">{_short_title(problem_title)}</h2>
    <div class="case-context">{opening[1]}</div>
    <div class="page-prose">{problem}</div>
  </div>
</section>

<section class="case-approach" id="diseno" aria-labelledby="diseno-title">
  <div class="container">
    <div class="case-approach-heading"><p class="case-section-label">El enfoque</p><h2 id="diseno-title">{approach_title}</h2></div>
    <ol class="case-process">{process}</ol>
  </div>
</section>

<section class="case-solution" id="solucion" aria-labelledby="solucion-title">
  <div class="container">
    <div class="case-solution-heading"><p class="case-section-label">El producto</p><h2 id="solucion-title">{_short_title(solution_title)}</h2><div class="page-prose">{solution_copy[0]}</div></div>
    <figure class="case-product-overview">
      <a href="/assets/projects/despegar-cotizador-original.png" target="_blank" rel="noopener" aria-label="Ampliar captura del cotizador de Despegar (nueva pestaña)"><img src="/assets/projects/despegar-cotizador-original.png" alt="Vista completa del cotizador con una campaña de prueba: presupuesto, distribución por marca y país y paneles de productos." width="1633" height="887" loading="lazy" decoding="async"></a>
      <figcaption><span>Presupuesto, marcas y países en una misma vista.</span><a href="/assets/projects/despegar-cotizador-original.png" target="_blank" rel="noopener" aria-label="Ver captura completa del cotizador (nueva pestaña)">Ver captura completa</a></figcaption>
    </figure>
    <div class="case-product-workflow page-prose">{solution_copy[1]}</div>
    <div class="case-product-rules"><div>{_feature(features[0])}</div><div>{_feature(features[2])}</div></div>

    <div class="case-catalog">
      <figure class="case-catalog-figure">
        <a class="case-catalog-crop" href="/assets/projects/despegar-catalogo-original.png" target="_blank" rel="noopener" aria-label="Abrir captura original completa del catálogo (nueva pestaña)"><img src="/assets/projects/despegar-catalogo-original.png" alt="Detalle de la ventana Agregar Producto: buscador, formatos publicitarios, precios unitarios y selección de productos." width="1641" height="883" loading="lazy" decoding="async"></a>
        <figcaption><span>Detalle del catálogo del cotizador.</span><a href="/assets/projects/despegar-catalogo-original.png" target="_blank" rel="noopener" aria-label="Ver captura completa del catálogo (nueva pestaña)">Ver captura completa</a></figcaption>
      </figure>
      <div class="case-catalog-copy"><div>{_feature(features[1])}</div><div>{_feature(features[3])}</div></div>
    </div>
  </div>
</section>

<section class="case-results" id="resultados" aria-labelledby="resultados-title">
  <div class="container">
    <p class="case-section-label">Los resultados</p>
    <div class="case-results-lead">
      <h2 id="resultados-title">De horas<br>a minutos.</h2>
      <div class="case-results-story"><h3>{_short_title(results_title)}</h3>{result_copy[0]}<div class="case-results-adoption">{''.join(result_copy[1:])}</div></div>
    </div>
    <ul class="case-outcomes">{''.join(f'<li>{item}</li>' for item in _items(results))}</ul>
    <div class="case-evolution" id="evolucion"><h3>{evolution_title}</h3><div>{evolution}</div></div>
  </div>
</section>

<section class="page-contact" aria-labelledby="next-title"><div class="container page-contact-inner"><div><h2 id="next-title">{contact_title}</h2>{contact_copy}</div><div class="page-contact-actions"><a class="button button-dark" href="/es#contacto">Hablemos de tu negocio</a><a class="text-link" href="/es#consulta">Prefiero enviar una consulta</a></div></div></section>
'''
