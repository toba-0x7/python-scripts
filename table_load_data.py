# Documentation: https://catalog.us-east-1.prod.workshops.aws/workshops/3d705026-9edc-40e8-b353-bdabb116c89c/en-US/persisting-data/dynamodb/step-2
# This loads data from a zip file that was downloaded from the AWS documentation above

import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

table = dynamodb.Table('Movies')

with open("moviedata.json") as json_file:
    movies = json.load(json_file, parse_float = decimal.Decimal)
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']

        print("Adding movie:", year, title)

        table.put_item(
           Item={
               'year': year,
               'title': title,
               'info': info,
            }
        )
