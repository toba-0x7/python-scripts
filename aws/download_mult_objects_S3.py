import boto3
import os

s3_resource = boto3.client("s3")
cwd = os.getcwd()
cwd = cwd +"/download/" ***

files = s3_resource.list_objects(Bucket = "test-bucket-198538723")["Contents"]

for file in files:
    s3_resource.download_file(Bucket = "test-bucket-198538723", Key = file["Key"], Filename = cwd + file["Key"])