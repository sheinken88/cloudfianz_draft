import * as cdk from 'aws-cdk-lib';
import * as route53 from 'aws-cdk-lib/aws-route53';
import * as targets from 'aws-cdk-lib/aws-route53-targets';
import * as cloudfront from 'aws-cdk-lib/aws-cloudfront';
import { Construct } from 'constructs';

interface DnsRecordsStackProps extends cdk.StackProps {
  domain: string;
  hostedZone: route53.IHostedZone;
  stagingDistribution: cloudfront.IDistribution;
  prodDistribution?: cloudfront.IDistribution;
}

export class DnsRecordsStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props: DnsRecordsStackProps) {
    super(scope, id, props);

    const { domain, hostedZone, prodDistribution, stagingDistribution } = props;

    if (prodDistribution) {
      new route53.ARecord(this, 'ApexRecord', {
        zone: hostedZone,
        target: route53.RecordTarget.fromAlias(
          new targets.CloudFrontTarget(prodDistribution),
        ),
      });

      new route53.ARecord(this, 'WwwRecord', {
        zone: hostedZone,
        recordName: `www.${domain}`,
        target: route53.RecordTarget.fromAlias(
          new targets.CloudFrontTarget(prodDistribution),
        ),
      });
    }

    new route53.ARecord(this, 'StagingRecord', {
      zone: hostedZone,
      recordName: `staging.${domain}`,
      target: route53.RecordTarget.fromAlias(
        new targets.CloudFrontTarget(stagingDistribution),
      ),
    });
  }
}
