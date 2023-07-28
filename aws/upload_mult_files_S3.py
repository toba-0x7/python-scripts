#CODE DOES NOT WORK
import boto3

s3_resource = boto3.client("s3")

# Upload multiple files to S3 bucket
s3_resource.upload_file(
    Filename = "README.md", # Existing file in your CWD that you want to upload 
    Bucket = "test-bucket-198538723", # Name of bucket to upload to
    Key = "uploadtest2.png") # This will be the new name of the file in the bucket

import os
import glob

cwd = os.getcwd() # Gets current working directory

# cwd = cwd # Goes to directory in CWD; replace "/upload/" with the extension where your files are located
files = glob.glob(cwd + "*.json")
print(files)

for files in files:
    s3_resource = boto3.client("s3")
    s3_resource.upload_file(
    Filename = file,
    Bucket = "test-bucket-198538723"
    Key = file.split("/")[-1])


