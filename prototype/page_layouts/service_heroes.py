"""Project evidence tailored to each service, inside the shared hero layout."""


def hero_media(key):
    if key == 'servicio-desarrollo-software':
        return '''
      <figure class="service-hero-project">
        <div class="service-hero-preview">
          <img src="/assets/hero/despegar-cotizador-hero-v1.jpg" alt="Vista adaptada del cotizador de Despegar: presupuesto, productos y distribución por marca y país." width="1701" height="924" fetchpriority="high" decoding="async">
        </div>
        <figcaption><img src="/assets/brand/despegar-digifianz.png" alt="Despegar" width="180" height="52"><span><strong>Cotizador comercial a medida</strong><span>Vista adaptada del producto</span></span></figcaption>
      </figure>'''
    if key == 'servicio-integracion-sistemas':
        return '''
      <figure class="service-hero-project service-hero-project--integration">
        <div class="service-hero-canvas hero-system-map">
          <p class="hero-visual-title">Una oportunidad, dos sistemas</p>
          <div class="hero-system-pair">
            <div class="hero-system"><img src="/assets/brand/hubspot-official.svg" alt="HubSpot" width="1256" height="356"><span>CRM comercial</span></div>
            <svg class="hero-system-connection" viewBox="0 0 80 50" fill="none" aria-hidden="true"><path d="M4 16H74m-9-8 9 8-9 8M76 34H6m9-8-9 8 9 8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
            <div class="hero-system"><img class="hero-system-aws" src="/assets/aws/aws-logo-color.svg" alt="AWS" width="304" height="182"><span>Partner Central</span></div>
          </div>
          <div class="hero-sync-note"><span class="hero-sync-symbol" aria-hidden="true">↔</span><p>Los cambios se reflejan<br><strong>en ambos sistemas.</strong></p></div>
        </div>
        <figcaption><img src="/assets/brand/escala24x7-original.avif" alt="Escala24x7" width="1275" height="784"><span><strong>Oportunidades conectadas</strong><span>Esquema de la integración</span></span></figcaption>
      </figure>'''
    if key == 'servicio-automatizacion-procesos':
        return '''
      <figure class="service-hero-project service-hero-project--automation">
        <div class="service-hero-canvas hero-billing-flow">
          <div class="hero-flow-endpoint"><img class="hero-flow-hubspot" src="/assets/brand/hubspot-official.svg" alt="HubSpot" width="1256" height="356"><span>Membresías y<br><strong>condiciones comerciales</strong></span></div>
          <div class="hero-flow-connector" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="M12 0v21m-5-5 5 5 5-5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
          <div class="hero-contract-rules"><svg viewBox="0 0 40 40" fill="none" aria-hidden="true"><path d="M6 11h28M6 20h28M6 29h28" stroke="currentColor" stroke-width="1.5"/><circle cx="15" cy="11" r="4"/><circle cx="26" cy="20" r="4"/><circle cx="13" cy="29" r="4"/></svg><div><p>Aplicar las reglas del contrato</p><ul><li>Descuentos</li><li>Períodos</li><li>País</li></ul></div></div>
          <div class="hero-flow-connector" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="M12 0v21m-5-5 5 5 5-5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
          <div class="hero-flow-endpoint"><img class="hero-flow-odoo" src="/assets/brand/odoo-official.svg" alt="Odoo" width="919" height="495"><span>Generación de<br><strong>facturas</strong></span><svg class="hero-invoice-stack" viewBox="0 0 48 52" fill="none" aria-hidden="true"><path d="M12 7h29v37H12z"/><path d="M6 13h29v37H6z"/><path d="M13 24h15m-15 7h15m-15 7h9"/></svg></div>
          <p class="hero-flow-result">Más de <strong>15.000 facturas</strong> al mes</p>
        </div>
        <figcaption><img src="/assets/brand/consorcio-abierto-official.svg" alt="ConsorcioAbierto" width="216" height="28"><span><strong>Facturación automática</strong><span>Esquema del proceso</span></span></figcaption>
      </figure>'''
    raise ValueError(f'Unsupported service hero: {key}')
