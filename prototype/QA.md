# Revisión local v2 · 23 de octubre de 2026

La segunda propuesta está en [el selector de revisión](http://127.0.0.1:3001/review.html) y [la homepage directa](http://127.0.0.1:3001/index.html).

## Comprobaciones realizadas

- Inspección visual de apertura y casos en escritorio a 1440 px, y de la página completa en escritorio y móvil a 390 px. Una segunda revisión visual independiente no encontró bloqueos importantes de composición.
- Apertura revisada también a 360 px. Medición del ancho del documento a 360, 390, 768, 1024, 1280 y 1440 px: coincide con el viewport, sin desplazamiento horizontal de la página.
- Los 14 elementos de imagen cargan correctamente. Las capturas de Despegar conservan su proporción; las imágenes se encuadran dentro de superficies con overflow controlado.
- Cloudfianz coincide byte a byte con el original usado en las Slides. Las otras marcas son archivos de fuentes oficiales y no reconstrucciones tipográficas. Properix y Photonix tienen leyendas y textos alternativos que identifican su uso como contexto del cliente.
- Menú móvil: apertura y cierre al navegar comprobados.
- Selectores: clic en integración, avance con flecha derecha a automatización, cambio de etapa a Diseño y retorno a valores iniciales. La selección y los paneles de los dos grupos permanecen independientes. La orientación ARIA de soluciones cambia con el breakpoint.
- Lector: apertura del texto aprobado de desarrollo a medida y cierre con Escape comprobados.
- Preguntas frecuentes: expansión y cierre comprobados.
- Agenda: abre su aviso de simulación; el enlace alternativo lleva al formulario.
- Formulario: recorrido con datos de prueba y confirmación local comprobados; campos limpiados después. El código cancela el envío y no contiene persistencia de datos.
- Consola: sin errores ni advertencias durante los recorridos comprobados.
- Selector de revisión: Móvil cambia a 390 px y Escritorio vuelve a 1440 px.
- Comprobación estática: 41 IDs únicos, 14 anclas locales válidas, 7 destinos de lectura presentes y 15 referencias locales de imágenes/scripts existentes.
- `node --check` pasó para app.js y review.js; `git diff --check` pasó.
- CSS incluye foco visible y reducción de movimiento. No se presenta esta revisión como una auditoría completa de accesibilidad ni una prueba en dispositivos físicos.

## Correcciones durante la revisión

Se corrigió la proporción de las capturas en los casos, se aumentaron los pies de imagen a 12 px en escritorio y 11 px en móvil, se redujeron las etiquetas de la apertura y se reemplazó el badge de HubSpot por una frase institucional. Las capturas completas finales se tomaron con las imágenes cargadas, scroll al inicio y sin foco en el skip-link.

## Evidencia v2

Carpeta: `/Users/sheinken/Desktop/Cloudfianz/outputs/homepage-visual-v2-20261023/`

- `desktop-inicial.png`: apertura a 1440 × 1000.
- `desktop-casos.png`: caso Despegar a 1440 × 1000.
- `desktop-completa.png`: homepage completa a 1440 px.
- `mobile-inicial.png`: apertura a 390 × 844.
- `mobile-completa.png`: homepage completa a 390 px.

## Fuentes

- [Marcas e imágenes de contexto](dist/assets/brand/SOURCES.md).
- [Capturas del cotizador Despegar](dist/assets/projects/SOURCES.md).
- Textos aprobados: `outputs/homepage-20261022/` del workspace.

## Límites

La agenda, la recepción de consultas, la política de privacidad y la medición comercial no están conectadas. El envío es una simulación explícita. Los servicios y casos usan un lector provisional; el diseño de sus páginas queda fuera de esta entrega. La propuesta es local, usa `noindex, nofollow` y no fue publicada.


## Actualización de casos · 29 de octubre de 2026

Se reemplazaron los textos de Despegar, Photonix y ConsorcioAbierto y se añadieron Escala24x7 y ADS Mexicana. Se actualizaron el índice, los resúmenes de la homepage y los ejemplos relacionados en servicios. El generador utiliza ahora `prototype/content/` como fuente vigente.

Comprobado: apertura de los cinco casos desde la homepage, índice con cinco entradas, enlaces internos generados válidos (9 contenidos), títulos y descripciones SEO presentes en las fuentes. Revisión visual de las nuevas reseñas en escritorio y a 390 px; sin desborde horizontal. Revisado el titular ampliado de ConsorcioAbierto en móvil y el lector sin desborde; cierre con Escape correcto. Sin errores de consola durante la revisión.

Capturas: `outputs/casos-web-20261029/nuevos-casos-desktop.png` y `nuevos-casos-mobile.png` en el workspace. La edición continúa siendo local; no se desplegó ni se crearon rutas SEO independientes.

## Primeras páginas independientes · 29 de octubre de 2026

Rutas: `/es/desarrollo-software-a-medida` y `/es/casos/despegar-cotizador-hubspot`. Enlazadas desde `/es`, desde los textos relacionados y entre sí. La homepage conserva su composición.

### Verificado

- Inspección visual de ambas aperturas en escritorio a 1440 px, de los proyectos y contratación/FAQ del servicio, y de los resultados del caso. Captura completa del caso inspeccionada, con ambas imágenes cargadas.
- Caso Despegar revisado visualmente a 390 px. Medición del ancho del documento a 360, 390, 768, 1024 y 1440 px: coincide con el viewport, sin desborde horizontal. Las cinco imágenes cargaron correctamente.
- Navegación real desde Desarrollo al caso Despegar. Anclas de proyectos y secciones del caso comprobadas. El encabezado de Resultados queda debajo de la cabecera fija.
- Pestañas de contratación: clic en Diseño y avance con flecha derecha a Implementación; una sola pestaña seleccionada y un solo panel visible. Expansión de una pregunta frecuente comprobada.
- Lectores de Photonix desde Desarrollo e Integración desde Despegar: contenido cargado desde la ruta absoluta, cierre con Escape y enlaces a las páginas nuevas presentes. Corregida la filtración de los tamaños de titulares de páginas internas hacia estos diálogos.
- HTML generado: un H1 por página, IDs únicos, descripción y canonical propios, enlaces y recursos locales existentes. Las tres páginas tienen 14, 7 y 5 imágenes, respectivamente, con textos alternativos.
- HTTP local: las tres rutas devuelven 200; variantes con barra final o `index.html` redirigen con 301 a la URL acordada; se conservan parámetros de consulta. Rutas desconocidas y directorios devuelven 404; URLs malformadas, 400. HEAD no devuelve cuerpo; métodos distintos de GET/HEAD devuelven 405.
- El servidor envía `X-Robots-Tag: noindex, nofollow` y `/robots.txt` bloquea rastreo. Los HTML incluyen `noindex, nofollow`. No se publicó el sitio.
- `npm run build:proposal`, comprobación de sintaxis de `app.js`, `review.js` y `serve.mjs`, y comprobación de whitespace de Git.

### Pendiente de completar en navegador

El control del navegador dejó de responder al final de la pasada y no se recuperó al intentar obtener la pestaña ni el inventario. No se considera cerrada la revisión visual de esta entrega.

- Inspección visual del servicio en móvil y tablet.
- Selector de las tres páginas y modos de dispositivo en `review.html`.
- Recorrido final de menú móvil y CTA de contacto desde las páginas nuevas, navegación atrás/adelante y lectura de consola.

La implementación responsive y los destinos de contacto están presentes; esta lista distingue lo implementado de lo comprobado visualmente. Agenda, envío, privacidad y medición continúan siendo provisionales.

### Evidencia

`outputs/paginas-web-20261029/` del workspace contiene `despegar-desktop.png`, `despegar-desktop-completa.png`, `despegar-mobile.png` y `despegar-mobile-completa.png`. Las capturas completas conservan el contenido entero para revisar composición y lectura. Los tamaños intermedios se midieron en navegador; no representan pruebas en dispositivos físicos.

## Segunda composición de servicio y caso · 30 de octubre de 2026

Se sustituyó la presentación repetida de título/columna por composiciones específicas: apertura de producto abierta, necesidades en dos niveles, portfolio con tres tratamientos, decisión de lectura acotada, alcance con jerarquía propia y cuatro formas de contratación visibles. Despegar incorpora portada de proyecto, ficha horizontal, contexto lateral, enfoque editorial, solución con evidencia amplia, resultados sobre azul y epílogo compacto.

### Comprobaciones de esta entrega

- Inspección visual de ambas aperturas a 1440 × 1000 y 390 × 844, y de sus capturas completas. Inspección adicional del portfolio, preguntas frecuentes, solución y resultados. Una revisión visual independiente del servicio no encontró solapamientos, cortes de contenido ni problemas bloqueantes.
- En ambas páginas, el ancho del documento coincide con el viewport a 360, 390, 768, 1024 y 1440 px. La apertura del servicio recorta intencionalmente la captura, dentro de su superficie; la imagen completa aparece en Proyectos y en el caso.
- Todos los recursos de imagen cargados antes de las capturas completas. Se reutilizan archivos originales; Photonix conserva una leyenda y texto alternativo que distinguen el contexto institucional del trabajo desarrollado.
- Contenido: comparación normalizada de los 28 párrafos/elementos de lista del servicio y los 24 del caso contra los HTML nuevos, sin faltantes. Las cuatro opciones de contratación están disponibles sin JavaScript. Los textos fuente y metadatos SEO no se modificaron.
- Menú móvil: apertura, cierre y navegación desde el servicio a `/es#contacto`; menú cerrado al llegar. Navegación atrás/adelante comprobada.
- Pregunta frecuente abierta y cerrada en el servicio. Lectura de Integración desde Despegar en móvil, diálogo de 358 px dentro del viewport de 390 y cierre con Escape comprobados.
- Anclas de proyectos, solución y resultados comprobadas; título de Resultados a 225 px frente a una cabecera de 96 px, sin quedar tapado.
- Consola sin errores ni advertencias en el recorrido de las páginas nuevas.
- Comprobación estática de las tres páginas: un H1, IDs únicos, enlaces y anclas entre páginas válidos, recursos existentes y metadatos propios. Sintaxis Python válida, construcción completada y whitespace de Git comprobado.
- La homepage conserva su HTML generado y sus estilos. El CSS de Despegar sólo se carga en la ruta del caso. Agenda, formulario, política y analítica conservan su alcance provisional.

### Pendiente y límites

La revisión móvil del servicio y la navegación directa pendientes del 29 de octubre quedaron completadas. El selector `review.html` sigue pendiente de validación visual: al intentar adquirir su pestaña existente, que mostraba una página de error, la política de URL del navegador bloqueó la observación por protocolo no permitido. No se intentó eludir el bloqueo. Las páginas comerciales se revisaron directamente por HTTP local. El selector no cambió en esta entrega.

Esta revisión no equivale a una auditoría integral de accesibilidad, rendimiento o dispositivos físicos. El sitio sigue siendo local y fuera del índice.

### Capturas

Carpeta `outputs/paginas-visual-v2-20261030/` del workspace:

- `servicio-desktop.png` y `servicio-desktop-completa.png`.
- `servicio-mobile.png` y `servicio-mobile-completa.png`.
- `despegar-desktop.png` y `despegar-desktop-completa.png`.
- `despegar-mobile.png` y `despegar-mobile-completa.png`.
- `despegar-resultados-desktop.png` y `despegar-resultados-mobile.png`.

## Hero Despegar · 2 de noviembre de 2026

- Nueva composición: identidad lateral, título y descripción en un mismo eje y captura completa debajo. En móvil la identidad pasa a una fila y la escala del título se ajusta para evitar cortes excesivos.
- Reemplazada la imagen del hero por el PNG nítido de 1633 × 887 px incrustado en el documento interno `Caso de Estudio del Cotizador`. Archivo original y copia local idénticos byte por byte. Fuente y hash registrados en `dist/assets/projects/SOURCES.md`; corregida la afirmación anterior de que la imagen publicada era una captura original verificada.
- Construcción `npm run build:proposal` y `git diff --check` completados. Comparación del HTML contra el commit anterior: H1, descripción, cabecera, metadatos y todo el documento posterior al hero idénticos. Las reglas CSS ajenas al hero no cambian. Homepage y servicio conservan sus archivos.
- Revisión visual en navegador a 1440 × 1000 y 390 × 844. En móvil, ancho del documento de 390 px sin desborde; la imagen carga a sus dimensiones originales. Enlace a la imagen completa activado con Enter y nueva pestaña con el PNG de 1633 × 887 px comprobada.
- Evidencia en `outputs/despegar-hero-20261102/hero-desktop.jpg`, `hero-desktop-completo.jpg` y `hero-mobile.jpg`, fuera del checkout. Desktop también sin desborde y consola sin errores ni advertencias. Las pruebas usan viewports de navegador, no dispositivos físicos.
- El resto de las imágenes de la página y del sitio no se sustituyen en esta iteración; quedan para una revisión específica. Esta entrega se limita al hero, tal como se solicitó.

## Resumen e índice de Despegar · 2 de noviembre de 2026

- El cambio de negocio toma el nivel principal; negocio y solución acompañan en una columna secundaria. Sin tarjetas, bordes de tabla ni divisores verticales. Los seis textos de etiquetas y descripciones permanecen íntegros.
- Índice de 56 px en desktop, fijo debajo de la cabecera de 96 px. Capítulo activo indicado por color, subrayado y `aria-current="location"`. En móvil queda en el flujo con enlaces de al menos 44 px de alto. Las anclas siguen siendo enlaces nativos; la mejora JavaScript sólo indica posición y estado fijo.
- Inspección visual del resumen a 1440 × 1000 y 390 × 844, sin desborde horizontal. Clic en Resultados: índice entre los píxeles 96 y 152, título a 281 px y estado activo correcto. Navegación con Enter a Enfoque en móvil: título a 127 px, debajo de la cabecera de 74 px, e indicador actualizado.
- Revisión adicional a 360 y 1024 px, sin desborde. Los cuatro enlaces conservan 44 px de alto y caben en una sola fila a 360 px. A 1024 px, el índice comienza exactamente debajo de la cabecera de 86 px; Producto queda activo y su título a 261 px, libre de superposiciones.
- Comparación del HTML: hero y los cinco capítulos idénticos; homepage y servicio idénticos; IDs únicos. La transición al primer capítulo reduce su espacio superior y las anclas compensan el índice fijo. No cambian los textos, imágenes ni metadatos del caso.
- `npm run build:proposal`, `node --check prototype/dist/case-navigation.js` y `git diff --check` completados. La regla existente de movimiento reducido conserva el desplazamiento inmediato para esa preferencia.
- Capturas en `outputs/despegar-resumen-20261102/` del workspace: `resumen-desktop.jpg`, `resumen-mobile.jpg` e `indice-sticky-desktop.jpg`. Se conserva el versionado local sin publicación remota.

## Franja compacta de Despegar · revisión del 2 de noviembre de 2026

Esta revisión sustituye el resumen asimétrico y elimina el índice a pedido del usuario.

- Franja de tres columnas en desktop, en orden negocio, solución y cambio. Las tres descripciones usan 20 px; el cambio se diferencia por peso 600 y etiqueta verde. Fondo gris claro, sin divisores, tarjetas ni titulares de gran escala. Altura comprobada: 156 px a 1440 px de ancho.
- Eliminados el HTML del índice, su envoltorio, todos sus estilos, el archivo `case-navigation.js`, su carga y la compensación adicional para el índice fijo. Las anclas existentes de los capítulos siguen disponibles.
- Revisión visual en Chrome a 1440 × 1000 y 390 × 844. En móvil, conceptos apilados con texto de 18 px; franja de 266 px a 390 px. Anchos de documento comprobados a 360, 390 y 1440 px sin desborde horizontal.
- Construcción y `git diff --check` completados. Comparación contra la versión anterior: tres conceptos íntegros, hero y capítulos sin cambios de HTML, contacto intacto, homepage y servicio idénticos. Ajustado únicamente el espacio de transición al primer capítulo.
- Capturas: `outputs/despegar-franja-20261102/franja-desktop.jpg` y `franja-mobile.jpg` en el workspace. Trabajo local, sin push ni despliegue.

## Despegar: relato, producto y resultados · revisión integral del 2 de noviembre de 2026

- Hero simplificado a identidad, título y una frase de síntesis. Eliminada la franja redundante: el contexto se integra con el desafío en un eje editorial. La navegación interna permanece eliminada y el ancla anterior `#resumen` llega al relato.
- Enfoque presentado como tres etapas documentadas: relevamiento, validación e integración. Secuencia horizontal en desktop y vertical en móvil. La solución concentra la vista general original del cotizador, sus funcionalidades y un detalle de su catálogo. Resultados reserva el mayor énfasis a “De horas a minutos”; la evolución se integra al cierre de ese capítulo.
- PNG del catálogo recuperado del mismo documento interno que la vista general. Los dos archivos locales son idénticos byte por byte a sus originales; hashes y procedencia en `dist/assets/projects/SOURCES.md`. El recorte del catálogo es sólo de presentación CSS; su enlace permite ver el archivo completo. Las dos imágenes públicas anteriores ya no se utilizan en el caso.
- Dos ajustes editoriales acotados en el texto fuente: la apertura conserva la frase de solución y “antes equipo de Media Sales” pasa al contexto. El problema de las planillas y la adopción diaria permanecen en sus capítulos. Comparación normalizada de los 24 párrafos y elementos de lista del contenido vigente contra el HTML: todos presentes. H1, metadatos, cabecera, CTA y pie idénticos a la versión anterior.
- Inspección visual de apertura, proceso, producto y resultados a 1440 × 1000 y 390 × 844. Ancho del documento igual al viewport a 360, 390, 768, 800, 1024 y 1440 px. Catálogo encuadrado sin alterar su contenido; ambas capturas cargadas antes de guardar las vistas completas.
- Enlace al catálogo completo activado con Enter desde móvil: nueva pestaña con PNG de 1641 × 883 px verificada. Se conserva foco visible y el aviso accesible de nueva pestaña. La vista general también ofrece ampliación mediante enlace nativo.
- Construcción `npm run build:proposal`, IDs únicos, un H1, recursos locales existentes y `git diff --check` verificados. Homepage, página de servicio y estilos/scripts compartidos idénticos. En `content.json` sólo cambia el caso Despegar. Sin errores de aplicación observados; Chrome muestra advertencias de una extensión externa (`locatorjs`), ajenas al sitio.
- Evidencia en `outputs/despegar-caso-v3-20261102/` del workspace: `desktop-completa.jpg`, `mobile-completa.jpg`, `producto-desktop.jpg`, `resultados-desktop.jpg`, `hero-mobile.jpg`, `proceso-mobile.jpg` y `resultados-mobile.jpg`. Los viewports de navegador no sustituyen pruebas en dispositivos físicos.
- Trabajo y versionado locales. El sitio sigue fuera del índice y no se publica. Las imágenes reutilizadas en otras páginas quedan fuera de esta revisión.

## Captura original en el hero aprobado · 2 de noviembre de 2026

- Se añade la vista general original del cotizador al hero: dos columnas equilibradas en desktop y captura debajo del texto en tablet/mobile. Título fluido de 40–48 px en dos columnas; se conserva la escala anterior al apilar. Imagen íntegra, con dimensiones explícitas, prioridad alta de carga y enlace de ampliación.
- Inspección visual a 1440 × 1000, 1200 × 900 y 390 × 844. El hero completo cabe en el viewport de 390 × 844. Sin desborde horizontal en 360, 390, 768, 1024, 1200 y 1440 px. Captura cargada con sus dimensiones originales de 1633 × 887 px.
- Ampliación activada con Enter: apertura del PNG original en una nueva pestaña verificada. Se conserva el foco visible y el aviso de nueva pestaña.
- Construcción y `git diff --check` completados. Comparación contra el commit anterior: textos del hero, metadatos y todo el HTML posterior al hero idénticos. Homepage, servicio, contenido fuente, estilos/scripts compartidos y bytes de la imagen original sin cambios.
- Evidencia: `outputs/despegar-hero-producto-20261102/hero-desktop.jpg` y `hero-mobile.jpg` en el workspace. Cambio versionado localmente, sin publicación remota.

## Servicio de software: concisión y diferenciación · 2 de noviembre de 2026

- Recorrido reducido de nueve a seis secciones: apertura, problemas, casos, metodología, contratación y FAQ/contacto. Despegar conserva la presentación destacada del hero y no se repite en Casos; Photonix y ADS comparten una estructura breve de cliente, resultado, solución y enlace.
- Se reemplaza la captura pública deteriorada por `despegar-cotizador-original.png`, completa y ampliable. Se retiran de esta página la segunda captura de Despegar y la foto institucional de Photonix. Fuentes actualizadas en `dist/assets/projects/SOURCES.md`.
- La diferenciación se concentra en “Tu operación define la solución”: evaluar configuración, integración o desarrollo según el proceso y el resultado buscado. Las explicaciones anteriores de elección y entrega se consolidan en diagnóstico, diseño e implementación. El respaldo de Digifianz forma parte del mismo bloque. Cuatro modalidades con entregables explícitos y contratación independiente.
- Textos revisados en el Markdown fuente; los 29 párrafos/elementos vigentes se verificaron en el HTML generado (las etiquetas de modalidades pasan a títulos sin punto final). Las cinco preguntas y sus respuestas coinciden exactamente con la versión anterior y permanecen en HTML, mediante `details` nativos que comparten grupo. H1, título SEO, meta description, canonical y ruta conservados.
- A 1440 × 1000, con las preguntas cerradas, altura total de 6588 a 3528 px; texto visible de `main` de 802 a 502 palabras. Son medidas del recorrido en navegador, no métricas de conversión. El contacto principal está visible en el primer viewport, también en móvil.
- Revisión visual de hero, casos, método, modalidades y FAQ en desktop y de apertura, proceso vertical y respuesta desplegada en 390 × 844. Medición adicional a 360, 768, 800 y 1024 px: ancho del documento igual al viewport, sin elementos que excedan el borde derecho. Captura original cargada a 1633 × 887 px.
- Integración, Photonix y ADS abren el contenido correspondiente en el lector; cierre con Escape comprobado. El enlace de integración conserva sus dos palabras en una línea para evitar una zona de clic fragmentada. FAQ abierta por teclado y por clic: abrir la segunda cierra la primera. CTA de cierre navega a `/es#contacto`. No se enviaron formularios.
- Construcción `npm run build:proposal`, recursos locales, IDs únicos y `git diff --check` comprobados. Sin errores en la consola del recorrido. El CSS nuevo sólo se carga en el servicio; homepage, caso Despegar y estilos/scripts compartidos conservan exactamente sus archivos. `content.json` sólo modifica este servicio.
- Capturas en `outputs/servicio-conciso-20261102/`: `hero-desktop.jpg`, `hero-mobile.jpg`, `metodo-desktop.jpg`, `metodo-mobile.jpg`, `faq-desktop.jpg`, `faq-mobile.jpg`, `desktop-completa.jpg` y `mobile-completa.jpg`. Pruebas con viewports de Chrome, no dispositivos físicos.
- Versionado local, sin push ni despliegue. Contacto y páginas aún mostradas en el lector conservan su alcance provisional. No se modificó la imagen utilizada en la homepage.
