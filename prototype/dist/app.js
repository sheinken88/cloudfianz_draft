const messages = JSON.parse(document.getElementById('site-messages').textContent);
const siteLocale = document.documentElement.lang.split('-')[0];
const menuButton = document.querySelector('.menu-toggle');
const menu = document.querySelector('#main-nav');
const solutionsMenu = menu.querySelector('.nav-solutions');
function closeMenu() {
  menuButton.setAttribute('aria-expanded', 'false');
  menu.classList.remove('is-open');
  solutionsMenu.open = false;
}
menuButton.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(open));
  menu.classList.toggle('is-open', open);
});
menu.addEventListener('click', (event) => { if (event.target.closest('a')) closeMenu(); });
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && solutionsMenu.open) {
    event.preventDefault();
    solutionsMenu.open = false;
    solutionsMenu.querySelector('summary').focus();
    return;
  }
  if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') {
    closeMenu(); menuButton.focus();
  }
});
document.addEventListener('click', (event) => {
  if (!solutionsMenu.contains(event.target)) solutionsMenu.open = false;
});
solutionsMenu.addEventListener('focusout', (event) => {
  if (event.relatedTarget && !solutionsMenu.contains(event.relatedTarget)) solutionsMenu.open = false;
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
  if (group.hasAttribute('data-progressive-tabs')) {
    activate(tabs[0]);
    tablist.hidden = false;
    group.classList.add('tabs-ready');
  }
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

document.addEventListener('click', (event) => {
  const contactLink = event.target.closest('[data-reader-contact]');
  if (contactLink) {
    if (!document.getElementById('contacto')) return;
    event.preventDefault(); reader.close(); infoDialog.close();
    document.getElementById('contacto').scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' });
    document.querySelector('[data-agenda]').focus({ preventScroll: true });
  }
  if (event.target.closest('[data-agenda]')) {
    event.preventDefault();
    document.querySelector('#info-content').innerHTML = messages.agenda;
    showDialog(infoDialog);
  }
  if (event.target.closest('[data-go-form]')) {
    event.preventDefault(); infoDialog.close();
    document.getElementById('consulta').scrollIntoView({ behavior: 'instant', block: 'start' });
    document.getElementById('hubspot-form-container')?.focus({ preventScroll: true });
  }
  if (event.target.closest('[data-privacy]')) {
    document.querySelector('#info-content').innerHTML = messages.privacy;
    showDialog(infoDialog);
  }
});

// Use the original HubSpot form on both contact entry points.
const hubspotContainer = document.querySelector('#hubspot-form-container');
if (hubspotContainer) {
  const status = document.querySelector('#hubspot-form-status');
  const showError = () => {
    status.hidden = false;
    status.textContent = messages.formError;
  };
  const timeout = window.setTimeout(showError, 20000);
  const script = document.createElement('script');
  script.src = 'https://js.hsforms.net/forms/embed/v2.js';
  script.async = true;
  script.onerror = () => { window.clearTimeout(timeout); showError(); };
  script.onload = () => {
    try {
      window.hbspt.forms.create({
        portalId: '599312',
        formId: '667182f6-5ce1-4df4-baac-b9309cfc78a4',
        region: 'na1',
        locale: siteLocale === 'pt' ? 'pt-br' : siteLocale,
        translations: { [siteLocale === 'pt' ? 'pt-br' : siteLocale]: { fieldLabels: messages.fields, submitText: messages.submit } },
        submitText: messages.submit,
        inlineMessage: messages.thanks,
        target: '#hubspot-form-container',
        onFormReady: ($form) => {
          // Translate only known consent text, preserving inputs, subscription IDs,
          // links, and the meaning of the original HubSpot configuration.
          const form = $form?.nodeType ? $form : $form?.[0];
          const consent = form?.querySelector('.legal-consent-container');
          if (consent) {
            const walker = consent.ownerDocument.createTreeWalker(consent, 4);
            let node;
            while ((node = walker.nextNode())) {
              const source = node.textContent.replace(/\s+/g, ' ').trim();
              const translated = messages.consent[source];
              if (translated) {
                node.textContent = node.textContent.replace(source, translated);
                // HubSpot may insert whitespace inside a sentence.
                if (node.textContent.replace(/\s+/g, ' ').trim() === source) {
                  node.textContent = ` ${translated} `;
                }
              }
            }
          }
          window.clearTimeout(timeout);
          status.hidden = true;
        },
      });
    } catch {
      window.clearTimeout(timeout);
      showError();
    }
  };
  document.head.appendChild(script);
}

// Native details keeps language navigation available without JavaScript.
const languageMenu = document.querySelector('.language-switcher');
if (languageMenu) {
  languageMenu.addEventListener('toggle', () => { if (languageMenu.open) closeMenu(); });
  document.addEventListener('click', (event) => {
    if (!languageMenu.contains(event.target)) languageMenu.open = false;
  });
  languageMenu.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      event.preventDefault();
      languageMenu.open = false;
      languageMenu.querySelector('summary').focus();
    }
  });
  languageMenu.addEventListener('focusout', (event) => {
    if (event.relatedTarget && !languageMenu.contains(event.relatedTarget)) languageMenu.open = false;
  });
  languageMenu.querySelectorAll('a').forEach((link) => {
    // IDs are shared across translations, so section links remain meaningful.
    link.hash = location.hash;
  });
}
