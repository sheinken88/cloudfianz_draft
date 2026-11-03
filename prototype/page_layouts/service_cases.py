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
        return mockup('scope', 'Vista ilustrativa de REVIANZ. Servicios, importes y margen con datos de ejemplo.', 'service-case-media service-case-mockup')
    if case == 'despegar':
        return '''<figure class="service-case-media">
          <div class="service-case-stage"><a href="/assets/projects/despegar-cotizador-original.png" target="_blank" rel="noopener" aria-label="Ampliar captura del cotizador de Despegar (nueva pestaña)"><img src="/assets/projects/despegar-cotizador-original.png" alt="Cotizador de Despegar: presupuesto y productos distribuidos por marca y país." width="1633" height="887" loading="lazy" decoding="async"></a></div>
          <figcaption>Captura real del cotizador desarrollado para Despegar.</figcaption>
        </figure>'''
    if case == 'properix':
        return '''<figure class="service-case-media">
          <div class="service-case-stage"><img src="/assets/brand/properix-product-context.png" alt="Interfaz de administración de Properix, como contexto del negocio de ConsorcioAbierto." width="610" height="253" loading="lazy" decoding="async"></div>
          <figcaption>Plataforma de Properix. Imagen de contexto del cliente, no de la integración.</figcaption>
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
          <figcaption>Esquema de la integración desarrollada para Escala24x7.</figcaption>
        </figure>'''
    raise ValueError(f'Unsupported service case: {case}')
