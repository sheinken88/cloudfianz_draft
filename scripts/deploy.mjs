#!/usr/bin/env node
import { execSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const env = process.argv[2] ?? 'staging';

if (env !== 'staging' && env !== 'prod') {
  console.error('Uso: node scripts/deploy.mjs [staging|prod]');
  process.exit(1);
}

function aws(query) {
  return execSync(
    `aws cloudformation list-exports --query "${query}" --output text`,
    { encoding: 'utf8' },
  ).trim();
}

const bucket = aws(`Exports[?Name=='CloudfianzBucket-${env}'].Value`);
const distId = aws(`Exports[?Name=='CloudfianzDistributionId-${env}'].Value`);

if (!bucket || !distId) {
  console.error(`No se encontraron exports de CDK para '${env}'.`);
  console.error("Corré primero: npm run infra:deploy");
  process.exit(1);
}

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const src = path.join(root, 'src');

console.log('Build de casos de éxito...');
execSync('node scripts/build-cases.mjs', { stdio: 'inherit', cwd: root });

console.log(`Sincronizando src/ → s3://${bucket}`);
execSync(
  `aws s3 sync "${src}" s3://${bucket} --delete --cache-control "no-cache" --exclude "assets/*" --exclude "data/*"`,
  { stdio: 'inherit', cwd: root },
);

const assets = path.join(src, 'assets');
try {
  execSync(
    `aws s3 sync "${assets}" s3://${bucket}/assets/ --delete --cache-control "public, max-age=2592000, immutable"`,
    { stdio: 'inherit', cwd: root },
  );
} catch {
  // assets/ puede estar vacío al inicio
}

console.log(`Invalidando cache CloudFront (${distId})...`);
const invalidationId = execSync(
  `aws cloudfront create-invalidation --distribution-id ${distId} --paths "/*" --query Invalidation.Id --output text`,
  { encoding: 'utf8' },
).trim();

console.log(`Invalidación: ${invalidationId} (~30s)`);
console.log(env === 'prod'
  ? 'Deploy prod → https://cloudfianz.com'
  : 'Deploy staging → https://staging.cloudfianz.com');
