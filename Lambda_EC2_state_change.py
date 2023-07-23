import boto3
import json

client = boto3.client("ec2")

def lambda_handler(event, context):
  ec2_instance_id = event['detail']['instance-id']
  response = client.describe_tags(
    Filters=[
        {
            'Name': 'resource-id',
            'Values': [ec2_instance_id]
        }
    ]
)
  print(response)


