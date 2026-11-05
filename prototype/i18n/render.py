"""Strict build-time localization of shared HTML. No browser translation or fallback."""
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from seo import HREFLANG, enrich_page, write_discovery_files

ROOT = Path(__file__).resolve().parent
LOCALES = {'es': ('es-AR', 'Español'), 'en': ('en', 'English'), 'pt': ('pt-BR', 'Português')}
ATTRS = {'alt', 'title', 'aria-label', 'placeholder'}
META = {'description', 'og:title', 'og:description'}


def normalize(text):
    return ' '.join(text.split())


class Localizer(HTMLParser):
    def __init__(self, locale, catalog, routes):
        super().__init__(convert_charrefs=False)
        self.locale, self.catalog, self.routes = locale, catalog, routes
        self.output, self.missing, self.strings = [], set(), set()
        self.skip = False

    def translate(self, text):
        source = normalize(html.unescape(text))
        if source not in self.catalog and not re.search(r'[a-zA-ZÀ-ÿ]', source):
            return text
        self.strings.add(source)
        if self.locale == 'es':
            return text
        translated = self.catalog.get(source)
        if not translated:
            self.missing.add(source)
            return text
        return (' ' if text[:1].isspace() else '') + html.escape(translated, quote=False) + (' ' if text[-1:].isspace() else '')

    def url(self, value):
        absolute = value.startswith('https://cloudfianz.com/')
        local = value.removeprefix('https://cloudfianz.com') if absolute else value
        path, sep, fragment = local.partition('#')
        if path in self.routes:
            value = self.routes[path][self.locale] + (sep + fragment if sep else '')
            if absolute:
                value = 'https://cloudfianz.com' + value
        return value

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip = True
        values = dict(attrs)
        rendered = []
        for key, value in attrs:
            if value is None:
                rendered.append(key)
                continue
            if key in ATTRS or (tag == 'meta' and key == 'content' and values.get('name', values.get('property')) in META):
                value = html.unescape(self.translate(value))
            if key in ('href', 'src') or (tag == 'meta' and values.get('property') == 'og:url' and key == 'content'):
                value = self.url(value)
            if tag == 'html' and key == 'lang':
                value = LOCALES[self.locale][0]
            if tag == 'meta' and values.get('property') == 'og:locale' and key == 'content':
                value = {'es':'es_AR','en':'en_US','pt':'pt_BR'}[self.locale]
            rendered.append(f'{key}="{html.escape(value, quote=True)}"')
        self.output.append('<' + tag + (' ' + ' '.join(rendered) if rendered else '') + '>')

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.output[-1] = self.output[-1][:-1] + '/>'

    def handle_endtag(self, tag):
        self.output.append(f'</{tag}>')
        if tag in ('script', 'style'):
            self.skip = False

    def handle_data(self, data):
        self.output.append(data if self.skip else self.translate(data))

    def handle_entityref(self, name):
        self.output.append(f'&{name};')

    def handle_charref(self, name):
        self.output.append(f'&#{name};')

    def handle_comment(self, data):
        self.output.append('<!--' + data + '-->')

    def handle_decl(self, decl):
        self.output.append('<!' + decl + '>')


def switcher(locale, paths):
    label = {'es':'Cambiar idioma','en':'Change language','pt':'Alterar idioma'}[locale]
    items = ''.join(f'<li><a href="{paths[code]}" lang="{tag}" hreflang="{HREFLANG[code]}"' + (' aria-current="true"' if code == locale else '') + f'>{name}<span aria-hidden="true">{code.upper()}</span></a></li>' for code, (tag, name) in LOCALES.items())
    return f'<details class="language-switcher"><summary aria-label="{label}"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4" ry="9"/><path d="M3 12h18"/></svg><span>{locale.upper()}</span><span class="nav-chevron" aria-hidden="true"></span></summary><ul aria-label="{label}">{items}</ul></details>'


def build_locales(documents, dist):
    route_config = json.loads((ROOT / 'routes.json').read_text())
    route_map = {paths['es']: paths for paths in route_config.values()}
    catalogs = {code: json.loads((ROOT / f'{code}.json').read_text()) for code in ('en','pt')}
    runtime = json.loads((ROOT / 'runtime.json').read_text())
    for key, values in runtime.items():
        if set(values) != set(LOCALES) or not all(values.values()):
            raise ValueError(f'Runtime message {key} must be translated into es/en/pt')
        if isinstance(values['es'], dict) and any(set(v) != set(values['es']) or not all(v.values()) for v in values.values()):
            raise ValueError(f'Runtime message {key} has incomplete field translations')
    pending, missing = {}, {}
    for key, source in documents.items():
        if key not in route_config:
            raise ValueError(f'Missing localized routes for {key}')
        paths = route_config[key]
        for locale in LOCALES:
            parser = Localizer(locale, catalogs.get(locale, {}), route_map)
            parser.feed(source)
            if parser.missing:
                missing.setdefault(locale, set()).update(parser.missing)
            output = ''.join(parser.output)
            alternates = ''.join(f'<link rel="alternate" hreflang="{HREFLANG[code]}" href="https://cloudfianz.com{paths[code]}">' for code in LOCALES)
            alternates += f'<link rel="alternate" hreflang="x-default" href="https://cloudfianz.com{paths["es"]}">'
            output = output.replace('</head>', alternates + '<link rel="stylesheet" href="/language-switcher.css"></head>')
            output = output.replace('<!-- LANGUAGE_SWITCHER -->', switcher(locale, paths))
            localized_runtime = {name: value[locale] for name, value in runtime.items()}
            output = output.replace('</head>', '<script id="site-messages" type="application/json">' + json.dumps(localized_runtime, ensure_ascii=False).replace('<', '\\u003c') + '</script></head>')
            path = dist / paths[locale].lstrip('/') / 'index.html'
            pending[path] = output
            if key == 'home' and locale == 'es':
                pending[dist / 'index.html'] = output
    if missing:
        (ROOT / 'missing.json').write_text(json.dumps({k: sorted(v) for k,v in missing.items()}, ensure_ascii=False, indent=2) + '\n')
        raise ValueError('Missing translations; see prototype/i18n/missing.json. Update BOTH catalogs before building.')
    for key, paths in route_config.items():
        for locale, route in paths.items():
            path = dist / route.lstrip('/') / 'index.html'
            if path in pending:
                pending[path] = enrich_page(pending[path], key, locale, route_config)
                if key == 'home' and locale == 'es':
                    pending[dist / 'index.html'] = pending[path]
    for path, output in pending.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(output)
    (ROOT / 'missing.json').unlink(missing_ok=True)
    (dist / 'localized-routes.json').write_text(json.dumps(route_config, indent=2) + '\n')
    write_discovery_files(dist, route_config)
    print(f'Localized {len(documents)} pages in {len(LOCALES)} languages (strict coverage).')
