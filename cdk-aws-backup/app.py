#!/usr/bin/env python3

import sys
from aws_cdk import core
from cdk_aws_backup.cdk_aws_backup_stack import CdkAwsBackupStack


app = core.App()
core_env = core.Environment(region='eu-west-1')
CdkAwsBackupStack(app, "CdkAwsBackupStack", env=core_env)
app.synth()
