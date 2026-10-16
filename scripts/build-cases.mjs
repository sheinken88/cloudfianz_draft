#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const casesPath = path.join(root, 'src/data/cases.json');
const indexPath = path.join(root, 'src/index.html');

function esc(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function bi(field) {
  return `<span data-es>${esc(field.es)}</span><span data-en>${esc(field.en)}</span>`;
}

function logoHtml(c) {
  const src = c.logoImage
    ?? (c.logo && /\.(png|jpe?g|svg|webp|gif|avif)$/i.test(c.logo) ? c.logo : null);
  if (src) {
    const colorClass = c.logoColor ? ' case-logo-img--color' : '';
    return `<img src="${esc(src)}" alt="${esc(c.title.en)}" class="case-logo-img${colorClass}">`;
  }
  return `<div class="case-logo">${esc(c.logo ?? 'CLIENT')}</div>`;
}

function renderCase(c, index) {
  const logo = logoHtml(c);

  const stats = (c.stats ?? [])
    .map((s) => `<div><b>${esc(s.value)}</b>${bi(s.label)}</div>`)
    .join('');

  const detailBtn = c.detail
    ? `\n          <button type="button" class="case-more" onclick="openCaseModal(${index})"><span data-es>Ver más</span><span data-en>Learn more</span> →</button>`
    : '';

  return `      <div class="case">
        <div class="case-top">${logo}</div>
        <div class="case-body">
          <div class="cat">${bi(c.category)}</div>
          <h4>${bi(c.title)}</h4>
          <p>${bi(c.description)}</p>
          <div class="case-stat">${stats}</div>${detailBtn}
        </div>
      </div>`;
}

function renderCasesData(cases) {
  const payload = cases.map((c) => ({
    category: c.category,
    title: c.title,
    logoImage: c.logoImage ?? null,
    logoColor: Boolean(c.logoColor),
    detail: c.detail ?? null,
  }));
  return `<script type="application/json" id="cases-data">\n${JSON.stringify(payload)}\n</script>`;
}

function renderJsonLd(cases) {
  const itemList = {
    '@context': 'https://schema.org',
    '@type': 'ItemList',
    name: 'Cloudfianz Case Studies',
    itemListElement: cases.map((c, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      item: {
        '@type': 'CreativeWork',
        name: c.title.en,
        description: c.description.en,
        about: c.category.en,
      },
    })),
  };
  return `<script type="application/ld+json">\n${JSON.stringify(itemList)}\n</script>`;
}

function replaceBlock(html, startMarker, endMarker, content) {
  const start = html.indexOf(startMarker);
  const end = html.indexOf(endMarker);
  if (start === -1 || end === -1 || end <= start) {
    throw new Error(`Marcadores no encontrados: ${startMarker} / ${endMarker}`);
  }
  return (
    html.slice(0, start + startMarker.length) +
    '\n' +
    content +
    '\n' +
    html.slice(end)
  );
}

const cases = JSON.parse(fs.readFileSync(casesPath, 'utf8'));
const casesHtml = cases.map(renderCase).join('\n');
const casesData = renderCasesData(cases);
const casesLd = renderJsonLd(cases);

let html = fs.readFileSync(indexPath, 'utf8');
html = replaceBlock(html, '<!-- CASES:START -->', '<!-- CASES:END -->', casesHtml);
html = replaceBlock(html, '<!-- CASES-DATA:START -->', '<!-- CASES-DATA:END -->', casesData);
html = replaceBlock(html, '<!-- CASES-LD:START -->', '<!-- CASES-LD:END -->', casesLd);

fs.writeFileSync(indexPath, html, 'utf8');

const esDir = path.join(root, 'src/es');
fs.mkdirSync(esDir, { recursive: true });
fs.copyFileSync(indexPath, path.join(esDir, 'index.html'));

console.log(`Build cases: ${cases.length} caso(s) inyectados en index.html`);
