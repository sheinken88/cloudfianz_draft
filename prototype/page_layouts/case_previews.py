"""Compact, non-interactive project evidence for the case index."""
from page_layouts.revianz_mockups import mockup


def _figure(kind, content, caption):
    return f'''<figure class="case-preview case-preview--{kind}">
      <div class="case-preview-stage">{content}</div>
      <figcaption>{caption}</figcaption>
    </figure>'''


def _arrow():
    return '<svg class="case-preview-arrow" viewBox="0 0 24 16" fill="none" aria-hidden="true"><path d="M2 8h19m-6-5 6 5-6 5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def case_preview(key):
    if key == 'caso-despegar':
        return _figure('despegar', '''<img class="case-preview-capture" src="/assets/hero/despegar-cotizador-hero-v1.jpg" alt="Vista adaptada del cotizador de Despegar con presupuesto y productos distribuidos por marca y país." width="1701" height="924" loading="lazy" decoding="async">''', 'Vista adaptada del cotizador de Despegar.')
    if key == 'caso-revianz':
        return mockup('scope-services', 'Vista ilustrativa de REVIANZ. Datos de ejemplo.', 'case-preview case-preview--revianz')
    if key == 'caso-properix':
        return _figure('consorcio', '''<div class="case-preview-billing">
          <div class="case-preview-billing-end"><img class="case-preview-hubspot" src="/assets/brand/hubspot-official.svg" alt="HubSpot" width="1256" height="356" loading="lazy"><span>Membresías</span></div>
          <span class="case-preview-down" aria-hidden="true">↓</span>
          <div class="case-preview-rules"><strong>Reglas del contrato</strong><span>Descuentos, períodos y país</span></div>
          <span class="case-preview-down" aria-hidden="true">↓</span>
          <div class="case-preview-billing-end"><img class="case-preview-odoo" src="/assets/brand/odoo-official.svg" alt="Odoo" width="919" height="495" loading="lazy"><span>Facturas generadas</span></div>
        </div>''', 'Esquema de la facturación de ConsorcioAbierto.')
    if key == 'caso-photonix':
        return _figure('photonix', '''<img class="case-preview-photo" src="/assets/brand/photonix-instalaciones-official.jpg" alt="Equipamiento médico durante un trabajo de instalación de Photonix." width="1200" height="900" loading="lazy" decoding="async">''', 'Foto de la actividad de Photonix. Imagen de contexto.')
    if key == 'caso-escala24x7':
        return _figure('escala', '''<div class="case-preview-sync">
          <p>Sincronización de oportunidades</p>
          <div class="case-preview-system-pair">
            <div class="case-preview-system"><img class="case-preview-hubspot" src="/assets/brand/hubspot-official.svg" alt="HubSpot" width="1256" height="356" loading="lazy"><span>CRM comercial</span></div>
            <svg class="case-preview-sync-arrows" viewBox="0 0 40 40" fill="none" aria-hidden="true"><path d="M3 13h34m-7-6 7 6-7 6M37 27H3m7-6-7 6 7 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
            <div class="case-preview-system"><img class="case-preview-aws" src="/assets/aws/aws-logo-color.svg" alt="AWS" width="304" height="182" loading="lazy"><span>Partner Central</span></div>
          </div>
          <p class="case-preview-system-result">Datos actualizados en ambos sistemas</p>
        </div>''', 'Esquema de la integración de Escala24x7.')
    if key == 'caso-ads-mexicana':
        return _figure('ads', f'''<div class="case-preview-quote">
          <img class="case-preview-hubspot" src="/assets/brand/hubspot-official.svg" alt="HubSpot" width="1256" height="356" loading="lazy">
          <div class="case-preview-quote-flow"><span>Datos del negocio</span>{_arrow()}<strong>Cotizador a medida</strong>{_arrow()}<span>Propuesta registrada</span></div>
          <p>Más de <strong>50 cotizaciones diarias</strong></p>
        </div>''', 'Esquema del proceso comercial de ADS Mexicana.')
    raise ValueError(f'Unsupported case preview: {key}')
