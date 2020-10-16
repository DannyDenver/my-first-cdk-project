import aws_cdk.aws_s3 as _s3
from aws_cdk import core
import aws_cdk.aws_iam as _iam

class InitAppStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        _s3.Bucket(
            self, 
            "myBucketID", 
            bucket_name="myfirstcdkprojectbucket32",
            versioned=False,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access= _s3.BlockPublicAccess.BLOCK_ALL
        )

        mybucket = _s3.Bucket(
            self,
            "myBucketId1"
        )

        _iam.Group(self, "gid")

        output1 = core.CfnOutput(self, "myBucketOutput1", value=mybucket.bucket_name,
        description="My first cdk bucket", export_name="myBucketOutput1")
