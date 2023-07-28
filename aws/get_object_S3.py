# CODE WORKS
# Download object from S3 bucket

import boto3

s3_resource = boto3.client("s3")

# Sub actual bucket name and Key name of object; Filename = name of new file created when you download from bucket
s3_resource.download_file(Bucket = "test-bucket-198538723", Key = "uploadtest1.png", Filename = "downloadtest1.png")