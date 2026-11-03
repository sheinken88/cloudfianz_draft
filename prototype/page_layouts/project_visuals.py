"""Real context and documented process diagrams for the individual project stories."""


def _arrow(two_way=False):
    path = 'M3 13h34m-7-6 7 6-7 6M37 27H3m7-6-7 6 7 6' if two_way else 'M3 20h34m-8-7 8 7-8 7'
    return f'<svg class="pv-arrow" viewBox="0 0 40 40" fill="none" aria-hidden="true"><path d="{path}" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def _hubspot(lazy=False):
    loading = ' loading="lazy"' if lazy else ''
    return f'<img class="pv-hubspot" src="/assets/brand/hubspot-official.svg" alt="HubSpot" width="1256" height="356" decoding="async"{loading}>'


def _aws(lazy=False):
    loading = ' loading="lazy"' if lazy else ''
    return f'<img class="pv-aws" src="/assets/aws/aws-logo-color.svg" alt="AWS" width="304" height="182" decoding="async"{loading}>'


def hero_visual(key):
    if key == 'caso-photonix':
        return '''<figure class="pv-figure pv-hero pv-hero-photo">
          <div class="pv-photo-stage"><img src="/assets/brand/photonix-ethos-official.jpg" alt="Equipamiento de radioterapia Ethos en una imagen institucional de Photonix." width="1920" height="1080" fetchpriority="high" decoding="async"></div>
          <figcaption>Equipamiento de radioterapia. Imagen de contexto de la actividad de Photonix.</figcaption>
        </figure>'''
    if key == 'caso-escala24x7':
        return f'''<figure class="pv-figure pv-hero pv-hero-integration">
          <div class="pv-cover-stage">
            <p class="pv-cover-title">Oportunidades conectadas</p>
            <div class="pv-cover-pair">
              <div class="pv-cover-platform">{_hubspot()}<span>CRM comercial</span></div>
              {_arrow(True)}
              <div class="pv-cover-platform">{_aws()}<span>Partner Central</span></div>
            </div>
            <p class="pv-cover-note">La información comercial se actualiza en ambos sentidos.</p>
          </div>
          <figcaption>Esquema de la integración desarrollada para Escala24x7.</figcaption>
        </figure>'''
    if key == 'caso-ads-mexicana':
        return f'''<figure class="pv-figure pv-hero pv-hero-quotation">
          <div class="pv-cover-stage pv-quotation-cover">
            <p class="pv-cover-title">Del negocio a la propuesta</p>
            <div class="pv-quotation-pair">
              <div class="pv-quotation-crm">{_hubspot()}<span>Datos del negocio</span></div>
              {_arrow(True)}
              <div class="pv-quotation-tool"><strong>Cotizador<br>a medida</strong><span>Reglas de ADS</span></div>
            </div>
            <p class="pv-cover-note">La cotización queda registrada en el negocio de HubSpot.</p>
          </div>
          <figcaption>Esquema del proceso comercial de ADS Mexicana, no una captura del software.</figcaption>
        </figure>'''
    raise ValueError(f'Unsupported project hero: {key}')


def solution_visual(key, items=None):
    if key == 'caso-photonix':
        return f'''<figure class="pv-figure pv-solution pv-operation">
          <div class="pv-solution-stage">
            <div class="pv-operation-flow">
              <div class="pv-role"><p class="pv-role-title">Técnicos</p><ul><li>Consultan la agenda</li><li>Registran la orden y la firma</li><li>Envían la constancia por email</li></ul></div>
              {_arrow(True)}
              <div class="pv-shared-system"><p class="pv-shared-title">Sistema de servicio técnico</p><p>Contratos, equipos, casos,<br>servicios y clientes</p><div class="pv-hosting">{_aws(True)}<span>Alojado en AWS</span></div></div>
              {_arrow(True)}
              <div class="pv-role"><p class="pv-role-title">Administración</p><ul><li>Consulta el estado del servicio</li><li>Revisa contratos y facturación</li><li>Comparte el calendario operativo</li></ul></div>
            </div>
            <p class="pv-operation-note">La bitácora interna queda separada de la orden que recibe el cliente.</p>
          </div>
          <figcaption>Esquema del sistema desarrollado para Photonix: dos vistas sobre la misma información.</figcaption>
        </figure>'''
    if key == 'caso-escala24x7':
        exchange_copy = items if items is not None else [
            'Las oportunidades creadas por ventas en HubSpot se envían automáticamente a AWS Partner Central.',
            'Las oportunidades generadas por AWS llegan a HubSpot para su gestión comercial.',
            'Los cambios mantienen actualizados los pipelines de ambas plataformas sin replicar la información a mano.',
        ]
        if len(exchange_copy) != 3:
            raise ValueError('Escala24x7 requires its three documented exchanges.')
        return f'''<figure class="pv-figure pv-solution pv-exchanges">
          <div class="pv-solution-stage">
            <div class="pv-exchanges-heading"><p class="pv-detail-title">Cómo viajan las oportunidades</p><div class="pv-exchanges-brands">{_hubspot(True)}<span aria-hidden="true">/</span><div>{_aws(True)}<span>Partner Central</span></div></div></div>
            <ul class="pv-exchange-list">
              <li><div><strong>Creación desde ventas</strong><p>{exchange_copy[0]}</p></div><div class="pv-route"><span>HubSpot</span>{_arrow()}<span>AWS Partner Central</span></div></li>
              <li><div><strong>Oportunidades generadas por AWS</strong><p>{exchange_copy[1]}</p></div><div class="pv-route"><span>AWS Partner Central</span>{_arrow()}<span>HubSpot</span></div></li>
              <li><div><strong>Actualizaciones del pipeline</strong><p>{exchange_copy[2]}</p></div><div class="pv-route"><span>HubSpot</span>{_arrow(True)}<span>AWS Partner Central</span></div></li>
            </ul>
            <p class="pv-exchanges-note">Los campos de HubSpot se adaptan a la estructura que requiere AWS Partner Central.</p>
          </div>
          <figcaption>Intercambios de la integración de Escala24x7. Esquema explicativo.</figcaption>
        </figure>'''
    if key == 'caso-ads-mexicana':
        return f'''<figure class="pv-figure pv-solution pv-quotation">
          <div class="pv-solution-stage">
            <div class="pv-quotation-heading">{_hubspot(True)}<p class="pv-detail-title">Datos y cotizaciones vinculados al negocio</p></div>
            <ol class="pv-quotation-steps">
              <li><p class="pv-step-label">Datos del CRM</p><strong>La información ya está disponible</strong><p>Negocio, compañía, contactos y productos del catálogo.</p>{_arrow()}</li>
              <li><p class="pv-step-label">Reglas de ADS</p><strong>El cotizador aplica los cálculos</strong><p>Precios, descuentos y recomendaciones definidos para sus propuestas.</p>{_arrow()}</li>
              <li><p class="pv-step-label">Registro en HubSpot</p><strong>La propuesta queda asociada</strong><p>Se crea la cotización y se vincula al negocio correspondiente.</p></li>
            </ol>
          </div>
          <figcaption>Esquema del flujo del cotizador de ADS Mexicana.</figcaption>
        </figure>'''
    raise ValueError(f'Unsupported project solution: {key}')
