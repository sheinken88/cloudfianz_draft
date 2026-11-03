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
