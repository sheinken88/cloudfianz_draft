# Plan de continuidad del sitio

Actualizado el 2 de noviembre de 2026. Recupera el mapa aprobado el 22 de octubre y lo ajusta a los cinco casos entregados el 29 de octubre y al caso REVIANZ incorporado el 2 de noviembre. Mercado: Argentina y Latinoamérica en español.

## Punto de partida

- [x] Mensaje centrado en resultados de negocio y pertenencia a Digifianz.
- [x] Investigación SEO cualitativa y mapa de lanzamiento. No hay mediciones de volumen, dificultad o tráfico proyectado.
- [x] Textos de tres servicios y seis casos, con índice actualizado.
- [x] Primera base visual de la homepage en escritorio y móvil; queda abierta a mejoras.
- [x] Marcas originales y recursos visuales con procedencia documentada.
- [x] Snapshot local completo `draft-01`, commit `821d63c`, con bundle de respaldo.

Desarrollo de software a medida, Despegar y REVIANZ ya tienen páginas independientes, enlazadas desde la homepage y entre sí, listas para revisión. Los demás servicios, casos e índice siguen en un lector provisional. Agenda, formulario y privacidad son demostraciones; no hay recepción real ni analítica conectada.

## 1. Convertir el prototipo en un sitio con páginas propias

Doce páginas comerciales más privacidad:

| Página | Ruta propuesta |
| --- | --- |
| Inicio | `/es` |
| Desarrollo de software a medida | `/es/desarrollo-software-a-medida` |
| Integración de sistemas | `/es/integracion-de-sistemas` |
| Automatización de procesos | `/es/automatizacion-de-procesos` |
| Índice de casos | `/es/casos` |
| Despegar Ads | `/es/casos/despegar-cotizador-hubspot` |
| ConsorcioAbierto | `/es/casos/consorcioabierto-facturacion-hubspot-odoo` |
| Photonix | `/es/casos/photonix-servicio-tecnico` |
| Escala24x7 | `/es/casos/escala24x7-hubspot-aws-partner-central` |
| ADS Mexicana | `/es/casos/ads-mexicana-cotizador-hubspot` |
| REVIANZ para Digifianz | `/es/casos/revianz-gestion-financiera-proyectos` |
| Contacto | `/es/contacto` |
| Privacidad | `/es/privacidad` |

- [x] Diseñar e implementar una página de servicio y una de caso como base para revisar los dos tipos de página.
- [ ] Revisar con el usuario Desarrollo de software a medida y Despegar; incorporar los ajustes antes de extender la estructura.
- [ ] Aplicar esas bases a los otros servicios y casos, con contenido específico.
- [ ] Crear índice de casos y página de contacto.
- [ ] Sustituir los lectores modales por enlaces a URLs propias; conservar la lectura y los enlaces cruzados entre servicios, casos y contacto.
- [ ] Adaptar navegación compartida, pie, estados activos y recorridos móviles.

Entrega actual: Desarrollo de software a medida + caso Despegar, navegables desde la homepage y desde el selector de revisión. La siguiente etapa es ajustar estas dos bases con el feedback y aplicarlas al resto de los servicios y casos. Los ajustes quedan en commits locales posteriores a `draft-01`.

Revisión del 30 de octubre: se rediseñaron ambas páginas para variar las composiciones y dar mayor jerarquía al software real y los resultados. Los textos y metadatos aprobados se conservan. La contratación muestra las cuatro opciones independientes sin ocultarlas en pestañas. Esta segunda propuesta queda para revisión antes de extender el diseño.

## 2. Integrar SEO durante la construcción

- [ ] Contenido principal y metadatos propios en el HTML de cada ruta: título, descripción, canonical y jerarquía de encabezados.
- [ ] Enlaces internos rastreables y contexto suficiente para distinguir la intención de los tres servicios.
- [ ] Imágenes optimizadas, textos alternativos, rendimiento y accesibilidad en móvil.
- [ ] Respuestas de rutas correctas, página 404 y convención consistente de URLs.
- [ ] Preparar sitemap, robots y datos estructurados pertinentes al contenido visible.
- [ ] Inventariar URLs existentes y preparar redirecciones para la migración.
- [ ] Resolver idiomas y acceso estable a `/es`; conservar inicialmente la entrada inglesa existente. No señalar páginas sin traducción como equivalentes.
- [ ] Mantener el entorno de revisión fuera del índice; comprobar indexabilidad de producción al publicar.

El mapa original dejó la especialización general de HubSpot coordinada con Digifianz. Cloudfianz se centra en software a medida, integración y automatización, con casos que demuestran su experiencia.

Avance de esta entrega: las dos páginas nuevas incluyen el texto principal, un H1, título, descripción, canonical y Open Graph en su HTML, con enlaces nativos entre sí. La homepage también enlaza a esas URLs. El servidor local unifica las variantes con barra final o `index.html`, conserva los parámetros y devuelve 404 para rutas inexistentes. El resto de los puntos SEO queda pendiente para el sitio completo; el entorno de revisión mantiene `noindex, nofollow` y `robots.txt` con bloqueo de rastreo.

## 3. Hacer operativo el contacto

- [ ] Agenda real en `/es/contacto#agenda`, con disponibilidad y zona horaria; sin formulario previo obligatorio.
- [ ] Consulta escrita en `/es/contacto#consulta`, con nombre, empresa, email y necesidad.
- [ ] Recepción y seguimiento en HubSpot; identificar responsable y próxima acción.
- [ ] Confirmaciones reales, errores recuperables y alternativa cuando la agenda no carga o no tiene horarios.
- [ ] Política de privacidad correspondiente al tratamiento efectivo de datos.

Datos necesarios antes de conectar: agenda y disponibilidad, cuenta/formulario de HubSpot, destinatario y responsable comercial, entidad que recibe los datos y política aplicable. La invitación sigue siendo «Hablemos de tu negocio», sin foco promocional en gratuidad o duración.

## 4. Medir el recorrido comercial

- [ ] Revisar cuentas y accesos existentes antes de configurar Search Console, GA4 y HubSpot.
- [ ] Registrar origen de visita y ubicación del CTA, servicios y casos consultados, aperturas de agenda e inicio del formulario.
- [ ] Contar consultas al confirmar recepción y reservas al confirmar la agenda; no tratarlas como simples clics.
- [ ] Mantener datos personales y texto de consultas en el CRM, fuera de eventos de analítica.
- [ ] Vincular consulta y reserva del mismo contacto y evitar duplicación por reintentos o recargas.
- [ ] Seguir reuniones realizadas, calificación, oportunidades y contrataciones.

La métrica principal acordada es reuniones realizadas con oportunidades pertinentes. No se fijó una meta porcentual sin una línea de base.

## 5. Preparar el lanzamiento

- [ ] Revisar el sitio completo en escritorio y móvil: enlaces, teclado, formularios, agenda y rendimiento.
- [ ] Comprobar recepción comercial y medición de punta a punta.
- [ ] Revisar materiales de casos, atribución de marcas y cifras de la versión final.
- [ ] Elegir destino remoto y estrategia de publicación con el usuario. No hacer push al repositorio original ni desplegar sin indicación.
- [ ] Conservar snapshot de la versión de lanzamiento y plan de retorno.
- [ ] Después del lanzamiento, revisar indexación, consultas y calidad de los contactos para priorizar mejoras.

## Fuera del primer lanzamiento

Blog, página propia de equipo con perfiles personales, páginas por país o industria, ofertas genéricas por tecnología y páginas separadas de Auditoría, Diseño, Implementación y Soporte. «Cómo trabajamos» conserva esas cuatro formas de contratación dentro del sitio. Se reconsideran páginas adicionales cuando haya contenido y una necesidad comercial concretos.

## Fuentes del plan

- Mapa e investigación: `outputs/homepage-20261022/investigacion-seo-y-mapa-lanzamiento.md` del workspace.
- Recorrido comercial y medición: `outputs/homepage-20261022/propuesta-homepage-v2.md`.
- Diseño y secuencia: `outputs/homepage-20261022/brief-diseno-homepage.md`.
- Contacto: `outputs/homepage-20261022/contenido-lanzamiento-v1/contacto.md`.
- Contenidos vigentes: `prototype/content/`.
- Reglas de versionado: [VERSIONADO.md](VERSIONADO.md).

Este documento actualiza el alcance de tres a cinco casos; los documentos históricos se conservan sin reescribirlos.

## Incorporación de REVIANZ · 2 de noviembre de 2026

Caso desarrollado para Digifianz, con página propia, metadatos y capturas originales del entorno de demostración. Se incorpora al inicio, al portfolio de desarrollo a medida, al índice y al contenido de automatización. El índice y automatización conservan su lector provisional. No se modifican los casos anteriores ni se atribuyen métricas de mejora sin datos. Esta incorporación amplía el mapa a seis casos y queda para revisión local.
