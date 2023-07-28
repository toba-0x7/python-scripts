
# List S3 buckets
# import boto3 as AWS can be used as alias
import boto3

s3 = boto3.client('s3') # .client (you can use .client or .resource but function calls are different bw the two)

response = s3.list_buckets() # response typically comes back as a dictioanry or JSON obkect

buckets = response["Buckets"]

for bucket in buckets:
    print(bucket["Name"])
    