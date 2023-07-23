# Create S3 bucket using AWS CLI

import boto3

aws_resource = boto3.resource("s3")

# Name the bucket uniquely, no spaces
bucket = aws_resource.Bucket("test-bucket-1985387234")

response = bucket.create(
    ACL='public-read', #for private bucket, change 'public-read' to 'private'
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
    
)

print(response)

# CLI command to run: python3.7 <file_name>