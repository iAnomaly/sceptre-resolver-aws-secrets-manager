# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='sceptre-resolver-aws-secrets-manager',
    version="1.0.0",
    py_modules=['aws_secrets_manager'],
    entry_points={
        'sceptre.resolvers': [
            'aws_secrets_manager = aws_secrets_manager:AwsSecretsManager',
        ],
    }
)
