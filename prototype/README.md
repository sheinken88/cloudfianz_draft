# Propuesta local del sitio · Cloudfianz

Prototipo local de Cloudfianz. La Home presenta la empresa; Desarrollo a medida, Integraciones y Automatizaciones tienen páginas independientes con una arquitectura compartida y contenido específico. La revisión del 3 de noviembre de 2026 organiza cada servicio alrededor de aplicaciones concretas, casos reales y una única metodología. La página de Casos de éxito reúne seis proyectos, todos con página individual: Despegar, REVIANZ, ConsorcioAbierto, Photonix, Escala24x7 y ADS Mexicana.

## Ver la propuesta

Desde la raíz del repositorio: `npm run dev:proposal`.

- [Revisión con selector de página y de escritorio/móvil](http://127.0.0.1:3001/review.html).
- [Homepage](http://127.0.0.1:3001/es).
- [Desarrollo de software a medida](http://127.0.0.1:3001/es/desarrollo-software-a-medida).
- [Integración de sistemas](http://127.0.0.1:3001/es/integracion-de-sistemas).
- [Automatización de procesos](http://127.0.0.1:3001/es/automatizacion-de-procesos).
- [Casos de éxito](http://127.0.0.1:3001/es/casos).
- [Caso ConsorcioAbierto](http://127.0.0.1:3001/es/casos/consorcioabierto-facturacion-hubspot-odoo).
- [Caso Despegar](http://127.0.0.1:3001/es/casos/despegar-cotizador-hubspot).
- [Caso REVIANZ](http://127.0.0.1:3001/es/casos/revianz-gestion-financiera-proyectos).

El selector permite revisar las once páginas a distintos anchos. El servidor queda limitado a `127.0.0.1:3001`; esta entrega es una vista local para revisión, no un despliegue. Después de editar las fuentes, ejecutar `npm run build:proposal` y recargar el navegador. El servidor no incorpora recarga automática. Si se cambia el mapa de rutas, reiniciar el servidor.

## Dirección visual

La [dirección visual v2](DIRECCION-VISUAL-V2.md) define azul profundo `#0B1D3A`, verde `#12B5A5`, blanco `#FFFFFF`, gris `#F5F7FA` y tinta `#0E1726`. El naranja `#FF7A2F` queda reservado para un uso justificado. Manrope es la familia de titulares e Inter la de lectura.

El enlace «Casos» de la cabecera y del pie navega al índice `/es/casos`. Los CTA de proyectos de la Home y los servicios abren páginas completas, incluido el enlace a ConsorcioAbierto de la sección AWS.

La cabecera compartida incluye un desplegable «Soluciones» con enlaces directos a Software a medida, Integraciones y Automatizaciones. En móvil se despliega dentro del menú principal; admite teclado, cierre con Escape, clic exterior y salida del foco.

La Home revisada el 3 de noviembre de 2026 sigue el recorrido Hero → Clientes → Soluciones → Casos → Metodología → Infraestructura AWS → Digifianz → Contacto. El hero mantiene la imagen ambiental y presenta «Software a medida para mejorar cómo funciona tu negocio». Debajo, una fila con movimiento continuo reúne los logos originales de Despegar, ConsorcioAbierto, Photonix, Escala24x7, ADS Mexicana y Digifianz, sin texto lateral. Digifianz usa su variante coral original sobre blanco. El carril no tiene botón de pausa visible; conserva pausa al pasar el puntero, navegación por teclado y una alternativa estática para movimiento reducido. Las tres soluciones tienen CTA propios. «Casos de éxito» presenta una selección de proyectos, con el subtítulo debajo del título. Reúne Despegar, REVIANZ y ConsorcioAbierto en resúmenes compactos; sus enlaces «Conocé el caso» adoptan el botón verde claro del sistema, con borde suave y esquinas redondeadas. El banner de contacto cierra esa sección después del enlace al índice. La metodología usa el selector de modalidades de Desarrollo a Medida en una versión breve para la Home: auditoría, diseño, implementación y soporte, con un panel activo que resume actividad y entregable. Sin JavaScript se muestran todos los paneles. La sección de infraestructura AWS incorpora la marca original y cuatro iconos oficiales en color: API Gateway, Lambda, EventBridge y S3. Una superficie blanca reúne los servicios con beneficios concretos —conectar, automatizar, responder a eventos y almacenar—; el texto introductorio resume el valor de los servicios administrados y enlaza al caso ConsorcioAbierto. La sección institucional de Digifianz vuelve a explicar la pertenencia de Cloudfianz antes del contacto. La [dirección vigente del inicio](DIRECCION-INICIO-V3.md) registra esta edición y sus antecedentes.

El título de Desarrollo es «Construimos herramientas cuando el software existente no alcanza». Integraciones propone «Conectá tus sistemas y dejá de cargar la misma información dos veces»; Automatizaciones, «Automatizá las tareas que se repiten todos los días». Las tres páginas siguen Hero → Problemas y soluciones → Casos reales → Cómo trabajamos → FAQ → CTA. Los tres Hero incluyen recursos de proyectos: Desarrollo muestra la captura real ampliable de Despegar; Integraciones, el esquema HubSpot ↔ AWS Partner Central de Escala24x7; Automatizaciones, el flujo de facturación HubSpot → reglas de contrato → Odoo de ConsorcioAbierto. Comparten superficie mint, identidad del cliente y orden de lectura responsive. Los CTA de los casos comparten `.case-button` con la Home: fondo mint `#E8F4F0`, texto verde oscuro, borde discreto, radio de 8 px y foco visible.

La referencia BairesDev se usa para trabajar escala, ritmo y peso de la evidencia. Los recursos visuales son de Cloudfianz, Digifianz, AWS y los clientes; no se copian recursos de esa referencia. La homepage abandona los logos recompuestos, diagramas simulados y flechas decorativas de la v1.

La implementación adapta columnas, navegación y selectores a móvil. La validación visual y de interacción de esta versión se registra por separado en [QA.md](QA.md).

## Contenido y recursos originales

La versión anterior aprobada se conserva en `outputs/homepage-20261022/` del workspace. Los textos vigentes están en `prototype/content/`: incluyen los cinco casos adaptados de los borradores del usuario del 29 de octubre de 2026 y REVIANZ (desarrollado para Digifianz), su índice y los servicios con ejemplos actualizados. Las notas editoriales de implementación quedan fuera de las páginas y del lector.

## Editar y generar

- `templates/home.html`: fuente de la homepage y de la cabecera, pie y diálogos compartidos. No editar directamente el `dist/index.html` generado.
- `content/*.md`: textos vigentes de servicios y casos, incluidos sus títulos y descripciones SEO.
- `build-pages.py`: generación de la homepage y las páginas independientes. Ejecuta primero `build-content.py` para regenerar el lector.
- `page_layouts/service.py`: composición común de los tres servicios, alimentada por sus textos vigentes. `page_layouts/service_cases.py` reúne las identidades y recursos visuales de sus casos; `page_layouts/service_heroes.py` contiene las tres composiciones visuales del Hero.
- `page_layouts/cases.py` y `page_layouts/case_previews.py`: índice de seis casos y sus recursos visuales compactos.
- `page_layouts/case.py`, `page_layouts/revianz.py`, `page_layouts/properix.py` y `page_layouts/project.py`: composiciones de las seis páginas individuales de casos. Cada una conserva su contenido aprobado y distingue las capturas de los esquemas e imágenes de contexto.
- `page-routes.json`: mapa de servicios, índice y casos con página propia. Todos sus enlaces se generan como URLs normales; no requieren el lector provisional.
- `dist/home-page.css` y `dist/home-page.js`: presentación de Home y carril de clientes; los estilos y el movimiento quedan aislados de las páginas internas.
- `dist/styles.css` y `dist/app.js`: base visual e interacciones compartidas. `dist/pages.css` define el sistema de las páginas internas; `dist/service-page.css` se comparte entre los tres servicios y `dist/case-page.css` agrega la composición específica de Despegar.
- `dist/review.html` y `dist/review.js`: interfaz local de revisión.
- `serve.mjs`: servidor local sin dependencias adicionales, con rutas explícitas, redirecciones a URLs sin barra final y respuestas 404 reales. No es infraestructura de producción.

`npm run build:proposal` regenera todos los HTML y `content.json`. `npm run dev:proposal` construye y arranca el servidor. El contenido principal de las páginas está incluido en el HTML: no depende de abrir un modal ni de JavaScript para leerse. Los metadatos canonical y Open Graph apuntan al destino propuesto de producción; el prototipo continúa bloqueado para indexación.

La composición vigente se documenta en [DIRECCION-PAGINAS-V2.md](DIRECCION-PAGINAS-V2.md). La [primera dirección](DIRECCION-PAGINAS.md) se conserva como antecedente. Cada servicio presenta tres aplicaciones con ejemplos y dos casos contenidos en artículos neutrales: Desarrollo reúne Despegar y REVIANZ; Integraciones, ConsorcioAbierto y Escala24x7; Automatizaciones, ConsorcioAbierto y Despegar. Los mismos proyectos muestran capacidades distintas según el servicio. Una única sección de metodología combina cuatro pestañas y entregables específicos; las preguntas frecuentes y el cierre también corresponden a cada capacidad. La pertenencia a Digifianz permanece en la Home y el pie compartido. Escala24x7 conserva los logos oficiales de HubSpot y AWS con sonrisa naranja en su esquema de sincronización.

- [Fuentes de marca e imágenes de contexto](dist/assets/brand/SOURCES.md): logo Cloudfianz recuperado del archivo usado en las presentaciones, logos oficiales de clientes y Digifianz, dimensiones, procedencia y hashes. Los archivos se conservan intactos.
- [Fuentes de capturas de producto](dist/assets/projects/SOURCES.md): originales de Despegar y antecedentes visuales de REVIANZ con procedencia y hashes. El documento distingue los originales de las imágenes públicas anteriores de Despegar.

Las captions distinguen el trabajo mostrado: Despegar es una captura del proyecto; la interfaz de Properix ilustra la plataforma del cliente y no la integración desarrollada por Cloudfianz; la imagen Photonix presenta equipamiento de radioterapia como contexto de su actividad. No se incorporan nombres ni fotos de personas del equipo.

## Alcance y límites de la revisión

La entrega incluye once páginas: Home, tres servicios, índice de casos y seis casos individuales. No sustituye la web actual en `src/`. Los contenidos de casos y servicios se leen en sus URLs propias; ningún enlace público abre el lector provisional.

La agenda y el envío del formulario son simulaciones identificadas como tales. El formulario valida los campos y muestra una confirmación de prueba, sin enviar ni guardar los datos ingresados. No hay recepción comercial, reserva de reuniones ni medición conectadas. La política de privacidad permanece como aviso provisional.

El prototipo tiene `noindex, nofollow`. La recepción de consultas, la agenda, la política definitiva, la analítica, el SEO técnico de lanzamiento y el despliegue quedan para la etapa posterior a la revisión del diseño.

La [dirección del caso REVIANZ](DIRECCION-CASO-REVIANZ.md) documenta la nueva composición y sus fuentes. `dist/revianz-page.css` sólo se carga en esa página; el preview de inicio usa los estilos compartidos del mockup.

Revisión de REVIANZ: el sitio usa los mockups ilustrativos del producto, portados desde sus componentes oficiales. La Home conserva el preview de rentabilidad, Desarrollo el de alcance y el índice una versión compacta de alcance; las vistas completas permanecen en el caso. `page_layouts/revianz_mockups.py`, `data/revianz-mockups-es.json` y `dist/revianz-mockups.css` mantienen una única implementación compartida. Las capturas anteriores ya no se muestran.
