# [Sceptre](https://github.com/cloudreach/sceptre) [Resolver](https://sceptre.cloudreach.com/latest/docs/resolvers.html) for [AWS SecretsManager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/)

While AWS CloudFormation templates support the native [dynamic references](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html) `{{resolve:service-name:reference-key}}` construct, it only supports a small list of resources notably excluding ones such as `CloudFormation::Init` and `UserData`. This resolver bridges that gap.

Please be sure to implement the best practice of adding `NoEcho: true` on any template parameter containing secrets if you are not already. This prevents exposing the value in the console, CLI, etc.

## Installation
```sh
pip install --user https://github.com/iAnomaly/sceptre-resolver-aws-secrets-manager/archive/v1.0.0.tar.gz
```

## Usage
### Syntax
```yaml
parameters/sceptre_user_data:
  <name>: !aws_secrets_manager <secret_arn|secret_id>::<SecretBinary|SecretString>::<json_key>
```
### Example
```yaml
parameters:
  MasterUserPassword: !aws_secrets_manager mysql::SecretString::password
  MasterUsername: !aws_secrets_manager mysql::SecretString::username
```
