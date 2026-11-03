"""Case studies with a shared editorial system and project-specific visuals."""
import html
import re

from page_layouts.project_visuals import hero_visual, solution_visual


PROJECTS = {
    'caso-escala24x7': {
        'name': 'Escala24x7', 'category': 'Integración de sistemas',
        'logo': '/assets/brand/escala24x7-original.avif', 'dimensions': (1275, 784),
        'identity': 'integration', 'approach': None, 'evolution': 'Una integración',
        'facts': [('Trabajo de Cloudfianz', 'Integración bidireccional'),
                  ('Plataformas conectadas', 'HubSpot y AWS Partner Central'),
                  ('Alcance', 'Oportunidades y beneficios de AWS')],
        'delivery': 'Datos compatibles, sincronizaciones automáticas.',
    },
    'caso-photonix': {
        'name': 'Photonix', 'category': 'Desarrollo de software a medida',
        'logo': '/assets/brand/photonix-official.svg', 'dimensions': (170, 54),
        'identity': 'photonix', 'approach': 'Entender el proceso', 'evolution': 'Una base',
        'facts': [('Trabajo de Cloudfianz', 'Software de servicio técnico'),
                  ('Usuarios', 'Técnicos y administración'),
                  ('Implementación', 'Tres meses, del diagnóstico a producción')],
        'decision': ['Conocer el trabajo de cada equipo', 'Un sistema propio para sus reglas'],
        'delivery': 'De la definición al trabajo cotidiano.',
    },
    'caso-ads-mexicana': {
        'name': 'ADS Mexicana', 'category': 'Desarrollo a medida e integración',
        'logo': '/assets/brand/ads-mexicana-original.png', 'dimensions': (938, 410),
        'identity': 'quotation', 'approach': 'Elegir una solución', 'evolution': None,
        'facts': [('Trabajo de Cloudfianz', 'Cotizador a medida'),
                  ('Plataforma conectada', 'HubSpot'),
                  ('Implementación', 'Un año, del diagnóstico a puesta en funcionamiento')],
        'decision': ['Evaluar las reglas de cotización', 'Extender la plataforma existente'],
        'delivery': 'Un desarrollo ajustado al proceso comercial.',
    },
}


def _paragraphs(copy):
    return re.findall(r'<p>.*?</p>', copy, re.S)


def _items(copy):
    return re.findall(r'<li>(.*?)</li>', copy, re.S)


def _short_title(title):
    title = title.split(': ', 1)[-1]
    return title[0].upper() + title[1:]


def _feature(item):
    heading = re.search(r'<strong>(.*?)</strong>', item, re.S)
    title, copy = heading.group(1).rstrip('.'), item[heading.end():].strip()
    return f'<li><h3>{title}</h3><p>{copy}</p></li>'


def _results(key, title, copy):
    paragraphs = _paragraphs(copy)
    heading = html.escape(_short_title(title))
    if key == 'caso-ads-mexicana':
        return f'''<p class="story-section-label">Los resultados</p>
  <div class="story-result-lead story-result-with-metric">
    <div class="story-metric"><p>Más de <strong>50</strong><span>cotizaciones por día</span></p><p class="story-metric-detail">De horas de cálculo a propuestas en minutos</p></div>
    <div class="story-result-summary"><h2 id="story-results-title">{heading}</h2>{paragraphs[0]}</div>
  </div>
  <div class="story-result-details"><div><h3>Más tiempo para la gestión comercial</h3>{paragraphs[1]}</div><div><h3>Con el plan de HubSpot existente</h3>{paragraphs[2]}</div></div>'''
    if key == 'caso-photonix':
        return f'''<div class="story-result-lead"><div><p class="story-section-label">Los resultados</p><h2 id="story-results-title">{heading}</h2></div><div class="story-result-summary">{paragraphs[0]}</div></div>
  <div class="story-result-details"><div><h3>Planificación y seguimiento compartidos</h3>{paragraphs[1]}</div><div><h3>Infraestructura acorde a la operación</h3>{paragraphs[2]}</div></div>'''
    outcomes = ''.join(_feature(item) for item in _items(copy))
    return f'''<div class="story-result-lead"><div><p class="story-section-label">Los resultados</p><h2 id="story-results-title">{heading}</h2></div><div class="story-result-summary">{''.join(paragraphs)}</div></div>
  <ul class="story-outcomes">{outcomes}</ul>'''


def build_project(key, meta, intro, sections, routes):
    project = PROJECTS[key]

    def section(prefix):
        return next((title, copy) for title, copy in sections.items() if title.startswith(prefix))

    opening = _paragraphs(intro)
    problem_title, problem = section('El problema')
    solution_title, solution = section('La solución')
    results_title, results = section('Resultados')
    contact_title, contact = section('¿')
    width, height = project['dimensions']
    facts = ''.join(f'<div><dt>{label}</dt><dd>{value}</dd></div>' for label, value in project['facts'])
    approach = ''
    if project['approach']:
        approach_title, approach_copy = section(project['approach'])
        decisions = ''.join(f'<div><h3>{title}</h3><div class="story-prose">{paragraph}</div></div>'
                            for title, paragraph in zip(project['decision'], _paragraphs(approach_copy)))
        approach = f'''<section class="story-approach story-section" id="enfoque" aria-labelledby="story-approach-title"><div class="container">
  <div class="story-chapter-heading"><p class="story-section-label">La decisión técnica</p><h2 id="story-approach-title">{html.escape(approach_title)}</h2></div>
  <div class="story-decisions">{decisions}</div>
</div></section>'''
    evolution = ''
    if project['evolution']:
        evolution_title, evolution_copy = section(project['evolution'])
        evolution = f'''<section class="story-evolution story-section" id="evolucion" aria-labelledby="story-evolution-title"><div class="container story-evolution-grid">
  <div><p class="story-section-label">Próximos pasos</p><h2 id="story-evolution-title">{html.escape(evolution_title)}</h2></div><div class="story-prose">{evolution_copy}</div>
</div></section>'''
    # Preserve the source order around the feature list: overview, capabilities, delivery.
    before_list, after_list = re.split(r'<ul>.*?</ul>', solution, maxsplit=1, flags=re.S)
    solution_intro = _paragraphs(before_list)
    solution_items = _items(solution)
    features = '' if key == 'caso-escala24x7' else '<ul class="story-features">' + ''.join(
        _feature(item) for item in solution_items) + '</ul>'
    return f'''
<section class="story-hero" aria-labelledby="story-title">
  <div class="container">
    <nav class="breadcrumbs" aria-label="Ubicación"><ol><li><a href="/es">Inicio</a></li><li><a href="/es/casos">Casos</a></li><li aria-current="page">{project['name']}</li></ol></nav>
    <div class="story-hero-grid">
      <div class="story-hero-copy">
        <div class="story-identity story-identity-{project['identity']}"><div class="story-client-logo"><img src="{project['logo']}" alt="{project['name']}" width="{width}" height="{height}"></div><p>{project['category']}</p></div>
        <h1 id="story-title">{html.escape(meta['H1'])}</h1>
        <div class="story-hero-summary">{opening[0]}</div>
      </div>
      {hero_visual(key)}
    </div>
    <dl class="story-project-facts">{facts}</dl>
  </div>
</section>
<section class="story-challenge story-section container" id="problema" aria-labelledby="story-problem-title">
  <aside class="story-client" aria-labelledby="story-client-title"><h2 id="story-client-title">El cliente</h2>{''.join(opening[1:])}</aside>
  <div><div class="story-chapter-heading"><p class="story-section-label">El desafío</p><h2 id="story-problem-title">{html.escape(_short_title(problem_title))}</h2></div><div class="story-prose">{problem}</div></div>
</section>
{approach}
<section class="story-solution story-section" id="solucion" aria-labelledby="story-solution-title"><div class="container">
  <div class="story-solution-heading"><div class="story-chapter-heading"><p class="story-section-label">La solución</p><h2 id="story-solution-title">{html.escape(_short_title(solution_title))}</h2></div><div class="story-prose">{solution_intro[0]}</div></div>
  {solution_visual(key, solution_items)}
  <div class="story-solution-overview story-prose">{''.join(solution_intro[1:])}</div>
{features}
  <div class="story-delivery"><h3>{project['delivery']}</h3><div class="story-prose">{after_list}</div></div>
</div></section>
<section class="story-results story-section" id="resultados" aria-labelledby="story-results-title"><div class="container">
  {_results(key, results_title, results)}
</div></section>
{evolution}
<section class="page-contact story-contact" aria-labelledby="story-contact-title"><div class="container page-contact-inner">
  <h2 id="story-contact-title">{html.escape(contact_title)}</h2>{contact}
  <div class="page-contact-actions"><a class="button button-dark" href="/es#consulta">Contanos qué necesitás</a><a class="text-link" href="/es/casos">Ver todos los casos</a></div>
</div></section>
'''
