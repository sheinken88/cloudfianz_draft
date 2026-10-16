#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { CertificateStack } from '../lib/certificate-stack';
import { DnsRecordsStack } from '../lib/dns-records-stack';
import { DnsStack } from '../lib/dns-stack';
import { WebsiteStack } from '../lib/website-stack';

const app = new cdk.App();

const DOMAIN = 'cloudfianz.com';

const env = {
  account: process.env.CDK_DEFAULT_ACCOUNT,
  region: process.env.CDK_DEFAULT_REGION ?? 'us-east-1',
};

const usEast1 = {
  account: process.env.CDK_DEFAULT_ACCOUNT,
  region: 'us-east-1',
};

// 1. Hosted zone (copiar NS al registrador)
const dnsStack = new DnsStack(app, 'DnsStack', {
  env,
  domain: DOMAIN,
});

// 2. Certificado ACM (us-east-1, requerido por CloudFront)
const certStack = new CertificateStack(app, 'CertificateStack', {
  env: usEast1,
  domain: DOMAIN,
  hostedZone: dnsStack.hostedZone,
});
certStack.addDependency(dnsStack);

const stagingOnly = app.node.tryGetContext('stagingOnly') !== 'false';

// 3. Sitios S3 + CloudFront
let prodStack: WebsiteStack | undefined;
if (!stagingOnly) {
  prodStack = new WebsiteStack(app, 'WebsiteStack-prod', {
    env,
    environment: 'prod',
    domain: DOMAIN,
    certificate: certStack.certificate,
  });
  prodStack.addDependency(certStack);
}

const stagingStack = new WebsiteStack(app, 'WebsiteStack-staging', {
  env,
  environment: 'staging',
  domain: `staging.${DOMAIN}`,
  certificate: certStack.certificate,
});
stagingStack.addDependency(certStack);

// 4. Registros DNS → CloudFront
const recordsStack = new DnsRecordsStack(app, 'DnsRecordsStack', {
  env,
  domain: DOMAIN,
  hostedZone: dnsStack.hostedZone,
  prodDistribution: prodStack?.distribution,
  stagingDistribution: stagingStack.distribution,
});
recordsStack.addDependency(dnsStack);
recordsStack.addDependency(stagingStack);
if (prodStack) {
  recordsStack.addDependency(prodStack);
}

app.synth();
