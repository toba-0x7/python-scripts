# Documentation: https://catalog.us-east-1.prod.workshops.aws/workshops/3d705026-9edc-40e8-b353-bdabb116c89c/en-US/persisting-data/dynamodb/step-4
# How to scan a table (reads EVERY item in the entire table and returns ALL the data in the table)
# Can provide an optional fiter_expression so that only the items matching your criteria are returned
# Filter is applied only after the ENTIRE table has been scanned
# Scan Movies table (contains 5,000 items) with filter to retrieve only movies from the 1950s

import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-2') # Adjust region

table = dynamodb.Table('Movies')

fe = Key('year').between(1950, 1959)
pe = "#yr, title, info.rating"
# Expression Attribute Names for Projection Expression only.
ean = { "#yr": "year", }
esk = None


response = table.scan(
    FilterExpression=fe,
    ProjectionExpression=pe, # Specifies the attributes you want in the scan result
    ExpressionAttributeNames=ean
    )

for i in response['Items']:
    print(json.dumps(i, cls=DecimalEncoder))

while 'LastEvaluatedKey' in response:
    response = table.scan(
        ProjectionExpression=pe,
        FilterExpression=fe, # specifies a condition that returns only items that satisfy the condition
        ExpressionAttributeNames= ean,
        ExclusiveStartKey=response['LastEvaluatedKey']
        )

    for i in response['Items']:
        print(json.dumps(i, cls=DecimalEncoder))

