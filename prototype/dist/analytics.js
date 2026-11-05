// Local event queue only. No tracker, cookies, network calls or form field values.
// Connect a consent-aware analytics provider at launch; filter out preview events.
(() => {
  const allowed = new Set(['contact_cta_click', 'meeting_intent', 'generate_lead']);
  const meta = name => document.querySelector(`meta[name="${name}"]`)?.content;
  let leadRecorded = false;
  window.cloudfianzTrack = event => {
    if (!allowed.has(event) || (event === 'generate_lead' && leadRecorded)) return;
    if (event === 'generate_lead') leadRecorded = true;
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      event,
      site_environment: meta('site-environment') || 'preview',
      page_key: meta('site-page'),
      page_language: document.documentElement.lang,
      // Canonical pathname excludes arbitrary query strings, hashes and user data.
      page_path: new URL(document.querySelector('link[rel="canonical"]').href).pathname,
      form_location: meta('site-page') === 'home' ? 'home' : 'contact',
    });
  };
  document.addEventListener('click', event => {
    const link = event.target.closest('a');
    if (!link) return;
    if (link.hasAttribute('data-agenda')) {
      window.cloudfianzTrack('meeting_intent'); // Intent, never a confirmed booking.
    } else if (/^\/(es\/contacto|en\/contact|pt\/contato)$/.test(new URL(link.href).pathname) || link.hasAttribute('data-go-form')) {
      window.cloudfianzTrack('contact_cta_click');
    }
  });
})();
