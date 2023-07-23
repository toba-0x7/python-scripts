# Documentation: https://catalog.us-east-1.prod.workshops.aws/workshops/3d705026-9edc-40e8-b353-bdabb116c89c/en-US/persisting-data/dynamodb/step-5
# Delete an existing table

import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

table = dynamodb.Table('Movies')

table.delete()
