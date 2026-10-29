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
