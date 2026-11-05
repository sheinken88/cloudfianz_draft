"""Regression checks for localized static output; standard library only."""
import json
import sys
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from render import Localizer, LOCALES
from seo import HREFLANG
ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
routes = json.loads((ROOT / 'i18n/routes.json').read_text())
spanish_routes = json.loads((ROOT / 'page-routes.json').read_text())
assert set(routes) == {'home', *spanish_routes}
for key, path in spanish_routes.items():
    assert routes[key]['es'] == path
paths = {v for group in routes.values() for v in group.values()}
assert len(paths) == len(routes) * 3
vercel = json.loads((ROOT.parent / 'vercel.json').read_text())
assert paths == {item['source'] for item in vercel['rewrites']}

class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(); self.tags=[]; self.ids=set(); self.feed(source)
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); self.tags.append((tag,a))
        if 'id' in a:
            assert a['id'] not in self.ids, f'Duplicate id {a["id"]}'
            self.ids.add(a['id'])

pages={}
for path in paths:
    source=(DIST / path.lstrip('/') / 'index.html').read_text()
    pages[path]=Page(source)
    assert '<!-- LANGUAGE_SWITCHER -->' not in source
    assert 'data-content=' not in source, f'Legacy reader link in {path}'
    assert 'id="site-messages"' in source
for key, group in routes.items():
    assert set(group)==set(LOCALES)
    for code,path in group.items():
        tags=pages[path].tags
        assert next(a['lang'] for t,a in tags if t=='html')==LOCALES[code][0]
        canonical=[a['href'] for t,a in tags if t=='link' and a.get('rel')=='canonical']
        assert canonical==['https://cloudfianz.com'+path]
        alternates={a['hreflang']:a['href'] for t,a in tags if t=='link' and a.get('rel')=='alternate'}
        for language,(tag,_) in LOCALES.items():
            assert alternates[HREFLANG[language]]=='https://cloudfianz.com'+group[language]
        assert any(t=='a' and a.get('aria-current')=='true' and a.get('href')==path for t,a in tags)
        for t,a in tags:
            if t!='a' or 'href' not in a: continue
            href=a['href']; url=urlsplit(href)
            if url.scheme or url.netloc: continue
            destination=url.path or path
            if destination in paths:
                if 'hreflang' not in a:
                    assert destination.split('/')[1]==code, (path,href)
                if url.fragment and 'data-agenda' not in a:
                    assert url.fragment in pages[destination].ids, (path,href)
            elif href.startswith('/'):
                assert (DIST / destination.lstrip('/')).is_file(), (path,href)

# A changed source must NOT silently use stale translations.
p=Localizer('en', {'Texto anterior':'Previous text'}, {})
p.feed('<p>Nuevo texto sin traducción</p><img alt="Nueva descripción">')
assert p.missing=={'Nuevo texto sin traducción','Nueva descripción'}
p=Localizer('pt', {'Texto':'Texto traduzido'}, {})
p.feed('<p>Texto</p>')
assert not p.missing and ''.join(p.output)=='<p>Texto traduzido</p>'
runtime=json.loads((ROOT / 'i18n/runtime.json').read_text())
for key,value in runtime.items():
    assert set(value)==set(LOCALES),key
    assert all(value.values()),key
# Exercise the actual build guard in isolation: missing text must not emit pages.
from tempfile import TemporaryDirectory
from unittest.mock import patch
import render
with TemporaryDirectory() as directory:
    temporary = Path(directory)
    (temporary / 'routes.json').write_text(json.dumps({'home': {'es':'/es','en':'/en','pt':'/pt'}}))
    for filename in ('en.json', 'pt.json', 'runtime.json'):
        (temporary / filename).write_text('{}')
    with patch.object(render, 'ROOT', temporary):
        try:
            render.build_locales({'home': '<p>Nueva frase pendiente</p>'}, temporary / 'dist')
        except ValueError as error:
            assert 'Missing translations' in str(error)
        else:
            raise AssertionError('Build accepted untranslated content')
    assert not (temporary / 'dist').exists()
    assert set(json.loads((temporary / 'missing.json').read_text())) == {'en','pt'}
print(f'PASS: {len(paths)} localized pages, internal links, language switchers, canonical/hreflang, runtime messages and missing-translation guard.')
