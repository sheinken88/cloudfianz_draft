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
