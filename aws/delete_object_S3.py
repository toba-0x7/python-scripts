# CODE WORKS
# Delete single object from S3 bucket

import boto3

s3_resource = boto3.client("s3")

s3_resource.delete_object(Bucket = "test-bucket-198538723", Key = "uploadtest2.png") # Sub specific bucket and file names
