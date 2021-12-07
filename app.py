#!/usr/bin/env python3

from aws_cdk import core

from ecs_py.ecs_py_stack import EcsPyStack


app = core.App()
EcsPyStack(app, "ecs-py")

app.synth()
