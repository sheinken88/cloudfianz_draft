# Cloudfianz — sitio web

One-page estática (HTML/CSS/JS) con i18n EN/ES, casos de éxito desde JSON y hosting en **S3 + CloudFront**.

| Entorno | URL |
|--------|-----|
| Producción | https://cloudfianz.com |
| Staging | https://staging.cloudfianz.com |

Documentación de AWS/CDK: **[docs/INFRASTRUCTURE.md](docs/INFRASTRUCTURE.md)**

---

## Requisitos

- **Node.js 18+**
- **AWS CLI v2** con acceso a la cuenta donde está desplegada la infra (ver infra doc)
- Opcional: `aws-cdk` global si vas a cambiar stacks (`npm install -g aws-cdk`)

---

## Primer uso

```powershell
cd Cloudfianz
npm install
npm run infra:install   # solo si tocás CDK en infra/
npm run dev             # http://localhost:3000
```

`npm run dev` ejecuta el build de casos y sirve `src/`.

---

## Dónde editar contenido

| Qué | Archivo |
|-----|---------|
| Página principal (copy, estilos, modales) | `src/index.html` |
| Casos de éxito | `src/data/cases.json` |
| Imágenes, logos, favicon | `src/assets/` |
| Videos del hero | `src/assets/videos/intro.mp4` (ES), `intro_en.mp4` (EN) — ver `src/assets/videos/README.txt` |

**Idiomas:** textos con pares `<span data-es>` / `<span data-en>`. La ruta `/es` muestra español; el toggle y la cookie `cf_lang` coordinan con la CloudFront Function (detalle en infra doc).

**Build:** `npm run build` inyecta casos en `index.html` y copia a `src/es/index.html` (carpeta generada, no versionar).

---

## Publicar cambios (solo contenido)

Usá la **cuenta AWS correcta** (exports `CloudfianzBucket-*` / `CloudfianzDistributionId-*`):

```powershell
aws sts get-caller-identity   # validar cuenta antes de deploy

npm run deploy:staging   # prueba en staging
npm run deploy:prod      # producción + invalidación CloudFront
```

No hace falta CDK para cambios de HTML/assets si la infra ya existe.

---

## Cambios de infraestructura

Solo si modificás `infra/`:

```powershell
cd infra
npm run synth
npm run deploy:all    # o stacks individuales — ver docs/INFRASTRUCTURE.md
```

---

## Estructura del repo

```
Cloudfianz/
├── src/                 # Sitio servido en S3
├── scripts/
│   ├── build-cases.mjs
│   └── deploy.mjs
├── infra/               # AWS CDK (TypeScript)
├── docs/
│   └── INFRASTRUCTURE.md
└── Plan/                # Notas/planificación interna (opcional)
```

---

## Subir a GitHub (handoff)

1. Repo **privado** en la organización correspondiente.
2. **No** subir: `node_modules/`, `infra/cdk.out/`, credenciales `.env`, videos `.mp4` muy pesados (ver `.gitignore`; usar Git LFS o almacén compartido).
3. En la raíz del proyecto:

```powershell
git init
git add .
git status    # revisar que no entren node_modules ni mp4
git commit -m "Initial commit: Cloudfianz site + CDK"
git remote add origin <URL-del-repo>
git push -u origin main
```

4. Dar al compañero: acceso al repo + usuario IAM/SSO en la cuenta AWS de Cloudfianz + enlace a `docs/INFRASTRUCTURE.md`.

HubSpot (formulario de contacto) está embebido en `src/index.html` (portal/form ID públicos; no son secretos).

---

## Comandos rápidos

| Comando | Acción |
|---------|--------|
| `npm run dev` | Local con live reload |
| `npm run build` | Regenerar casos + `es/index.html` |
| `npm run deploy:staging` | Build + S3 staging + invalidación CF |
| `npm run deploy:prod` | Build + S3 prod + invalidación CF |
| `npm run infra:synth` | Sintetizar plantillas CDK |
