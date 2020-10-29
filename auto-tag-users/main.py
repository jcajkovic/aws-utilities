import boto3
import toml
from botocore.exceptions import ClientError

config = toml.load('/app/config.toml')

sts_client = boto3.client(
    'sts', aws_access_key_id=config['aws']['aws_access_key_id'],
    aws_secret_access_key=config['aws']['aws_secret_access_key'],
    region_name=config['aws']['region']
)

def assume_role(account_number):
    # Call the assume_role method of the STSConnection object and pass the role
    # ARN and a role session name.
    aws_resource_clients = {}

    # mfa_TOTP = raw_input("Enter the MFA code: ")

    assumedRoleObject = sts_client.assume_role(
        RoleArn="arn:aws:iam::"+account_number+":role/Inventory",
        RoleSessionName="AssumeRoleOperatorSession",
        # SerialNumber=mfa_device_id,
        # TokenCode=mfa_TOTP
    )

    # From the response that contains the assumed role, get the temporary
    # credentials that can be used to make subsequent API calls
    credentials = assumedRoleObject['Credentials']

    iam_client = boto3.client(
        'iam', aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken'],
        region_name='eu-west-1'
    )

    aws_resource_clients = {'iam': iam_client}

    return aws_resource_clients


def tag_iam_accounts(iam_client):

  emaildomain = config['email']['domain']

  users = iam_client.list_users()

  for user in users['Users']:
    print('Tagging user: ' + user['UserName'] + ' with email: ' + user['UserName'] + emaildomain)
    iam_client.tag_user(
      UserName=user['UserName'],
      Tags=[{
        'Key': 'email',
        'Value': user['UserName'] + emaildomain
      }]
    )

for account in config['accounts']['accounts_list']:
  aws_clients = assume_role(account)
  tag_iam_accounts(aws_clients['iam'])
