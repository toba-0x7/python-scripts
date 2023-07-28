# CODE WORKS
import boto3

s3_resource = boto3.client("s3")

# Upload single file to S3 bucket
s3_resource.upload_file(
    Filename = "README.md", # Existing file in your CWD that you want to upload 
    Bucket = "test-bucket-198538723", # Name of bucket to upload to
    Key = "uploadtest1.png") # This will be the new name of the file in the bucket
    