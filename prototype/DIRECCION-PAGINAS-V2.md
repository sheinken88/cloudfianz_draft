# Segunda dirección para servicio y caso · 30 de octubre de 2026

## Sistema que se conserva

Azul profundo #0B1D3A, verde #12B5A5, blanco #FFFFFF, menta #E8F4F0 y gris de lectura #55616F. Manrope para títulos e Inter para lectura. Contenedor máximo de 1280 px y textos de 55–75 caracteres. Los logos y capturas reales no se alteran. El contenido aprobado y sus metadatos se mantienen.

## Problema de la primera composición

Necesidades, decisión, alcance y contratación repiten la misma relación título/columna de texto. Despegar presenta cinco capítulos con idéntica grilla y divisores. La card de apertura apila demasiadas superficies alrededor del producto. Variar solamente el color no resuelve esa monotonía.

## Desarrollo de software

Apertura de producto: el título ocupa el área principal, la captura real crece hacia el borde sobre una única superficie y el logo/caption quedan fuera de su marco. El bloque de necesidades utiliza una entrada amplia seguida de dos aplicaciones abiertas; no suma iconos ni marcadores arbitrarios. El portfolio distingue la demostración de software de Despegar, el contexto institucional de Photonix y el volumen comercial de ADS.

```
[titular y propósito     ][captura real a sangre       ]
[CTA                    ][marca y acceso al proyecto  ]

[cuándo hace falta       ][introducción               ]
[aplicación comercial amplia                           ]
[operación                     ][nuevos servicios      ]

[Despegar: imagen amplia                    ][caso      ]
[Photonix: contexto + relato     ][ADS: volumen + relato]

         [decisión: título + lectura acotada]
[alcance sobre azul: título amplio + compromiso       ]
[                 definición, validación y entrega    ]

[cuatro opciones independientes visibles, dos columnas]
[FAQ                    ][preguntas expandibles       ]
[Digifianz y CTA contextual                            ]
```

## Despegar

La portada combina identidad auténtica, resultado y producto con una ficha de proyecto horizontal. El problema se lee con contexto lateral; el enfoque destaca la decisión de conservar HubSpot como centro. La solución presenta una captura ancha y capacidades agrupadas; resultados tiene su propia superficie de contraste y la evolución funciona como epílogo compacto. Los capítulos se distinguen por su función y contenido.

## Revisión contra el brief

Se descarta una grilla de tres tarjetas para las aplicaciones y otra grilla idéntica para los casos: jerarquizar por contenido aporta más que cambiar el radio o la sombra. Se mantiene la familia tipográfica porque la debilidad está en composición y ritmo. La presencia de software real, sus reglas comerciales y las diferencias entre proyectos son el recurso visual distintivo; no se agregan dashboards, diagramas ficticios ni estadísticas decorativas. En móvil, lectura lineal y títulos más contenidos, sin carruseles obligatorios ni información inaccesible al teclado.


## Casos unificados y titular complementario · 3 de noviembre de 2026

Desarrollo de Software a Medida adopta «Software diseñado para los procesos de tu empresa» como propuesta de titular complementario a «Software a medida para mejorar cómo funciona tu negocio», que pasa a la Home. La bajada del servicio conserva sus aplicaciones comerciales, operativas y de nuevos servicios digitales.

REVIANZ y Photonix comparten un artículo blanco con borde discreto y radio de 16 px, sobre el fondo mist del design system. La marca, el contexto, el título, los dos párrafos y los enlaces ocupan la columna izquierda. El producto o imagen institucional ocupa un marco neutro a la derecha. En móvil, se apilan en ese mismo orden. Las marcas mantienen sus identidades dentro de este sistema común.

Ambos casos usan el CTA compartido `.case-button` verde mint de la Home. El enlace externo de REVIANZ conserva una jerarquía secundaria. Los textos aprobados y las aclaraciones de las imágenes se mantienen; el mockup de alcance de REVIANZ conserva todos sus servicios, importes y margen, con una disposición compacta de sus cifras. Photonix incorpora su logo original y su imagen se sigue identificando como contexto institucional.


## Escala24x7 en Desarrollo a Medida · 3 de noviembre de 2026

Por pedido del usuario, Escala24x7 reemplaza a REVIANZ en «Nuestro trabajo» del servicio. Mantiene el marco compartido con Photonix, el logo original, dos párrafos breves y el CTA mint. El texto resume la integración bidireccional entre HubSpot y AWS Partner Central y su beneficio operativo. La columna visual muestra un esquema tipográfico de esa conexión, identificado como tal; no representa una captura del software. El enlace abre el caso aprobado en el lector existente. Home y página del caso REVIANZ conservan su contenido.

El esquema de Escala24x7 incorpora los logos originales de HubSpot (SVG naranja de su sitio oficial) y AWS (variante monocroma oficial utilizada en la Home). Se conservan sin filtros ni recoloraciones, dentro de módulos blancos de igual jerarquía y con tamaños ópticos equilibrados. Las etiquetas «CRM comercial» y «Partner Central» aclaran la función de cada extremo.

Por preferencia posterior del usuario, el esquema de Escala24x7 adopta la variante oficial histórica de AWS con letras oscuras y sonrisa naranja. El SVG original se conserva intacto y con procedencia documentada en assets/aws/SOURCES.md. Se mantiene el tamaño y la disposición del esquema.


## Arquitectura compartida y capacidades específicas · 3 de noviembre de 2026

La nueva evaluación del usuario reemplaza la selección anterior de proyectos: Desarrollo vuelve a destacar Despegar y REVIANZ. Escala24x7 pasa a Integraciones, junto con ConsorcioAbierto. Automatizaciones muestra ConsorcioAbierto y Despegar con foco en facturación y documentos comerciales.

Los tres servicios comparten Hero → Problemas y soluciones → Casos reales → Cómo trabajamos → Preguntas frecuentes → CTA. La Home presenta Cloudfianz; cada servicio explica una capacidad con aplicaciones y ejemplos propios. Los titulares son:

- Desarrollo: «Construimos herramientas cuando el software existente no alcanza».
- Integraciones: «Conectá tus sistemas y dejá de cargar la misma información dos veces».
- Automatizaciones: «Automatizá las tareas que se repiten todos los días».

El Hero usa título a la izquierda y explicación con CTA a la derecha, sobre mist. Los recursos de los proyectos se reservan para los casos. Tres aplicaciones presentan la situación, la solución y un ejemplo concreto. Las cards de casos conservan el sistema de la Home: marco neutro, identidad del cliente, resumen breve, CTA mint y una única vista. Despegar usa una captura real ampliable; REVIANZ, un mockup ilustrativo de alcance; ConsorcioAbierto, una imagen de contexto identificada; Escala, el esquema HubSpot ↔ AWS con sonrisa naranja.

La metodología aparece una sola vez, con cuatro pestañas y entregables adaptados a cada servicio. Las preguntas frecuentes y el cierre también son específicos. La explicación institucional de Digifianz permanece en la Home y el pie compartido. Las páginas completas de casos mantienen su contenido.

Un único constructor (`page_layouts/service.py`) y una hoja de estilos (`dist/service-page.css`) sostienen esta arquitectura. `page_layouts/service_cases.py` concentra los recursos de casos. Se retiran el constructor y CSS duplicados de capacidades; el contenido de cada servicio sigue editable en Markdown.


## Hero de Desarrollo con producto real · 3 de noviembre de 2026

El Hero de Desarrollo incorpora la captura real del cotizador de Despegar, completa y sin alteraciones, sobre una superficie mint con borde suave. El logo original y un pie breve identifican el proyecto; la imagen enlaza al original para ampliarla. Se conserva el titular y la bajada, reunidos con los CTA a la izquierda en escritorio. La captura equilibra el bloque a la derecha. En móvil, el orden es titular, proyecto, descripción y acciones; el DOM respeta ese mismo recorrido de lectura y foco.

La variante se limita a Desarrollo mediante `service-hero-grid--project`. Las otras páginas conservan sus composiciones y el portfolio mantiene los dos casos. No se agregan cifras, interfaces ficticias ni movimiento automático.


## Recursos visuales en los tres Hero de servicios · 3 de noviembre de 2026

Integraciones y Automatizaciones adoptan el layout de Desarrollo: título y descripción con CTA a la izquierda, proyecto a la derecha. En móvil, el recurso aparece después del título y antes de la descripción. La captura de Despegar permanece intacta.

Integraciones muestra HubSpot ↔ AWS Partner Central con los logos oficiales, dos módulos equivalentes y flechas bidireccionales. La marca Escala24x7 y «Esquema de la integración» identifican el proyecto. Automatizaciones muestra el recorrido de las membresías en HubSpot, las reglas del contrato (descuentos, períodos y país) y la generación de facturas en Odoo. «Más de 15.000 facturas al mes» corresponde al caso documentado de ConsorcioAbierto; su marca y «Esquema del proceso» aclaran la evidencia.

Los esquemas son HTML/SVG estático; no simulan interfaces de producto ni presentan controles interactivos. Los logos mantienen sus archivos originales, incluida la sonrisa naranja de AWS. El SVG de Odoo se recuperó del sitio oficial y conserva su espacio de seguridad; fuente y hash en `dist/assets/brand/ODOO-SOURCE.md`. `page_layouts/service_heroes.py` mantiene estas composiciones junto con el Hero de Desarrollo.


## Índice de casos y páginas individuales · 3 de noviembre de 2026

`/es/casos` reúne Despegar, REVIANZ, ConsorcioAbierto, Photonix, Escala24x7 y ADS Mexicana en una grilla de dos columnas, que pasa a una columna en móvil. El título «Casos de éxito» y la introducción abren sobre mist. Cada artículo combina un recurso visual, la marca original, la capacidad aplicada, un resumen concreto y el CTA mint compartido. Las captions distinguen la captura real de Despegar, la vista ilustrativa de REVIANZ, la foto de contexto de Photonix y los esquemas de los otros proyectos. El cierre invita a conversar sobre una necesidad similar.

ConsorcioAbierto cuenta con página propia: contexto, problema, enfoque, solución, resultados y contacto. El Hero muestra el flujo HubSpot → AWS → Odoo con logos oficiales y la cifra mensual documentada. Photonix, Escala24x7 y ADS Mexicana también pasan del lector provisional a páginas completas con identidad, recurso visual, desarrollo del caso y CTA. Conservan los párrafos y listas aprobados; las composiciones y colores responden al sistema del sitio. Despegar y REVIANZ conservan sus páginas existentes.

Los enlaces «Casos» del menú y pie, «Ver todos los casos», las marcas de clientes y los CTA de proyectos navegan a estas rutas. El botón «Conocé cómo lo aplicamos en ConsorcioAbierto» de AWS en Home va directamente a `/es/casos/consorcioabierto-facturacion-hubspot-odoo`. Las páginas individuales vuelven al índice desde el breadcrumb. No quedan enlaces de casos que abran un popup.


## Hero de Casos y portada unificada de Despegar · 3 de noviembre de 2026

La apertura textual sobre mist se reemplaza por una composición de producto sobre navy #0B1D3A. «Casos de éxito» gana escala, la bajada se acorta y el CTA mint lleva al índice de proyectos. A la derecha, dos vistas escalonadas muestran el cotizador de Despegar y el detalle de alcance de REVIANZ. Se preservan Manrope, Inter y la paleta existente. En móvil queda solo la vista de Despegar para contener la altura; REVIANZ continúa en la grilla.

El usuario confirmó que la imagen correcta es la variante limpia, sin Digifianz en la cabecera ni acentos azules junto a las marcas. El mismo JPG adaptado se utiliza en todas las vistas generales del cotizador y sus ampliaciones, incluida Home y Solución en el caso individual. Las leyendas distinguen su tratamiento de marketing. El catálogo conserva su imagen específica.


## Apertura compacta del índice · 3 de noviembre de 2026

Tras el rechazo del Hero navy, el índice adopta una apertura blanca con H1 y bajada centrados. Se elimina la composición superpuesta, las vistas repetidas y el botón que bajaba a la grilla. El breadcrumb permanece alineado a la izquierda. La primera fila de casos es la evidencia visual de la página y aparece inmediatamente debajo.

El H1 usa Manrope a 64 px en escritorio y escala hasta 36 px en móvil. La cabecera ocupa aproximadamente 269 px a 1440 px de ancho y 237 px a 390 px. Se mantienen los textos, seis cards, destinos nativos y la versión limpia del cotizador. La primera imagen del índice carga con prioridad alta por estar ahora en el primer pantallazo.


## ConsorcioAbierto con jerarquía de caso completo · 3 de noviembre de 2026

La página toma como referencia la portada de Despegar y la lectura editorial de REVIANZ. El Hero navy combina la marca original, «Más de 15.000 facturas al mes, con las reglas de cada contrato» y la imagen del cliente aportada en el chat, sobre una única superficie mint. La ficha inferior resume trabajo, plataformas y países. La imagen mantiene su proporción y transparencia; su leyenda distingue el contexto del cliente de la integración desarrollada.

El contexto y desafío comparten una sección blanca de dos columnas. La decisión técnica se presenta sobre mist en dos bloques: qué se evaluó y cómo se resolvió. El esquema de integración sale del Hero y acompaña la explicación de Solución: tres plataformas conectadas en horizontal en escritorio, con recorrido vertical en móvil. Las cuatro reglas y la nota de implementación completan ese capítulo. Resultados conserva la cifra documentada y sus tres beneficios, sobre navy; el cierre mantiene los enlaces a consulta, servicios e índice.

Los párrafos y listas aprobados se conservan. La segunda oración de la apertura se traslada a la introducción de Solución, sin alterar sus hechos. El cambio de H1 concentra el resultado y evita repetir el nombre que ya identifica el logo.


## Photonix, Escala24x7 y ADS Mexicana con un criterio común · 3 de noviembre de 2026

Las tres páginas extienden la dirección de ConsorcioAbierto. El Hero navy reúne logo original, titular de resultado, apertura breve y una ficha de tres datos específicos del proyecto. El contexto del cliente acompaña al desafío dentro de una misma sección blanca. Photonix y ADS incorporan la decisión técnica en dos bloques; Escala24x7 pasa directamente del desafío a la solución. Los H1 dejan de repetir la marca y el detalle de las aperturas se conserva al comienzo de Solución.

La superficie mint de Solución contiene composiciones diferentes según el trabajo realizado:

- Photonix presenta los roles de técnicos y administración alrededor del sistema de servicio técnico alojado en AWS.
- Escala24x7 integra sus tres intercambios originales en el diagrama: creación desde HubSpot, oportunidades generadas por AWS y actualizaciones de ambos pipelines. Cada ítem aparece una sola vez.
- ADS Mexicana recorre tres pasos: datos disponibles en el CRM, aplicación de las reglas de cálculo y cotización registrada en el negocio de HubSpot.

Los resultados comparten una superficie navy y una jerarquía adaptada a la evidencia: ADS destaca más de 50 cotizaciones por día y el paso de horas de cálculo a propuestas en minutos. Photonix y Escala24x7 presentan sus capacidades operativas documentadas. El cierre común mantiene los enlaces de consulta, servicios e índice. Se conservan los párrafos, listas y matices aprobados, incluyendo los límites del costo de infraestructura de Photonix y las funcionalidades que todavía corresponden a etapas posteriores.


## Contacto, Cómo trabajamos y navegación compartida · 3 de noviembre de 2026

El alcance vigente pasa a trece páginas: Home, tres servicios, índice, seis casos individuales, `/es/contacto` y `/es/como-trabajamos`. La cabecera y el pie llevan a las nuevas páginas; los CTA de consulta apuntan a Contacto. La Home conserva el formulario y las anclas `/es#contacto`, `/es#consulta` y `/es#como-trabajamos` para los enlaces anteriores.

Contacto prioriza una apertura práctica y breve, con título navy sobre blanco y formulario sobre mint, visible junto al texto en escritorio. Sus cuatro campos son Nombre, Empresa, Email de trabajo y Qué necesitás resolver. La explicación de qué pasa después queda junto al contenido en escritorio y después del formulario en móvil. Mantiene la simulación local de Home: valida los campos y muestra una confirmación de prueba, con una nota explícita de que no envía ni guarda datos. El formulario continúa sin backend conectado.

Cómo trabajamos desarrolla cuatro modalidades contratables por separado: auditoría, diseño, implementación y soporte. El selector utiliza pestañas con mejora progresiva; sin JavaScript, todos los contenidos permanecen visibles. Cada panel relaciona la actividad con sus entregables y la participación del cliente. Los acuerdos iniciales, ejemplos de proyectos y preguntas frecuentes breves explican cómo definir el trabajo; alcance, presupuesto, calendario y responsabilidades se acuerdan para cada proyecto.

El pie se extrae a `templates/footer.html`, con `dist/footer.css` compartido por las trece páginas. Agrupa Soluciones, los enlaces de Cloudfianz, el respaldo de Digifianz y el aviso de privacidad. `templates/home.html` mantiene la cabecera y los diálogos comunes; `build-pages.py` incorpora la plantilla del pie durante la generación. Los textos de las páginas nuevas viven en `content/pagina-contacto.md` y `content/pagina-como-trabajamos.md`, con composiciones en `page_layouts/contact.py` y `page_layouts/method.py` y estilos en `dist/contact-page.css` y `dist/method-page.css`.
