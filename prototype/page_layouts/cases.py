"""A compact case directory, with one project per card and real page destinations."""
import html
import re
from page_layouts.case_previews import case_preview


PROJECTS = [
    ('caso-despegar', 'Despegar Ads', 'Software a medida · Integración', 'despegar-digifianz.png', 180, 52, 'despegar'),
    ('caso-revianz', 'REVIANZ para Digifianz', 'Software a medida', None, 0, 0, 'revianz'),
    ('caso-properix', 'ConsorcioAbierto', 'Integración · Automatización', 'consorcio-abierto-official.svg', 216, 28, 'properix'),
    ('caso-photonix', 'Photonix', 'Software a medida', 'photonix-official.svg', 650, 205, 'photonix'),
    ('caso-escala24x7', 'Escala24x7', 'Integración de sistemas', 'escala24x7-original.avif', 1275, 784, 'escala'),
    ('caso-ads-mexicana', 'ADS Mexicana', 'Software a medida · Automatización', 'ads-mexicana-original.png', 938, 410, 'ads'),
]


def build_cases(meta, intro, sections, routes):
    cards = []
    for key, section, category, asset, width, height, slug in PROJECTS:
        copy = sections[section]
        title = re.search(r'<h3>(.*?)</h3>', copy, re.S).group(1)
        paragraphs = re.findall(r'<p>.*?</p>', copy, re.S)
        summary = ''.join(paragraphs[:-1])
        label = re.search(r'<a [^>]+>(.*?)</a>', paragraphs[-1]).group(1)
        if asset:
            dimensions = f' width="{width}" height="{height}"' if width and height else ''
            brand = f'<img src="/assets/brand/{asset}" alt="{html.escape(section)}"{dimensions} loading="lazy">'
        else:
            brand = '<span class="cases-revianz-brand" role="img" aria-label="REVIANZ"><span aria-hidden="true">RZ</span><strong aria-hidden="true">Revianz</strong></span>'
        preview = case_preview(key)
        if key == 'caso-despegar':
            preview = preview.replace('loading="lazy"', 'fetchpriority="high"')
        cards.append(f'''<article class="cases-card cases-card--{slug}" aria-labelledby="{key}-title">
          {preview}
          <div class="cases-card-copy">
            <div class="cases-card-brand">{brand}</div>
            <p class="cases-card-category">{category}</p>
            <h2 id="{key}-title">{title}</h2>
            <div class="cases-card-summary">{summary}</div>
            <div class="cases-card-action"><a class="case-button" href="{routes[key]}">{label}</a></div>
          </div>
        </article>''')
    closing_title = next(title for title in sections if title.startswith('¿Reconocés'))
    return f'''
<section class="cases-hero" aria-labelledby="cases-hero-title">
  <div class="container">
    <nav class="breadcrumbs" aria-label="Ubicación"><ol><li><a href="/es">Inicio</a></li><li aria-current="page">Casos</li></ol></nav>
    <div class="cases-hero-heading">
      <h1 id="cases-hero-title">{html.escape(meta['H1'])}</h1>
      <div class="cases-hero-intro">{intro}</div>
    </div>
  </div>
</section>
<section class="cases-collection" id="proyectos" aria-label="Proyectos de nuestros clientes"><div class="container cases-grid">{''.join(cards)}</div></section>
<section class="page-contact cases-contact" aria-labelledby="cases-contact-title"><div class="container page-contact-inner"><h2 id="cases-contact-title">{closing_title}</h2>{sections[closing_title]}<div class="page-contact-actions"><a class="button button-dark" href="/es#consulta">Contanos qué necesitás</a><a class="text-link" href="/es#soluciones">Conocé nuestras soluciones</a></div></div></section>
'''
