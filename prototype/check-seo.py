"""Check crawlability boundaries, metadata and release contents without a network."""
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import urlparse
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent
release = '--release' in sys.argv
DIST = ROOT / ('release/site' if release else 'dist')
routes = json.loads((ROOT / 'i18n/routes.json').read_text())
expected_paths = {p for group in routes.values() for p in group.values()}
expected_urls = {'https://cloudfianz.com' + p for p in expected_paths}


class Document(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.tags, self.schemas = [], []
        self.structured = False
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.structured = True

    def handle_data(self, data):
        if self.structured:
            self.schemas.append(json.loads(data))

    def handle_endtag(self, tag):
        if tag == 'script':
            self.structured = False


for route in sorted(expected_paths):
    source = (DIST / route.lstrip('/') / 'index.html').read_text()
    page = Document(source)
    meta = {}
    for tag, attrs in page.tags:
        if tag == 'meta':
            name = attrs.get('name', attrs.get('property'))
            meta.setdefault(name, []).append(attrs.get('content'))
    assert len(meta['robots']) == 1
    assert ('noindex' not in meta['robots'][0]) if release else ('noindex' in meta['robots'][0])
    assert meta['site-environment'] == ['production' if release else 'preview']
    assert meta['description'][0]
    for name in ('og:title', 'og:description', 'og:url', 'og:image', 'og:image:alt', 'twitter:card', 'twitter:title', 'twitter:description', 'twitter:image'):
        assert len(meta[name]) == 1 and meta[name][0], (route, name)
    canonical = 'https://cloudfianz.com' + route
    assert meta['og:url'] == [canonical]
    assert meta['og:description'] == meta['description']
    assert (DIST / urlparse(meta['og:image'][0]).path.lstrip('/')).is_file()
    assert len(page.schemas) == 1
    graph = {node['@type']: node for node in page.schemas[0]['@graph']}
    assert {'Organization', 'WebSite', 'WebPage'} <= graph.keys()
    assert graph.keys() <= {'Organization', 'WebSite', 'WebPage', 'BreadcrumbList'}
    assert graph['Organization']['parentOrganization']['name'] == 'Digifianz'
    assert 'sameAs' not in graph['Organization'] # Digifianz is a parent, not an alias.
    assert graph['WebPage']['url'] == canonical
    assert graph['WebPage']['description'] == meta['description'][0]
    locale = route.split('/')[1]
    assert graph['WebPage']['inLanguage'] == {'es':'es-AR','en':'en','pt':'pt-BR'}[locale]
    if route.count('/') > 1:
        crumbs = graph['BreadcrumbList']['itemListElement']
        assert len(crumbs) >= 2 and crumbs[-1]['item'] == canonical
        assert [c['position'] for c in crumbs] == list(range(1, len(crumbs) + 1))
        for crumb in crumbs:
            assert crumb['name'] in source, (route, crumb['name'])
    else:
        assert 'BreadcrumbList' not in graph
    for tag, attrs in page.tags:
        if tag == 'img' and 'srcset' in attrs:
            assert attrs.get('sizes') and 'alt' in attrs
            for variant in attrs['srcset'].split(','):
                assert (DIST / variant.strip().split()[0].lstrip('/')).is_file()

ns = {'s':'http://www.sitemaps.org/schemas/sitemap/0.9', 'h':'http://www.w3.org/1999/xhtml'}
sitemap = ET.parse(DIST / 'sitemap.xml')
urls = sitemap.findall('s:url', ns)
assert len(urls) == len(expected_urls) == 39
assert {url.find('s:loc', ns).text for url in urls} == expected_urls
for url in urls:
    alternates = {link.attrib['hreflang']: link.attrib['href'] for link in url.findall('h:link', ns)}
    assert set(alternates) == {'es', 'en', 'pt-BR', 'x-default'}
    group = next(group for group in routes.values() if url.find('s:loc', ns).text.removeprefix('https://cloudfianz.com') in group.values())
    for locale, tag in {'es':'es','en':'en','pt':'pt-BR'}.items():
        assert alternates[tag] == 'https://cloudfianz.com' + group[locale]
    assert alternates['x-default'] == alternates['es']

robots = (DIST / 'robots.txt').read_text()
assert 'Allow: /' in robots and not re.search(r'^Disallow:\s*/\s*$', robots, re.M)
config_path = ROOT / 'release/vercel.production.json' if release else ROOT.parent / 'vercel.json'
config = json.loads(config_path.read_text())
headers = [h for rule in config['headers'] for h in rule['headers'] if rule['source'] == '/(.*)' and h['key'].lower() == 'x-robots-tag']
if release:
    assert not headers and 'Sitemap: https://cloudfianz.com/sitemap.xml' in robots
    assert not list(DIST.rglob('review*')) and not (DIST / 'content.json').exists()
    assert len(list(DIST.rglob('*.html'))) == 40
    assert config['outputDirectory'] == 'prototype/release/site'
else:
    # After migration the real-domain repo can explicitly serve release/site.
    # A preview-serving configuration must ALWAYS retain its HTTP protection.
    assert config['outputDirectory'] in ('prototype/dist', 'prototype/release/site')
    if config['outputDirectory'] == 'prototype/dist':
        assert len(headers) == 1 and 'noindex' in headers[0]['value']
    else:
        assert config['buildCommand'] == 'npm run build:release' and not headers
    assert 'Sitemap:' not in robots
    for src, entry in json.loads((ROOT / 'image-variants.json').read_text()).items():
        assert hashlib.sha256((DIST / src.lstrip('/')).read_bytes()).hexdigest() == entry['sha256'], f'Regenerate image variants: {src}'
        assert all((DIST / v['src'].lstrip('/')).exists() for v in entry['variants'])
print(f'PASS: 39 pages, metadata, structured data, sitemap, images and {"indexable isolated release" if release else "protected preview"}.')
