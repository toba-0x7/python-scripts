# Import the boto3 library, which allows interaction with AWS services.
import boto3

# Create an instance of the S3 resource using boto3.
s3 = boto3.resource('s3')

# Loop through all the S3 buckets available using the 'all()' method of the S3 resource.
# This will retrieve a list of all S3 buckets associated with the AWS account.
for bucket in s3.buckets.all():
    # Print the name of each S3 bucket.
    print(bucket.name)
