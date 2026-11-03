"""A practical method page: independent engagements, decisions and real examples."""
import html
import re


def _paragraphs(copy):
    return re.findall(r'<p>.*?</p>', copy, re.S)


def _subsections(copy):
    parts = re.split(r'<h3>(.*?)</h3>', copy)
    return parts[0], [(parts[i], parts[i + 1]) for i in range(1, len(parts), 2)]


def _labeled_paragraph(copy, label):
    match = re.search(rf'<p><strong>{re.escape(label)}:</strong> (.*?)</p>', copy, re.S)
    if not match:
        raise ValueError(f'Missing method content: {label}')
    return f'<p>{match.group(1)}</p>'


def build_method(meta, intro, sections, routes):
    def section(prefix):
        return next((title, copy) for title, copy in sections.items() if title.startswith(prefix))

    agreement_title, agreement_copy = section('Qué acordamos')
    _, agreements = _subsections(agreement_copy)
    agreement_rows = ''.join(f'<div><dt>{title}</dt><dd>{copy}</dd></div>' for title, copy in agreements)

    modes_title, modes_copy = section('Elegí la modalidad')
    modes_intro, modes = _subsections(modes_copy)
    if len(modes) != 4:
        raise ValueError('The method page requires four independently contractable modalities')
    hints = ['Evaluar las alternativas', 'Definir la solución', 'Construir y poner en uso', 'Acompañar la operación']
    tabs, panels = [], []
    for i, ((name, copy), hint) in enumerate(zip(modes, hints), 1):
        title = re.sub(r'</?(?:p|strong)>', '', _paragraphs(copy)[0])
        activity = _labeled_paragraph(copy, 'Qué hacemos')
        delivery = _labeled_paragraph(copy, 'Qué recibís')
        participation = _labeled_paragraph(copy, 'Cómo participa tu equipo')
        tabs.append(f'<button type="button" role="tab" id="mp-tab-{i}" aria-controls="mp-panel-{i}" aria-selected="{str(i == 1).lower()}" tabindex="{0 if i == 1 else -1}"><span class="mp-tab-name">{name}</span><span class="mp-tab-hint">{hint}</span></button>')
        panels.append(f'''<div class="mp-panel" id="mp-panel-{i}" role="tabpanel" aria-labelledby="mp-tab-{i}" tabindex="0">
          <h3>{title}</h3>
          <div class="mp-panel-grid">
            <div class="mp-panel-story"><div class="mp-activity"><h4>Qué hacemos</h4>{activity}</div><div class="mp-participation"><h4>Cómo participa tu equipo</h4>{participation}</div></div>
            <aside class="mp-delivery" aria-labelledby="mp-delivery-{i}"><h4 id="mp-delivery-{i}">Qué recibís</h4>{delivery}</aside>
          </div>
        </div>''')

    cases_title, cases_copy = section('Así se aplica')
    _, cases = _subsections(cases_copy)
    brands = [
        '<img class="mp-logo-photonix" src="/assets/brand/photonix-official.svg" alt="Photonix" width="170" height="54" loading="lazy">',
        '<img class="mp-logo-consorcio" src="/assets/brand/consorcio-abierto-official.svg" alt="ConsorcioAbierto" width="216" height="28" loading="lazy">',
    ]
    if len(cases) != len(brands):
        raise ValueError('Method case copy and brand configuration must match')
    case_articles = []
    for (heading, copy), brand in zip(cases, brands):
        title = heading.split(': ', 1)[1]
        title = title[0].upper() + title[1:]
        paragraphs = _paragraphs(copy)
        link = re.search(r'<a [^>]+>.*?</a>', paragraphs[-1], re.S).group(0)
        link = link.replace('<a ', '<a class="case-button" ', 1)
        case_articles.append(f'<article class="mp-example"><div class="mp-example-brand">{brand}</div><h3>{title}</h3><div class="mp-example-copy">{"".join(paragraphs[:-1])}</div>{link}</article>')

    faq_title, faq_copy = section('Preguntas frecuentes')
    _, questions = _subsections(faq_copy)
    faqs = ''.join(f'<details name="mp-questions"><summary>{question}<span class="plus" aria-hidden="true"></span></summary>{answer}</details>' for question, answer in questions)
    contact_title, contact_copy = section('Hablemos')
    contact_paragraphs = _paragraphs(contact_copy)
    contact_url = routes.get('pagina-contacto', '/es/contacto')
    body = f'''
<section class="mp-hero" aria-labelledby="mp-title">
  <div class="container">
    <nav class="breadcrumbs" aria-label="Ubicación"><ol><li><a href="/es">Inicio</a></li><li aria-current="page">Cómo trabajamos</li></ol></nav>
    <div class="mp-hero-grid">
      <div class="mp-hero-copy"><h1 id="mp-title">{html.escape(meta['H1'])}</h1><div class="mp-hero-intro">{_paragraphs(intro)[0]}</div><div class="mp-hero-actions"><a class="button button-dark" href="{contact_url}">Contanos en qué punto estás</a><a class="text-link" href="#mp-modalidades">Ver modalidades de trabajo</a></div></div>
      <aside class="mp-agreement" aria-labelledby="mp-agreement-title"><h2 id="mp-agreement-title">{agreement_title}</h2><dl>{agreement_rows}</dl></aside>
    </div>
  </div>
</section>
<section class="mp-modalities mp-section" id="mp-modalidades" aria-labelledby="mp-modes-title"><div class="container">
  <div class="mp-section-intro"><h2 id="mp-modes-title">{modes_title}</h2>{modes_intro}</div>
  <div class="mp-process" data-tabs data-progressive-tabs>
    <div class="mp-tabs" role="tablist" aria-label="Modalidades de trabajo" hidden>{''.join(tabs)}</div>
    <div class="mp-panels">{''.join(panels)}</div>
  </div>
</div></section>
<section class="mp-examples mp-section" aria-labelledby="mp-examples-title"><div class="container"><h2 id="mp-examples-title">{cases_title}</h2><div class="mp-example-list">{''.join(case_articles)}</div></div></section>
<section class="mp-faq mp-section container" aria-labelledby="mp-faq-title"><h2 id="mp-faq-title">{faq_title}</h2><div class="faq-list">{faqs}</div></section>
<section class="mp-contact mp-section" aria-labelledby="mp-contact-title"><div class="container mp-contact-grid"><div><h2 id="mp-contact-title">{contact_title}</h2>{contact_paragraphs[0]}</div><div class="mp-contact-action"><a class="button" href="{contact_url}">Contanos en qué punto estás</a>{''.join(contact_paragraphs[1:])}</div></div></section>
'''
    # Supports existing content rendering as well as the full native route table.
    for key, route in routes.items():
        body = body.replace(f'href="#{key}" data-content="{key}"', f'href="{route}"')
    return body
