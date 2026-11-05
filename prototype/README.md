# Propuesta local del sitio · Cloudfianz

Prototipo local de Cloudfianz. La Home presenta la empresa; Desarrollo a medida, Integraciones y Automatizaciones tienen páginas independientes con una arquitectura compartida y contenido específico. La revisión del 3 de noviembre de 2026 organiza cada servicio alrededor de aplicaciones concretas, casos reales y una única metodología. La página de Casos de éxito reúne seis proyectos, todos con página individual: Despegar, REVIANZ, ConsorcioAbierto, Photonix, Escala24x7 y ADS Mexicana. Cómo trabajamos y Contacto completan el recorrido con páginas propias.

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
- [Cómo trabajamos](http://127.0.0.1:3001/es/como-trabajamos).
- [Contacto](http://127.0.0.1:3001/es/contacto).

El selector permite revisar las trece páginas a distintos anchos. El servidor queda limitado a `127.0.0.1:3001`; esta entrega es una vista local para revisión, no un despliegue. Después de editar las fuentes, ejecutar `npm run build:proposal` y recargar el navegador. El servidor no incorpora recarga automática. Si se cambia el mapa de rutas, reiniciar el servidor.

## Dirección visual

La [dirección visual v2](DIRECCION-VISUAL-V2.md) define azul profundo `#0B1D3A`, verde `#12B5A5`, blanco `#FFFFFF`, gris `#F5F7FA` y tinta `#0E1726`. El naranja `#FF7A2F` queda reservado para un uso justificado. Manrope es la familia de titulares e Inter la de lectura.

El enlace «Casos» de la cabecera y del pie navega al índice `/es/casos`. Los CTA de proyectos de la Home y los servicios abren páginas completas, incluido el enlace a ConsorcioAbierto de la sección AWS. «Cómo trabajamos» lleva a `/es/como-trabajamos`; la navegación de contacto y los CTA de consulta llevan a `/es/contacto`. La Home conserva su formulario y los destinos anteriores `/es#contacto`, `/es#consulta` y `/es#como-trabajamos` siguen disponibles.

La cabecera compartida incluye un desplegable «Soluciones» con enlaces directos a Software a medida, Integraciones y Automatizaciones. En móvil se despliega dentro del menú principal; admite teclado, cierre con Escape, clic exterior y salida del foco.

La Home revisada el 3 de noviembre de 2026 sigue el recorrido Hero → Clientes → Soluciones → Casos → Metodología → Infraestructura AWS → Digifianz → Contacto. El hero mantiene la imagen ambiental y presenta «Software a medida para vender mejor y operar con más control». Debajo, una fila con movimiento continuo reúne los logos originales de Despegar, ConsorcioAbierto, Photonix, Escala24x7, ADS Mexicana y Digifianz, sin texto lateral. Digifianz usa su variante coral original sobre blanco. El carril no tiene botón de pausa visible; conserva pausa al pasar el puntero, navegación por teclado y una alternativa estática para movimiento reducido. Las tres soluciones tienen CTA propios. «Casos de éxito» presenta una selección de proyectos, con el subtítulo debajo del título. Reúne Despegar, REVIANZ y ConsorcioAbierto en resúmenes compactos; sus enlaces «Conocé el caso» adoptan el botón verde claro del sistema, con borde suave y esquinas redondeadas. El banner de contacto cierra esa sección después del enlace al índice. La metodología usa el selector de modalidades de Desarrollo a Medida en una versión breve para la Home: auditoría, diseño, implementación y soporte, con un panel activo que resume actividad y entregable. Sin JavaScript se muestran todos los paneles. La sección de infraestructura AWS, actualizada el 5 de noviembre de 2026 con el texto aportado por el usuario, abre con «Tu solución, sobre la misma infraestructura que usan las empresas más grandes del mundo». Conserva la marca original y una superficie blanca con cuatro beneficios: seguridad de nivel enterprise, alta disponibilidad, capacidad ajustable y costo proporcional al uso. Los acompañan los iconos oficiales en color de AWS Shield, Elastic Load Balancing, AWS Auto Scaling y AWS Cost Explorer. El texto introductorio menciona Netflix, Airbnb, NASA, ISO 27001, SOC 2 y GDPR; el enlace al caso ConsorcioAbierto se conserva. La sección institucional de Digifianz vuelve a explicar la pertenencia de Cloudfianz antes del contacto. La [dirección vigente del inicio](DIRECCION-INICIO-V3.md) registra esta edición y sus antecedentes.

El título de Desarrollo es «Construimos herramientas cuando el software existente no alcanza». Integraciones propone «Conectá tus sistemas y dejá de cargar la misma información dos veces»; Automatizaciones, «Automatizá las tareas que se repiten todos los días». Las tres páginas siguen Hero → Problemas y soluciones → Casos reales → Cómo trabajamos → FAQ → CTA. Los tres Hero incluyen recursos de proyectos: Desarrollo muestra la vista adaptada del cotizador de Despegar; Integraciones, el esquema HubSpot ↔ AWS Partner Central de Escala24x7; Automatizaciones, el flujo de facturación HubSpot → reglas de contrato → Odoo de ConsorcioAbierto. Comparten superficie mint, identidad del cliente y orden de lectura responsive. Los CTA de los casos comparten `.case-button` con la Home: fondo mint `#E8F4F0`, texto verde oscuro, borde discreto, radio de 8 px y foco visible.

La referencia BairesDev se usa para trabajar escala, ritmo y peso de la evidencia. Los recursos visuales son de Cloudfianz, Digifianz, AWS y los clientes; no se copian recursos de esa referencia. La homepage abandona los logos recompuestos, diagramas simulados y flechas decorativas de la v1.

La implementación adapta columnas, navegación y selectores a móvil. La validación visual y de interacción de esta versión se registra por separado en [QA.md](QA.md).

## Contenido y recursos originales

La versión anterior aprobada se conserva en `outputs/homepage-20261022/` del workspace. Los textos vigentes están en `prototype/content/`: incluyen los cinco casos adaptados de los borradores del usuario del 29 de octubre de 2026 y REVIANZ (desarrollado para Digifianz), su índice, los servicios con ejemplos actualizados y las páginas de Contacto y Cómo trabajamos. Las notas editoriales de implementación quedan fuera de las páginas y del lector.

## Editar y generar

- `templates/home.html`: fuente de la homepage y de la cabecera y diálogos compartidos. No editar directamente el `dist/index.html` generado.
- `templates/footer.html`: fuente única del pie compartido. `build-pages.py` lo inserta en Home y en todas las páginas internas; `dist/footer.css` contiene sus estilos comunes.
- `content/*.md`: textos vigentes de servicios, casos, índice y páginas generales, incluidos sus títulos y descripciones SEO. `pagina-contacto.md` y `pagina-como-trabajamos.md` alimentan las dos páginas nuevas.
- `build-pages.py`: generación de la homepage y las páginas independientes. Ejecuta primero `build-content.py` para regenerar el lector.
- `page_layouts/service.py`: composición común de los tres servicios, alimentada por sus textos vigentes. `page_layouts/service_cases.py` reúne las identidades y recursos visuales de sus casos; `page_layouts/service_heroes.py` contiene las tres composiciones visuales del Hero.
- `page_layouts/cases.py` y `page_layouts/case_previews.py`: índice de seis casos y sus recursos visuales compactos.
- `page_layouts/case.py`, `page_layouts/revianz.py`, `page_layouts/properix.py` y `page_layouts/project.py`: composiciones de las seis páginas individuales de casos. Cada una conserva su contenido aprobado y distingue las capturas de los esquemas e imágenes de contexto.
- `page_layouts/contact.py` y `page_layouts/method.py`: páginas de Contacto y Cómo trabajamos. Sus estilos específicos están en `dist/contact-page.css` y `dist/method-page.css`.
- `page-routes.json`: mapa de servicios, índice, casos, Contacto y Cómo trabajamos. Todos sus enlaces se generan como URLs normales; no requieren el lector provisional.
- `dist/home-page.css` y `dist/home-page.js`: presentación de Home y carril de clientes; los estilos y el movimiento quedan aislados de las páginas internas.
- `dist/styles.css` y `dist/app.js`: base visual e interacciones compartidas. `dist/pages.css` define el sistema de las páginas internas; `dist/service-page.css` se comparte entre los tres servicios y `dist/case-page.css` agrega la composición específica de Despegar.
- `dist/review.html` y `dist/review.js`: interfaz local de revisión.
- `serve.mjs`: servidor local sin dependencias adicionales, con rutas explícitas, redirecciones a URLs sin barra final y respuestas 404 reales. No es infraestructura de producción.

`npm run build:proposal` regenera todos los HTML y `content.json`. `npm run dev:proposal` construye y arranca el servidor. El contenido principal de las páginas está incluido en el HTML: no depende de abrir un modal ni de JavaScript para leerse. Los metadatos canonical y Open Graph apuntan al destino propuesto de producción; el prototipo continúa bloqueado para indexación.

La composición vigente se documenta en [DIRECCION-PAGINAS-V2.md](DIRECCION-PAGINAS-V2.md). La [primera dirección](DIRECCION-PAGINAS.md) se conserva como antecedente. Cada servicio presenta tres aplicaciones con ejemplos y dos casos contenidos en artículos neutrales: Desarrollo reúne Despegar y REVIANZ; Integraciones, ConsorcioAbierto y Escala24x7; Automatizaciones, ConsorcioAbierto y Despegar. Los mismos proyectos muestran capacidades distintas según el servicio. Una única sección de metodología combina cuatro pestañas y entregables específicos; las preguntas frecuentes y el cierre también corresponden a cada capacidad. La pertenencia a Digifianz permanece en la Home y el pie compartido. Escala24x7 conserva los logos oficiales de HubSpot y AWS con sonrisa naranja en su esquema de sincronización.

- [Fuentes de marca e imágenes de contexto](dist/assets/brand/SOURCES.md): logo oficial de Cloudfianz aportado por el usuario el 5 de noviembre de 2026, logos oficiales de clientes y Digifianz, dimensiones, procedencia y hashes. Los archivos se conservan intactos.
- [Fuentes de capturas de producto](dist/assets/projects/SOURCES.md): originales de Despegar y antecedentes visuales de REVIANZ con procedencia y hashes. El documento distingue los originales de las imágenes públicas anteriores de Despegar.

Las descripciones accesibles distinguen el trabajo mostrado: Despegar usa la vista adaptada del cotizador; la interfaz de Properix ilustra la plataforma del cliente y no la integración desarrollada por Cloudfianz; la imagen Photonix presenta equipamiento de radioterapia como contexto de su actividad. Los pies visibles solo indican «Datos de ejemplo» donde corresponde. No se incorporan nombres ni fotos de personas del equipo.

## Alcance y límites de la revisión

La entrega incluye trece páginas: Home, tres servicios, índice de casos, seis casos individuales, Contacto y Cómo trabajamos. No sustituye la web actual en `src/`. Los contenidos de casos y servicios se leen en sus URLs propias; ningún enlace público abre el lector provisional.

La agenda sigue siendo una simulación identificada como tal. El formulario de Home y Contacto está conectado al embed original de HubSpot y sus envíos son reales. No hay reserva de reuniones ni medición propia conectadas. La política de privacidad permanece como aviso provisional.

El prototipo tiene `noindex, nofollow`. El SEO técnico y los eventos locales de conversión ya están preparados; la configuración de producción, la agenda real, la política definitiva y la conexión de analítica/atribución quedan detalladas en la lista de lanzamiento al final de este documento.

La [dirección del caso REVIANZ](DIRECCION-CASO-REVIANZ.md) documenta la nueva composición y sus fuentes. `dist/revianz-page.css` sólo se carga en esa página; el preview de inicio usa los estilos compartidos del mockup.

Revisión de REVIANZ: el sitio usa los mockups ilustrativos del producto, portados desde sus componentes oficiales. La Home conserva el preview de rentabilidad, Desarrollo el de alcance y el índice una versión compacta de alcance; las vistas completas permanecen en el caso. `page_layouts/revianz_mockups.py`, `data/revianz-mockups-es.json` y `dist/revianz-mockups.css` mantienen una única implementación compartida. Las capturas anteriores ya no se muestran.

## Revisión del Hero de Casos y de Despegar · 3 de noviembre de 2026

El índice abre con título y bajada centrados sobre blanco, en una cabecera compacta. La primera fila de proyectos aporta el recurso visual inmediatamente después de la introducción. La grilla y las páginas individuales conservan su arquitectura.

Todas las vistas generales del cotizador usan `assets/hero/despegar-cotizador-hero-v1.jpg`, la variante limpia confirmada por el usuario: sin logo Digifianz ni líneas azules junto a las marcas. Aparece en Home, Hero y portfolio de Desarrollo, portfolio de Automatizaciones, card del índice, y Hero y Solución del caso Despegar. Sus ampliaciones abren el mismo JPG; los pies la identifican como vista adaptada. El PNG original queda como archivo histórico.

## Caso ConsorcioAbierto · revisión visual

La página individual adopta el sistema editorial de Despegar y REVIANZ: portada navy con resultado principal, imagen aportada por el usuario, ficha de trabajo/plataformas/alcance y capítulos diferenciados. El desafío conserva el contexto del cliente; el enfoque explica qué se evaluó y qué decisión tomó Cloudfianz. La sección mint de Solución reúne el esquema HubSpot → AWS → Odoo, las cuatro reglas y la implementación. El resultado mensual y sus beneficios operativos cierran la historia antes del contacto.

`assets/projects/consorcioabierto-plataforma-usuario.png` se conserva intacto, se puede ampliar y se identifica como contexto del producto del cliente. No representa la integración desarrollada por Cloudfianz. Fuente, dimensiones y hash en el registro de imágenes de proyectos.

## Photonix, Escala24x7 y ADS Mexicana · revisión conjunta

Las tres páginas adoptan el criterio editorial de ConsorcioAbierto: Hero navy con logo original, titular centrado en el resultado y ficha de tres datos; contexto y desafío en una misma sección; decisión técnica cuando corresponde; Solución sobre mint y resultados sobre navy. El cierre compartido reúne consulta, servicios e índice de casos. Los detalles retirados de las aperturas pasan a Solución, conservando el contenido aprobado.

Cada solución mantiene un esquema propio: Photonix conecta técnicos y administración con el sistema alojado en AWS; Escala24x7 presenta sus tres intercambios originales una sola vez dentro del diagrama; ADS Mexicana organiza el recorrido en datos del CRM, cálculos y registro de la cotización. El resultado de ADS destaca más de 50 cotizaciones diarias. Las leyendas siguen distinguiendo los esquemas de la imagen de contexto de Photonix.

## Contacto, Cómo trabajamos y pie compartido

Contacto abre con una explicación breve y el formulario visible junto al título en escritorio. Comparte con la Home el formulario original de HubSpot (portal `599312`, formulario `667182f6-5ce1-4df4-baac-b9309cfc78a4`, región `na1`). El embed se define en `templates/contact-form.html` y se carga desde `dist/app.js`, con estados de carga y error. Los envíos son reales y se gestionan en HubSpot. La explicación del siguiente paso acompaña el formulario sin comprometer un plazo de respuesta.

Cómo trabajamos presenta auditoría, diseño, implementación y soporte como modalidades independientes. El selector se activa progresivamente con JavaScript; sin él, se leen todos los paneles. Cada modalidad explica actividad, entregables y participación del equipo. Los acuerdos de alcance y validación, ejemplos de proyectos y preguntas frecuentes breves completan el recorrido hacia Contacto; presupuesto, calendario y responsabilidades se definen según cada proyecto.

El pie común agrupa los enlaces de Soluciones y Cloudfianz, la pertenencia a Digifianz y el acceso al aviso de privacidad. Su plantilla y CSS se comparten entre las trece páginas para mantener la navegación y presentación consistentes.

## Idiomas: español, inglés y portugués de Brasil

El sitio se genera en **39 páginas estáticas**: las mismas trece páginas en `/es`, `/en` y `/pt`. El selector conserva la página equivalente, utiliza el diseño del sitio y funciona sin JavaScript; con JavaScript también cierra con Escape/clic exterior y conserva el fragmento de navegación inicial. Cada página tiene `lang`, canonical y enlaces `hreflang` recíprocos. Las rutas públicas se definen en `i18n/routes.json` y se publican mediante las reescrituras de `vercel.json`.

La regla permanente está en `../AGENTS.md`: **todo cambio del sitio incluye los tres idiomas sin que el usuario tenga que pedirlo**.

### Cómo cambiar contenido

1. Editar el texto español en la plantilla, layout o archivo de contenido correspondiente.
2. Agregar la versión inglesa y portuguesa en `i18n/en.json` y `i18n/pt.json`. La clave es el texto español con espacios normalizados. El build traduce nodos de texto y atributos descriptivos, sin duplicar layouts.
3. Para mensajes generados por JavaScript, editar `i18n/runtime.json` en los tres idiomas. No incluir textos de interfaz directamente en `dist/app.js`.
4. Ejecutar `npm run build:proposal`, `npm run check:i18n`, `npm run check:seo`, `node --check prototype/dist/app.js` y `git diff --check`.
5. Revisar escritorio y móvil en los tres idiomas y conservar los archivos generados junto con las fuentes.

El build **falla si falta una traducción** y escribe `i18n/missing.json` con los textos pendientes. No existe fallback silencioso al español. Una frase modificada requiere una nueva traducción, de modo que no se publica la versión antigua de otro idioma por accidente. Los nombres propios y las marcas se conservan de manera explícita en los catálogos. `missing.json` es un diagnóstico temporal; desaparece al completar el build.

El formulario conserva el portal y formulario originales de HubSpot. Recibe el locale de la página (`es`, `en` o `pt-br`) y traducciones de campos, botón y confirmación. El callback documentado `onFormReady` traduce los textos de consentimiento conocidos sin modificar casillas, IDs de suscripción, enlaces ni valores enviados. Si cambia el consentimiento en HubSpot, revisar las claves originales y las tres traducciones en `runtime.json`; no se reemplazan textos remotos desconocidos. Referencia técnica: https://developers.hubspot.com/docs/cms/start-building/features/forms/legacy-forms

Las capturas originales de productos y los logos conservan su idioma de origen. Los textos editoriales, diagramas HTML, descripciones y pies de imagen sí están traducidos. El lector provisional ya no se utiliza para navegar: cada caso y servicio tiene su propia página traducida.

Validación de la implementación: las 39 páginas se abrieron a 390 px y 1440 px sin desbordamiento horizontal. Se revisaron visualmente el selector móvil y de escritorio, el cambio entre páginas equivalentes y el formulario con consentimiento traducido. No se enviaron consultas al CRM.

Las imágenes de proyectos se muestran como contenido estático: no se abren al hacer clic ni ofrecen enlaces de ampliación. Se conservan los textos alternativos en los tres idiomas. Los pies genéricos de producción se eliminan; los mockups de REVIANZ indican únicamente «Datos de ejemplo», «Sample data» o «Dados de exemplo».

## SEO y AEO preparados · 5 de noviembre de 2026

Alcance aprobado: mejorar las trece páginas existentes en tres idiomas, sin nuevas páginas comerciales ni nombres del equipo. Mercados: LATAM, USA y Europa. El H1 comercial elegido se conserva. El título SEO de Home pasa a «Software a medida e integración de sistemas | Cloudfianz», con sus versiones inglesa y portuguesa.

`seo.py` completa Open Graph y Twitter Cards en las 39 páginas: título, descripción, URL canónica, idioma y una imagen social existente. El JSON-LD describe `Organization`, `WebSite`, `WebPage` y, donde ya hay una ruta de navegación visible, `BreadcrumbList`. Los textos salen de la página localizada. La organización se identifica como Cloudfianz con Digifianz como organización matriz; no se incluyen personas, opiniones, puntajes ni acreditaciones. Los datos estructurados ayudan a describir el contenido, sin garantizar resultados enriquecidos ni citas en IA.

`hreflang` usa `es`, `en` y `pt-BR`; `lang="es-AR"` conserva el dialecto editorial. Las relaciones recíprocas y `x-default` coinciden con el sitemap. `sitemap.xml` se genera desde el mapa de rutas con las 39 URLs del dominio final, sin fechas ficticias de modificación ni URLs de pruebas. La preview no lo anuncia a buscadores.

Cuatro imágenes raster utilizadas en el sitio tienen variantes WebP y tamaños responsive, sin modificar los originales, logos, textos alternativos, recortes ni la interacción. La imagen principal completa pasa de aproximadamente 357 a 117 KiB y la imagen principal de Despegar de 304 a 69 KiB. Las variantes y su manifiesto están versionados; los builds normales no requieren Pillow. Para regenerarlas tras cambiar los originales:

```sh
python3 prototype/optimize-images.py
npm run build:proposal
npm run check:seo
```

El script opcional de optimización necesita Pillow. El chequeo de SEO detecta si un original cambió y las variantes quedaron obsoletas. Los ahorros indicados son tamaños de archivos, no mediciones de Core Web Vitals.

### Preview y paquete de producción

| Comando / archivo | Resultado |
| --- | --- |
| `npm run build:proposal` | Genera `prototype/dist`, siempre con `noindex, nofollow`. |
| `vercel.json` actual | Sirve `prototype/dist` y agrega `X-Robots-Tag: noindex, nofollow` a todas las respuestas. |
| `prototype/dist/robots.txt` | Permite leer las páginas para que los crawlers vean el `noindex`; no anuncia el sitemap. |
| `npm run check:seo` | Verifica las 39 páginas, metadata, schema, sitemap, imágenes y eventos sin datos personales. |
| `npm run build:release` | Reconstruye y verifica la preview, luego prepara un paquete indexable separado en `prototype/release/site` y lo verifica. No publica nada. |
| `prototype/release/vercel.production.json` | Configuración opcional para el repositorio del dominio real si se elige Vercel. No se aplica automáticamente. |

No se usa `VERCEL_ENV` para decidir indexación: el proyecto de pruebas también puede llamar Production a su rama principal. La salida indexable solo se obtiene mediante el comando explícito de empaquetado. `release/` es generado, está ignorado por Git y no se debe editar a mano. El paquete excluye `review.html`, `review.js`, `content.json` y otros archivos de revisión. Mantiene exactamente las 39 rutas públicas y el documento raíz de respaldo.

### Medición preparada, pendiente de conectar

`dist/analytics.js` crea eventos en `window.dataLayer`, únicamente en memoria. No carga Google Analytics, GTM ni otro proveedor; no crea cookies ni realiza solicitudes de seguimiento. Esto no cambia el funcionamiento del formulario externo de HubSpot existente.

| Evento | Cuándo ocurre | Significado |
| --- | --- | --- |
| `contact_cta_click` | Clic a Contacto o al acceso al formulario | Intención de contactar; no es un lead. |
| `meeting_intent` | Clic para coordinar una conversación | Intención; no confirma una reunión reservada. |
| `generate_lead` | Callback `onFormSubmitted` de HubSpot | Envío completado; se registra una sola vez por carga de página. |

Los parámetros son `site_environment`, `page_key`, `page_language`, `page_path` canónico y `form_location`. No se copian nombres, emails, mensajes, valores de campos, queries ni fragmentos. Preview y producción se diferencian explícitamente. La conversión está conectada al callback documentado de éxito, no a un clic ni al comienzo del envío. Los tests simulan eventos; no envían leads al CRM.

### Menciones públicas de Digifianz verificadas

La [Home en español de Digifianz](https://www.digifianz.com/es/) y la [página de Inbound Marketing y RevOps](https://www.digifianz.com/es/agencia-inbound-marketing-revops) incluyen enlaces a cloudfianz.com en el menú «Soluciones a Medida». Es una mención de navegación compartida, no un testimonio ni una recomendación editorial independiente. Verificado el 5 de noviembre de 2026. No se modificó Digifianz ni se contactó a terceros. La relación con Digifianz ya está explicada de forma visible en Cloudfianz y se refleja como `parentOrganization`, no como `sameAs`.

## Pendientes al migrar al repositorio y dominio reales

### 1. Conectar el despliegue correcto

- Confirmar que el dominio seguirá siendo `https://cloudfianz.com`, el hostname preferido (con o sin www), el repositorio y el hosting efectivos. Las URLs canónicas, sitemap, schema y tarjetas sociales están preparadas para ese dominio.
- El `npm run deploy:prod` heredado todavía usa `scripts/deploy.mjs` y publica `src/`. **No usarlo para lanzar el rediseño.** Implementar el pipeline para publicar `prototype/release/site`, después de ejecutar `npm run build:release`.
- Si se elige Vercel: en el repositorio REAL, reemplazar la configuración raíz con la configuración generada `prototype/release/vercel.production.json` después de revisar la migración de URLs. Usa `npm run build:release` y sirve `prototype/release/site`. La configuración del repositorio draft debe seguir sirviendo `prototype/dist` con su cabecera noindex.
- Si se mantiene AWS: adaptar la sincronización S3 y las reglas de CloudFront para las 39 rutas; Vercel rewrites no se aplican allí. Eliminar el fallback heredado de errores 403/404 a Home con estado 200 en `infra/lib/website-stack.ts`. Una URL inexistente debe devolver un 404 real, y cada URL válida debe resolver su HTML sin depender de JavaScript.
- Configurar HTTPS, redirección al hostname preferido, compresión Brotli/gzip y caché apropiada. No marcar assets con nombres estables como immutable sin versionarlos o invalidarlos al reemplazarlos.
- Mantener la preview sin indexar; si el hosting ofrece protección de acceso, puede añadirse como protección adicional. No retirar sus cabeceras al habilitar el dominio real.

### 2. Preservar URLs y enlaces existentes

- Inventariar las URLs públicas anteriores con Search Console, sitemap y enlaces externos antes de reemplazarlas. La versión original del repo tiene la Home inglesa en `/`; la nueva usa `/en` y actualmente lleva `/` a español mediante una redirección temporal. Resolver esa decisión antes de publicar.
- Preparar redirecciones 301/308 uno a uno para URLs retiradas o renombradas. No enviar todos los casos al inicio. Unificar `/index.html`, las rutas terminadas en `/index.html`, barras finales y variantes www con sus destinos canónicos.
- Revisar los destinos de los enlaces de Digifianz a Cloudfianz y sus fragmentos antiguos. Los fragmentos no llegan al servidor: conservar anclas compatibles o actualizar los enlaces de origen si hace falta.
- Mantener una canonical propia por idioma, los alternates recíprocos y `x-default`; no canonicalizar todo a español. Si cambia la decisión de Home por defecto, actualizar redirección y alternates conjuntamente.

### 3. Abrir indexación solo en producción

- Publicar el paquete indexable, cuyo HTML usa `index, follow, max-image-preview:large` y cuyo robots anuncia `https://cloudfianz.com/sitemap.xml`.
- Verificar las respuestas del dominio REAL: 200 en las 39 URLs, ausencia de `noindex` en HTML y cabeceras, robots y sitemap con 200 y tipo correcto, 301/308 donde corresponda y 404 en rutas inexistentes. Revisar también headers o bloqueos agregados por CDN/WAF/hosting, fuera del repo.
- Probar con agentes de Googlebot, Bingbot y OAI-SearchBot y confirmar que no reciben challenges de acceso. El robots de producción permite crawling general, incluido OAI-SearchBot; cualquier política específica sobre bots de entrenamiento es una decisión separada de visibilidad en búsquedas.
- Verificar el dominio en Google Search Console y Bing Webmaster Tools; enviar el sitemap y solicitar inspección de Home, un servicio y un caso por idioma. No enviar el sitemap de preview. La elegibilidad técnica no garantiza indexación o citas.
- Revisar con Rich Results Test el JSON-LD y la correspondencia de breadcrumbs, y comprobar las tarjetas al compartir enlaces. La imagen social utiliza la foto institucional existente y su descripción localizada.

### 4. Activar medición y atribución

- Elegir/configurar la propiedad GA4 o proveedor equivalente y, si corresponde, GTM. Incorporar sus IDs reales y el mecanismo de consentimiento aplicable antes de activar sus etiquetas; no están incluidos en este cambio.
- Conectar los eventos de la tabla anterior, excluir `site_environment=preview` y registrar `generate_lead` como conversión una sola vez. Evitar duplicarlo con detección automática de formularios o eventos de otro embed.
- Configurar la confirmación REAL del calendario si se habilitan reuniones: `meeting_intent` no debe contarse como reserva. El flujo actual no confirma reuniones.
- Verificar la atribución en HubSpot: origen, página de entrada, idioma, campañas y vínculo posterior con oportunidades. El embed existente no reemplaza la configuración de analítica/atribución del portal.
- Realizar un envío controlado autorizado, comprobar su llegada a HubSpot y al sistema de medición y gestionar el registro de prueba. Probar cancelación/error para comprobar que no se cuentan como conversiones.
- Preparar reportes de clics orgánicos y leads/oportunidades por página, idioma y país. Registrar por separado tráfico referido desde asistentes, menciones y citas; no son la misma métrica.

### 5. Rendimiento y mantenimiento de las páginas actuales

- Medir Home, servicios y casos con PageSpeed Insights/Lighthouse en el hosting final, con móvil y conexiones lentas. Revisar el impacto real de Google Fonts, HubSpot y scripts de medición antes de optimizarlos o diferirlos.
- Incorporar medición de campo cuando haya tráfico: objetivos al percentil 75 de LCP ≤ 2,5 s, INP ≤ 200 ms y CLS ≤ 0,1. No se obtuvo una puntuación de rendimiento ni datos de usuarios reales en esta implementación.
- Revisar títulos, snippets y consultas reales por mercado; mejorar respuestas de las FAQs existentes y la precisión de los casos sin crear nuevas páginas. Incorporar fechas de resultados o testimonios únicamente cuando estén respaldados y autorizados; no inventar cifras, nombres ni acreditaciones.
- Mantener verificaciones de idiomas y SEO en CI. Tras cada cambio de contenido, actualizar ES/EN/PT, regenerar preview/release y comprobar metadata y sitemap. No se requiere un archivo llms.txt ni se añaden promesas de aparecer en IA.

Referencias: [indexación y noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing), [idiomas y regiones](https://developers.google.com/search/docs/specialty/international/localized-versions), [datos de organizaciones](https://developers.google.com/search/docs/appearance/structured-data/organization), [funciones de IA en Google](https://developers.google.com/search/docs/appearance/ai-features), [bots de OpenAI](https://developers.openai.com/api/docs/bots), [callback de HubSpot](https://developers.hubspot.com/docs/cms/start-building/features/forms/legacy-forms).
