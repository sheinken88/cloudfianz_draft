// Enhance the original, keyboard-accessible client list with a seamless loop.
const clientStrip = document.querySelector('[data-client-marquee]');
if (clientStrip) {
  const track = clientStrip.querySelector('.home-client-track');
  const clients = track.querySelector('.home-client-logos');
  const copy = clients.cloneNode(true);
  copy.setAttribute('aria-hidden', 'true');
  copy.querySelectorAll('a').forEach(link => { link.tabIndex = -1; });
  track.append(copy);
  clientStrip.classList.add('is-enhanced');

  function syncPageVisibility() {
    clientStrip.classList.toggle('is-inactive', document.hidden);
  }
  document.addEventListener('visibilitychange', syncPageVisibility);
  syncPageVisibility();
}
