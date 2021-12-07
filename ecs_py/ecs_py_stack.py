from aws_cdk import core 
import aws_cdk.aws_ecs as ecs
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_iam as iam

import os.path

class EcsPyStack(core.Stack):


    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        dirname = os.path.dirname(__file__)

        input_bucket = s3.Bucket(self, "test-input-bucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            versioned=True
        )
        output_bucket = s3.Bucket(self, "test-ouput-bucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            versioned=True
        )

        print('input_bucket:', input_bucket)

        cluster = ecs.Cluster(self, "ML-Deomo-Cluster",
        )


        task_definition = ecs.FargateTaskDefinition(self, "ML-Deomo",
            memory_limit_mib=1024,
            cpu=512,
        )
        task_definition.add_to_task_role_policy(iam.PolicyStatement(
                    actions=["*"],
                    # principals=[iam.AnyPrincipal()],
                    resources=[input_bucket.bucket_arn, output_bucket.bucket_arn]
                )
        )

        task_definition.add_to_execution_role_policy(iam.PolicyStatement(
                    actions=["*"],
                    # principals=[iam.AnyPrincipal()],
                    resources=[input_bucket.bucket_arn, output_bucket.bucket_arn]
                )
        )
        
        
        task_definition.add_container("container01",
            image=ecs.ContainerImage.from_asset(
                os.path.join(dirname, "..", "docker")),
                )
        
