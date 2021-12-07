from aws_cdk import (
        core,
        assertions
    )

from ecs_py.ecs_py_stack import EcsPyStack


def test_sqs_queue_created():
    app = core.App()
    stack = EcsPyStack(app, "ecs-py")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = EcsPyStack(app, "ecs-py")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
