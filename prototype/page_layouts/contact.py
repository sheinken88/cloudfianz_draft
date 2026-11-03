"""A focused contact page using the prototype's existing form behavior."""
import html


def build_contact(meta, intro, sections, routes):
    next_title, next_copy = next(
        (title, copy) for title, copy in sections.items()
        if title.startswith('Qué pasa después')
    )
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
        <form id="contact-form" aria-labelledby="cp-form-title" aria-describedby="cp-form-note">
          <div class="cp-form-row">
            <div class="cp-field"><label for="name">Nombre</label><input id="name" name="nombre" type="text" autocomplete="name" required maxlength="100"></div>
            <div class="cp-field"><label for="company">Empresa</label><input id="company" name="empresa" type="text" autocomplete="organization" required maxlength="120"></div>
          </div>
          <div class="cp-field"><label for="email">Email de trabajo</label><input id="email" name="email" type="email" autocomplete="email" required maxlength="254"></div>
          <div class="cp-field"><label for="message">¿Qué necesitás resolver?</label><textarea id="message" name="consulta" rows="4" required maxlength="3000" aria-describedby="message-help"></textarea><p class="cp-field-help" id="message-help">Contanos cómo lo resolvés hoy y qué te gustaría cambiar. Con unas líneas alcanza.</p></div>
          <button class="button button-dark cp-submit" type="submit">Enviar consulta</button>
          <p class="cp-form-note" id="cp-form-note">Propuesta local: este formulario permite probar el recorrido. No envía ni guarda tus datos.</p>
          <div id="form-status" class="cp-status" role="status" hidden></div>
        </form>
      </div>
      <div class="cp-next" aria-labelledby="cp-next-title">
        <h2 id="cp-next-title">{html.escape(next_title)}</h2>
        <div>{next_copy}</div>
      </div>
    </div>
  </div>
</section>
'''
