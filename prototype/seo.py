"""Shared metadata from localized, visible content. Preview is always noindex."""
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin
from xml.etree import ElementTree as ET

ORIGIN = 'https://cloudfianz.com'
HREFLANG = {'es': 'es', 'en': 'en', 'pt': 'pt-BR'}
LANGUAGE = {'es': 'es-AR', 'en': 'en', 'pt': 'pt-BR'}
OG_LOCALE = {'es': 'es_AR', 'en': 'en_US', 'pt': 'pt_BR'}
SOCIAL_IMAGE = '/assets/hero/cloudfianz-team-work-v3.jpg'
PREVIEW_ROBOTS = '# Preview: HTML and HTTP noindex must remain enabled.\nUser-agent: *\nAllow: /\n'


def responsive_images(source):
    manifest = json.loads((Path(__file__).resolve().parent / 'image-variants.json').read_text())

    def replace(match):
        tag = match.group()
        src = re.search(r'\bsrc="([^"]+)"', tag)
        entry = manifest.get(src.group(1)) if src else None
        if not entry:
            return tag
        variants = entry['variants']
        tag = tag.replace(src.group(), f'src="{variants[-1]["src"]}"')
        srcset = ', '.join(f'{v["src"]} {v["width"]}w' for v in variants)
        # Full-width is conservative for case screenshots; the cropped Home hero
        # needs enough source pixels to fill its mobile height without blur.
        sizes = '(max-width: 599px) 600px, 100vw' if 'cloudfianz-team-work-v3' in src.group(1) else '100vw'
        return tag[:-1] + f' srcset="{srcset}" sizes="{sizes}">'

    return re.sub(r'<img\b[^>]*>', replace, source)


class PageMetadata(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.title, self.description, self.brand_description = '', '', ''
        self.breadcrumbs = []
        self.in_title = self.in_brand = self.in_breadcrumbs = False
        self.crumb = None
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'title':
            self.in_title = True
        if tag == 'meta' and a.get('name') == 'description':
            self.description = a['content']
        if tag == 'p' and 'fz-footer-description' in a.get('class', '').split():
            self.in_brand = True
        if tag == 'nav' and 'breadcrumbs' in a.get('class', '').split():
            self.in_breadcrumbs = True
        if self.in_breadcrumbs and tag == 'li':
            self.crumb = {'name': '', 'href': None}
        if self.crumb is not None and tag == 'a':
            self.crumb['href'] = a.get('href')

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_brand:
            self.brand_description += data
        if self.crumb is not None:
            self.crumb['name'] += data

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        if tag == 'p':
            self.in_brand = False
        if tag == 'li' and self.crumb is not None:
            self.crumb['name'] = ' '.join(self.crumb['name'].split())
            self.breadcrumbs.append(self.crumb)
            self.crumb = None
        if tag == 'nav':
            self.in_breadcrumbs = False


def enrich_page(source, key, locale, routes):
    page = PageMetadata(source)
    if not all((page.title, page.description, page.brand_description)):
        raise ValueError(f'Incomplete visible metadata for {key}/{locale}')
    canonical = ORIGIN + routes[key][locale]
    # One implementation for Home and all inner pages, after localization.
    source = re.sub(r'<meta\b[^>]*(?:property="og:[^"]+"|name="twitter:[^"]+")[^>]*>\s*', '', source)
    metadata = {
        'og:title': page.title, 'og:description': page.description,
        'og:type': 'website', 'og:url': canonical, 'og:site_name': 'Cloudfianz',
        'og:locale': OG_LOCALE[locale], 'og:image': ORIGIN + SOCIAL_IMAGE,
        'og:image:type': 'image/jpeg', 'og:image:width': '1672', 'og:image:height': '941',
        'og:image:alt': page.brand_description,
        'twitter:card': 'summary_large_image', 'twitter:title': page.title,
        'twitter:description': page.description, 'twitter:image': ORIGIN + SOCIAL_IMAGE,
        'twitter:image:alt': page.brand_description,
    }
    tags = [f'<meta {"property" if name.startswith("og:") else "name"}="{name}" content="{html.escape(value, quote=True)}">' for name, value in metadata.items()]
    tags += [f'<meta property="og:locale:alternate" content="{value}">' for code, value in OG_LOCALE.items() if code != locale]
    tags += [f'<meta name="site-environment" content="preview">', f'<meta name="site-page" content="{key}">']
    org_id, site_id = ORIGIN + '/#organization', ORIGIN + '/#website'
    graph = [
        {'@type': 'Organization', '@id': org_id, 'name': 'Cloudfianz', 'url': ORIGIN + '/',
         'description': page.brand_description, 'logo': ORIGIN + '/assets/brand/cloudfianz-official.svg',
         'parentOrganization': {'@type': 'Organization', 'name': 'Digifianz', 'url': 'https://www.digifianz.com/'}},
        {'@type': 'WebSite', '@id': site_id, 'url': ORIGIN + '/', 'name': 'Cloudfianz',
         'publisher': {'@id': org_id}, 'inLanguage': list(LANGUAGE.values())},
        {'@type': 'WebPage', '@id': canonical + '#webpage', 'url': canonical,
         'name': page.title, 'description': page.description, 'inLanguage': LANGUAGE[locale],
         'isPartOf': {'@id': site_id}, 'about': {'@id': org_id}},
    ]
    if page.breadcrumbs:
        graph[-1]['breadcrumb'] = {'@id': canonical + '#breadcrumb'}
        graph.append({'@type': 'BreadcrumbList', '@id': canonical + '#breadcrumb',
                      'itemListElement': [
                          {'@type': 'ListItem', 'position': index, 'name': crumb['name'],
                           'item': urljoin(ORIGIN, crumb['href']) if crumb['href'] else canonical}
                          for index, crumb in enumerate(page.breadcrumbs, 1)]})
    structured = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False).replace('<', '\\u003c')
    tags.append(f'<script type="application/ld+json">{structured}</script>')
    return responsive_images(source.replace('</head>', '\n'.join(tags) + '\n</head>'))


def write_discovery_files(dist, routes):
    namespace = 'http://www.sitemaps.org/schemas/sitemap/0.9'
    xhtml = 'http://www.w3.org/1999/xhtml'
    ET.register_namespace('', namespace)
    ET.register_namespace('xhtml', xhtml)
    root = ET.Element(f'{{{namespace}}}urlset')
    for group in routes.values():
        for path in group.values():
            url = ET.SubElement(root, f'{{{namespace}}}url')
            ET.SubElement(url, f'{{{namespace}}}loc').text = ORIGIN + path
            for locale, alternate in group.items():
                ET.SubElement(url, f'{{{xhtml}}}link', rel='alternate', hreflang=HREFLANG[locale], href=ORIGIN + alternate)
            ET.SubElement(url, f'{{{xhtml}}}link', rel='alternate', hreflang='x-default', href=ORIGIN + group['es'])
    ET.indent(root)
    (dist / 'sitemap.xml').write_bytes(ET.tostring(root, encoding='utf-8', xml_declaration=True))
    # Crawlers must be able to read noindex. Never advertise the preview sitemap.
    (dist / 'robots.txt').write_text(PREVIEW_ROBOTS)
