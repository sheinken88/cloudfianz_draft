# Servicio de software: recuperar profundidad, afinar la lectura

Revisión del 2 de noviembre de 2026, posterior a la propuesta simplificada `c7739c4`.

## Base y límites

Se recuperan los textos y la arquitectura de `bd456b4`: apertura, problemas desarrollados, portfolio de tres clientes, criterio de solución, alcance y entrega, modalidades, FAQ, respaldo y contacto. No se fija una meta de reducción de palabras o altura. La prioridad es explicar el criterio de Cloudfianz y las condiciones de una inversión en software.

Paleta: azul `#0B1D3A`, verde `#12B5A5`, blanco `#FFFFFF`, menta `#E8F4F0`, gris `#55616F`. Manrope para títulos e Inter para lectura. Se conserva la apertura corregida, con H1 de 56 px y captura íntegra. Capítulos de 42 px, subtítulos de 27–34 px y cuerpo de 16–17 px. Márgenes de 76 px en desktop y 48–56 px en móvil; no se comprime el cuerpo del texto.

```
[propuesta original + CTA       ][producto real, presentación breve]

[problemas del cliente: introducción y explicaciones completas    ]
[venta: bloque principal                                        ]
[operación                     ][nuevo servicio                 ]

[portfolio: Despegar, otra vista original del producto + relato   ]
[Photonix: contexto + relato    ][ADS: resultado + relato        ]

       [Criterio: evaluar alternativas y costos de operación]
[Alcance: resultado acordado, condiciones, validación y traspaso  ]
[Modalidades de contratación: cuatro entradas independientes     ]
[FAQ compacta, con respuestas íntegras                            ]
[Respaldo Digifianz                                              ]
[Contacto                                                       ]
```

## Revisión contra el pedido

- Se recupera el texto original completo de problemas, proyectos, alternativas, alcance, modalidades y FAQ. Sólo cambia el título de contratación para distinguirlo del proceso. No vuelve la secuencia esquemática de diagnóstico/diseño/implementación de la versión breve.
- Hero y portfolio cumplen funciones distintas: la apertura muestra el producto con una identificación breve y lleva al caso dentro del portfolio; allí se explica el proyecto y se accede a la historia completa. Se evita repetir la misma captura usando la vista general en el hero y el catálogo original en el portfolio.
- Se retoman las composiciones del portfolio anterior, incluida la imagen institucional de Photonix con su identificación explícita. No se presenta esa foto como software desarrollado y no se recrean logos ni interfaces.
- Los ajustes son de escala, aire y legibilidad: capítulos más contenidos, espaciado entre secciones, imagen íntegra y ampliable, FAQ nativa exclusiva y objetivos de clic cómodos. Se conservan las diferencias entre los bloques en lugar de convertir todo en tres columnas de servicios.
- Los estilos siguen siendo exclusivos del servicio. Se conserva el caso Despegar aprobado, la homepage y el alcance provisional del contacto. Versionar como una nueva iteración; no revertir ni borrar commits anteriores.

## Dar presencia al respaldo de Digifianz

La franja institucional de 136 px se convierte en un bloque secundario con título visible, dos párrafos breves y marca con credencial y enlace. Se conserva su ubicación antes del contacto. Fondo azul `#0B1D3A`, título Manrope de 36 px (menor que los capítulos), cuerpo Inter de 16 px y texto secundario `#C1CFDB`; dos columnas de 250 px y ancho flexible, separación de 78 px y padding vertical de 54 px. En móvil se apilan, con título de 30 px y logo de 175 px.

```
[Digifianz                ][El respaldo de Digifianz                  ]
[Elite Partner de HubSpot ][Relación entre las marcas y qué aporta    ]
[Conocé Digifianz         ][esa experiencia a la solución del cliente ]
```

El título y la relación explícita con una empresa consolidada aportan presencia; la credencial aporta evidencia. No se agregan cifras, premios, nombres de personas ni insignias recreadas. La condición de Elite está verificada el 2 de noviembre de 2026 en el [directorio oficial de HubSpot](https://ecosystem.hubspot.com/es/marketplace/solutions/digifianz). La marca enlaza al sitio institucional. El resto de la página conserva su arquitectura y contenido.

### Ajuste de redundancia

El logo identifica la empresa; el título explica el aporte: “Experiencia de negocio detrás del software”. La relación entre Cloudfianz y Digifianz sigue explícita en el primer párrafo. El enlace pasa a “Conocé la empresa”, con nombre accesible que conserva el texto visible y especifica el destino. Se mantienen la composición, los tokens y las proporciones anteriores; esta revisión sólo edita dos etiquetas para que cada elemento cumpla una función distinta.

## Equilibrio de la sección de necesidades

Retoque localizado, sin cambiar textos ni estructura. Se mantiene el bloque de ventas con fondo mint y las dos aplicaciones complementarias sobre blanco. Paleta existente: navy #0B1D3A, mint #E8F4F0, blanco #FFFFFF, gris #55616F y verde de lectura #3E5D54. Manrope para títulos, Inter para cuerpo.

```
[Título e introducción, sin cambios de contenido          ]
[Venta: título          ][Explicación                    ]  fondo mint
[Operación              ][Nuevo servicio                 ]
[Explicación            ][Explicación                    ]
```

El ajuste usa la misma retícula de dos columnas, medianil e inset en los tres bloques, con títulos de 30 px y cuerpos de 16 px. El fondo ya distingue la aplicación principal: no necesita además un título desproporcionado. El título del bloque mint se alinea arriba con su explicación. El espaciado inferior mantiene el ritmo y la alineación vertical; en móvil se conservan los mismos márgenes interiores y una columna de lectura. Se revisó el plan contra el pedido: no se agregan tarjetas, iconos, líneas, imágenes ni nuevos mensajes.

### Segunda revisión: hacer visible la relación entre las aplicaciones

El ajuste anterior resultó demasiado tenue. Se mantiene el orden y el contenido, pero la composición comunica ahora que las tres situaciones pertenecen a la misma propuesta: introducción en dos columnas equilibradas y un único fondo mint que reúne ventas, operación y nuevos servicios. No se crean tarjetas individuales. Se utiliza una sola separación horizontal dentro del grupo para distinguir la aplicación principal del par complementario.

```
[Título de la sección       ][Introducción                    ]
┌ Fondo mint común, radios de 8 px ───────────────────────────┐
│ [Ventas: título           ][Explicación                    ] │
│ ────────────────────────────────────────────────────────── │
│ [Operación                ][Nuevo servicio                 ]│
│ [Explicación              ][Explicación                    ]│
└────────────────────────────────────────────────────────────┘
```

Se conservan navy #0B1D3A, mint #E8F4F0, blanco #FFFFFF y gris #55616F; Manrope e Inter. H2 de 38 px en desktop, H3 de 30 px, cuerpo de 16–17 px. En móvil, introducción y aplicaciones se apilan con un mismo eje de lectura. La diferencia debe percibirse en la composición completa, sin depender de comparar unos pocos píxeles de espaciado.

### Tres situaciones con el mismo peso

Se adopta la propuesta del usuario: tres columnas iguales, sin destacar la primera. Se elimina la superficie mint conjunta y se acorta cada descripción a 2–3 líneas, acompañada por un ejemplo funcional explícito. La introducción se reduce a una frase.

Paleta: blanco #FFFFFF, navy #0B1D3A, gris #55616F, línea #DCE3E9 y acento #08796F para identificar los ejemplos. Manrope 28 px para los tres títulos, Inter 16 px para descripciones y 15 px para ejemplos. Sin tarjetas, iconos ni fondos de color.

```
[Título de sección             ][Introducción breve             ]
[Venta y atención       ][Operación que creció ][Nuevo servicio ]
[Descripción breve     ][Descripción breve    ][Descripción    ]
[Ejemplo: cotizador    ][Ejemplo: panel       ][Ejemplo: portal]
```

Los ejemplos concretan el tipo de solución: cotizador conectado al CRM, panel de proyectos y facturación, portal para solicitar y seguir servicios. Son ejemplos de aplicaciones, sin atribuir un proyecto o resultado no documentado. Las descripciones se verifican visualmente sin truncamiento ni ocultar contenido. Debajo de 900 px se apilan los tres conceptos para conservar el ancho de lectura.

## Arquitectura narrativa integrada · implementación del 2 de noviembre

Se aplica el recorrido aprobado: propuesta → identificación → evidencia → abordaje → contratación → confianza y contacto. Esta revisión reemplaza el orden de capítulos descrito al principio del documento, conservando el historial de decisiones.

Paleta existente: navy #0B1D3A, verde #12B5A5, blanco #FFFFFF, fondo suave #F5F7FA, mint #E8F4F0 y gris #55616F. Manrope para títulos e Inter para lectura; H1, H2 y necesidades mantienen sus escalas. Lectura alineada a la izquierda, cuerpos de 16–17 px, columnas fluidas y una columna en móvil. El protagonismo visual sigue en los productos reales, no en decoraciones o nuevos componentes.

```
[Hero: propuesta + contacto        ][Despegar: captura + enlace al caso]
[Necesidades: venta       ][operación       ][nuevo servicio           ]
[Nuestro trabajo: REVIANZ, contexto + solución + cambio + mockup       ]
[Photonix: imagen institucional    ][contexto + solución + cambio      ]
[Del problema a una solución en uso: título + propósito                ]
[01 Entender                     ][alternativas y criterio            ]
[02 Diseñar                      ][alcance y resultado esperado       ]
[03 Construir                    ][revisiones y validación            ]
[04 Poner en uso y evaluar        ][aceptación y transferencia         ]
[Cómo trabajar con nosotros: cuatro servicios con entregables         ]
[Digifianz: respaldo consolidado                                       ]
[Preguntas frecuentes compactas                                        ]
[Contacto                                                             ]
```

Despegar aparece una sola vez en el hero, con acceso directo a su caso. El portfolio desarrolla REVIANZ y Photonix, con la misma lógica de necesidad, solución y cambio, pero con jerarquía principal/secundaria. ADS conserva su contenido y acceso en el índice general. El mockup oficial de REVIANZ se identifica como ilustrativo; la foto de Photonix como institucional.

Se fusionan criterio y alcance en una secuencia editorial sin tarjetas ni controles nuevos. Los números representan pasos reales; los párrafos conservan evaluación de alternativas, costos de operación, definición de alcance, validación y traspaso. Contratación explica puntos de entrada y entregables independientes, sin repetir el proceso. Digifianz precede a las FAQ y el contacto. Revisión contra el pedido: se mantiene la profundidad donde aporta decisión, las necesidades breves aprobadas y la identidad visual, evitando nuevos bloques promocionales o repetir los casos.

### Necesidades: separar lectura y ejemplos

El usuario percibe la sección comprimida. Se conserva todo el texto y las tres columnas, pero se cambia su composición: encabezado y bajada sobre el mismo eje, ancho de lectura acotado y separación de 64 px antes de las aplicaciones. Los subtítulos pasan a 26 px frente al encabezado de 42 px. Descripciones y ejemplos comparten ejes horizontales mediante subgrid; cada ejemplo tiene una superficie suave #F5F7FA e inset propio, sin encerrar la aplicación completa en una tarjeta. Se conservan navy #0B1D3A, gris #55616F, acento #08796F, blanco, Manrope e Inter. En móvil las aplicaciones se apilan con 44 px entre ellas.

```
[Título, ancho de lectura acotado                         ]
[Bajada                                                  ]

[Venta y atención     ][Operación         ][Nuevo servicio]
[Descripción         ][Descripción       ][Descripción   ]

[ Ejemplo en gris    ][ Ejemplo en gris  ][ Ejemplo gris ]
```

La intervención distingue tres niveles de lectura sin agregar contenido, números ni iconos. El espacio se concentra entre grupos, en vez de aumentar todas las separaciones por igual.

### Portfolio: apertura del caso REVIANZ

Se elimina el vacío bajo el título del caso. La marca se distingue del título descriptivo; debajo, contexto y cambio forman dos columnas de lectura. La acción principal se alinea al encabezado y el enlace externo mantiene un nivel secundario. El mockup sigue inmediatamente después de esta introducción. En móvil el orden es título, explicación, acciones y producto. Se mantienen Manrope/Inter, navy #0B1D3A, blanco, mist #F5F7FA, gris #55616F y acento #08796F. No se agrega una tarjeta envolvente, iconos ni contenido nuevo. Photonix y el resto de la página conservan su composición.

```
[REVIANZ                                                ]
[Título descriptivo                ][Ver caso / sitio    ]
[Contexto y solución               ][Cambio              ]
[Mockup oficial                                         ]
```
