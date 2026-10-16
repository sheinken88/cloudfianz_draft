# Cloudfianz — Cambios de contenido v2

> Este documento especifica los cambios a aplicar sobre el staging actual (`staging.cloudfianz.com`).
> Cada cambio indica qué sección modificar, qué texto reemplazar y qué agregar.
> El diseño y la paleta no cambian — solo contenido y estructura de secciones.

---

## Cambio 1 — IA como capa habilitada por la infraestructura

### Dónde aplicar

**Sección "Escalera de valor" — Nivel 02 "Ordená tus datos"** y **Sección AWS "Infraestructura AWS real, en producción"**.

---

### 1A — Actualizar nivel 02 de la escalera de valor

**Texto actual del nivel 02:**
```
Ordená tus datos
Centralizá tu información dispersa y activala con cloud escalable.
✓ Arquitectura serverless en AWS
✓ Data Lake corporativo
✓ Base para IA y agentes internos
```

**Reemplazar por:**
```
Datos + IA listos para operar
Centralizá tu información y activá procesos controlados por IA — sobre infraestructura AWS diseñada para eso.
✓ Arquitectura serverless en AWS
✓ Data Lake corporativo
✓ Agentes de IA internos sobre tus propios datos
✓ Automatizaciones auditables y controladas
```

---

### 1B — Agregar tarjeta en la sección AWS

En la grilla de tecnologías AWS, agregar una tarjeta nueva al final:

```html
<div class="tech-card">
  <span class="eyebrow">AI Agents</span>
  <p>Automatización inteligente sobre tus datos y procesos</p>
</div>
```

**Texto EN:** `Intelligent automation over your data and processes`
**Texto ES:** `Automatización inteligente sobre tus datos y procesos`

---

### 1C — Agregar bloque de IA después de la sección AWS

Agregar una nueva subsección inmediatamente después de la grilla de tecnologías AWS, antes del bloque "Cómo trabajamos":

**Título ES:** `La IA no es un producto separado — es lo que se activa cuando tus sistemas están bien conectados`
**Título EN:** `AI isn't a separate product — it's what activates when your systems are properly connected`

**Cuerpo ES:**
> Con tu infraestructura en AWS y tus datos centralizados, implementamos agentes que automatizan decisiones completas: desde triaje de solicitudes hasta orquestación de procesos operativos enteros. Todo auditable, controlado y escalable desde el primer día.

**Cuerpo EN:**
> With your infrastructure on AWS and centralized data, we implement agents that automate complete decisions — from request triage to full operational process orchestration. All auditable, controlled, and scalable from day one.

**3 bullets ES:**
- Agentes sobre tus datos propios — sin depender de terceros
- Procesos automáticos con reglas que definís vos
- Escalable: de un agente piloto a una operación completa

**3 bullets EN:**
- Agents trained on your own data — no third-party dependency
- Automatic processes with rules you define
- Scalable: from a pilot agent to a full operation

**Diseño sugerido:** fondo `--navy`, eyebrow `// IA aplicada` / `// applied AI`, mismo estilo que la sección SaaS destacado pero más compacto (sin visual a la derecha, texto centrado + bullets en 3 columnas).

---

## Cambio 2 — SaaS como activo de la empresa

### Dónde aplicar

**Sección estrella "★ SERVICIO DESTACADO"** — agregar un bloque nuevo debajo del copy principal y antes del botón CTA.

---

### Texto a agregar

**Título ES:** `Tu SaaS no es un gasto — es un activo de tu empresa`
**Título EN:** `Your SaaS isn't a cost — it's a company asset`

**Cuerpo ES:**
> A diferencia de un software de terceros, tu plataforma es propiedad intelectual 100% tuya. No tiene techo de plan, no cobra por asiento y crece exactamente donde tu operación lo necesita. Con el tiempo, puede convertirse en una ventaja competitiva difícil de replicar — o incluso en una línea de negocio adicional.

**Cuerpo EN:**
> Unlike third-party software, your platform is 100% your intellectual property. No plan limits, no per-seat fees, and it grows exactly where your operation needs it. Over time, it can become a competitive moat that's hard to replicate — or even an additional revenue stream.

**3 bullets comparativos — agregar a la lista existente (que ya tiene ✕ y ✓):**

ES:
```
✓ Propiedad intelectual 100% tuya
✓ Sin costo por asiento ni límite de plan
✓ Activo que crece con tu empresa
```

EN:
```
✓ 100% your intellectual property
✓ No per-seat cost or plan ceiling
✓ An asset that compounds with your business
```

---

## Cambio 3 — Reducción de costos de membresías

### Dónde aplicar — dos lugares

**3A — Sección "Dos tipos de empresas" — Path 1 (el de los límites del software)**

Al texto actual del path 1:
```
Tu software llegó a su límite
Integraciones custom, migraciones complejas y APIs que conectan todo tu stack — cuando las herramientas estándar no alcanzan o extenderlas se vuelve demasiado costoso.
```

**Agregar al final del párrafo:**

ES:
> Muchos clientes además reducen o eliminan costos de suscripción al reemplazar herramientas redundantes con integraciones o módulos propios. El desarrollo se paga una vez; la membresía, todos los meses.

EN:
> Many clients also reduce or eliminate subscription costs by replacing redundant tools with custom integrations or modules. Development is a one-time cost; the membership is monthly.

---

**3B — Agregar pregunta en el FAQ** (ver Cambio 4 más abajo, pregunta #2).

---

## Cambio 4 — FAQ generalizado (sin foco en HubSpot)

### Reemplazar las 4 preguntas actuales por estas 5

---

**Pregunta 1**

ES: `¿Con qué tipos de software y plataformas trabajan?`
EN: `What types of software and platforms do you work with?`

Respuesta ES:
> Con cualquier stack. Trabajamos con HubSpot, Salesforce, SAP, Monday, sistemas legacy, ERPs propietarios, plataformas de ecommerce y cualquier software que exponga una API o base de datos. Si tu herramienta puede conectarse, nosotros podemos integrarla.

Respuesta EN:
> Any stack. We work with HubSpot, Salesforce, SAP, Monday, legacy systems, proprietary ERPs, ecommerce platforms, and any software that exposes an API or database. If your tool can connect, we can integrate it.

---

**Pregunta 2**

ES: `¿Pueden ayudarme a reducir mis costos de herramientas y suscripciones?`
EN: `Can you help me reduce my tool and subscription costs?`

Respuesta ES:
> Sí. Una integración o módulo custom puede reemplazar procesos que hoy pagás por suscripción mensual — eliminar una herramienta redundante o evitar subir de plan. El desarrollo se paga una vez; el ahorro, todos los meses.

Respuesta EN:
> Yes. A custom integration or module can replace processes you currently pay for monthly — eliminating a redundant tool or avoiding a plan upgrade. Development is a one-time cost; the savings are monthly.

---

**Pregunta 3** *(mantener, actualizar texto levemente)*

ES: `¿Qué diferencia a un SaaS a medida de un software estándar?`
EN: `What makes a custom SaaS different from standard software?`

Respuesta ES:
> Un SaaS a medida se diseña alrededor de tu proceso exacto, sin features que no usás ni límites que te frenen. Es propiedad intelectual tuya, escala según tu demanda real y no depende de las decisiones de pricing de un tercero.

Respuesta EN:
> A custom SaaS is designed around your exact process — no unused features, no arbitrary limits. It's your intellectual property, scales with your real demand, and doesn't depend on a third party's pricing decisions.

---

**Pregunta 4** *(nueva)*

ES: `¿Cuánto tiempo toma desarrollar una integración o un SaaS a medida?`
EN: `How long does it take to build an integration or a custom SaaS?`

Respuesta ES:
> Depende de la complejidad. Una integración entre dos plataformas puede estar en producción en 3 a 6 semanas. Un SaaS a medida desde MVP hasta lanzamiento suele tomar entre 2 y 5 meses. En la primera consulta técnica te damos una estimación real basada en tu caso.

Respuesta EN:
> It depends on complexity. An integration between two platforms can be in production in 3 to 6 weeks. A custom SaaS from MVP to launch typically takes 2 to 5 months. In the first technical consultation we give you a real estimate based on your case.

---

**Pregunta 5** *(mantener sin cambios)*

ES: `¿Trabajan en inglés y español?`
EN: `Do you work in English and Spanish?`

Respuesta ES:
> Sí. Somos un equipo bilingüe EN/ES, atendiendo empresas en Estados Unidos, Europa y Latinoamérica.

Respuesta EN:
> Yes. We are a bilingual EN/ES team, serving companies in the United States, Europe and Latin America.

---

## Resumen de cambios para Cursor

| # | Sección afectada | Tipo de cambio |
|---|---|---|
| 1A | Escalera de valor — Nivel 02 | Reemplazar título, cuerpo y bullets |
| 1B | AWS tech grid | Agregar tarjeta "AI Agents" |
| 1C | Después de sección AWS | Agregar bloque nuevo de IA (fondo navy) |
| 2 | Sección SaaS destacado | Agregar bloque "activo de empresa" + 3 bullets |
| 3A | Two paths — Path 1 | Agregar párrafo de reducción de costos |
| 4 | FAQ completo | Reemplazar las 4 preguntas por 5 nuevas |

**Lo que NO cambia:** diseño, paleta, tipografía, estructura general de secciones, navbar, hero, credibility bar, casos de éxito, sección Digifianz backing, footer, modal, sistema bilingüe.

---

*Cloudfianz · cloudfianz.com · backed by Digifianz*
