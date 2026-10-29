const menuButton = document.querySelector('.menu-toggle');
const menu = document.querySelector('#main-nav');
function closeMenu() {
  menuButton.setAttribute('aria-expanded', 'false');
  menu.classList.remove('is-open');
}
menuButton.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(open));
  menu.classList.toggle('is-open', open);
});
menu.addEventListener('click', (event) => { if (event.target.closest('a')) closeMenu(); });
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') {
    closeMenu(); menuButton.focus();
  }
});
matchMedia('(min-width: 800px)').addEventListener('change', closeMenu);

document.querySelectorAll('[data-tabs]').forEach((group) => {
  const tabs = [...group.querySelectorAll('[role="tab"]')];
  const tablist = group.querySelector('[role="tablist"]');
  if (tablist.classList.contains('solution-tablist')) {
    const narrow = matchMedia('(max-width: 799px)');
    const syncOrientation = () => tablist.setAttribute('aria-orientation', narrow.matches ? 'horizontal' : 'vertical');
    syncOrientation();
    narrow.addEventListener('change', syncOrientation);
  }
  function activate(tab, focus = false) {
    tabs.forEach((item) => {
      const active = item === tab;
      item.setAttribute('aria-selected', String(active));
      item.tabIndex = active ? 0 : -1;
      document.getElementById(item.getAttribute('aria-controls')).hidden = !active;
    });
    if (focus) tab.focus();
  }
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => activate(tab));
    tab.addEventListener('keydown', (event) => {
      let next;
      const vertical = tablist.getAttribute('aria-orientation') === 'vertical';
      if (event.key === 'ArrowRight' || (vertical && event.key === 'ArrowDown')) next = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft' || (vertical && event.key === 'ArrowUp')) next = (index + tabs.length - 1) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next !== undefined) { event.preventDefault(); activate(tabs[next], true); }
    });
  });
});

const reader = document.querySelector('#reader-dialog');
const infoDialog = document.querySelector('#info-dialog');
const dialogs = [reader, infoDialog];
function showDialog(dialog) {
  closeMenu();
  dialogs.forEach((other) => { if (other !== dialog && other.open) other.close(); });
  if (!dialog.open) dialog.showModal();
  document.body.classList.add('dialog-open');
  dialog.scrollTop = 0;
}
dialogs.forEach((dialog) => {
  dialog.querySelector('.close-dialog').addEventListener('click', () => dialog.close());
  dialog.addEventListener('close', () => {
    if (!dialogs.some((item) => item.open)) document.body.classList.remove('dialog-open');
  });
  dialog.addEventListener('click', (event) => {
    if (event.target === dialog) {
      const bounds = dialog.getBoundingClientRect();
      if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
    }
  });
});

let contentRequest;
async function openContent(key) {
  const target = document.querySelector('#reader-content');
  target.innerHTML = '<h1 id="reader-title">Contenido del proyecto</h1><p>Cargando el contenido…</p>';
  showDialog(reader);
  try {
    contentRequest ??= fetch('/content.json').then((response) => {
      if (!response.ok) throw new Error('No se pudo cargar el contenido');
      return response.json();
    }).catch((error) => { contentRequest = undefined; throw error; });
    const contents = await contentRequest;
    if (!contents[key]) throw new Error('Contenido no disponible');
    target.innerHTML = contents[key];
    reader.scrollTop = 0;
  } catch {
    target.innerHTML = '<h1 id="reader-title">No pudimos cargar el texto.</h1><p>Cerrá esta ventana e intentá abrir el caso o servicio de nuevo.</p>';
  }
}
document.addEventListener('click', (event) => {
  const contentLink = event.target.closest('[data-content]');
  if (contentLink) { event.preventDefault(); openContent(contentLink.dataset.content); }
  const contactLink = event.target.closest('[data-reader-contact]');
  if (contactLink) {
    if (!document.getElementById('contacto')) return;
    event.preventDefault(); reader.close(); infoDialog.close();
    document.getElementById('contacto').scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' });
    document.querySelector('[data-agenda]').focus({ preventScroll: true });
  }
  if (event.target.closest('[data-agenda]')) {
    event.preventDefault();
    document.querySelector('#info-content').innerHTML = '<p class="info-caption">Vista previa de la agenda</p><h2 id="info-title">Hablemos de tu negocio.</h2><p>Contanos qué querés mejorar y evaluemos cómo podemos ayudarte.</p><p>En la web publicada, este paso permitirá coordinar una reunión con Cloudfianz. La agenda todavía no está conectada en esta propuesta local.</p><a class="button" href="#consulta" data-go-form>Prefiero enviar una consulta </a>';
    showDialog(infoDialog);
  }
  if (event.target.closest('[data-go-form]')) {
    event.preventDefault(); infoDialog.close();
    document.getElementById('consulta').scrollIntoView({ behavior: 'instant', block: 'start' });
    document.getElementById('name').focus({ preventScroll: true });
  }
  if (event.target.closest('[data-privacy]')) {
    document.querySelector('#info-content').innerHTML = '<p class="info-caption">Propuesta local</p><h2 id="info-title">Privacidad</h2><p>Este prototipo no envía ni guarda los datos del formulario y no incluye herramientas de analítica.</p><p>La política de privacidad y los avisos del sitio se completarán al definir la recepción de consultas, la agenda y la medición, antes de publicar.</p>';
    showDialog(infoDialog);
  }
});

document.querySelector('#contact-form')?.addEventListener('submit', (event) => {
  event.preventDefault();
  const status = document.querySelector('#form-status');
  status.textContent = 'Prueba completada. En el sitio publicado recibirías la confirmación de tu consulta y el equipo continuaría la conversación por email. Esta prueba no envió ni guardó tus datos.';
  status.hidden = false;
  status.scrollIntoView({ behavior: 'instant', block: 'nearest' });
});
document.querySelector('#contact-form')?.addEventListener('input', () => { document.querySelector('#form-status').hidden = true; });
