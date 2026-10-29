# Caso ConsorcioAbierto

**URL propuesta:** `/es/casos/consorcioabierto-facturacion-hubspot-odoo`
**Title:** ConsorcioAbierto: más de 15.000 facturas al mes | Cloudfianz
**Meta description:** Una automatización a medida conecta HubSpot y Odoo para generar más de 15.000 facturas mensuales con reglas comerciales distintas en cuatro países.

## Apertura

**Texto de contexto:** ConsorcioAbierto · Integración y automatización de procesos

**H1:** ConsorcioAbierto: más de 15.000 facturas mensuales con HubSpot y Odoo conectados.

Cloudfianz desarrolló un flujo que automatiza la facturación mensual de ConsorcioAbierto. La solución toma las membresías de HubSpot y genera las facturas en Odoo, aplicando los descuentos, períodos y condiciones de cada contrato en Argentina, Uruguay, Paraguay y Colombia.

ConsorcioAbierto ofrece una plataforma de gestión administrativa y financiera para administraciones de consorcios. Su operación comprende más de 2.000 administraciones y 16.000 consorcios, con acuerdos comerciales que varían por cliente y país.

## El problema: contratos distintos, cálculos manuales cada mes

La empresa ya utilizaba Odoo para facturar, pero necesitaba un CRM para gestionar el ciclo comercial de las administraciones que pagan una membresía por su plataforma.

Cada cliente podía tener condiciones diferentes: descuentos proporcionales en el tiempo, períodos con distintos importes y particularidades por país. Aplicar esas reglas a mano generaba errores de facturación y consumía trabajo del equipo mes a mes.

La implementación de HubSpot con Digifianz comenzó con un objetivo concreto: conectar la gestión de las membresías con la facturación en Odoo.

## Una arquitectura adaptada a la complejidad de los contratos

El enfoque inicial contemplaba el módulo de suscripciones de HubSpot. Durante la implementación se comprobó que no permitía representar todas las condiciones con el detalle necesario.

Cloudfianz diseñó una alternativa: representar las membresías mediante negocios en pipelines de HubSpot y procesar sus reglas con AWS Step Functions y funciones Lambda. Esto permitió conservar la información comercial en el CRM y resolver la lógica particular de facturación fuera de sus limitaciones nativas.

## La solución: de la membresía a la factura

- **Membresías dentro de HubSpot.** Cada negocio registra el acuerdo comercial y su estado.
- **Condiciones por período.** Las líneas de producto representan la duración y el descuento correspondiente, separando el precio de las condiciones particulares del contrato.
- **Precios actualizados.** El proceso utiliza los productos de HubSpot para contemplar las actualizaciones mensuales, incluso en acuerdos anteriores.
- **Facturación en Odoo.** El flujo de AWS toma esa información, aplica las reglas del contrato y del país, y genera la facturación correspondiente.

El proyecto llevó un año y medio de punta a punta. Además del desarrollo, requirió ordenar y documentar criterios de descuento y facturación que antes se aplicaban manualmente. La estandarización de esas reglas fue parte central de la solución.

## Resultados: facturación a escala con reglas consistentes

Con las membresías cargadas y actualizadas en HubSpot, el proceso genera más de 15.000 facturas mensuales en Odoo en cuestión de horas, sin que el equipo tenga que calcular y cargar cada factura por separado.

El cambio operativo se refleja en tres capacidades concretas:

- **Un flujo para cuatro países.** La automatización contempla las particularidades de Argentina, Uruguay, Paraguay y Colombia.
- **Contratos con condiciones variables.** Los descuentos y períodos se procesan según las reglas definidas para cada membresía.
- **Menos cálculo y carga manual.** El equipo mantiene los acuerdos en el CRM y el flujo resuelve la generación de facturas.

La estandarización reduce la dependencia del criterio individual al aplicar los acuerdos.

## ¿Tu facturación depende de acuerdos difíciles de administrar a mano?

Contanos cómo se registran tus contratos y qué reglas necesita aplicar tu equipo cada mes. Evaluemos cómo conectar la información comercial con la facturación.

Conocé nuestros servicios de [integración de sistemas](servicio-integracion-sistemas.md) y [automatización de procesos](servicio-automatizacion-procesos.md).
