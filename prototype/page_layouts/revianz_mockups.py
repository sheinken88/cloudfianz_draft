"""Static ports of REVIANZ's published marketing mockups (not live product UI)."""
import html
import json
from pathlib import Path

COPY = json.loads((Path(__file__).resolve().parents[1] / 'data/revianz-mockups-es.json').read_text())


def mockup(kind, caption, class_name=''):
    if kind == 'scope':
        t = COPY['scopeDefinition']
        rows = ''.join(f'<div class="rm-service"><span>{service}</span><span>{hours}</span><strong>{amount}</strong></div>' for service, hours, amount in [('Lifecycle strategy', '48 h', '$7,200'), ('Campaign delivery', '72 h', '$10,800'), ('Reporting', '16 h', '$2,400')])
        label = 'Mockup de REVIANZ: servicios de un proyecto, horas, importes y vista previa de su margen. Datos ilustrativos.'
        body = f'''<div class="rm-paper rm-scope"><div class="rm-scope-header"><div><p class="rm-label">{t['economics']}</p><p class="rm-title">{t['program']}</p></div><span class="rm-status">{t['status']}</span></div><div class="rm-scope-body"><div class="rm-services">{rows}</div><div class="rm-economics"><p class="rm-label">{t['margin']}</p><p class="rm-percentage">38.4%</p><div class="rm-progress"><span></span></div><div class="rm-amount"><span>{t['revenue']}</span><strong>$20,400</strong></div><div class="rm-amount"><span>{t['deliveryCost']}</span><strong>$12,566</strong></div></div></div></div>'''
    elif kind == 'margin':
        t = COPY['liveMargin']
        label = 'Mockup de REVIANZ: evolución del margen, ingresos y costo de entrega. Cifras ilustrativas, no resultados de Digifianz.'
        # Same SVG curve and values as LiveMarginFlowMockup in REVIANZ.
        body = f'''<div class="rm-paper rm-live"><div class="rm-live-heading"><div><p class="rm-label">{t['title']}</p><p class="rm-percentage">42.8%</p></div><span class="rm-trend">+3.4 pts</span></div><svg viewBox="0 0 240 74" class="rm-chart" fill="none" aria-hidden="true"><defs><linearGradient id="rv-margin-fill" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#c4f751" stop-opacity="0.28"/><stop offset="1" stop-color="#c4f751" stop-opacity="0"/></linearGradient></defs><path d="M0 63 C28 61 38 49 62 51 C86 53 96 37 122 40 C147 43 158 24 181 28 C205 32 219 12 240 10 V74 H0 Z" fill="url(#rv-margin-fill)"/><path d="M0 63 C28 61 38 49 62 51 C86 53 96 37 122 40 C147 43 158 24 181 28 C205 32 219 12 240 10" stroke="#c4f751" stroke-width="2.5" stroke-linecap="round"/><circle cx="240" cy="10" r="4" fill="#c4f751"/></svg><div class="rm-live-totals"><div><p>{t['revenue']}</p><strong>$48,000</strong></div><div><p>{t['deliveryCost']}</p><strong>$27,456</strong></div></div></div>'''
    elif kind == 'invoice':
        t = COPY['invoice']
        label = 'Mockup de REVIANZ: conciliación entre factura del cliente y factura del socio, vinculadas al mismo proyecto. Datos ilustrativos.'
        # The original arrow is a relationship between the two invoices, not a CTA.
        body = f'''<div class="rm-paper rm-invoice"><div class="rm-invoice-heading"><p class="rm-title">{t['title']}</p><span class="rm-status">{t['matched']}</span></div><div class="rm-invoice-row"><div><strong>{t['client']}</strong><strong>$48,000</strong></div><p>{t['outgoing']}</p></div><div class="rm-match-arrow"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14m-7-7 7 7 7-7"/></svg></div><div class="rm-invoice-row rm-invoice-partner"><div><strong>{t['partner']}</strong><strong>$9,600</strong></div><p>{t['incoming']}</p></div></div>'''
    else:
        raise ValueError(f'Unknown REVIANZ mockup: {kind}')
    return f'<figure class="rv-mockup-figure {class_name}"><div class="revianz-mockup-stage"><div class="revianz-mockup" role="img" aria-label="{html.escape(label, quote=True)}"><div aria-hidden="true">{body}</div></div></div><figcaption>{html.escape(caption)}</figcaption></figure>'
