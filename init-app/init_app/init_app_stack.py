import aws_cdk.aws_s3 as _s3
from aws_cdk import core

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
