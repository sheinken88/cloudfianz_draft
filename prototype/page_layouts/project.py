"""Complete project stories for Escala24x7, Photonix and ADS Mexicana."""
import html
import re


PROJECTS = {
    'caso-escala24x7': {
        'name': 'Escala24x7',
        'category': 'Integración de sistemas',
        'logo': '/assets/brand/escala24x7-original.avif',
        'dimensions': (1275, 784),
        'visual': 'integration',
        'approach': None,
        'evolution': 'Una integración',
    },
    'caso-photonix': {
        'name': 'Photonix',
        'category': 'Desarrollo de software a medida',
        'logo': '/assets/brand/photonix-official.svg',
        'dimensions': (170, 54),
        'visual': 'photonix',
        'approach': 'Entender el proceso',
        'evolution': 'Una base',
    },
    'caso-ads-mexicana': {
        'name': 'ADS Mexicana',
        'category': 'Desarrollo a medida e integración',
        'logo': '/assets/brand/ads-mexicana-original.png',
        'dimensions': (938, 410),
        'visual': 'quotation',
        'approach': 'Elegir una solución',
        'evolution': None,
    },
}


def _paragraphs(copy):
    return re.findall(r'<p>.*?</p>', copy, re.S)


def _short_title(title):
    title = title.split(': ', 1)[-1]
    return title[0].upper() + title[1:]


def _visual(kind):
    if kind == 'integration':
        return '''<figure class="story-visual story-integration">
          <div class="story-integration-stage">
            <p class="story-visual-label">Sincronización bidireccional</p>
            <div class="story-integration-flow">
              <div class="story-system"><div class="story-system-brand"><img src="/assets/brand/hubspot-official.svg" alt="HubSpot" width="1256" height="356" decoding="async"></div><p>CRM comercial</p></div>
              <span class="story-flow-arrow" aria-hidden="true">⇄</span>
              <div class="story-system"><div class="story-system-brand"><img class="story-aws-logo" src="/assets/aws/aws-logo-color.svg" alt="AWS" width="304" height="182" decoding="async"></div><p>Partner Central</p></div>
            </div>
            <p class="story-visual-result">Oportunidades actualizadas<br>en ambas plataformas</p>
          </div>
          <figcaption>Esquema de la integración desarrollada para Escala24x7.</figcaption>
        </figure>'''
    if kind == 'photonix':
        return '''<figure class="story-visual story-photo">
          <div class="story-photo-stage"><img src="/assets/brand/photonix-ethos-official.jpg" alt="Equipo de radioterapia Ethos en una imagen institucional de Photonix." width="1920" height="1080" fetchpriority="high" decoding="async"></div>
          <figcaption>Equipamiento de radioterapia. Imagen institucional de Photonix como contexto de su actividad.</figcaption>
        </figure>'''
    return '''<figure class="story-visual story-quotation">
          <div class="story-quotation-stage">
            <img class="story-quotation-brand" src="/assets/brand/hubspot-official.svg" alt="HubSpot" width="1256" height="356" decoding="async">
            <ol class="story-quotation-flow">
              <li><strong>Datos del negocio</strong><span>Compañía, contactos y productos</span></li>
              <li><strong>Reglas de ADS</strong><span>Precios, descuentos y recomendaciones</span></li>
              <li><strong>Cotización en HubSpot</strong><span>Registrada en el negocio correspondiente</span></li>
            </ol>
          </div>
          <figcaption>Esquema del flujo de cotización. No es una captura del software.</figcaption>
        </figure>'''


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
    approach = ''
    if project['approach']:
        approach_title, approach_copy = section(project['approach'])
        approach = f'''<section class="story-approach story-section" id="enfoque" aria-labelledby="story-approach-title">
  <div class="container">
    <div class="story-chapter-heading"><p class="story-section-label">El enfoque</p><h2 id="story-approach-title">{html.escape(approach_title)}</h2></div>
    <div class="story-approach-copy story-prose">{approach_copy}</div>
  </div>
</section>'''
    evolution = ''
    if project['evolution']:
        evolution_title, evolution_copy = section(project['evolution'])
        evolution = f'''<section class="story-evolution story-section container" id="evolucion" aria-labelledby="story-evolution-title">
  <h2 id="story-evolution-title">{html.escape(evolution_title)}</h2><div class="story-prose">{evolution_copy}</div>
</section>'''
    return f'''
<section class="story-hero" aria-labelledby="story-title">
  <div class="container">
    <nav class="breadcrumbs" aria-label="Ubicación"><ol><li><a href="/es">Inicio</a></li><li><a href="/es/casos">Casos</a></li><li aria-current="page">{project['name']}</li></ol></nav>
    <div class="story-hero-grid">
      <div class="story-hero-copy">
        <div class="story-identity story-identity-{project['visual']}"><img src="{project['logo']}" alt="{project['name']}" width="{width}" height="{height}"><p>{project['category']}</p></div>
        <h1 id="story-title">{html.escape(meta['H1'])}</h1>
        <div class="story-hero-summary">{opening[0]}</div>
        <a class="text-link" href="#solucion">Explorá la solución</a>
      </div>
      {_visual(project['visual'])}
    </div>
  </div>
</section>
<section class="story-context" aria-labelledby="story-context-title"><div class="container story-context-grid"><h2 id="story-context-title">El contexto</h2><div class="story-prose">{''.join(opening[1:])}</div></div></section>
<section class="story-problem story-section container" id="problema" aria-labelledby="story-problem-title">
  <div class="story-chapter-heading"><p class="story-section-label">El desafío</p><h2 id="story-problem-title">{html.escape(_short_title(problem_title))}</h2></div>
  <div class="story-prose">{problem}</div>
</section>
{approach}
<section class="story-solution story-section" id="solucion" aria-labelledby="story-solution-title">
  <div class="container">
    <div class="story-chapter-heading"><p class="story-section-label">La solución</p><h2 id="story-solution-title">{html.escape(_short_title(solution_title))}</h2></div>
    <div class="story-solution-copy story-prose">{solution}</div>
  </div>
</section>
<section class="story-results story-section" id="resultados" aria-labelledby="story-results-title">
  <div class="container">
    <div class="story-chapter-heading"><p class="story-section-label">Los resultados</p><h2 id="story-results-title">{html.escape(_short_title(results_title))}</h2></div>
    <div class="story-results-copy story-prose">{results}</div>
  </div>
</section>
{evolution}
<section class="story-contact story-section" aria-labelledby="story-contact-title"><div class="container story-contact-grid"><div><h2 id="story-contact-title">{html.escape(contact_title)}</h2><div class="story-prose">{contact}</div></div><div class="story-contact-actions"><a class="button button-dark" href="/es#consulta">Contanos qué necesitás</a><a class="text-link" href="/es/casos">Ver todos los casos</a></div></div></section>
'''
