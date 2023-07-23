# Documentation: https://catalog.us-east-1.prod.workshops.aws/workshops/3d705026-9edc-40e8-b353-bdabb116c89c/en-US/persisting-data/dynamodb/step-1
# year - partition key (AttributeType N for number)
# title - sort key (AttributeType S for string)

import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

table = dynamodb.create_table(
    TableName='Movies', # Specify the table name
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year', 
            'AttributeType': 'N' # Specify data type as number
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S' # Specify data type as string
        },

    ],
    ProvisionedThroughput={ # This is required
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
