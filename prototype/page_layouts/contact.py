"""A focused contact page using the prototype's existing form behavior."""
import html
from pathlib import Path


def build_contact(meta, intro, sections, routes):
    next_title, next_copy = next(
        (title, copy) for title, copy in sections.items()
        if title.startswith('Qué pasa después')
    )
    contact_form = (Path(__file__).resolve().parents[1] / 'templates/contact-form.html').read_text().strip()
    return f'''
<section class="cp-section" aria-labelledby="cp-title">
  <div class="container">
    <nav class="breadcrumbs" aria-label="Ubicación"><ol><li><a href="/es">Inicio</a></li><li aria-current="page">Contacto</li></ol></nav>
    <div class="cp-grid">
      <div class="cp-copy">
        <h1 id="cp-title">{html.escape(meta['H1'])}</h1>
        <div class="cp-intro">{intro}</div>
      </div>
      <div class="cp-form-panel" id="consulta">
        <h2 id="cp-form-title">Tu consulta</h2>
        {contact_form}
      </div>
      <div class="cp-next" aria-labelledby="cp-next-title">
        <h2 id="cp-next-title">{html.escape(next_title)}</h2>
        <div>{next_copy}</div>
      </div>
    </div>
  </div>
</section>
'''
