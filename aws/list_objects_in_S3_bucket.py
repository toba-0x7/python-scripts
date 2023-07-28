# CODE WORKS

import boto3
s3_resource = boto3.client("s3")
objects = s3_resource.list_objects(Bucket="test-bucket-198538723")["Contents"] # Change bucket variable to bucket you want to access

print(len(objects)) # Gives you the number of objects in the bucket

for object in objects:
    print(object["Key"]) # Prints the Key (Name) of the object
    
    