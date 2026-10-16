# Cloudfianz — Infraestructura AWS CDK

> **Dominio:** cloudfianz.com  
> **Stack:** AWS CDK (TypeScript) · S3 · CloudFront · Route 53 · ACM  
> **Entornos:** prod (`cloudfianz.com`) · staging (`staging.cloudfianz.com`)  
> **Geo-routing:** LATAM → ES · US/EU/resto → EN  

---

## Índice

1. [Estructura del proyecto](#1-estructura-del-proyecto)
2. [Setup inicial](#2-setup-inicial)
3. [Workflow diario desde Cursor](#3-workflow-diario-desde-cursor)
4. [Código CDK](#4-código-cdk)
5. [CloudFront Function — Geo-router](#5-cloudfront-function--geo-router)
6. [Scripts de deploy](#6-scripts-de-deploy)
7. [Configurar DNS en el registrador](#7-configurar-dns-en-el-registrador)
8. [Headers AIO](#8-headers-aio)
9. [Referencia de comandos](#9-referencia-de-comandos)

---

## 1. Estructura del proyecto

```
cloudfianz/
├── src/                        ← Website (HTML, CSS, JS, assets)
│   ├── index.html
│   └── assets/
│       ├── css/
│       ├── js/
│       └── img/
├── infra/                      ← CDK — tocar solo cuando cambia la infra
│   ├── bin/
│   │   └── app.ts
│   ├── lib/
│   │   ├── certificate-stack.ts
│   │   ├── website-stack.ts
│   │   └── dns-stack.ts
│   ├── functions/
│   │   └── geo-router.js       ← CloudFront Function
│   ├── cdk.json
│   ├── package.json
│   └── tsconfig.json
├── scripts/
│   ├── deploy.sh               ← S3 sync + CF invalidation
│   └── dev.sh                  ← Servidor local
└── package.json                ← Comandos raíz
```

---

## 2. Setup inicial

### 2.1 Prerequisitos

```bash
# Node.js 18+
node --version

# AWS CLI v2
aws --version

# AWS CDK
npm install -g aws-cdk

# Configurar credenciales AWS
aws configure
# → AWS Access Key ID
# → AWS Secret Access Key
# → Default region: us-east-1
# → Output format: json
```

### 2.2 Instalar dependencias

```bash
# Raíz del proyecto
npm install

# Infra CDK
cd infra && npm install && cd ..
```

### 2.3 Bootstrap CDK (solo la primera vez por cuenta/región)

```bash
# Bootstrap en us-east-1 (necesario para certificado ACM)
cd infra
cdk bootstrap aws://ACCOUNT_ID/us-east-1

# Bootstrap en tu región principal si es diferente (ej: us-west-2)
cdk bootstrap aws://ACCOUNT_ID/us-west-2
```

Para obtener tu `ACCOUNT_ID`:
```bash
aws sts get-caller-identity --query Account --output text
```

### 2.4 Deploy de infraestructura (una sola vez)

```bash
cd infra

# Primero el certificado (us-east-1, requerido por CloudFront)
cdk deploy CertificateStack

# Luego todo lo demás
cdk deploy WebsiteStack-prod WebsiteStack-staging DnsStack
```

> ⚠️ El certificado ACM **no se valida hasta que el dominio apunte a Route 53**. Ver sección 7.

---

## 3. Workflow diario desde Cursor

Una vez que la infra está desplegada, el día a día es:

```bash
# Desarrollo local
npm run dev               # http://localhost:3000 con live reload

# Probar en staging
npm run deploy:staging    # sube src/ → S3 staging + invalida CF cache

# Publicar a producción
npm run deploy:prod       # sube src/ → S3 prod + invalida CF cache
```

**Flujo recomendado:**
```
editar en src/ → npm run dev → verificar local
  → npm run deploy:staging → verificar en staging.cloudfianz.com
  → npm run deploy:prod → live en cloudfianz.com
```

La invalidación de CloudFront tarda ~30 segundos. Después el cambio es visible globalmente.

---

## 4. Código CDK

### `infra/bin/app.ts`

```typescript
import * as cdk from 'aws-cdk-lib';
import { CertificateStack } from '../lib/certificate-stack';
import { WebsiteStack } from '../lib/website-stack';
import { DnsStack } from '../lib/dns-stack';

const app = new cdk.App();

const env = {
  account: process.env.CDK_DEFAULT_ACCOUNT,
  region: process.env.CDK_DEFAULT_REGION,
};

const usEast1 = { account: process.env.CDK_DEFAULT_ACCOUNT, region: 'us-east-1' };

// Certificado wildcard (debe estar en us-east-1 para CloudFront)
const certStack = new CertificateStack(app, 'CertificateStack', {
  env: usEast1,
  domain: 'cloudfianz.com',
});

// Entorno producción
new WebsiteStack(app, 'WebsiteStack-prod', {
  env,
  environment: 'prod',
  domain: 'cloudfianz.com',
  certificate: certStack.certificate,
});

// Entorno staging
new WebsiteStack(app, 'WebsiteStack-staging', {
  env,
  environment: 'staging',
  domain: 'staging.cloudfianz.com',
  certificate: certStack.certificate,
});

// DNS (hosted zone + records)
new DnsStack(app, 'DnsStack', { env, domain: 'cloudfianz.com' });
```

---

### `infra/lib/certificate-stack.ts`

```typescript
import * as cdk from 'aws-cdk-lib';
import * as acm from 'aws-cdk-lib/aws-certificatemanager';
import * as route53 from 'aws-cdk-lib/aws-route53';
import { Construct } from 'constructs';

interface CertificateStackProps extends cdk.StackProps {
  domain: string;
}

export class CertificateStack extends cdk.Stack {
  public readonly certificate: acm.Certificate;

  constructor(scope: Construct, id: string, props: CertificateStackProps) {
    super(scope, id, props);

    const hostedZone = route53.HostedZone.fromLookup(this, 'Zone', {
      domainName: props.domain,
    });

    this.certificate = new acm.Certificate(this, 'Certificate', {
      domainName: props.domain,
      subjectAlternativeNames: [`*.${props.domain}`],
      validation: acm.CertificateValidation.fromDns(hostedZone),
    });

    new cdk.CfnOutput(this, 'CertificateArn', {
      value: this.certificate.certificateArn,
      exportName: 'CloudfianzCertificateArn',
    });
  }
}
```

---

### `infra/lib/website-stack.ts`

```typescript
import * as cdk from 'aws-cdk-lib';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as cloudfront from 'aws-cdk-lib/aws-cloudfront';
import * as origins from 'aws-cdk-lib/aws-cloudfront-origins';
import * as acm from 'aws-cdk-lib/aws-certificatemanager';
import * as s3deploy from 'aws-cdk-lib/aws-s3-deployment';
import { Construct } from 'constructs';
import * as path from 'path';

interface WebsiteStackProps extends cdk.StackProps {
  environment: 'prod' | 'staging';
  domain: string;
  certificate: acm.ICertificate;
}

export class WebsiteStack extends cdk.Stack {
  public readonly distributionId: string;
  public readonly bucketName: string;

  constructor(scope: Construct, id: string, props: WebsiteStackProps) {
    super(scope, id, props);

    const isProd = props.environment === 'prod';

    // ── S3 Bucket ──────────────────────────────────────────────
    const bucket = new s3.Bucket(this, 'WebsiteBucket', {
      bucketName: `cloudfianz-${props.environment}`,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      removalPolicy: isProd ? cdk.RemovalPolicy.RETAIN : cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: !isProd,
    });

    // ── CloudFront Function (geo-router) ───────────────────────
    const geoRouterFunction = new cloudfront.Function(this, 'GeoRouter', {
      functionName: `cloudfianz-geo-router-${props.environment}`,
      code: cloudfront.FunctionCode.fromFile({
        filePath: path.join(__dirname, '../functions/geo-router.js'),
      }),
      runtime: cloudfront.FunctionRuntime.JS_2_0,
    });

    // ── Response Headers Policy (AIO + seguridad) ──────────────
    const responseHeadersPolicy = new cloudfront.ResponseHeadersPolicy(this, 'SecurityHeaders', {
      responseHeadersPolicyName: `cloudfianz-headers-${props.environment}`,
      securityHeadersBehavior: {
        strictTransportSecurity: {
          accessControlMaxAge: cdk.Duration.days(365),
          includeSubdomains: true,
          override: true,
        },
        contentTypeOptions: { override: true },
        frameOptions: {
          frameOption: cloudfront.HeadersFrameOption.DENY,
          override: true,
        },
      },
      customHeadersBehavior: {
        customHeaders: [
          // AIO: crawlers siempre ven versión fresca del HTML
          // (Cache-Control por path se maneja en cache policy)
          {
            header: 'X-Robots-Tag',
            value: isProd ? 'index, follow' : 'noindex, nofollow',
            override: true,
          },
        ],
      },
    });

    // ── Cache policies ─────────────────────────────────────────
    // HTML: sin cache (AIO necesita versión fresca)
    const htmlCachePolicy = new cloudfront.CachePolicy(this, 'HtmlCachePolicy', {
      cachePolicyName: `cloudfianz-html-${props.environment}`,
      defaultTtl: cdk.Duration.seconds(0),
      maxTtl: cdk.Duration.seconds(0),
      minTtl: cdk.Duration.seconds(0),
    });

    // Assets: cache larga
    const assetsCachePolicy = new cloudfront.CachePolicy(this, 'AssetsCachePolicy', {
      cachePolicyName: `cloudfianz-assets-${props.environment}`,
      defaultTtl: cdk.Duration.days(1),
      maxTtl: cdk.Duration.days(30),
      minTtl: cdk.Duration.seconds(0),
    });

    // ── CloudFront Distribution ────────────────────────────────
    const distribution = new cloudfront.Distribution(this, 'Distribution', {
      defaultBehavior: {
        origin: origins.S3BucketOrigin.withOriginAccessControl(bucket),
        viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
        cachePolicy: htmlCachePolicy,
        responseHeadersPolicy,
        functionAssociations: [
          {
            function: geoRouterFunction,
            eventType: cloudfront.FunctionEventType.VIEWER_REQUEST,
          },
        ],
        compress: true,
      },
      additionalBehaviors: {
        // Assets con cache larga
        'assets/*': {
          origin: origins.S3BucketOrigin.withOriginAccessControl(bucket),
          viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
          cachePolicy: assetsCachePolicy,
          compress: true,
        },
      },
      domainNames: [props.domain, ...(isProd ? [`www.${props.domain.split('.').slice(-2).join('.')}`] : [])],
      certificate: props.certificate,
      defaultRootObject: 'index.html',
      errorResponses: [
        { httpStatus: 404, responseHttpStatus: 200, responsePagePath: '/index.html' },
        { httpStatus: 403, responseHttpStatus: 200, responsePagePath: '/index.html' },
      ],
      priceClass: cloudfront.PriceClass.PRICE_CLASS_100,
      comment: `Cloudfianz ${props.environment}`,
    });

    this.distributionId = distribution.distributionId;
    this.bucketName = bucket.bucketName;

    // ── Outputs (usados por scripts de deploy) ─────────────────
    new cdk.CfnOutput(this, 'DistributionId', {
      value: distribution.distributionId,
      exportName: `CloudfianzDistributionId-${props.environment}`,
    });
    new cdk.CfnOutput(this, 'BucketName', {
      value: bucket.bucketName,
      exportName: `CloudfianzBucket-${props.environment}`,
    });
    new cdk.CfnOutput(this, 'DistributionDomain', {
      value: distribution.distributionDomainName,
      exportName: `CloudfianzDomain-${props.environment}`,
    });
  }
}
```

---

### `infra/lib/dns-stack.ts`

```typescript
import * as cdk from 'aws-cdk-lib';
import * as route53 from 'aws-cdk-lib/aws-route53';
import * as targets from 'aws-cdk-lib/aws-route53-targets';
import * as cloudfront from 'aws-cdk-lib/aws-cloudfront';
import { Construct } from 'constructs';

interface DnsStackProps extends cdk.StackProps {
  domain: string;
}

export class DnsStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props: DnsStackProps) {
    super(scope, id, props);

    const zone = new route53.HostedZone(this, 'HostedZone', {
      zoneName: props.domain,
    });

    // Importar distribuciones por output
    const prodDistributionId = cdk.Fn.importValue('CloudfianzDistributionId-prod');
    const stagingDistributionId = cdk.Fn.importValue('CloudfianzDistributionId-staging');
    const prodDomain = cdk.Fn.importValue('CloudfianzDomain-prod');
    const stagingDomain = cdk.Fn.importValue('CloudfianzDomain-staging');

    // apex → prod CloudFront
    new route53.ARecord(this, 'ApexRecord', {
      zone,
      recordName: props.domain,
      target: route53.RecordTarget.fromAlias({
        bind: () => ({
          dnsName: prodDomain,
          hostedZoneId: 'Z2FDTNDATAQYW2', // hosted zone ID fijo de CloudFront
        }),
      }),
    });

    // www → redirect a apex (via CloudFront)
    new route53.CnameRecord(this, 'WwwRecord', {
      zone,
      recordName: `www.${props.domain}`,
      domainName: prodDomain,
    });

    // staging → staging CloudFront
    new route53.CnameRecord(this, 'StagingRecord', {
      zone,
      recordName: `staging.${props.domain}`,
      domainName: stagingDomain,
    });

    // Outputs — copiar estos NS al registrador
    new cdk.CfnOutput(this, 'NameServers', {
      value: cdk.Fn.join(', ', zone.hostedZoneNameServers!),
      description: 'Copiar estos 4 nameservers al registrador del dominio',
    });
  }
}
```

---

### `infra/cdk.json`

```json
{
  "app": "npx ts-node --prefer-ts-exts bin/app.ts",
  "watch": {
    "include": ["**"],
    "exclude": ["README.md", "cdk*.json", "node_modules"]
  },
  "context": {
    "@aws-cdk/aws-s3:blockPublicPolicy": true,
    "@aws-cdk/aws-cloudfront:defaultSecurityPolicyTLSv1.2_2021": true
  }
}
```

---

### `infra/package.json`

```json
{
  "name": "cloudfianz-infra",
  "version": "1.0.0",
  "scripts": {
    "build": "tsc",
    "watch": "tsc -w",
    "synth": "cdk synth",
    "diff": "cdk diff",
    "deploy:cert": "cdk deploy CertificateStack",
    "deploy:prod": "cdk deploy WebsiteStack-prod DnsStack",
    "deploy:staging": "cdk deploy WebsiteStack-staging",
    "deploy:all": "cdk deploy --all",
    "destroy:staging": "cdk destroy WebsiteStack-staging"
  },
  "dependencies": {
    "aws-cdk-lib": "^2.140.0",
    "constructs": "^10.0.0"
  },
  "devDependencies": {
    "@types/node": "^20",
    "aws-cdk": "^2.140.0",
    "ts-node": "^10",
    "typescript": "^5"
  }
}
```

---

## 5. CloudFront Function — Geo-router

### `infra/functions/geo-router.js`

```javascript
// CloudFront Function Runtime 2.0
// Corre en cada edge point-of-presence, sub-milisegundo, sin cold start.

var LATAM = [
  'MX','CO','AR','PE','VE','CL','EC','GT','CU',
  'BO','DO','HN','PY','SV','NI','CR','PA','UY'
];

function handler(event) {
  var request = event.request;
  var cookies = request.cookies;

  // Si el usuario ya eligió idioma manualmente → respetar su elección
  if (cookies['cf_lang'] && cookies['cf_lang'].value) {
    request.headers['x-cf-lang'] = { value: cookies['cf_lang'].value };
    return request;
  }

  // Detectar país del visitante
  var country = event.viewer.country || '';
  var lang = LATAM.indexOf(country) > -1 ? 'es' : 'en';

  // Inyectar header que el JS del HTML va a leer
  request.headers['x-cf-lang'] = { value: lang };

  return request;
}
```

### Integración en el HTML (`src/index.html`)

Agregar al bloque `<script>` de inicialización, **antes** de cualquier `setLang()`:

```javascript
// Leer idioma detectado por CloudFront (via meta tag inyectado)
// o fallback a cookie del usuario, o 'en' por defecto
function getInitialLang() {
  // 1. Cookie del usuario (override manual)
  var cookieMatch = document.cookie.match(/cf_lang=([a-z]{2})/);
  if (cookieMatch) return cookieMatch[1];

  // 2. Meta tag inyectado por el servidor/build (opcional)
  var meta = document.querySelector('meta[name="cf-lang"]');
  if (meta) return meta.getAttribute('content');

  // 3. Fallback: parámetro URL (útil para testing)
  var urlLang = new URLSearchParams(window.location.search).get('lang');
  if (urlLang === 'es' || urlLang === 'en') return urlLang;

  // 4. Default
  return 'en';
}

// Al cargar la página
document.addEventListener('DOMContentLoaded', function() {
  setLang(getInitialLang());
});

// Cuando el usuario cambia idioma manualmente (en el toggle)
function handleLangToggle(lang) {
  // Guardar en cookie por 1 año
  document.cookie = 'cf_lang=' + lang + '; max-age=31536000; path=/; SameSite=Lax';
  setLang(lang);
}
```

> **Nota:** CloudFront Functions puede inyectar el header `x-cf-lang` al request pero no modifica el HTML de respuesta directamente. La estrategia recomendada es leer el parámetro `?lang=` en testing local, y en producción usar la cookie `cf_lang` que persiste entre visitas. Para inyectar el idioma al primer load sin cookie, se puede usar Lambda@Edge (mayor costo) o simplemente dejar que el JS lo infiera del `navigator.language`.

---

## 6. Scripts de deploy

### `package.json` (raíz)

```json
{
  "name": "cloudfianz",
  "version": "1.0.0",
  "scripts": {
    "dev": "bash scripts/dev.sh",
    "deploy:staging": "bash scripts/deploy.sh staging",
    "deploy:prod": "bash scripts/deploy.sh prod",
    "infra:deploy": "cd infra && npm run deploy:all"
  },
  "devDependencies": {
    "live-server": "^1.2.2"
  }
}
```

---

### `scripts/dev.sh`

```bash
#!/bin/bash
# Servidor local con live reload
# Requiere: npm install (instala live-server)

echo "🚀 Iniciando servidor local en http://localhost:3000"
echo "   Ctrl+C para detener"
echo ""

npx live-server src/ \
  --port=3000 \
  --no-browser \
  --quiet
```

---

### `scripts/deploy.sh`

```bash
#!/bin/bash
# Deploy de contenido estático a S3 + invalidar CloudFront cache
# Uso: bash scripts/deploy.sh [staging|prod]

set -e

ENV=${1:-staging}

if [ "$ENV" != "staging" ] && [ "$ENV" != "prod" ]; then
  echo "❌ Uso: bash scripts/deploy.sh [staging|prod]"
  exit 1
fi

# Obtener nombres desde CDK outputs
BUCKET=$(aws cloudformation list-exports \
  --query "Exports[?Name=='CloudfianzBucket-${ENV}'].Value" \
  --output text)

DIST_ID=$(aws cloudformation list-exports \
  --query "Exports[?Name=='CloudfianzDistributionId-${ENV}'].Value" \
  --output text)

if [ -z "$BUCKET" ] || [ -z "$DIST_ID" ]; then
  echo "❌ No se encontraron outputs de CDK para el entorno '$ENV'."
  echo "   Asegurate de haber corrido 'npm run infra:deploy' primero."
  exit 1
fi

echo "📦 Sincronizando src/ → s3://${BUCKET}"
aws s3 sync src/ s3://$BUCKET \
  --delete \
  --cache-control "no-cache" \
  --exclude "assets/*"

# Assets con cache larga
aws s3 sync src/assets/ s3://$BUCKET/assets/ \
  --delete \
  --cache-control "public, max-age=2592000, immutable"

echo "🔄 Invalidando cache de CloudFront (${DIST_ID})..."
INVALIDATION_ID=$(aws cloudfront create-invalidation \
  --distribution-id $DIST_ID \
  --paths "/*" \
  --query 'Invalidation.Id' \
  --output text)

echo "⏳ Invalidación en progreso: ${INVALIDATION_ID}"
echo "   (~30 segundos para propagar globalmente)"
echo ""

if [ "$ENV" = "prod" ]; then
  echo "✅ Deploy a producción completado"
  echo "   🌐 https://cloudfianz.com"
else
  echo "✅ Deploy a staging completado"
  echo "   🌐 https://staging.cloudfianz.com"
fi
```

---

## 7. Configurar DNS en el registrador

### Paso 1 — Obtener los nameservers de Route 53

Después del primer `cdk deploy DnsStack`, Route 53 asigna 4 nameservers al hosted zone. Obtenerlos con:

```bash
# Opción A: desde los CDK outputs (aparece al final del deploy)
# Buscar el output "NameServers" en la consola del terminal

# Opción B: via AWS CLI
ZONE_ID=$(aws route53 list-hosted-zones-by-name \
  --dns-name cloudfianz.com \
  --query "HostedZones[0].Id" \
  --output text)

aws route53 get-hosted-zone \
  --id $ZONE_ID \
  --query "DelegationSet.NameServers" \
  --output table
```

Vas a obtener 4 nameservers con esta forma:
```
ns-XXX.awsdns-XX.com
ns-XXX.awsdns-XX.net
ns-XXX.awsdns-XX.org
ns-XXX.awsdns-XX.co.uk
```

### Paso 2 — Actualizar nameservers en el registrador

1. Ingresar al panel del registrador donde se compró `cloudfianz.com`
2. Ir a la configuración del dominio (suele llamarse **"DNS"**, **"Name Servers"**, o **"Gestión DNS"**)
3. Buscar la sección **"Nameservers"** o **"Custom nameservers"**
4. Seleccionar **"Usar nameservers personalizados"** (o "Custom")
5. Reemplazar los nameservers actuales por los 4 de AWS
6. Guardar

**Nombres comunes de la opción en registradores frecuentes:**

| Registrador | Dónde encontrarlo |
|---|---|
| GoDaddy | My Products → DNS → Nameservers → Change → Custom |
| Namecheap | Domain List → Manage → Nameservers → Custom DNS |
| Cloudflare Registrar | DNS → Nameservers |
| Google Domains / Squarespace | DNS → Custom name servers |
| Name.com | My Domains → Manage → Nameservers |

### Paso 3 — Esperar propagación

- **Tiempo:** 30 minutos a 48 horas (en la práctica suele ser menos de 2 horas)
- **Verificar propagación:**

```bash
# Verificar que el dominio ya apunta a AWS
dig cloudfianz.com NS +short

# Debe mostrar los 4 nameservers de AWS (awsdns-*)
# Si todavía muestra los NS del registrador anterior → esperar más
```

### Paso 4 — Validación automática del certificado ACM

Una vez que el dominio propaga a Route 53, ACM valida el certificado automáticamente vía DNS (CDK ya creó los registros CNAME de validación en Route 53). Verificar en la consola de AWS → Certificate Manager → el certificado debe pasar a estado **"Issued"**.

```bash
# Verificar estado del certificado
aws acm list-certificates \
  --query "CertificateSummaryList[?DomainName=='cloudfianz.com']" \
  --output table
```

---

## 8. Headers AIO

Los headers críticos para que ChatGPT, Perplexity y Google AI Overviews rastreen e indexen Cloudfianz correctamente ya están configurados en `WebsiteStack`:

| Header | Valor prod | Valor staging | Propósito |
|---|---|---|---|
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` | igual | HTTPS forzado — credibilidad crawlers |
| `X-Robots-Tag` | `index, follow` | `noindex, nofollow` | Evitar que staging se indexe |
| `X-Content-Type-Options` | `nosniff` | igual | Seguridad estándar |
| `Cache-Control` (HTML) | `no-cache` | `no-cache` | Crawlers AIO siempre ven versión fresca |
| `Cache-Control` (assets) | `public, max-age=2592000` | igual | Performance — no afecta indexing |

### Checklist AIO adicional (en el HTML)

Verificar que `src/index.html` incluye:

```html
<head>
  <!-- Hreflang: señal de idioma para crawlers -->
  <link rel="alternate" hreflang="en" href="https://cloudfianz.com/?lang=en" />
  <link rel="alternate" hreflang="es" href="https://cloudfianz.com/?lang=es" />
  <link rel="alternate" hreflang="x-default" href="https://cloudfianz.com/" />

  <!-- JSON-LD: Organization schema (3x citation lift en AI Overviews) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Cloudfianz",
    "url": "https://cloudfianz.com",
    "description": "Custom software development, AWS serverless architecture and HubSpot integrations. Backed by Digifianz.",
    "parentOrganization": {
      "@type": "Organization",
      "name": "Digifianz",
      "url": "https://digifianz.com"
    },
    "areaServed": ["US", "Europe", "LATAM"],
    "knowsLanguage": ["en", "es"]
  }
  </script>

  <!-- JSON-LD: FAQPage (insertar el bloque FAQ del sitio aquí) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Cloudfianz?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Cloudfianz is a custom software and cloud engineering firm backed by Digifianz, specializing in custom SaaS development, AWS serverless architecture, and HubSpot integrations."
        }
      }
    ]
  }
  </script>
</head>
```

### `src/robots.txt`

```
User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: https://cloudfianz.com/sitemap.xml
```

### `src/sitemap.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://cloudfianz.com/</loc>
    <lastmod>2026-08-18</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
    <xhtml:link rel="alternate" hreflang="en" href="https://cloudfianz.com/?lang=en"/>
    <xhtml:link rel="alternate" hreflang="es" href="https://cloudfianz.com/?lang=es"/>
  </url>
</urlset>
```

---

## 9. Referencia de comandos

### Desarrollo

```bash
npm run dev                    # Servidor local http://localhost:3000
```

### Deploy de contenido

```bash
npm run deploy:staging         # src/ → staging + invalidar CF cache
npm run deploy:prod            # src/ → prod + invalidar CF cache
```

### Infra CDK (solo cuando cambia infra)

```bash
cd infra
cdk diff                       # Ver qué va a cambiar antes de deployar
cdk deploy CertificateStack    # Solo certificado
cdk deploy WebsiteStack-prod   # Solo prod
cdk deploy WebsiteStack-staging # Solo staging
cdk deploy DnsStack            # Solo DNS
cdk deploy --all               # Todo
```

### Utilidades

```bash
# Ver outputs del stack (bucket names, distribution IDs)
aws cloudformation list-exports --output table

# Invalidar CF cache manualmente
aws cloudfront create-invalidation \
  --distribution-id DIST_ID \
  --paths "/*"

# Ver NS del hosted zone
aws route53 list-hosted-zones-by-name \
  --dns-name cloudfianz.com \
  --query "HostedZones[0].Id" --output text | \
  xargs -I{} aws route53 get-hosted-zone \
  --id {} --query "DelegationSet.NameServers"

# Verificar certificado
aws acm list-certificates \
  --query "CertificateSummaryList[?DomainName=='cloudfianz.com']" \
  --output table

# Verificar propagación DNS
dig cloudfianz.com NS +short
dig staging.cloudfianz.com +short
```

---

*Cloudfianz — backed by Digifianz · cloudfianz.com*
