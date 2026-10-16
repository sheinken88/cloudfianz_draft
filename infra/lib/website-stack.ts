import * as cdk from 'aws-cdk-lib';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as cloudfront from 'aws-cdk-lib/aws-cloudfront';
import * as origins from 'aws-cdk-lib/aws-cloudfront-origins';
import * as acm from 'aws-cdk-lib/aws-certificatemanager';
import { Construct } from 'constructs';
import * as path from 'path';

interface WebsiteStackProps extends cdk.StackProps {
  environment: 'prod' | 'staging';
  domain: string;
  certificate: acm.ICertificate;
}

export class WebsiteStack extends cdk.Stack {
  public readonly distribution: cloudfront.Distribution;

  constructor(scope: Construct, id: string, props: WebsiteStackProps) {
    super(scope, id, props);

    const isProd = props.environment === 'prod';

    const bucket = new s3.Bucket(this, 'WebsiteBucket', {
      bucketName: `cloudfianz-${props.environment}-${cdk.Aws.ACCOUNT_ID}`,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      removalPolicy: isProd ? cdk.RemovalPolicy.RETAIN : cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: !isProd,
      encryption: s3.BucketEncryption.S3_MANAGED,
    });

    const geoRouterFunction = new cloudfront.Function(this, 'GeoRouter', {
      functionName: `cloudfianz-geo-router-${props.environment}`,
      code: cloudfront.FunctionCode.fromFile({
        filePath: path.join(__dirname, '../functions/geo-router.js'),
      }),
      runtime: cloudfront.FunctionRuntime.JS_2_0,
    });

    const responseHeadersPolicy = new cloudfront.ResponseHeadersPolicy(
      this,
      'SecurityHeaders',
      {
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
            {
              header: 'X-Robots-Tag',
              value: isProd ? 'index, follow' : 'noindex, nofollow',
              override: true,
            },
          ],
        },
      },
    );

    const htmlCachePolicy = new cloudfront.CachePolicy(this, 'HtmlCachePolicy', {
      cachePolicyName: `cloudfianz-html-${props.environment}-${cdk.Aws.ACCOUNT_ID}`,
      defaultTtl: cdk.Duration.seconds(0),
      maxTtl: cdk.Duration.seconds(0),
      minTtl: cdk.Duration.seconds(0),
    });

    const assetsCachePolicy = new cloudfront.CachePolicy(this, 'AssetsCachePolicy', {
      cachePolicyName: `cloudfianz-assets-${props.environment}-${cdk.Aws.ACCOUNT_ID}`,
      defaultTtl: cdk.Duration.days(1),
      maxTtl: cdk.Duration.days(30),
      minTtl: cdk.Duration.seconds(0),
    });

    this.distribution = new cloudfront.Distribution(this, 'Distribution', {
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
        'assets/*': {
          origin: origins.S3BucketOrigin.withOriginAccessControl(bucket),
          viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
          cachePolicy: assetsCachePolicy,
          compress: true,
        },
      },
      domainNames: isProd
        ? [props.domain, `www.${props.domain}`]
        : [props.domain],
      certificate: props.certificate,
      defaultRootObject: 'index.html',
      errorResponses: [
        { httpStatus: 404, responseHttpStatus: 200, responsePagePath: '/index.html' },
        { httpStatus: 403, responseHttpStatus: 200, responsePagePath: '/index.html' },
      ],
      priceClass: cloudfront.PriceClass.PRICE_CLASS_100,
      comment: `Cloudfianz ${props.environment}`,
    });

    new cdk.CfnOutput(this, 'DistributionId', {
      value: this.distribution.distributionId,
      exportName: `CloudfianzDistributionId-${props.environment}`,
    });

    new cdk.CfnOutput(this, 'BucketName', {
      value: bucket.bucketName,
      exportName: `CloudfianzBucket-${props.environment}`,
    });

    new cdk.CfnOutput(this, 'DistributionDomain', {
      value: this.distribution.distributionDomainName,
      exportName: `CloudfianzDomain-${props.environment}`,
    });
  }
}
