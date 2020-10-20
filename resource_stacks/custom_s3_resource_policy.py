from aws_cdk import core
from aws_cdk import aws_s3 as _s3
from aws_cdk import aws_iam as _iam


class CustomS3ResourcePolicyStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, ** kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 Bucket):
        konstone_bkt = _s3.Bucket(self,
                                  "konstoneAssets",
                                  versioned=True,
                                  # doesnt work if there is content in bucket, manual delete necessary
                                  removal_policy=core.RemovalPolicy.DESTROY 
                                  )

        # Add Bucket Resource policy
        konstone_bkt.add_to_resource_policy(
            _iam.PolicyStatement(
                effect=_iam.Effect.ALLOW,
                actions=["s3:GetObject"],
                # give public access only to html files
                resources=[konstone_bkt.arn_for_objects("*.html")],
                # anyone can access
                principals=[_iam.AnyPrincipal()]
            )
        )

        konstone_bkt.add_to_resource_policy(
            _iam.PolicyStatement(
                effect=_iam.Effect.DENY,
                actions=["s3:*"],
                # any objects in the bucket
                resources=[f"{konstone_bkt.bucket_arn}/*"],
                principals=[_iam.AnyPrincipal()],
                # if secure transport is false deny access
                conditions={
                    "Bool": {"aws:SecureTransport": False}
                }
            )
        )
