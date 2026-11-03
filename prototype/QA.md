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

## Servicio de software: profundidad recuperada · 2 de noviembre de 2026

Esta revisión sustituye la simplificación de `c7739c4`, tomando la arquitectura y los textos de `bd456b4` como base, a pedido del usuario.

- Recuperados íntegramente los textos de apertura, problemas, los tres proyectos, evaluación de alternativas, costos operativos, alcance, validación, traspaso, modalidades y preguntas frecuentes. Comparación del Markdown con `bd456b4`: sólo difieren la nota de versión y el título “Modalidades de contratación”. Los 28 párrafos/elementos originales están en el HTML; las etiquetas de modalidades se presentan como títulos sin punto final.
- Portfolio único con Despegar, Photonix y ADS Mexicana. Hero con vista general original e identificación breve; “Ver el proyecto” llega al artículo de Despegar dentro del portfolio. El portfolio utiliza otra captura original, la del catálogo, completa y ampliable. Photonix recupera su imagen institucional con leyenda que la distingue del software desarrollado.
- Se elimina la secuencia esquemática de la versión breve. Criterio de solución, alcance y entrega vuelven a ser explicaciones separadas; contratación identifica las entradas independientes y sus entregables. Respaldos, FAQ y contacto conservan su lugar en la arquitectura anterior.
- Ajustes acotados de escala tipográfica y espaciado en el CSS exclusivo del servicio. Se mantiene la apertura con imagen corregida y el acordeón nativo exclusivo. Sin cambio de fuentes, paleta, cifras, marcas ni contenido factual.
- Inspección visual de hero, necesidades, portfolio, criterio, alcance, modalidades y cierre en las capturas completas a 1440 × 1000 y 390 × 844. Imágenes cargadas antes de guardar las capturas y página situada al inicio para evitar artefactos de cabecera fija. Ancho de documento igual al viewport y sin elementos fuera del borde a 360, 390, 768, 800, 1024 y 1440 px.
- Navegación del hero al artículo de Despegar comprobada: artículo a 125 px bajo una cabecera de 96 px. “Ver proyectos reales” comprobado en móvil. Apertura de Photonix por teclado en lector de 358 px dentro del viewport de 390 y cierre con Escape. Las cinco FAQ completas permanecen: abrir la segunda cierra la primera. Sin errores en la consola del recorrido.
- Construcción, whitespace de Git, IDs únicos, un H1 y recursos locales comprobados. H1 y metadatos SEO sin cambios. Homepage, página del caso Despegar y CSS/JS compartidos idénticos. En `content.json` sólo cambia el servicio de software.
- Evidencia en `outputs/servicio-profundidad-20261102/`: `hero-desktop.jpg`, `hero-mobile.jpg`, `portfolio-desktop.jpg`, `portfolio-mobile.jpg`, `criterio-alcance-desktop.jpg`, `desktop-completa.jpg` y `mobile-completa.jpg`. Verificación mediante viewports de navegador; no dispositivos físicos.
- Se conserva todo el historial en una nueva iteración local. Sin push ni despliegue; los destinos de contacto y los casos todavía mostrados en lector mantienen su alcance provisional.

## Mayor presencia del respaldo de Digifianz · 2 de noviembre de 2026

- El respaldo conserva su ubicación antes del contacto y gana título, dos párrafos breves, mayor presencia del logo oficial y enlace institucional. Explica la relación de marcas y cómo la experiencia de Digifianz conecta objetivos comerciales, operación y decisiones técnicas.
- Se incorpora la credencial textual “Elite Partner de HubSpot”, verificada en el directorio oficial de HubSpot el 2 de noviembre de 2026: https://ecosystem.hubspot.com/es/marketplace/solutions/digifianz. Sin cifras, personas ni insignias nuevas.
- Inspección visual en Chrome a 1440 × 1000 y 390 × 844. Franja de 297 px en desktop y 553 px en móvil; título de 36 y 30 px respectivamente. Logo cargado, sin desborde horizontal. Enlace institucional con destino HTTPS, nueva pestaña anunciada y área de 44 px de alto. Viewport temporal restablecido al finalizar.
- Construcción y comparación contra HEAD: el HTML y el Markdown del servicio sólo cambian en el respaldo. Homepage, Despegar y estilos/scripts compartidos idénticos. El ajuste de estilos está en el CSS exclusivo del servicio.
- Capturas en `outputs/servicio-respaldo-digifianz-20261102/`: `respaldo-desktop.jpg` y `respaldo-mobile.jpg`. Verificación mediante viewports de navegador; sin publicación remota.

## Respaldo: reducir repetición de marca · 2 de noviembre de 2026

- Título cambiado a “Experiencia de negocio detrás del software” y enlace visible a “Conocé la empresa”. El nombre accesible conserva ese texto, especifica Digifianz y anuncia la nueva pestaña. El párrafo mantiene explícita la relación entre ambas marcas.
- Revisión en Chrome a 1440 × 1000 y 390 × 844: título en una y dos líneas respectivamente, sin desborde horizontal. La franja conserva su altura desktop de 297 px; no se modificaron estilos ni composición.
- Construcción, `git diff --check` y comparación de HTML completados: sólo cambian el título y las etiquetas del enlace. Capturas en `outputs/servicio-respaldo-editorial-20261102/` del workspace. Iteración local sin push.

## REVIANZ para Digifianz · incorporación del 2 de noviembre de 2026

- Nuevo caso en `/es/casos/revianz-gestion-financiera-proyectos`, con título, descripción, canonical, Open Graph, un H1 y contenido principal en HTML. Conserva el bloqueo de indexación del entorno de revisión.
- Presencia en el inicio y el portfolio de software mediante un reporte de producto a ancho completo. Se incorpora también al índice y al contenido de automatización, que conservan sus lectores provisionales. Desarrollo de software mantiene Despegar, Photonix y ADS Mexicana; el caso Despegar no cambia.
- Fuentes: descripción del usuario, README y funcionalidades implementadas del proyecto local Boom2.0 y página pública de REVIANZ. Cliente identificado como Digifianz y producto como REVIANZ. No se inventan métricas de ahorro, crecimiento, márgenes reales ni una situación previa no documentada.
- Tres capturas originales del centro de ayuda del producto: reporte por proyecto, vista de margen y generación de factura. Archivos intactos, con hashes y procedencia registrados; aproximadamente 208 KB en total. Se evitan las recreaciones de marketing y las pantallas con datos bancarios. Leyendas de demostración, textos alternativos y enlaces de ampliación. El idioma original de las pantallas se conserva.
- Inspección visual del caso completo en desktop y de apertura/producto en 390 × 844. Revisión de los previews del inicio y servicio en 1440 × 1000 y 390 × 844, sin desborde horizontal; medición adicional del caso a 360 y 768 px, también sin desborde. Las tres imágenes cargan con sus dimensiones originales. Se corrigió la separación entre la leyenda de facturación y su enlace de ampliación.
- Navegación al caso comprobada desde inicio, servicio, índice y automatización. Índice muestra los seis casos; ambos lectores llevan a la URL propia de REVIANZ. Ampliación del reporte activada con Enter: nueva pestaña con JPG 1920 × 650 verificada. No se enviaron formularios. Sin errores de consola observados en el recorrido del caso.
- Construcción, `git diff --check`, IDs únicos, un H1 por página, recursos locales y destinos de las rutas comprobados. Comparación con el commit anterior: home sólo suma el preview y cambia “Ver los cinco casos” por “Ver todos los casos”; servicio sólo suma el artículo REVIANZ. HTML de Despegar idéntico. En `content.json` sólo cambian REVIANZ, software, automatización e índice.
- Evidencia en `outputs/caso-revianz-20261102/`: caso completo en desktop/mobile, previews del inicio y servicio en desktop/mobile. Pruebas en viewports de navegador, no dispositivos físicos. Servidor local iniciado en 127.0.0.1:3001 con la nueva ruta; selector de revisión actualizado. No se modificó el proyecto Boom2.0 ni se publicó el sitio.

## REVIANZ: mockups del producto · revisión del 2 de noviembre de 2026

- Se reemplazan las capturas completas de REVIANZ en inicio, servicio y caso por los mockups oficiales de definición de alcance, margen y conciliación de facturas, según la nueva preferencia del usuario. Las capturas anteriores se conservan como archivos históricos, sin referencias en las páginas generadas.
- Los visuales del ejemplo son componentes HTML/SVG. Se portaron a una implementación estática compartida, con Inter, paleta y datos de la fuente original. Traducciones comparadas contra `marketing.mockups` de `messages/es.json`: idénticas. La curva de margen conserva su geometría SVG. Las cifras se identifican como ilustrativas, no como resultados financieros de Digifianz.
- Los mockups se exponen como ilustraciones con nombre accesible; su contenido visual no se anuncia dos veces y sus elementos no son controles falsos. En móvil, el mockup de alcance apila servicios y margen para conservar legibilidad.
- Inspección visual del visual principal en el servicio y de apertura, margen y facturación en el caso a 1440 px; detalle de alcance y caso en 390 × 844. Sin desborde horizontal a 360, 390, 1024 y 1440 px. Navegación de inicio al caso verificada. Las dimensiones del producto son fluidas y no dependen de una captura raster reducida.
- Construcción, `git diff --check`, IDs únicos, un H1 por página y cantidades esperadas de ilustraciones accesibles comprobados (1 en inicio, 1 en software, 3 en el caso). `content.json`, caso Despegar y sus estilos permanecen idénticos. No se modificó Boom2.0.
- Evidencia en `outputs/revianz-mockups-20261102/`: vistas desktop y mobile del caso y detalle, junto al visual del servicio y el inicio. Versionado local; sin publicación remota.

## REVIANZ: imagen en el contexto · 2 de noviembre de 2026

- Se agrega el mockup oficial de compartir un alcance con una empresa socia. Título y ambos párrafos se reúnen a la izquierda; el visual acompaña a la derecha. En móvil, texto e ilustración se apilan. Se conserva el texto completo.
- La traducción de `shareFlow` se copia del proyecto original, con su empresa de ejemplo, estados e iconos. Ilustración con nombre accesible, leyenda y contenido visual oculto al lector de pantalla para evitar duplicación.
- Construcción y comparación contra HEAD: HTML del caso idéntico fuera de la sección de contexto; `content.json`, inicio, servicio y Despegar sin modificaciones. Cuatro mockups accesibles e IDs únicos en el caso. `git diff --check` sin errores.
- Inspección visual a 1440 × 783 y 390 × 844, comprobación adicional a 360 × 800: sin desborde horizontal y sin errores de consola observados. Viewport restablecido. Capturas desktop y móvil en `outputs/revianz-contexto-20261102/` del workspace. Cambio local, sin publicación.

## REVIANZ: enlace al producto · 2 de noviembre de 2026

- Enlace “Visitar revianz.com” agregado al preview del inicio, al proyecto en desarrollo de software y a los datos del producto en el hero del caso. Conserva el enlace interno para leer el caso. Destino HTTPS, apertura en nueva pestaña anunciada en el nombre accesible y `rel="noopener noreferrer"`.
- Construcción y `git diff --check` completados. Verificados los tres enlaces generados. Apertura desde el servicio comprobada en Chrome: carga la página pública de REVIANZ en una pestaña nueva. A 390 px, enlaces con área de 44 px de alto y sin desborde horizontal. Captura en `outputs/revianz-enlace-20261102/enlace-desktop.jpg`.

## REVIANZ: cierre más claro y acceso al producto · 2 de noviembre de 2026

- Se unifican resultados y conclusión en una sola composición: título y síntesis a la izquierda, tres beneficios a la derecha, botón “Conocé REVIANZ” junto a la síntesis. Se elimina la conclusión redundante; el texto del cierre pasa de 140 a 69 palabras, manteniendo margen, facturación y colaboración. La edición también está en el Markdown y el lector de contenido.
- CTA de 16 px y 58 px de alto, con contraste navy/mint. Conserva HTTPS, nueva pestaña, `noopener noreferrer` y nombre accesible que anuncia la apertura. En móvil se presenta después de los beneficios, a ancho completo.
- Inspección visual en Chrome a 1440 × 783 y 390 × 844; comprobación adicional a 1024 × 768. Sin desbordes horizontales ni errores de consola observados. Viewport restablecido al finalizar. Evidencia en `outputs/revianz-cierre-20261102/cierre-desktop.jpg` y `cierre-mobile.jpg` del workspace.
- Construcción, IDs únicos y `git diff --check` correctos. Comparación del HTML contra HEAD: cambios exclusivamente dentro de la sección de resultados; en `content.json` sólo cambia el caso REVIANZ. Inicio, servicio, Despegar, hero del caso y CTA de contacto permanecen idénticos.

## Servicio: equilibrio de necesidades · 2 de noviembre de 2026

- Retoque exclusivo de `.application-lead` y `.application-pair` en el CSS del servicio. Se conserva contenido y estructura: aplicación de ventas destacada en mint y dos aplicaciones complementarias sobre blanco. Los tres subtítulos comparten tamaño, interlínea y saltos equilibrados; cuerpos de 16 px con interlínea de 28 px.
- Retícula de dos columnas iguales con medianil de 64 px e inset de 40 px en desktop. Título principal del bloque alineado arriba y explicación sobre el mismo eje que la segunda columna inferior. En móvil se igualan los insets de lectura; debajo de 640 px las aplicaciones complementarias usan una sola columna.
- Inspección en Chrome a 1440, 768 y 390 px. Desktop: subtítulos de 30 px y 75 px de altura; tablet: títulos inferiores de 28 px y 70 px de altura; móvil: tres subtítulos de 26 px, mismo eje horizontal y ancho de 302 px. Sin desbordes en tablet/móvil. Capturas de sección completa en `outputs/servicio-necesidades-20261102/necesidades-desktop.jpg` y `necesidades-mobile.jpg`. Viewport restablecido.
- Construcción y `git diff --check` correctos. HTML generado, Markdown, contenido JSON y demás estilos permanecen idénticos. Versionado local.

## Servicio: composición conjunta de necesidades · 2 de noviembre de 2026

- Segunda iteración tras el comentario de que el retoque anterior no se percibía. Introducción en dos columnas y superficie mint compartida para las tres aplicaciones, manteniendo la aplicación principal y las dos complementarias. Se conserva la totalidad del texto y el orden. Separación horizontal entre la aplicación principal y el par; en móvil se mantiene una separación equivalente entre cada aplicación.
- Inspección visual a 1440 y 390 px; comprobación adicional a 1024 px, sin desborde. Desktop: sección de 800 px de alto. Prueba visual en `outputs/servicio-necesidades-v2-20261102/necesidades-desktop.jpg`.
- Se encontró que la pestaña existente del navegador integrado aún tenía una versión anterior del servicio (sin REVIANZ ni el respaldo ampliado). Se recargó y comprobó en DOM la nueva agrupación y el caso REVIANZ. Se dejó visible la sección actualizada en la pestaña del usuario. El servidor ya usa `Cache-Control: no-store`; no se cambiaron políticas de caché.
- Construcción y `git diff --check` correctos. Comparación del HTML: fuera de la sección de necesidades no cambia nada; dentro, el texto es idéntico. No cambian el Markdown, `content.json`, las otras páginas ni estilos compartidos.

## Servicio: tres columnas con ejemplos · 2 de noviembre de 2026

- Se adopta la distribución solicitada: tres columnas equivalentes con título, descripción breve y ejemplo. Se elimina el fondo mint, la primera fila destacada y el reparto 1+2. La introducción se reduce a una frase. Las ediciones están también en el Markdown y el lector de contenido.
- Ejemplos concretos de aplicación: cotizador con reglas propias conectado al CRM, panel de proyectos con responsables/costos/facturación y portal de solicitud y seguimiento de servicios. Se presentan como ejemplos, sin atribuir clientes ni resultados nuevos.
- Validación del layout en anchos CSS reales de 1440, 1200, 900, 853 y 390 px. Se ajustó la copia para respetar el máximo de tres líneas incluso a 900 px, el ancho mínimo de la distribución de tres columnas. En la versión final las tres descripciones ocupan dos líneas a 900 y 1440 px. Los ejemplos comienzan en el mismo eje vertical. Sin desbordes horizontales observados; debajo de 900 px se apilan. No hay truncamiento ni contenido oculto.
- Captura final en Chrome a 1440 px, sección de aproximadamente 572 px de alto (antes 800 px). Evidencia: `outputs/servicio-necesidades-columnas-20261102/desktop.png`. Navegador integrado recargado y viewport temporal restablecido.
- Construcción, IDs únicos y `git diff --check` correctos. HTML del servicio idéntico fuera de necesidades; en `content.json` cambia únicamente desarrollo de software. Inicio y casos sin cambios.

## Servicio: recorrido comercial integrado · 2 de noviembre de 2026

- Se implementa la arquitectura aprobada: hero con Despegar como evidencia única, tres necesidades, REVIANZ y Photonix, abordaje integrado, contratación por entregables, Digifianz, FAQ y contacto. El enlace del hero abre directamente el caso Despegar. ADS permanece en el índice completo, accesible desde el servicio.
- Se conservan evaluación de alternativas, costos de operación/mantenimiento, alcance, criterios de mejora, validación con el cliente y documentación/código/configuración según contrato. Las cuatro modalidades se pueden contratar independientemente. Se precisa que la firma de conformidad en Photonix corresponde al cliente; no se agregan métricas nuevas.
- Revisión visual en Chrome a 1440 × 900 y 390 × 844: proyectos, secuencia de cuatro pasos, contratación y cierre legibles. Comprobación adicional a 360, 768 y 1024 px sin desbordes horizontales. Fotografías/logos con carga diferida comprobados al recorrer la página; captura Despegar, mockup REVIANZ y fotografía institucional Photonix conservan su identificación. Sin errores de consola observados. Viewport de Chrome restablecido.
- Se verifican apertura de los lectores Photonix e índice completo, acceso directo del hero al caso Despegar y retorno. FAQ operable con Enter, con una sola pregunta abierta a la vez. Recursos locales, rutas, anchors y lectores validados; IDs únicos y un H1 en el documento inicial. No se enviaron formularios.
- `npm run build:proposal` y `git diff --check` correctos. Comparación con HEAD confirma H1/title/meta/canonical y bloques de necesidades, FAQ, respaldo y contacto íntegros (cambia su orden). En `content.json` sólo cambia software; inicio y casos individuales no cambian.
- Evidencia en `outputs/servicio-narrativa-20261102/`: página desktop completa; proyectos, proceso y cierre en desktop/mobile; hero mobile. Se recargó la pestaña del navegador integrado y se comprobó el nuevo orden y los dos artículos de portfolio. Queda en el inicio del servicio, lista para revisión local. No se publicó el sitio.

## Necesidades: aire y jerarquía · 2 de noviembre de 2026

- Encabezado y bajada sobre un mismo eje, separados de las tres aplicaciones; subtítulos secundarios y ejemplos con fondo gris suave e inset propio. Texto y HTML intactos. Alineación de títulos, descripciones y ejemplos mediante subgrid.
- Inspección visual a 1440 y 390 px; comprobación adicional a 900 y 768 px sin desborde horizontal. En desktop los ejemplos comparten eje superior; en mobile se apilan con separación entre aplicaciones. Evidencia: `outputs/necesidades-aire-20261102/desktop.png` y `mobile.png`.
- Build y diff check correctos; sólo cambian los estilos de necesidades y la documentación. Viewport de Chrome restablecido y pestaña del navegador integrado recargada con los estilos nuevos.

## Portfolio: cabecera del caso REVIANZ · 2 de noviembre de 2026

- Marca y título descriptivo diferenciados; contexto y cambio debajo en dos columnas. Botón principal al caso y enlace secundario al sitio. En móvil, título, explicación, acciones y mockup en ese orden.
- Inspección visual a 1440 y 390 px; revisión a 1024 y 768 px sin desbordes. Viewport restablecido. Evidencia en `outputs/portfolio-apertura-20261102/desktop.png` y `mobile.png`.
- Build y diff check correctos. Comparación HTML confirma cambios exclusivamente dentro del artículo REVIANZ; se conservan párrafos, mockup, URL del caso y enlace externo HTTPS con nueva pestaña y noopener/noreferrer. Contenido JSON y demás páginas intactos.

## Portfolio: apertura con menos carga textual · 2 de noviembre de 2026

- Encabezado reducido a «Nuestro trabajo», sin la bajada genérica. Separación de 64 px respecto del caso (44 px en mobile). El mockup sigue al título; explicación y acciones se leen debajo del producto.
- Inspección visual a 1440 y 390 px, sin desbordes horizontales. Capturas en `outputs/portfolio-ritmo-20261102/desktop.png` y `mobile.png`. Viewport restablecido y pestaña del navegador integrado recargada con el nuevo orden.
- Build y diff check correctos. Comparación automática confirma HTML idéntico fuera del portfolio y conservación exacta de los párrafos y del mockup REVIANZ. En `content.json` sólo cambia el servicio de software.

## Portfolio: contenido antes de la imagen · 2 de noviembre de 2026

- Se reordena únicamente el mockup REVIANZ después de la explicación y sus enlaces. Se conservan textos y estilos.
- Build y diff check correctos. Navegador integrado recargado, orden DOM comprobado y captura visual guardada en `outputs/portfolio-ritmo-20261102/contenido-arriba.png`. Viewport temporal restablecido.


## Abordaje: etapas interactivas · 2 de noviembre de 2026

- Cuatro tarjetas de etapa con un panel visible a la vez. Se conservan íntegros los cuatro títulos y explicaciones originales, y el enlace al servicio de integración. El resto del HTML del servicio permanece idéntico; fuentes Markdown, contenido JSON y otras páginas no cambian.
- Se reutiliza el controlador de pestañas existente, con una inicialización progresiva exclusiva de este componente. Sin JS, los cuatro detalles están renderizados y visibles; con JS se muestra la primera etapa. Roles, relaciones tab/panel, selección y tabindex sincronizados.
- Verificados clic, navegación con flechas, Home/End y Tab al panel con foco visible. Apertura y cierre del lector de integración correctos. Sin errores de consola observados.
- Revisión visual a 1440 y 390 px en Chrome; comprobación adicional a 900 px sin desbordes. Capturas en `outputs/proceso-interactivo-20261102/desktop.png` y `mobile.png`. Viewports temporales restablecidos y pestaña de pruebas cerrada. Navegador integrado recargado y dejado en `#como-abordamos`.
- Build, sintaxis JS y diff check correctos. Comprobación automática de IDs únicos, conservación exacta de textos y ausencia de cambios fuera de la sección. Transiciones de color desactivadas con preferencia de movimiento reducido.


## Unificación de abordaje y contratación · 2 de noviembre de 2026

- Una sola sección «Cómo podés trabajar con nosotros», con Auditoría, Diseño, Implementación y Soporte contratables por separado. Cada opción integra criterio de trabajo y entregable. Implementación reúne validación, puesta en uso y transferencia; soporte mantiene capacidad mensual para incidentes, mantenimiento y ajustes menores.
- Título de panel a todo el ancho, explicación a la izquierda y entregable destacado a la derecha. Se elimina altura mínima y numeración secuencial. En mobile se apilan explicación y entregable; etiquetas ajustadas para caber a 360 px.
- Verificados selección de las cuatro modalidades y navegación por teclado. Revisión visual a 1440 y 390 px; medidas a 360 y 900 px sin desbordes y nombres de tarjetas dentro del espacio disponible. Sin errores de consola observados. Capturas finales en `outputs/modalidades-unificadas-20261102/desktop.png` y `mobile.png`.
- Build y diff check correctos. Comprobación automática: HTML idéntico fuera de las dos secciones unificadas, cuatro paneles y entregables, IDs únicos; sólo cambia software en `content.json`. Se actualizó el Markdown fuente para mantener consistente el lector de contenido. JS sin cambios.
- Navegador integrado recargado en la sección unificada; viewport de pruebas restablecido y pestaña temporal de Chrome cerrada. El respaldo de Digifianz sigue inmediatamente después del bloque unificado.


## FAQ: jerarquía y lectura · 2 de noviembre de 2026

- Encabezado sobre una columna centrada de hasta 1040 px; preguntas de 18 px, respuesta de 16 px y controles más/menos de 32 px. Pregunta abierta sobre mint, primera respuesta visible por defecto. Las cinco preguntas y respuestas se conservan exactamente.
- Verificados Enter para abrir, cierre de la respuesta anterior por el atributo name, Espacio para cerrar y clic para reabrir. Foco de teclado visible. Acordeón nativo sin dependencia de JS.
- Revisión visual a 1440 y 390 px; comprobación adicional a 360 px sin desbordes. Evidencia en `outputs/faq-editorial-20261102/desktop.png` y `mobile.png`. Viewport restablecido y pestaña temporal cerrada. Navegador integrado recargado y dejado en `#preguntas-frecuentes`.
- Build y diff check correctos. Comparación automática confirma HTML idéntico fuera de FAQ y texto completo sin cambios. Markdown, contenido JSON, otras páginas y JS intactos.


## CTA final: invitación y contacto directo · 2 de noviembre de 2026

- Franja navy con título enfocado en negocio, contexto del próximo paso y tranquilidad para quienes aún no definieron el proyecto. Una sola acción «Contanos qué necesitás» lleva directamente al formulario existente `/es#consulta`.
- Se comprobó el recorrido por clic: URL correcta, formulario presente y comienzo de la sección visible en mobile (aproximadamente 84 px desde el borde superior). No se completó ni envió el formulario. Sigue siendo un prototipo sin recepción conectada.
- Inspección visual a 1440 y 390 px; comprobación a 360 px sin desbordes. Botón de unos 58 px de alto, foco blanco visible mediante Tab desde la última FAQ. Capturas en `outputs/cta-final-20261102/desktop.png` y `mobile.png`. Viewport restablecido y pestaña temporal cerrada.
- Build y diff check correctos. Comparación automática confirma HTML idéntico fuera del CTA final y un único enlace al formulario. Sólo cambia software en el contenido JSON; otras páginas y JS intactos. Navegador integrado recargado y dejado en `#conversemos`.

## Inicio con narrativa propia · 2 de noviembre de 2026

- Build `npm run build:proposal`: inicio y cinco páginas nativas, sin errores.
- Verificación de las seis páginas: un H1 por página, IDs únicos, assets locales existentes, destinos internos y contenidos del lector válidos.
- Desktop 1280 px: hero de marca, tres servicios visibles, tres casos con el texto antes de la imagen, criterio y respaldo de Digifianz, contacto. La página de software mantiene sus estilos y contenido; sus enlaces relacionados ahora apuntan a las dos nuevas páginas nativas.
- Responsive: sin desborde horizontal a 320, 390, 468, 768 y 1280 px. Se corrigió la altura del mockup de REVIANZ a 320 px para evitar cortar su contenido.
- Mobile 390 px: menú abre y se cierra al navegar; índice accesible con los seis casos; agenda de prueba abre y su alternativa lleva al formulario y enfoca Nombre.
- Formulario probado con datos ficticios. La confirmación informa que no se envió ni guardó información, como corresponde a esta propuesta local.
- Integración y automatización: rutas nativas verificadas en desktop y mobile, cinco preguntas en cada una y acordeones funcionales.
- Se sustituyó la captura pública antigua de Despegar en el inicio por `despegar-cotizador-original.png`. Logos originales y mockup de REVIANZ conservados; las imágenes de contexto y las cifras ilustrativas están identificadas.
- Verificaciones `node --check` de app.js y serve.mjs, y `git diff --check`: correctas.
- Evidencia de revisión: `/Users/sheinken/Desktop/Cloudfianz/outputs/homepage-narrativa-20261102/` (fuera del repositorio).
- Formulario, agenda, privacidad y analítica siguen pendientes de conexión para publicación; esta iteración no publica ni envía consultas.

## Ajuste editorial del inicio · 2 de noviembre de 2026

- Build y verificación de IDs, H1, imágenes, estilos y anchors: correctos.
- Tres relatos destacados: Despegar, REVIANZ y ConsorcioAbierto. Recuperan la presentación amplia anterior; no se restauran las capturas públicas alteradas de Despegar.
- Se retira el bloque de ejemplos de Photonix y ADS Mexicana. Sus casos siguen disponibles en el índice.
- Hero con InvoiceMatchFlowMockup de REVIANZ, datos ilustrativos identificados. Caso REVIANZ con ScopeDefinitionMockup y enlace al sitio del producto.
- Digifianz en sección independiente de ancho completo, logo original y mayor jerarquía.
- Revisado visualmente en 1280 y 390 px; sin desbordes a 320, 390, 768 y 1280 px.
- Cambios acotados a la homepage, su CSS y la inserción de su mockup en el build; no hay cambios generados en páginas internas.
- Capturas: `/Users/sheinken/Desktop/Cloudfianz/outputs/homepage-editorial-20261102/`.

### Hero con ConsorcioAbierto

Se reemplazó el mockup de REVIANZ del hero por la imagen oficial de contexto del cliente y su logo original. Encuadre CSS verificado visualmente en 1280 y 390 px, sin desbordes también en 320 px. Build y diff sin errores. El resto de las secciones y páginas conserva su implementación.

### Hero con mockup conceptual · 2 de noviembre de 2026

- Imagen generada con la herramienta integrada a pedido del usuario: cotización, operación y resultados. Prompt y procedencia en `dist/assets/hero/`; original PNG preservado en outputs.
- JPEG de 1254 × 1254 px, 203 KB, con dimensiones explícitas, carga prioritaria y texto alternativo que identifica el carácter conceptual.
- Build correcto. Inspección visual a 1280 y 390 px; imagen cargada y sin desbordes también a 320 px. Viewport restablecido al terminar.
- Comparación con HEAD confirma contenido idéntico fuera de la figura del hero. Sin cambios en páginas interiores.
- Capturas desktop y mobile: `/Users/sheinken/Desktop/Cloudfianz/outputs/hero-mockup-20261102/`.

## Hero ambiental con equipo joven · 2 de noviembre de 2026

- Se reemplaza el mockup de producto por una imagen ambiental a todo el ancho, con difuminado blanco hacia el titular y la paleta de Cloudfianz. El texto y los CTA aprobados se mantienen.
- Escena generada de cuatro personas ficticias diferenciadas. La revisión final corrige el botón superior duplicado de la camisa, a pedido del usuario. Procedencia y prompts en `dist/assets/hero/`.
- Build y `git diff --check` correctos. Comparación confirma que todo el HTML posterior al hero sigue idéntico.
- Desktop 1280 px, mobile 390 y 320 px revisados. Imagen cargada, sin desbordes horizontales. En mobile, transición vertical y encuadre derecho con altura proporcional para conservar los rostros dentro de la imagen.
- Capturas finales y PNG original en `/Users/sheinken/Desktop/Cloudfianz/outputs/hero-equipo-20261102/`.
- Exploración del mockup Despegar guardada previamente en el commit local `21bdf6c`. No hubo publicación ni cambios remotos.

## Galería y marca REVIANZ en el inicio · 2 de noviembre de 2026

- Se reemplaza el mockup único por tres vistas existentes: alcance y servicios, rentabilidad y facturación. La variante compacta de alcance tiene una descripción accesible acorde con su contenido.
- Marca oficial `BrandMark` portada desde Boom2.0, con proporciones y colores preservados; procedencia documentada en el registro de marcas.
- Desktop 1280 px: tres paneles de 364 × 360 px, alineados. Tablet 1024 px: carril de 928 px con contenido desplazable de 1282 px. Mobile 390 px: paneles de 308 px, con vista siguiente parcialmente visible.
- Se comprobó el desplazamiento horizontal por los tres paneles hasta el último. Sin desborde de página ni contenido interno cortado a 320 y 390 px.
- Build correcto, tres figuras en la galería, IDs únicos. Estilos de la galería acotados al inicio; las páginas internas generadas no cambian.
- Capturas en `/Users/sheinken/Desktop/Cloudfianz/outputs/revianz-home-gallery-20261102/`.


## Sistema editorial del portfolio de Home · 2 de noviembre de 2026

- Despegar, REVIANZ y ConsorcioAbierto comparten artículos blancos, cabecera de marca y categoría, título/CTA y relato/resultado, con el producto debajo sobre un fondo neutro. Las identidades originales permanecen dentro de logos e interfaces.
- Se conserva la captura original completa de Despegar, sin perspectiva ni recorte. ConsorcioAbierto utiliza la imagen de contexto existente, sin el banner navy, frase promocional o logo duplicado. REVIANZ conserva su marca oficial y las tres vistas con sus datos ilustrativos identificados.
- Desktop 1280 px: artículos de 1136 px, imágenes con un marco común de aproximadamente 420 px de alto y galería de tres vistas de 330 px. Contenido completo arriba de las imágenes.
- Responsive revisado a 1024, 390 y 320 px: sin desborde horizontal de página. Galería REVIANZ con desplazamiento nativo, dos vistas y una parte de la tercera en tablet, primera vista y adelanto de la siguiente en mobile. A 320 px los paneles tienen 230 px; se ajustó el porcentaje para evitar un desborde de 2 px. No hay contenido interno cortado y se comprobó el recorrido hasta facturación.
- El enlace de ConsorcioAbierto abre el caso correcto en el lector existente. Las rutas de Despegar y REVIANZ, los assets, IDs únicos y H1 se verificaron en el HTML generado.
- Build y `git diff --check` correctos. Comparación confirma que todo el HTML fuera de los artículos del portfolio es idéntico al anterior; sin cambios en las páginas internas ni estilos compartidos.
- Capturas desktop y mobile en `/Users/sheinken/Desktop/Cloudfianz/outputs/portfolio-system-20261102/`. Cambios guardados sólo en el historial local.


## Portfolio compacto en Home · 3 de noviembre de 2026

- Cada caso se resume en titular, un único párrafo y acceso al detalle. Se retira la repetición de «Qué cambió» y se conservan logos, imágenes, enlaces y las tres vistas REVIANZ. Los textos completos de las páginas de casos no cambian.
- Desktop 1280 px: Despegar pasa de 833 a 628 px, REVIANZ de 831 a 650 px y ConsorcioAbierto de 818 a 627 px. La sección completa mide aproximadamente 2363 px.
- Capturas con altura máxima de 276 px dentro de un marco de 320 px. REVIANZ conserva altura natural, con menos padding y separaciones; no se recortan los mockups ni se reduce su tipografía de lectura.
- Revisión visual a 1280 y 390 px; comprobaciones a 320 y 1024 px sin desbordes de página ni de los elementos internos de los mockups. Desplazamiento horizontal hasta la tercera vista verificado a 320 px.
- Build y diff check correctos, un H1, IDs únicos y assets existentes. HTML fuera de los casos idéntico al anterior; sin cambios en páginas internas. Viewport restablecido.
- Evidencia en `/Users/sheinken/Desktop/Cloudfianz/outputs/portfolio-compact-20261103/desktop.jpg` y `mobile.jpg`.


## Ritmo y jerarquía de la Home · 3 de noviembre de 2026

- Arquitectura final: Hero, respaldo breve de Digifianz, soluciones, casos, metodología y contacto. Se retiran la franja repetida de logos y el bloque institucional extenso del cierre.
- Un resultado, un párrafo, un enlace y una sola imagen por caso. REVIANZ conserva el mockup de margen con su nota de datos ilustrativos. CTA contextual después del segundo caso; acceso único al índice al terminar.
- A 1280 px CSS: página de 4696 px y sección de casos de 1755 px, incluido el nuevo CTA. Artículos de aproximadamente 393, 410 y 359 px. Se conservan proporciones y contenido completo de las imágenes.
- Revisión visual en escritorio y móvil. Sin desbordes de página ni internos a 320, 360, 390, 1024 y 1280 px. Se corrigió el encabezado del mockup a 320 px mediante tipografía adaptable y flex-wrap. Las medidas CSS se verificaron en el navegador; el zoom del navegador requiere compensación en las capturas.
- CTA intermedio comprobado hacia contacto. Menú móvil abre y se cierra al navegar. ConsorcioAbierto abre el lector correcto y permite cerrarlo. Los tres CTA de servicios tienen rutas nativas válidas y una altura mínima de 48 px.
- Build correcto y diff sin errores. Revisión estática independiente: IDs únicos, un H1, un solo mockup REVIANZ, assets existentes, enlaces nativos y lectores válidos. Las cinco páginas internas no tienen cambios y no cargan los estilos de Home.
- Formulario y agenda mantienen su comportamiento de demostración local. Sin publicación.
- Capturas en `/Users/sheinken/Desktop/Cloudfianz/outputs/home-rhythm-20261103/`.
