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
