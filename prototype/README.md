# Segunda propuesta visual · Cloudfianz

Prototipo local de la homepage, revisado el 23 de octubre de 2026. Conserva la paleta, el contenido y el recorrido aprobados; cambia la composición, la tipografía, las imágenes y los componentes de la primera propuesta.

## Ver la propuesta

Desde la raíz del repositorio: `npm run dev:proposal`.

- [Revisión con selector de escritorio y móvil](http://127.0.0.1:3001/review.html).
- [Homepage directa](http://127.0.0.1:3001/index.html).

El selector permite revisar distintos anchos sin modificar la página. El servidor queda limitado a `127.0.0.1:3001`; esta entrega es una vista local para revisión, no un despliegue.

## Dirección visual

La [dirección visual v2](DIRECCION-VISUAL-V2.md) define azul profundo `#0B1D3A`, verde `#12B5A5`, blanco `#FFFFFF`, gris `#F5F7FA` y tinta `#0E1726`. El naranja `#FF7A2F` queda reservado para un uso justificado. Manrope es la familia de titulares e Inter la de lectura.

La apertura azul presenta el titular completo en blanco junto a una captura real del cotizador de Despegar. Le sigue una franja con los logos auténticos de los clientes. Las necesidades se leen abiertas en tres columnas; las soluciones usan un selector que relaciona cada capacidad con un caso. Los tres casos destacados se presentan con imágenes amplias, texto y cambios concretos. Escala24x7 y ADS Mexicana se incorporan como reseñas con enlaces al texto completo; sus nombres son títulos, sin recreaciones de logos. Auditoría, diseño, implementación y soporte conservan entradas independientes. El respaldo de Digifianz, las preguntas frecuentes y el contacto completan el recorrido.

La referencia BairesDev se usa para trabajar escala, ritmo y peso de la evidencia. Los recursos visuales son de Cloudfianz, Digifianz y los clientes; no se copian recursos de esa referencia. La homepage abandona los logos recompuestos, diagramas simulados y flechas decorativas de la v1.

La implementación adapta columnas, navegación y selectores a móvil. La validación visual y de interacción de esta versión se registra por separado en [QA.md](QA.md).

## Contenido y recursos originales

La versión anterior aprobada se conserva en `outputs/homepage-20261022/` del workspace. Los textos vigentes están en `prototype/content/`: incluyen los cinco casos adaptados de los borradores del usuario del 29 de octubre de 2026, su índice y los servicios con ejemplos actualizados. El lector provisional usa `dist/content.json`, que se regenera desde la raíz del repo con `python3 prototype/build-content.py`. Las notas editoriales de implementación quedan fuera del lector.

- [Fuentes de marca e imágenes de contexto](dist/assets/brand/SOURCES.md): logo Cloudfianz recuperado del archivo usado en las presentaciones, logos oficiales de clientes y Digifianz, dimensiones, procedencia y hashes. Los archivos se conservan intactos.
- [Fuentes de las capturas Despegar](dist/assets/projects/SOURCES.md): dos capturas públicas del proyecto publicadas por Digifianz. El desenfoque ya pertenece a las imágenes originales.

Las captions distinguen el trabajo mostrado: Despegar es una captura del proyecto; la interfaz de Properix ilustra la plataforma del cliente y no la integración desarrollada por Cloudfianz; la imagen Photonix presenta equipamiento de radioterapia como contexto de su actividad. No se incorporan nombres ni fotos de personas del equipo.

## Alcance y límites de la revisión

La entrega se limita al diseño de la homepage y no sustituye la web actual en `src/`. Los enlaces a servicios y casos abren los textos aprobados en un lector; no representan el diseño final de esas páginas.

La agenda y el envío del formulario son simulaciones identificadas como tales. El formulario valida los campos y muestra una confirmación de prueba, sin enviar ni guardar los datos ingresados. No hay recepción comercial, reserva de reuniones ni medición conectadas. La política de privacidad permanece como aviso provisional.

El prototipo tiene `noindex, nofollow`. La recepción de consultas, la agenda, la política definitiva, la analítica, el SEO técnico de lanzamiento y el despliegue quedan para la etapa posterior a la revisión del diseño.
