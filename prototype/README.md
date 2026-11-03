# Propuesta local del sitio · Cloudfianz

Prototipo local de Cloudfianz. La homepage conserva la dirección visual revisada el 23 de octubre de 2026 y los cinco casos actualizados el 29 de octubre y REVIANZ, incorporado el 2 de noviembre. Desarrollo de software a medida, Despegar y REVIANZ tienen páginas independientes; su composición se revisó el 30 de octubre para mejorar jerarquía y variedad sin cambiar los textos aprobados.

## Ver la propuesta

Desde la raíz del repositorio: `npm run dev:proposal`.

- [Revisión con selector de página y de escritorio/móvil](http://127.0.0.1:3001/review.html).
- [Homepage](http://127.0.0.1:3001/es).
- [Desarrollo de software a medida](http://127.0.0.1:3001/es/desarrollo-software-a-medida).
- [Caso Despegar](http://127.0.0.1:3001/es/casos/despegar-cotizador-hubspot).
- [Caso REVIANZ](http://127.0.0.1:3001/es/casos/revianz-gestion-financiera-proyectos).

El selector permite revisar las cuatro páginas a distintos anchos. El servidor queda limitado a `127.0.0.1:3001`; esta entrega es una vista local para revisión, no un despliegue. Después de editar las fuentes, ejecutar `npm run build:proposal` y recargar el navegador. El servidor no incorpora recarga automática.

## Dirección visual

La [dirección visual v2](DIRECCION-VISUAL-V2.md) define azul profundo `#0B1D3A`, verde `#12B5A5`, blanco `#FFFFFF`, gris `#F5F7FA` y tinta `#0E1726`. El naranja `#FF7A2F` queda reservado para un uso justificado. Manrope es la familia de titulares e Inter la de lectura.

La Home revisada el 3 de noviembre de 2026 sigue el recorrido Hero → Clientes → Soluciones → Casos → Metodología → Infraestructura AWS → Digifianz → Contacto. El hero mantiene la imagen ambiental y presenta «Software a medida para mejorar cómo funciona tu negocio». Debajo, una fila con movimiento continuo reúne los logos originales de Despegar, ConsorcioAbierto, Photonix, Escala24x7, ADS Mexicana y Digifianz, sin texto lateral. Digifianz usa su variante coral original sobre blanco. El carril no tiene botón de pausa visible; conserva pausa al pasar el puntero, navegación por teclado y una alternativa estática para movimiento reducido. Las tres soluciones tienen CTA propios. «Casos de éxito» presenta una selección de proyectos, con el subtítulo debajo del título. Reúne Despegar, REVIANZ y ConsorcioAbierto en resúmenes compactos; sus enlaces «Conocé el caso» adoptan el botón verde claro del sistema, con borde suave y esquinas redondeadas. El banner de contacto cierra esa sección después del enlace al índice. La metodología usa el selector de modalidades de Desarrollo a Medida en una versión breve para la Home: auditoría, diseño, implementación y soporte, con un panel activo que resume actividad y entregable. Sin JavaScript se muestran todos los paneles. La sección de infraestructura AWS incorpora la marca original y cuatro iconos oficiales en color: API Gateway, Lambda, EventBridge y S3. Una superficie blanca reúne los servicios con beneficios concretos —conectar, automatizar, responder a eventos y almacenar—; el texto introductorio resume el valor de los servicios administrados y enlaza al caso ConsorcioAbierto. La sección institucional de Digifianz vuelve a explicar la pertenencia de Cloudfianz antes del contacto. La [dirección vigente del inicio](DIRECCION-INICIO-V3.md) registra esta edición y sus antecedentes.

El título de Desarrollo de software a medida es «Software diseñado para los procesos de tu empresa», como complemento específico de la promesa general del inicio. Los CTA de los casos comparten `.case-button` entre Home y servicio: fondo mint `#E8F4F0`, texto verde oscuro, borde discreto, radio de 8 px y foco visible.

La referencia BairesDev se usa para trabajar escala, ritmo y peso de la evidencia. Los recursos visuales son de Cloudfianz, Digifianz, AWS y los clientes; no se copian recursos de esa referencia. La homepage abandona los logos recompuestos, diagramas simulados y flechas decorativas de la v1.

La implementación adapta columnas, navegación y selectores a móvil. La validación visual y de interacción de esta versión se registra por separado en [QA.md](QA.md).

## Contenido y recursos originales

La versión anterior aprobada se conserva en `outputs/homepage-20261022/` del workspace. Los textos vigentes están en `prototype/content/`: incluyen los cinco casos adaptados de los borradores del usuario del 29 de octubre de 2026 y REVIANZ (desarrollado para Digifianz), su índice y los servicios con ejemplos actualizados. Las notas editoriales de implementación quedan fuera de las páginas y del lector.

## Editar y generar

- `templates/home.html`: fuente de la homepage y de la cabecera, pie y diálogos compartidos. No editar directamente el `dist/index.html` generado.
- `content/*.md`: textos vigentes de servicios y casos, incluidos sus títulos y descripciones SEO.
- `build-pages.py`: generación de la homepage y las páginas independientes. Ejecuta primero `build-content.py` para regenerar el lector.
- `page_layouts/service.py`, `page_layouts/case.py` y `page_layouts/revianz.py`: composiciones de servicio y caso, separadas del generador y alimentadas por los textos vigentes.
- `page-routes.json`: mapa de los contenidos que ya tienen página propia. Sus enlaces se generan como URLs normales, también dentro de los lectores provisionales.
- `dist/home-page.css` y `dist/home-page.js`: presentación de Home y carril de clientes; los estilos y el movimiento quedan aislados de las páginas internas.
- `dist/styles.css` y `dist/app.js`: base visual e interacciones compartidas. `dist/pages.css` define el sistema de las páginas internas y el servicio; `dist/case-page.css` agrega la composición específica del caso y sólo se carga en esa página.
- `dist/review.html` y `dist/review.js`: interfaz local de revisión.
- `serve.mjs`: servidor local sin dependencias adicionales, con rutas explícitas, redirecciones a URLs sin barra final y respuestas 404 reales. No es infraestructura de producción.

`npm run build:proposal` regenera todos los HTML y `content.json`. `npm run dev:proposal` construye y arranca el servidor. El contenido principal de las páginas está incluido en el HTML: no depende de abrir un modal ni de JavaScript para leerse. Los metadatos canonical y Open Graph apuntan al destino propuesto de producción; el prototipo continúa bloqueado para indexación.

La composición vigente se documenta en [DIRECCION-PAGINAS-V2.md](DIRECCION-PAGINAS-V2.md). La [primera dirección](DIRECCION-PAGINAS.md) se conserva como antecedente. El servicio presenta las cuatro formas de contratación mediante pestañas y reúne Escala24x7 y Photonix en artículos con un marco visual común; las páginas de casos mantienen su composición específica para contexto, enfoque, solución, resultados y evolución. Las capturas permiten ampliar el software real; Photonix mantiene la leyenda que identifica su imagen como contexto institucional. Escala24x7 presenta su logo original y un esquema de la sincronización HubSpot ↔ AWS Partner Central con los logos oficiales de ambas plataformas, con acceso al caso completo en el lector.

- [Fuentes de marca e imágenes de contexto](dist/assets/brand/SOURCES.md): logo Cloudfianz recuperado del archivo usado en las presentaciones, logos oficiales de clientes y Digifianz, dimensiones, procedencia y hashes. Los archivos se conservan intactos.
- [Fuentes de capturas de producto](dist/assets/projects/SOURCES.md): originales de Despegar y antecedentes visuales de REVIANZ con procedencia y hashes. El documento distingue los originales de las imágenes públicas anteriores de Despegar.

Las captions distinguen el trabajo mostrado: Despegar es una captura del proyecto; la interfaz de Properix ilustra la plataforma del cliente y no la integración desarrollada por Cloudfianz; la imagen Photonix presenta equipamiento de radioterapia como contexto de su actividad. No se incorporan nombres ni fotos de personas del equipo.

## Alcance y límites de la revisión

La entrega incluye la homepage y las primeras páginas de servicio y caso, y no sustituye la web actual en `src/`. Desarrollo de software a medida, Despegar y REVIANZ ya tienen URLs propias y navegación entre sí. Los demás servicios, casos e índice continúan en un lector provisional hasta revisar y extender estas bases.

La agenda y el envío del formulario son simulaciones identificadas como tales. El formulario valida los campos y muestra una confirmación de prueba, sin enviar ni guardar los datos ingresados. No hay recepción comercial, reserva de reuniones ni medición conectadas. La política de privacidad permanece como aviso provisional.

El prototipo tiene `noindex, nofollow`. La recepción de consultas, la agenda, la política definitiva, la analítica, el SEO técnico de lanzamiento y el despliegue quedan para la etapa posterior a la revisión del diseño.

La [dirección del caso REVIANZ](DIRECCION-CASO-REVIANZ.md) documenta la nueva composición y sus fuentes. `dist/revianz-page.css` sólo se carga en esa página; el preview de inicio usa los estilos compartidos del mockup.

Revisión de REVIANZ: el sitio usa los mockups ilustrativos del producto, portados desde sus componentes oficiales. La Home conserva sólo el preview de rentabilidad; las vistas completas permanecen en las páginas internas. `page_layouts/revianz_mockups.py`, `data/revianz-mockups-es.json` y `dist/revianz-mockups.css` mantienen una única implementación compartida por inicio y caso. Las capturas anteriores ya no se muestran.
