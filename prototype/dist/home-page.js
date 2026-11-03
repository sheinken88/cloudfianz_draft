// Enhance the original, keyboard-accessible client list with a seamless loop.
const clientStrip = document.querySelector('[data-client-marquee]');
if (clientStrip) {
  const track = clientStrip.querySelector('.home-client-track');
  const clients = track.querySelector('.home-client-logos');
  const toggle = clientStrip.querySelector('.home-client-toggle');
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  const copy = clients.cloneNode(true);
  copy.setAttribute('aria-hidden', 'true');
  copy.querySelectorAll('a').forEach(link => { link.tabIndex = -1; });
  track.append(copy);
  clientStrip.classList.add('is-enhanced');

  function syncMotionPreference() {
    toggle.hidden = reducedMotion.matches;
  }
  toggle.addEventListener('click', () => {
    const paused = clientStrip.dataset.paused !== 'true';
    clientStrip.dataset.paused = String(paused);
    toggle.setAttribute('aria-label', paused
      ? 'Reanudar movimiento de logos'
      : 'Pausar movimiento de logos');
  });
  reducedMotion.addEventListener('change', syncMotionPreference);
  syncMotionPreference();

  function syncPageVisibility() {
    clientStrip.classList.toggle('is-inactive', document.hidden);
  }
  document.addEventListener('visibilitychange', syncPageVisibility);
  syncPageVisibility();
}
