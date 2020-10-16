#!/usr/bin/env python3

from aws_cdk import core

from init_app.init_app_stack import InitAppStack

env=core.Environment(account="164549288284", region="us-east-1")


app = core.App()
InitAppStack(app, "init-app", env=env)

app.synth()
