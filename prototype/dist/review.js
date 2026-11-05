const frame = document.querySelector('#site');
const wrap = document.querySelector('.frame-wrap');
const preview = document.querySelector('.preview');
const desktop = document.querySelector('#desktop');
const mobile = document.querySelector('#mobile');
const sizes = document.querySelector('#size');
let mode = 'desktop';
function layout() {
  const width = Number(sizes.value);
  const padding = mode === 'mobile' ? 32 : 36;
  const scale = Math.min(1, (preview.clientWidth - padding) / width);
  const height = Math.max(300, (preview.clientHeight - 36) / scale);
  frame.style.width = `${width}px`;
  frame.style.height = `${height}px`;
  frame.style.transform = `scale(${scale})`;
  wrap.style.width = `${width * scale}px`;
  wrap.style.height = `${height * scale}px`;
  document.querySelector('.dimension').textContent = `${width} px · ${Math.round(scale * 100)} %`;
}
function setMode(next) {
  mode = next;
  desktop.setAttribute('aria-pressed', String(mode === 'desktop'));
  mobile.setAttribute('aria-pressed', String(mode === 'mobile'));
  preview.classList.toggle('mobile', mode === 'mobile');
  const values = mode === 'desktop' ? [1440, 1280, 1024, 768] : [390, 360, 430];
  sizes.replaceChildren(...values.map((width) => new Option(`${width} px`, width)));
  layout();
}
desktop.addEventListener('click', () => setMode('desktop'));
mobile.addEventListener('click', () => setMode('mobile'));
sizes.addEventListener('change', layout);
new ResizeObserver(layout).observe(preview);
layout();

const pages = document.querySelector('#page');
const openPage = document.querySelector('#open-page');
const locale = document.querySelector('#locale');
const originalPages = [...pages.options].map(option => ({label: option.textContent, path: option.value}));
fetch('/localized-routes.json').then(response => response.json()).then(routes => {
  const groups = Object.values(routes);
  function refreshOptions(code, current) {
    pages.replaceChildren(...originalPages.map(item => {
      const paths = groups.find(group => group.es === item.path);
      return new Option(item.label, paths[code]);
    }));
    pages.value = current;
    openPage.href = current;
  }
  locale.addEventListener('change', () => {
    const paths = groups.find(group => Object.values(group).includes(pages.value));
    const next = paths[locale.value];
    refreshOptions(locale.value, next);
    frame.src = next;
  });
  pages.addEventListener('change', () => {
    frame.src = pages.value;
    openPage.href = pages.value;
  });
  frame.addEventListener('load', () => {
    try {
      const current = frame.contentWindow.location.pathname;
      const code = current.split('/')[1];
      if (groups.some(group => group[code] === current)) {
        locale.value = code;
        refreshOptions(code, current);
      }
    } catch { /* Only same-origin preview navigation is tracked. */ }
  });
});
