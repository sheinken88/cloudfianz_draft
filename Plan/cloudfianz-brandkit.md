# Cloudfianz — Brand Kit & Estructura de Página

> Documento de referencia para desarrollo en Cursor.  
> La página de muestra fue aprobada en diseño y paleta. Este documento captura fielmente todos los tokens, estructura y patrones del mockup original para replicar y ajustar en producción.

---

## Índice

1. [Identidad de marca](#1-identidad-de-marca)
2. [Paleta de colores](#2-paleta-de-colores)
3. [Tipografía](#3-tipografía)
4. [Tokens CSS](#4-tokens-css)
5. [Estructura de página](#5-estructura-de-página)
6. [Patrones de componentes](#6-patrones-de-componentes)
7. [Sistema bilingüe EN/ES](#7-sistema-bilingüe-enes)
8. [Decisiones de diseño bloqueadas](#8-decisiones-de-diseño-bloqueadas)

---

## 1. Identidad de marca

**Nombre:** Cloudfianz  
**Dominio:** cloudfianz.com  
**Tagline EN:** Custom software & cloud engineering — backed by Digifianz  
**Tagline ES:** Ingeniería de software y cloud a medida — respaldado por Digifianz  

**Posicionamiento:** Marca independiente de ingeniería técnica. No es una sub-sección de Digifianz sino una unidad de negocio propia con identidad y dominio separados, que hereda la credibilidad de Digifianz (HubSpot Elite Partner, +10 años).

**Logo temporal:** Texto `Cloudfianz` en Space Grotesk Bold + `by Digifianz` en Inter Regular, tamaño reducido, debajo o al lado. El logo definitivo se diseñará después — el código debe soportar reemplazarlo fácilmente con un `<img>`.

**Audiencia principal:**
- Empresas SaaS/Software que necesitan desarrollo técnico custom
- Empresas de Logística con operaciones complejas
- Servicios Profesionales que usan HubSpot y necesitan integraciones avanzadas
- Mercados: US, Europa, LATAM (bilingüe EN/ES)

---

## 2. Paleta de colores

### Colores principales

| Token | Hex | Uso |
|---|---|---|
| `--navy` | `#0B1D3A` | Color primario. Fondos oscuros, navbar, secciones ancla |
| `--teal` | `#12B5A5` | Acento primario. CTAs principales, highlights, bordes activos |
| `--orange` | `#FF7A2F` | Acento secundario. Badges urgentes, highlights de servicio estrella, hover states |

### Colores de texto y fondo

| Token | Hex | Uso |
|---|---|---|
| `--ink` | `#0E1726` | Texto principal sobre fondos claros |
| `--muted` | `#5B6879` | Texto secundario, subtítulos, labels |
| `--gray` | `#F5F7FA` | Fondo de secciones alternas, cards de contenido |

### Uso de colores por sección

```
Navbar          → fondo --navy, texto blanco
Hero            → fondo --navy (gradiente sutil hacia #0d2347), texto blanco
Credibility bar → fondo blanco o --gray, texto --muted
Two paths       → fondo --gray, cards blancas con borde --teal
Value ladder    → fondos alternados: blanco / --gray / --navy
SaaS section    → fondo --navy con acento --teal
AWS section     → fondo --gray, iconografía técnica
Case studies    → fondo blanco, cards con borde-left --teal
Digifianz back  → fondo --gray con logo Digifianz
FAQ             → fondo blanco
CTA final       → fondo --navy, botón --teal
Footer          → fondo #07121F (más oscuro que --navy)
```

### Colores de estado

```css
--success: #10B981;   /* confirmaciones, checks */
--warning: #F59E0B;   /* alertas suaves */
--error:   #EF4444;   /* errores de formulario */
```

---

## 3. Tipografía

### Fuentes

| Rol | Familia | Pesos | Import |
|---|---|---|---|
| Headlines | **Space Grotesk** | 600, 700 | Google Fonts |
| Body | **Inter** | 400, 500, 600 | Google Fonts |
| Labels técnicos / eyebrows | **JetBrains Mono** | 400, 500 | Google Fonts |

### Import en HTML

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

### Escala tipográfica

```css
/* Headlines — Space Grotesk */
h1 { font-family: 'Space Grotesk', sans-serif; font-size: clamp(2.2rem, 5vw, 3.5rem); font-weight: 700; line-height: 1.1; }
h2 { font-family: 'Space Grotesk', sans-serif; font-size: clamp(1.6rem, 3.5vw, 2.5rem); font-weight: 700; line-height: 1.2; }
h3 { font-family: 'Space Grotesk', sans-serif; font-size: clamp(1.2rem, 2.5vw, 1.6rem); font-weight: 600; line-height: 1.3; }

/* Body — Inter */
p  { font-family: 'Inter', sans-serif; font-size: 1rem; font-weight: 400; line-height: 1.7; }
.lead { font-size: 1.125rem; font-weight: 400; line-height: 1.6; }

/* Eyebrows / labels técnicos — JetBrains Mono */
.eyebrow {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--teal);
}
```

### Patrones de texto recurrentes

```html
<!-- Eyebrow antes de título de sección -->
<span class="eyebrow">// servicios</span>
<h2>Tu software, tus reglas</h2>

<!-- Label técnico en cards -->
<span class="eyebrow">AWS Lambda</span>

<!-- Tagline de hero -->
<p class="lead">Texto introductorio más largo...</p>
```

---

## 4. Tokens CSS

Pegar en `:root` al inicio del CSS global:

```css
:root {
  /* Paleta principal */
  --navy:   #0B1D3A;
  --teal:   #12B5A5;
  --orange: #FF7A2F;
  --ink:    #0E1726;
  --muted:  #5B6879;
  --gray:   #F5F7FA;

  /* Estados */
  --success: #10B981;
  --warning: #F59E0B;
  --error:   #EF4444;

  /* Tipografía */
  --font-head: 'Space Grotesk', sans-serif;
  --font-body: 'Inter', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  /* Espaciado base */
  --section-py: clamp(4rem, 8vw, 7rem);   /* padding vertical de secciones */
  --container:  1200px;                    /* max-width del contenido */
  --gap:        1.5rem;                    /* gap estándar entre elementos */

  /* Bordes y radios */
  --radius-sm:  6px;
  --radius-md:  12px;
  --radius-lg:  20px;

  /* Sombras */
  --shadow-card: 0 2px 20px rgba(11,29,58,.08);
  --shadow-hover: 0 8px 32px rgba(11,29,58,.14);

  /* Transiciones */
  --transition: 0.2s ease;
}
```

---

## 5. Estructura de página

La página es **one-page** con scroll vertical. 13 secciones en orden:

```
① Navbar
② Hero
③ Credibility bar
④ Two paths (¿quién eres?)
⑤ Value ladder (3 niveles de servicio)
⑥ SaaS a medida (sección estrella)
⑦ AWS infrastructure
⑧ Case studies
⑨ Digifianz backing
⑩ FAQ accordion
⑪ CTA final
⑫ Footer
⑬ Modal HubSpot (overlay, se abre con CTA)
```

---

### ① Navbar

**Comportamiento:** sticky top, fondo `--navy`, sombra al hacer scroll.

```html
<nav class="navbar">
  <div class="container">
    <!-- Logo izquierda -->
    <a href="#" class="logo">
      Cloudfianz
      <span class="logo-sub">by Digifianz</span>
    </a>

    <!-- Links centrales (desktop) -->
    <ul class="nav-links">
      <li><a href="#servicios" data-en="Services" data-es="Servicios">Services</a></li>
      <li><a href="#casos" data-en="Cases" data-es="Casos">Cases</a></li>
      <li><a href="#faq" data-en="FAQ" data-es="FAQ">FAQ</a></li>
    </ul>

    <!-- Derecha: toggle idioma + CTA -->
    <div class="nav-actions">
      <button class="lang-toggle" onclick="handleLangToggle('es')">ES</button>
      <button class="lang-toggle" onclick="handleLangToggle('en')">EN</button>
      <button class="btn btn-primary" onclick="openModal()"
        data-en="Talk to us" data-es="Hablemos">Talk to us</button>
    </div>
  </div>
</nav>
```

```css
.navbar {
  position: sticky; top: 0; z-index: 100;
  background: var(--navy);
  padding: 1rem 0;
  transition: box-shadow var(--transition);
}
.navbar.scrolled { box-shadow: 0 2px 24px rgba(0,0,0,.25); }

.logo {
  font-family: var(--font-head);
  font-size: 1.4rem; font-weight: 700;
  color: #fff; text-decoration: none;
  display: flex; flex-direction: column; line-height: 1.1;
}
.logo-sub {
  font-family: var(--font-body);
  font-size: 0.65rem; font-weight: 400;
  color: var(--teal); letter-spacing: 0.04em;
}

.lang-toggle {
  background: transparent; border: 1.5px solid rgba(255,255,255,.3);
  color: #fff; border-radius: var(--radius-sm);
  padding: 4px 10px; font-size: 0.75rem; cursor: pointer;
  transition: all var(--transition);
}
.lang-toggle:hover, .lang-toggle.active {
  border-color: var(--teal); color: var(--teal);
}
```

---

### ② Hero

**Fondo:** `--navy` con gradiente sutil. Texto blanco. 2 CTAs: primario (teal) + secundario (outline blanco).

```html
<section class="hero">
  <div class="container">
    <span class="eyebrow" data-en="// cloud engineering" data-es="// ingeniería cloud">
      // cloud engineering
    </span>
    <h1 data-en="Your software, built for your business"
        data-es="Tu software, diseñado para tu empresa">
      Your software, built for your business
    </h1>
    <p class="lead"
      data-en="We design and build custom SaaS, cloud infrastructure on AWS and HubSpot integrations. No adapting your business to a tool — the tool adapts to you."
      data-es="Diseñamos y construimos SaaS a medida, infraestructura cloud en AWS e integraciones con HubSpot. Sin adaptar tu empresa a un software — el software se adapta a ti.">
      We design and build custom SaaS...
    </p>
    <div class="hero-actions">
      <button class="btn btn-primary" onclick="openModal()"
        data-en="Start a project" data-es="Iniciar proyecto">Start a project</button>
      <a href="#servicios" class="btn btn-outline"
        data-en="See services" data-es="Ver servicios">See services</a>
    </div>
  </div>
</section>
```

```css
.hero {
  background: linear-gradient(135deg, var(--navy) 0%, #0d2347 100%);
  padding: var(--section-py) 0;
  text-align: center;
}
.hero h1 { color: #fff; margin: 1rem 0; }
.hero .lead { color: rgba(255,255,255,.75); max-width: 640px; margin: 0 auto 2.5rem; }
.hero-actions { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
```

---

### ③ Credibility bar

Franja de stats/logos. Fondo blanco, texto `--muted`. Separa el hero visualmente.

```html
<section class="credibility-bar">
  <div class="container">
    <div class="cred-grid">
      <div class="cred-item">
        <strong>10+</strong>
        <span data-en="years of experience" data-es="años de experiencia">years of experience</span>
      </div>
      <div class="cred-item">
        <strong>55+</strong>
        <span data-en="HubSpot certifications" data-es="certificaciones HubSpot">HubSpot certifications</span>
      </div>
      <div class="cred-item">
        <strong>AWS</strong>
        <span data-en="Select Partner" data-es="Select Partner">Select Partner</span>
      </div>
      <div class="cred-item">
        <strong>US · EU · LATAM</strong>
        <span data-en="markets served" data-es="mercados atendidos">markets served</span>
      </div>
    </div>
  </div>
</section>
```

```css
.credibility-bar {
  background: #fff;
  padding: 2rem 0;
  border-bottom: 1px solid #E8ECF2;
}
.cred-grid {
  display: flex; gap: 2rem;
  justify-content: center; flex-wrap: wrap;
}
.cred-item {
  display: flex; flex-direction: column; align-items: center;
  gap: 0.25rem; text-align: center;
}
.cred-item strong {
  font-family: var(--font-head); font-size: 1.6rem;
  color: var(--navy);
}
.cred-item span { font-size: 0.8rem; color: var(--muted); }
```

---

### ④ Two paths

Cards de identificación de audiencia. Fondo `--gray`, 2 cards lado a lado.

```html
<section class="two-paths" id="servicios">
  <div class="container">
    <span class="eyebrow" data-en="// who is this for" data-es="// para quién es esto">// who is this for</span>
    <h2 data-en="Two types of companies work with us"
        data-es="Dos tipos de empresas trabajan con nosotros">
      Two types of companies work with us
    </h2>
    <div class="paths-grid">
      <div class="path-card">
        <div class="path-icon">⚡</div>
        <h3 data-en="Your software hit its limits"
            data-es="Tu software llegó a su límite">
          Your software hit its limits
        </h3>
        <p data-en="Custom integrations, complex migrations and APIs that connect your entire stack — when off-the-shelf tools can't keep up or get too expensive to extend."
           data-es="Integraciones custom, migraciones complejas y APIs que conectan todo tu stack — cuando las herramientas estándar no alcanzan o extenderlas se vuelve demasiado costoso.">
          Custom integrations...
        </p>
        <div class="path-examples">
          <span class="tag">HubSpot</span>
          <span class="tag">Salesforce</span>
          <span class="tag">SAP</span>
          <span class="tag">Monday</span>
          <span class="tag" data-en="Spreadsheets" data-es="Excel / Sheets">Spreadsheets</span>
        </div>
      </div>
      <div class="path-card path-card--featured">
        <div class="path-icon">🚀</div>
        <h3 data-en="You need software built for your business"
            data-es="Necesitas software diseñado para tu empresa">
          You need software built for your business
        </h3>
        <p data-en="We build your SaaS from scratch. Your processes, your rules, your competitive advantage."
           data-es="Construimos tu SaaS desde cero. Tus procesos, tus reglas, tu ventaja competitiva.">
          We build your SaaS from scratch...
        </p>
      </div>
    </div>
  </div>
</section>
```

```css
.two-paths { background: var(--gray); padding: var(--section-py) 0; }
.two-paths h2 { text-align: center; margin: 0.5rem 0 3rem; }

.paths-grid { display: grid; grid-template-columns: 1fr 1fr; gap: var(--gap); }

.path-card {
  background: #fff; border-radius: var(--radius-md);
  padding: 2.5rem; box-shadow: var(--shadow-card);
  border-top: 3px solid transparent;
  transition: box-shadow var(--transition);
}
.path-card:hover { box-shadow: var(--shadow-hover); }
.path-card--featured { border-top-color: var(--teal); }

.path-icon { font-size: 2rem; margin-bottom: 1rem; }
.path-examples { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 1.25rem; }

@media (max-width: 700px) {
  .paths-grid { grid-template-columns: 1fr; }
}
```

---

### ⑤ Value ladder

3 niveles de servicio en progresión. Alternancia de fondos: blanco / `--gray` / `--navy`.

```html
<section class="value-ladder">
  <div class="container">
    <span class="eyebrow" data-en="// services" data-es="// servicios">// services</span>
    <h2 data-en="From integration to full platform"
        data-es="De la integración a la plataforma completa">
      From integration to full platform
    </h2>

    <!-- Nivel 1 -->
    <div class="ladder-item">
      <div class="ladder-label">01</div>
      <div class="ladder-content">
        <h3 data-en="HubSpot integrations & custom APIs"
            data-es="Integraciones HubSpot y APIs custom">HubSpot integrations & custom APIs</h3>
        <p data-en="We connect your CRM with your entire tech stack. Complex migrations, bidirectional sync, custom objects."
           data-es="Conectamos tu CRM con todo tu stack. Migraciones complejas, sincronización bidireccional, objetos custom.">
          We connect your CRM...
        </p>
        <ul class="feature-list">
          <li data-en="Custom HubSpot integrations" data-es="Integraciones HubSpot a medida">Custom HubSpot integrations</li>
          <li data-en="Complex data migrations" data-es="Migraciones de datos complejas">Complex data migrations</li>
          <li data-en="REST & GraphQL API development" data-es="Desarrollo de APIs REST y GraphQL">REST & GraphQL API development</li>
        </ul>
      </div>
    </div>

    <!-- Nivel 2 -->
    <div class="ladder-item ladder-item--alt">
      <div class="ladder-label">02</div>
      <div class="ladder-content">
        <h3 data-en="AWS serverless architecture"
            data-es="Arquitectura serverless en AWS">AWS serverless architecture</h3>
        <p>Lambda · API Gateway · EventBridge · SQS · S3 · Data Lakes</p>
      </div>
    </div>

    <!-- Nivel 3 -->
    <div class="ladder-item ladder-item--dark">
      <div class="ladder-label">03</div>
      <div class="ladder-content">
        <span class="eyebrow" data-en="// flagship" data-es="// servicio estrella">// flagship</span>
        <h3 data-en="Custom SaaS development"
            data-es="Desarrollo de SaaS a medida">Custom SaaS development</h3>
        <p data-en="We build the platform your company needs — not the one that exists in the market."
           data-es="Construimos la plataforma que tu empresa necesita, no la que existe en el mercado.">
          We build the platform...
        </p>
      </div>
    </div>
  </div>
</section>
```

```css
.value-ladder { padding: var(--section-py) 0; background: #fff; }
.value-ladder h2 { text-align: center; margin: 0.5rem 0 3rem; }

.ladder-item {
  display: grid; grid-template-columns: 80px 1fr;
  gap: 2rem; align-items: start;
  padding: 3rem 0; border-top: 1px solid #E8ECF2;
}
.ladder-item--alt { background: var(--gray); margin: 0 -1.5rem; padding: 3rem 1.5rem; }
.ladder-item--dark { background: var(--navy); margin: 0 -1.5rem; padding: 3rem 1.5rem; border-radius: var(--radius-md); }
.ladder-item--dark h3, .ladder-item--dark p { color: #fff; }
.ladder-item--dark .eyebrow { color: var(--teal); }

.ladder-label {
  font-family: var(--font-mono); font-size: 2.5rem;
  color: var(--teal); font-weight: 700; line-height: 1;
}

.feature-list { list-style: none; margin-top: 1rem; }
.feature-list li {
  padding: 0.4rem 0 0.4rem 1.4rem; position: relative;
  color: var(--muted); font-size: 0.9rem;
}
.feature-list li::before {
  content: '→'; position: absolute; left: 0; color: var(--teal);
}
```

---

### ⑥ SaaS a medida (sección estrella)

Destaque visual del servicio principal. Fondo `--navy`, layout 60/40 con visual a la derecha.

```html
<section class="saas-feature">
  <div class="container">
    <div class="saas-grid">
      <div class="saas-copy">
        <span class="eyebrow" data-en="// our flagship" data-es="// servicio estrella">// our flagship</span>
        <h2 data-en="Stop adapting your business to a software"
            data-es="Deja de adaptar tu empresa a un software">
          Stop adapting your business to a software
        </h2>
        <p data-en="Most companies twist their processes to fit tools that weren't built for them. We build the platform that fits your operation — from scratch, on AWS, designed to scale."
           data-es="La mayoría de las empresas tuercen sus procesos para encajar en herramientas que no fueron diseñadas para ellas. Nosotros construimos la plataforma que se ajusta a tu operación.">
          Most companies twist their processes...
        </p>
        <button class="btn btn-primary" onclick="openModal()"
          data-en="Build my SaaS" data-es="Construir mi SaaS">Build my SaaS</button>
      </div>
      <div class="saas-visual">
        <!-- Placeholder: reemplazar con screenshot/mockup del producto -->
        <div class="saas-visual-placeholder">
          <span class="eyebrow">dashboard preview</span>
        </div>
      </div>
    </div>
  </div>
</section>
```

```css
.saas-feature { background: var(--navy); padding: var(--section-py) 0; }
.saas-feature h2, .saas-feature p { color: #fff; }
.saas-feature p { color: rgba(255,255,255,.75); }

.saas-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }
.saas-visual-placeholder {
  background: rgba(255,255,255,.06); border-radius: var(--radius-md);
  aspect-ratio: 4/3; display: flex; align-items: center; justify-content: center;
  border: 1.5px dashed rgba(18,181,165,.4);
}
```

---

### ⑦ AWS Infrastructure

Grid de tecnologías. Fondo `--gray`, iconografía con labels en JetBrains Mono.

```html
<section class="aws-section">
  <div class="container">
    <span class="eyebrow" data-en="// infrastructure" data-es="// infraestructura">// infrastructure</span>
    <h2 data-en="Built on AWS" data-es="Construido en AWS">Built on AWS</h2>
    <p class="section-sub" data-en="We build serverless, scalable architectures using AWS native services."
       data-es="Construimos arquitecturas serverless y escalables con servicios nativos de AWS.">
      We build serverless...
    </p>
    <div class="tech-grid">
      <div class="tech-card"><span class="eyebrow">Lambda</span><p>Serverless compute</p></div>
      <div class="tech-card"><span class="eyebrow">API Gateway</span><p>REST & WebSocket APIs</p></div>
      <div class="tech-card"><span class="eyebrow">EventBridge</span><p>Event-driven architecture</p></div>
      <div class="tech-card"><span class="eyebrow">SQS</span><p>Message queuing</p></div>
      <div class="tech-card"><span class="eyebrow">S3</span><p>Object storage & Data Lakes</p></div>
      <div class="tech-card"><span class="eyebrow">AI Agents</span><p>Internal automation</p></div>
    </div>
  </div>
</section>
```

```css
.aws-section { background: var(--gray); padding: var(--section-py) 0; text-align: center; }
.aws-section h2 { margin: 0.5rem 0 1rem; }
.section-sub { color: var(--muted); max-width: 560px; margin: 0 auto 3rem; }

.tech-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--gap); }
.tech-card {
  background: #fff; border-radius: var(--radius-md);
  padding: 1.5rem; text-align: left;
  border-left: 3px solid var(--teal);
  box-shadow: var(--shadow-card);
  transition: box-shadow var(--transition);
}
.tech-card:hover { box-shadow: var(--shadow-hover); }
.tech-card p { color: var(--muted); font-size: 0.875rem; margin-top: 0.5rem; }

@media (max-width: 700px) {
  .tech-grid { grid-template-columns: repeat(2, 1fr); }
}
```

---

### ⑧ Case studies

3 cards de casos. Fondo blanco, borde-left `--teal`. **Placeholders ahora, reemplazar con casos reales con nombre de cliente.**

```html
<section class="cases" id="casos">
  <div class="container">
    <span class="eyebrow" data-en="// case studies" data-es="// casos de éxito">// case studies</span>
    <h2 data-en="Results that speak" data-es="Resultados que hablan">Results that speak</h2>
    <div class="cases-grid">

      <div class="case-card">
        <div class="case-industry eyebrow">SaaS · Logistics</div>
        <h3 data-en="[Client name] reduced ops time by 60% with a custom platform"
            data-es="[Nombre cliente] redujo tiempo operativo 60% con plataforma a medida">
          [Client name] reduced ops time by 60%...
        </h3>
        <p data-en="We built a custom route management SaaS replacing 3 separate tools."
           data-es="Construimos un SaaS de gestión de rutas reemplazando 3 herramientas separadas.">
          We built a custom route management SaaS...
        </p>
        <div class="case-tags">
          <span class="tag">Custom SaaS</span>
          <span class="tag">AWS Lambda</span>
          <span class="tag">React</span>
        </div>
      </div>

      <div class="case-card">
        <div class="case-industry eyebrow">HubSpot · Integration</div>
        <h3>[Client name] — HubSpot + ERP bidirectional sync</h3>
        <p>Real-time sync between HubSpot and SAP, zero manual data entry.</p>
        <div class="case-tags">
          <span class="tag">HubSpot API</span>
          <span class="tag">SAP</span>
          <span class="tag">EventBridge</span>
        </div>
      </div>

      <div class="case-card">
        <div class="case-industry eyebrow">Data · AWS</div>
        <h3>[Client name] — Data Lake for business intelligence</h3>
        <p>Unified data lake consolidating 5 sources, dashboards in real time.</p>
        <div class="case-tags">
          <span class="tag">S3</span>
          <span class="tag">Athena</span>
          <span class="tag">QuickSight</span>
        </div>
      </div>

    </div>
  </div>
</section>
```

```css
.cases { background: #fff; padding: var(--section-py) 0; }
.cases h2 { text-align: center; margin: 0.5rem 0 3rem; }

.cases-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--gap); }
.case-card {
  border-radius: var(--radius-md); padding: 2rem;
  border-left: 4px solid var(--teal);
  box-shadow: var(--shadow-card);
  transition: box-shadow var(--transition);
}
.case-card:hover { box-shadow: var(--shadow-hover); }
.case-industry { margin-bottom: 0.75rem; }
.case-card h3 { font-size: 1rem; margin-bottom: 0.75rem; }
.case-card p { color: var(--muted); font-size: 0.875rem; margin-bottom: 1rem; }

.case-tags { display: flex; gap: 0.5rem; flex-wrap: wrap; }
.tag {
  background: var(--gray); color: var(--ink);
  font-size: 0.7rem; font-weight: 600; padding: 3px 8px;
  border-radius: 4px; font-family: var(--font-mono);
}

@media (max-width: 900px) {
  .cases-grid { grid-template-columns: 1fr; }
}
```

---

### ⑨ Digifianz backing

Sección de credibilidad y respaldo. Fondo `--gray`, layout centrado con logo de Digifianz.

```html
<section class="backing">
  <div class="container">
    <div class="backing-inner">
      <!-- Logo Digifianz placeholder -->
      <div class="backing-logo">
        <span style="font-family: var(--font-head); font-size: 1.5rem; color: var(--navy);">Digifianz</span>
      </div>
      <h2 data-en="Backed by 10+ years of HubSpot expertise"
          data-es="Respaldado por +10 años de expertise en HubSpot">
        Backed by 10+ years of HubSpot expertise
      </h2>
      <p data-en="Cloudfianz is the technical engineering unit of Digifianz — HubSpot Elite Partner with 55+ certifications and Custom Integration accreditation. You get a specialized engineering team with the backing of a proven B2B agency."
         data-es="Cloudfianz es la unidad de ingeniería técnica de Digifianz — HubSpot Elite Partner con 55+ certificaciones y acreditación de Custom Integration. Obtienes un equipo de ingeniería especializado con el respaldo de una agencia B2B consolidada.">
        Cloudfianz is the technical engineering unit...
      </p>
      <div class="backing-stats">
        <div><strong>Elite Partner</strong><span>HubSpot</span></div>
        <div><strong>55+</strong><span data-en="Certifications" data-es="Certificaciones">Certifications</span></div>
        <div><strong>Custom Integration</strong><span data-en="Accreditation" data-es="Acreditación">Accreditation</span></div>
        <div><strong>US · EU · LATAM</strong><span>Markets</span></div>
      </div>
    </div>
  </div>
</section>
```

```css
.backing { background: var(--gray); padding: var(--section-py) 0; }
.backing-inner { max-width: 760px; margin: 0 auto; text-align: center; }
.backing-logo { margin-bottom: 1.5rem; }
.backing h2 { margin-bottom: 1.5rem; }
.backing p { color: var(--muted); margin-bottom: 2.5rem; }

.backing-stats {
  display: flex; gap: 2rem; justify-content: center; flex-wrap: wrap;
}
.backing-stats > div {
  display: flex; flex-direction: column; align-items: center; gap: 0.25rem;
}
.backing-stats strong { font-family: var(--font-head); font-size: 1.1rem; color: var(--navy); }
.backing-stats span { font-size: 0.75rem; color: var(--muted); }
```

---

### ⑩ FAQ accordion

Fondo blanco. Preguntas diseñadas con respuesta-primero (clave para AIO/GEO). Schema JSON-LD en `<head>`.

```html
<section class="faq" id="faq">
  <div class="container">
    <span class="eyebrow" data-en="// faq" data-es="// preguntas frecuentes">// faq</span>
    <h2 data-en="Frequent questions" data-es="Preguntas frecuentes">Frequent questions</h2>
    <div class="faq-list">

      <div class="faq-item">
        <button class="faq-q" onclick="toggleQ(this)">
          <span data-en="What is Cloudfianz and how is it different from Digifianz?"
                data-es="¿Qué es Cloudfianz y en qué se diferencia de Digifianz?">
            What is Cloudfianz and how is it different from Digifianz?
          </span>
          <span class="faq-arrow">+</span>
        </button>
        <div class="faq-a">
          <p data-en="Cloudfianz is the software engineering and cloud infrastructure unit of Digifianz. While Digifianz focuses on HubSpot strategy and marketing automation, Cloudfianz handles technical implementations: custom SaaS development, AWS serverless architecture, complex API integrations and data migrations."
             data-es="Cloudfianz es la unidad de ingeniería de software e infraestructura cloud de Digifianz. Mientras Digifianz se enfoca en estrategia HubSpot y automatización de marketing, Cloudfianz maneja las implementaciones técnicas: desarrollo de SaaS a medida, arquitectura serverless en AWS, integraciones complejas de APIs y migraciones de datos.">
            Cloudfianz is the software engineering unit...
          </p>
        </div>
      </div>

      <!-- Repetir patrón para cada pregunta -->

    </div>
  </div>
</section>
```

```css
.faq { background: #fff; padding: var(--section-py) 0; }
.faq h2 { text-align: center; margin: 0.5rem 0 3rem; }
.faq-list { max-width: 720px; margin: 0 auto; }

.faq-item { border-bottom: 1px solid #E8ECF2; }
.faq-q {
  width: 100%; background: none; border: none;
  display: flex; justify-content: space-between; align-items: center;
  padding: 1.25rem 0; cursor: pointer; text-align: left;
  font-family: var(--font-head); font-size: 1rem; font-weight: 600;
  color: var(--ink); gap: 1rem;
}
.faq-arrow {
  font-size: 1.5rem; color: var(--teal);
  transition: transform var(--transition); flex-shrink: 0;
}
.faq-item.open .faq-arrow { transform: rotate(45deg); }

.faq-a {
  max-height: 0; overflow: hidden;
  transition: max-height 0.35s ease;
}
.faq-item.open .faq-a { max-height: 400px; }
.faq-a p { color: var(--muted); padding-bottom: 1.25rem; line-height: 1.7; }
```

```javascript
function toggleQ(btn) {
  const item = btn.closest('.faq-item');
  const isOpen = item.classList.contains('open');
  // Cerrar todos
  document.querySelectorAll('.faq-item.open').forEach(el => el.classList.remove('open'));
  // Abrir el clickeado (si no estaba abierto)
  if (!isOpen) item.classList.add('open');
}
```

---

### ⑪ CTA final

Fondo `--navy`. Un solo mensaje, un solo botón. Sin distracciones.

```html
<section class="cta-final">
  <div class="container">
    <h2 data-en="Ready to build?" data-es="¿Listo para construir?">Ready to build?</h2>
    <p data-en="Tell us about your project. We'll respond within 24 hours."
       data-es="Cuéntanos sobre tu proyecto. Respondemos en menos de 24 horas.">
      Tell us about your project. We'll respond within 24 hours.
    </p>
    <button class="btn btn-primary btn-lg" onclick="openModal()"
      data-en="Start a project" data-es="Iniciar proyecto">Start a project</button>
  </div>
</section>
```

```css
.cta-final {
  background: var(--navy); padding: var(--section-py) 0; text-align: center;
}
.cta-final h2 { color: #fff; margin-bottom: 1rem; }
.cta-final p { color: rgba(255,255,255,.7); margin-bottom: 2.5rem; }
```

---

### ⑫ Footer

Fondo `#07121F` (más oscuro que `--navy`). 3 columnas + copyright.

```html
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="logo">Cloudfianz <span class="logo-sub">by Digifianz</span></div>
        <p data-en="Custom software & cloud engineering"
           data-es="Ingeniería de software y cloud a medida">
          Custom software & cloud engineering
        </p>
      </div>
      <div class="footer-links">
        <h4 data-en="Services" data-es="Servicios">Services</h4>
        <ul>
          <li><a data-en="Custom SaaS" data-es="SaaS a medida">Custom SaaS</a></li>
          <li><a data-en="AWS Architecture" data-es="Arquitectura AWS">AWS Architecture</a></li>
          <li><a data-en="HubSpot Integrations" data-es="Integraciones HubSpot">HubSpot Integrations</a></li>
          <li><a data-en="API Development" data-es="Desarrollo de APIs">API Development</a></li>
        </ul>
      </div>
      <div class="footer-links">
        <h4>Cloudfianz</h4>
        <ul>
          <li><a data-en="Case studies" data-es="Casos de éxito">Case studies</a></li>
          <li><a data-en="About" data-es="Nosotros">About</a></li>
          <li><a data-en="Contact" data-es="Contacto">Contact</a></li>
          <li><a href="https://digifianz.com" target="_blank">Digifianz →</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2026 Cloudfianz — a Digifianz company · cloudfianz.com</p>
    </div>
  </div>
</footer>
```

```css
.footer { background: #07121F; padding: 4rem 0 2rem; }
.footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 3rem; margin-bottom: 3rem; }
.footer-brand .logo { color: #fff; margin-bottom: 0.75rem; }
.footer-brand p { color: rgba(255,255,255,.45); font-size: 0.875rem; }
.footer-links h4 { color: rgba(255,255,255,.5); font-size: 0.7rem; font-weight: 600; letter-spacing: .08em; text-transform: uppercase; margin-bottom: 1rem; }
.footer-links ul { list-style: none; }
.footer-links li { margin-bottom: 0.5rem; }
.footer-links a { color: rgba(255,255,255,.65); text-decoration: none; font-size: 0.875rem; transition: color var(--transition); }
.footer-links a:hover { color: var(--teal); }
.footer-bottom { border-top: 1px solid rgba(255,255,255,.08); padding-top: 2rem; text-align: center; }
.footer-bottom p { color: rgba(255,255,255,.3); font-size: 0.8rem; }
```

---

### ⑬ Modal HubSpot

Overlay con formulario embebido de HubSpot. Se activa con `openModal()`.

```html
<!-- Modal -->
<div class="modal-overlay" id="modal" onclick="closeModalOutside(event)">
  <div class="modal-box">
    <button class="modal-close" onclick="closeModal()">×</button>
    <h3 data-en="Tell us about your project"
        data-es="Cuéntanos sobre tu proyecto">Tell us about your project</h3>
    <p data-en="We'll respond within 24 hours."
       data-es="Respondemos en menos de 24 horas.">We'll respond within 24 hours.</p>

    <!-- En producción: reemplazar con embed de HubSpot form -->
    <div id="hubspot-form-container">
      <!-- HubSpot script va aquí:
      <script charset="utf-8" type="text/javascript" src="//js.hsforms.net/forms/embed/v2.js"></script>
      <script>
        hbspt.forms.create({
          region: "na1",
          portalId: "TU_PORTAL_ID",
          formId: "TU_FORM_ID"
        });
      </script>
      -->
      <p style="color:var(--muted);text-align:center;padding:2rem">[HubSpot form embed]</p>
    </div>
  </div>
</div>
```

```css
.modal-overlay {
  display: none; position: fixed; inset: 0; z-index: 1000;
  background: rgba(7,18,31,.85); backdrop-filter: blur(4px);
  align-items: center; justify-content: center;
}
.modal-overlay.open { display: flex; }

.modal-box {
  background: #fff; border-radius: var(--radius-lg);
  padding: 2.5rem; max-width: 520px; width: 90%; position: relative;
  animation: modalIn .2s ease;
}
@keyframes modalIn {
  from { transform: translateY(12px); opacity: 0; }
  to   { transform: translateY(0);    opacity: 1; }
}
.modal-close {
  position: absolute; top: 1rem; right: 1.25rem;
  background: none; border: none; font-size: 1.75rem; cursor: pointer;
  color: var(--muted); line-height: 1;
}
.modal-box h3 { margin-bottom: 0.5rem; }
.modal-box > p { color: var(--muted); margin-bottom: 1.5rem; }
```

```javascript
function openModal() {
  document.getElementById('modal').classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeModal() {
  document.getElementById('modal').classList.remove('open');
  document.body.style.overflow = '';
}
function closeModalOutside(e) {
  if (e.target === document.getElementById('modal')) closeModal();
}
// Cerrar con Escape
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeModal(); });
```

---

## 6. Patrones de componentes

### Botones

```css
.btn {
  display: inline-flex; align-items: center; justify-content: center;
  padding: 0.75rem 1.75rem; border-radius: var(--radius-sm);
  font-family: var(--font-body); font-size: 0.9rem; font-weight: 600;
  cursor: pointer; border: 2px solid transparent;
  text-decoration: none; transition: all var(--transition);
  white-space: nowrap;
}
.btn-primary {
  background: var(--teal); color: #fff;
  border-color: var(--teal);
}
.btn-primary:hover { background: #0fa090; border-color: #0fa090; }

.btn-outline {
  background: transparent; color: #fff;
  border-color: rgba(255,255,255,.5);
}
.btn-outline:hover { border-color: #fff; }

.btn-lg { padding: 1rem 2.25rem; font-size: 1rem; }
```

### Container

```css
.container {
  max-width: var(--container);
  margin: 0 auto;
  padding: 0 1.5rem;
}
```

### Responsive breakpoints

```css
/* Tablet */
@media (max-width: 900px) {
  .saas-grid     { grid-template-columns: 1fr; }
  .footer-grid   { grid-template-columns: 1fr 1fr; }
  .cases-grid    { grid-template-columns: 1fr; }
}

/* Mobile */
@media (max-width: 560px) {
  .paths-grid    { grid-template-columns: 1fr; }
  .tech-grid     { grid-template-columns: repeat(2, 1fr); }
  .footer-grid   { grid-template-columns: 1fr; }
  .ladder-item   { grid-template-columns: 1fr; }
  .hero-actions  { flex-direction: column; align-items: center; }
}
```

---

## 7. Sistema bilingüe EN/ES

### Principio

Todos los textos del sitio tienen atributos `data-en` y `data-es` en el elemento HTML. Una función JavaScript central (`setLang()`) los aplica. El idioma inicial se detecta por CloudFront geo-routing (ver `cloudfianz-infra.md`).

### Atributos en el HTML

```html
<!-- Ejemplo de uso -->
<h2 data-en="Our services" data-es="Nuestros servicios">Our services</h2>
<button data-en="Contact us" data-es="Contáctanos">Contact us</button>
<p data-en="English text" data-es="Texto en español">English text</p>
```

### Función JS

```javascript
function setLang(lang) {
  // Aplicar textos
  document.querySelectorAll('[data-en]').forEach(el => {
    const text = el.getAttribute('data-' + lang);
    if (text) el.textContent = text;
  });

  // Guardar preferencia en cookie (CloudFront la lee en próximas visitas)
  document.cookie = 'cf_lang=' + lang + '; max-age=31536000; path=/; SameSite=Lax';

  // Actualizar estado visual del toggle
  document.querySelectorAll('.lang-toggle').forEach(btn => {
    btn.classList.toggle('active', btn.textContent.trim().toLowerCase() === lang);
  });

  // Guardar en variable global para referencia
  window.currentLang = lang;
}

// Inicialización (al cargar la página)
function getInitialLang() {
  const cookie = document.cookie.match(/cf_lang=([a-z]{2})/);
  if (cookie) return cookie[1];
  const urlParam = new URLSearchParams(window.location.search).get('lang');
  if (urlParam === 'es' || urlParam === 'en') return urlParam;
  return 'en';
}

document.addEventListener('DOMContentLoaded', () => {
  setLang(getInitialLang());
});
```

### Toggle en el navbar

```html
<button class="lang-toggle" onclick="setLang('en')">EN</button>
<button class="lang-toggle" onclick="setLang('es')">ES</button>
```

---

## 8. Decisiones de diseño bloqueadas

Estas decisiones están aprobadas y no deben cambiar sin consenso del equipo:

| Decisión | Valor |
|---|---|
| Paleta de color | navy `#0B1D3A` · teal `#12B5A5` · orange `#FF7A2F` |
| Tipografía headlines | Space Grotesk (no cambiar) |
| Tipografía body | Inter |
| Labels técnicos | JetBrains Mono |
| Estructura | One-page, 13 secciones en el orden definido |
| Idiomas | Bilingual EN/ES, con `data-en`/`data-es` en cada elemento |
| CTA principal | Abre modal de HubSpot (no navega a otra página) |
| Servicio estrella | Custom SaaS a medida (siempre destacado sobre otros servicios) |
| Cyberseguridad | NO incluir nunca en ningún servicio comunicado |
| Respaldo de marca | "backed by Digifianz" o "by Digifianz" — siempre presente |
| Logo | Temporal (texto). Cuando llegue el logo definitivo, va en `<img>` en el `.logo` del navbar y footer |
| Blog | No en la versión de lanzamiento |

---

*Cloudfianz · cloudfianz.com · backed by Digifianz*
