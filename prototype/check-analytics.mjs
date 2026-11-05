// Verify privacy and conversion semantics without sending a real HubSpot lead.
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import vm from 'node:vm';
const script = await readFile(new URL('./dist/analytics.js', import.meta.url), 'utf8');
for (const environment of ['preview', 'production', undefined]) {
  const window = {};
  const handlers = {};
  const document = {
    documentElement: {lang:'pt-BR'},
    querySelector: selector => ({
      'meta[name="site-environment"]': environment ? {content:environment} : undefined,
      'meta[name="site-page"]': {content:'home'},
      'link[rel="canonical"]': {href:'https://cloudfianz.com/pt'},
    })[selector],
    addEventListener: (event, handler) => { handlers[event] = handler; },
  };
  vm.runInNewContext(script, {window, document, URL});
  const click = (href, attributes=[]) => handlers.click({target:{closest:()=>({href,hasAttribute:name=>attributes.includes(name)})}});
  click('https://cloudfianz.com/pt/contato?email=private@example.com#private');
  click('https://cloudfianz.com/pt#agenda', ['data-agenda']);
  assert.equal(window.dataLayer.length, 2);
  assert.equal(window.dataLayer[1].event, 'meeting_intent');
  assert.ok(!window.dataLayer.some(row=>row.event === 'generate_lead'));
  window.cloudfianzTrack('generate_lead', {email:'private@example.com'});
  window.cloudfianzTrack('generate_lead');
  window.cloudfianzTrack('invalid_event');
  assert.equal(window.dataLayer.length, 3);
  assert.equal(window.dataLayer[2].event, 'generate_lead');
  assert.equal(window.dataLayer[2].page_path, '/pt');
  assert.equal(window.dataLayer[2].site_environment, environment || 'preview');
  assert.ok(!JSON.stringify(window.dataLayer).includes('private'));
}
console.log('PASS: contact intent, success-only conversion queue, deduplication, preview fallback and no form/query data.');
