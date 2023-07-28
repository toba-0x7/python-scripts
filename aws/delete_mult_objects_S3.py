import boto3
import os

s3_resource = boto3.client("s3")
objects = s3_resource.list_objects(Bucket = "test-bucket-198538723")["Contents"]

for object in objects:
    response = s3_resource.delete_object(Bucket = "test-bucket-198538723", Key = object["Key"])
    