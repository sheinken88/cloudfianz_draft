"""REVIANZ case with the product’s official illustrative mockups."""
import html
import re
from page_layouts.revianz_mockups import mockup


def build_revianz(meta, intro, sections, routes):
    def section(prefix):
        return next((title, copy) for title, copy in sections.items() if title.startswith(prefix))

    opening = re.findall(r'<p>.*?</p>', intro, re.S)[0]
    challenge_title, challenge = section('El desafío')
    solution_title, solution = section('La solución')
    parts = re.split(r'<h3>(.*?)</h3>', solution)
    margin_title, margin = parts[1:3]
    billing_title, billing = parts[3:5]
    collaboration_title, collaboration = parts[5:7]
    results_title, results = section('Qué permite')
    results_intro = re.findall(r'<p>.*?</p>', results, re.S)[0]
    results_items = re.findall(r'<li>(.*?)</li>', results, re.S)
    outcomes = ''.join('<li>' + re.sub(r'^<strong>(.*?)\.</strong>\s*(.*)$', r'<h3>\1</h3><p>\2</p>', item, flags=re.S) + '</li>' for item in results_items)
    product_link = re.search(r'<a href="https://revianz\.com/"[^>]*>.*?</a>', results).group()
    product_link = product_link.replace('<a ', '<a class="button rv-product-cta" aria-label="Conocé REVIANZ (nueva pestaña)" ', 1)
    contact_title, contact = section('¿Tu operación')
    report = mockup('scope')
    preview = mockup('margin')
    invoice = mockup('invoice')
    collaboration_preview = mockup('share')
    return f'''
<section class="rv-hero">
  <div class="container">
    <nav class="breadcrumbs" aria-label="Ubicación"><ol><li><a href="/es">Inicio</a></li><li><a href="/es/casos">Casos</a></li><li aria-current="page">REVIANZ para Digifianz</li></ol></nav>
    <div class="rv-cover"><div><p class="rv-context">REVIANZ · Desarrollado para Digifianz</p><h1>{html.escape(meta['H1'])}</h1><div class="rv-summary">{opening}</div></div><dl class="rv-facts"><div><dt>Cliente</dt><dd>Digifianz</dd></div><div><dt>Trabajo de Cloudfianz</dt><dd>Desarrollo de software a medida</dd></div><div><dt>Producto</dt><dd>Gestión operativa y financiera de proyectos<br><a class="rv-product-link" href="https://revianz.com/" target="_blank" rel="noopener noreferrer" aria-label="Visitar revianz.com (nueva pestaña)">Visitar revianz.com</a></dd></div></dl></div>
    {report}
  </div>
</section>
<section class="rv-context-section container" id="contexto" aria-labelledby="rv-context-title"><div class="rv-context-copy"><h2 id="rv-context-title">{challenge_title.split(': ', 1)[1].capitalize()}</h2><div class="page-prose">{challenge}</div></div>{collaboration_preview}</section>
<section class="rv-product"><div class="container">
  <div class="rv-product-heading"><p class="rv-context">La solución</p><h2>{solution_title.split(': ', 1)[1].capitalize()}</h2><div class="page-prose">{parts[0]}</div></div>
  <div class="rv-margin"><div><h3>{margin_title}</h3><div class="page-prose">{margin}</div><p class="rv-detail-note">La vista de margen relaciona ingresos y costo de entrega para entender el resultado del proyecto.</p></div>{preview}</div>
  <div class="rv-billing">{invoice}<div><h3>{billing_title}</h3><div class="page-prose">{billing}</div><h3>{collaboration_title}</h3><div class="page-prose">{collaboration}</div></div></div>
</div></section>
<section class="rv-results" id="resultados" aria-labelledby="rv-results-title"><div class="container rv-results-inner"><div class="rv-results-heading"><h2 id="rv-results-title">Una base compartida para decidir.</h2>{results_intro}</div><ul class="rv-outcomes">{outcomes}</ul><div class="rv-results-action">{product_link}</div></div></section>
<section class="page-contact" aria-labelledby="next-title"><div class="container page-contact-inner"><div><h2 id="next-title">{contact_title}</h2>{contact}</div><div class="page-contact-actions"><a class="button button-dark" href="/es/contacto">Hablemos de tu negocio</a><a class="text-link" href="/es/casos">Ver todos los casos</a></div></div></section>
'''
