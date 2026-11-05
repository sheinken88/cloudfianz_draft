"""Existing project identities and evidence inside the shared service card."""
from page_layouts.revianz_mockups import mockup


BRANDS = {
    'despegar': '<img class="service-case-logo-despegar" src="/assets/brand/despegar-digifianz.png" alt="Despegar" width="180" height="52" loading="lazy">',
    'revianz': '<span class="service-rv-logo" role="img" aria-label="REVIANZ"><span class="service-rv-logo-symbol" aria-hidden="true">RZ</span><span class="service-rv-logo-wordmark" aria-hidden="true">Revianz</span></span>',
    'properix': '<img class="service-case-logo-consorcio" src="/assets/brand/consorcio-abierto-official.svg" alt="ConsorcioAbierto" width="216" height="28" loading="lazy">',
    'escala24x7': '<img class="service-case-logo-escala" src="/assets/brand/escala24x7-original.avif" alt="Escala24x7" width="1275" height="784" loading="lazy">',
}


def case_media(case):
    if case == 'revianz':
        return mockup('scope', 'service-case-media service-case-mockup')
    if case == 'despegar':
        return '''<figure class="service-case-media">
          <div class="service-case-stage"><div class="static-image"><img src="/assets/hero/despegar-cotizador-hero-v1.jpg" alt="Vista adaptada del cotizador de Despegar: presupuesto y productos distribuidos por marca y país." width="1701" height="924" loading="lazy" decoding="async"></div></div>
        </figure>'''
    if case == 'properix':
        return '''<figure class="service-case-media">
          <div class="service-case-stage"><img src="/assets/brand/properix-product-context.png" alt="Interfaz de administración de Properix, como contexto del negocio de ConsorcioAbierto." width="610" height="253" loading="lazy" decoding="async"></div>
        </figure>'''
    if case == 'escala24x7':
        return '''<figure class="service-case-media">
          <div class="service-case-stage service-integration-stage">
            <p class="service-integration-label">Sincronización bidireccional</p>
            <div class="service-integration-flow">
              <div class="service-integration-system"><div class="service-integration-brand"><img src="/assets/brand/hubspot-official.svg" alt="HubSpot" width="1256" height="356" loading="lazy" decoding="async"></div><span>CRM comercial</span></div>
              <span class="service-integration-arrows" aria-hidden="true">⇄</span>
              <div class="service-integration-system"><div class="service-integration-brand"><img class="service-integration-aws" src="/assets/aws/aws-logo-color.svg" alt="AWS" width="304" height="182" loading="lazy" decoding="async"></div><span>Partner Central</span></div>
            </div>
            <p class="service-integration-result">Oportunidades actualizadas<br>en ambas plataformas</p>
          </div>
        </figure>'''
    raise ValueError(f'Unsupported service case: {case}')
