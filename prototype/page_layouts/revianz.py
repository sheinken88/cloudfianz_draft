"""REVIANZ case: documented capabilities and unmodified product captures."""
import html
import re


def build_revianz(meta, intro, sections, routes):
    def section(prefix):
        return next((title, copy) for title, copy in sections.items() if title.startswith(prefix))

    def figure(filename, alt, width, height, caption, name, priority=False):
        src = '/assets/projects/' + filename
        loading = 'fetchpriority="high"' if priority else 'loading="lazy"'
        return f'''<figure class="rv-capture"><a href="{src}" target="_blank" rel="noopener" aria-label="Ampliar {name} (nueva pestaña)"><img src="{src}" alt="{alt}" width="{width}" height="{height}" {loading} decoding="async"></a><figcaption><span>{caption}</span><a href="{src}" target="_blank" rel="noopener" aria-label="Ver {name} a tamaño completo (nueva pestaña)">Ampliar captura</a></figcaption></figure>'''

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
    outcomes = ''.join(f'<li>{item}</li>' for item in results_items)
    evolution_title, evolution = section('Software que acompaña')
    contact_title, contact = section('¿Tu operación')
    report = figure('revianz-rentabilidad-original.jpg', 'Reporte real de REVIANZ: rentabilidad por proyecto con ingresos, costos, comisiones y margen, en el entorno de demostración.', 1920, 650, 'Rentabilidad por proyecto. Captura del entorno de demostración de REVIANZ.', 'reporte de rentabilidad de REVIANZ', True)
    preview = figure('revianz-margen-original.jpg', 'Vista previa de un proyecto de demostración en REVIANZ: margen mensual, monto, comisiones y servicios.', 580, 960, 'Vista previa del margen. Datos de demostración.', 'vista de margen de REVIANZ')
    invoice = figure('revianz-facturacion-original.jpg', 'Generación de una factura en REVIANZ, con consolidación, fechas y términos de pago en un entorno de prueba.', 1140, 940, 'Generación de factura vinculada al cliente. Datos de demostración.', 'facturación de REVIANZ')
    return f'''
<section class="rv-hero">
  <div class="container">
    <nav class="breadcrumbs" aria-label="Ubicación"><ol><li><a href="/es">Inicio</a></li><li><a href="/es#casos">Casos</a></li><li aria-current="page">REVIANZ para Digifianz</li></ol></nav>
    <div class="rv-cover"><div><p class="rv-context">REVIANZ · Desarrollado para Digifianz</p><h1>{html.escape(meta['H1'])}</h1><div class="rv-summary">{opening}</div></div><dl class="rv-facts"><div><dt>Cliente</dt><dd>Digifianz</dd></div><div><dt>Trabajo de Cloudfianz</dt><dd>Desarrollo de software a medida</dd></div><div><dt>Producto</dt><dd>Gestión operativa y financiera de proyectos</dd></div></dl></div>
    {report}
    <p class="rv-demo-note">Los importes de las capturas ilustran el funcionamiento del producto; no representan resultados financieros de Digifianz.</p>
  </div>
</section>
<section class="rv-context-section container"><h2>{challenge_title.split(': ', 1)[1].capitalize()}</h2><div class="page-prose">{challenge}</div></section>
<section class="rv-product"><div class="container">
  <div class="rv-product-heading"><p class="rv-context">La solución</p><h2>{solution_title.split(': ', 1)[1].capitalize()}</h2><div class="page-prose">{parts[0]}</div></div>
  <div class="rv-margin"><div><h3>{margin_title}</h3><div class="page-prose">{margin}</div><p class="rv-detail-note">El detalle del proyecto reúne servicios, importes y comisiones para leer el margen en contexto.</p></div>{preview}</div>
  <div class="rv-billing">{invoice}<div><h3>{billing_title}</h3><div class="page-prose">{billing}</div><h3>{collaboration_title}</h3><div class="page-prose">{collaboration}</div></div></div>
</div></section>
<section class="rv-results"><div class="container"><div class="rv-results-heading"><h2>Una base compartida para decidir.</h2><div>{results_intro}</div></div><ul>{outcomes}</ul><div class="rv-evolution"><h3>{evolution_title}</h3><div>{evolution}</div></div></div></section>
<section class="page-contact" aria-labelledby="next-title"><div class="container page-contact-inner"><div><h2 id="next-title">{contact_title}</h2>{contact}</div><div class="page-contact-actions"><a class="button button-dark" href="/es#contacto">Hablemos de tu negocio</a><a class="text-link" href="/es#consulta">Prefiero enviar una consulta</a></div></div></section>
'''
