import boto3

resource = boto3.resource("s3")

# To use len, create variable of bucket list, then call len on it
bucket_list = list(resource.buckets.all())
print(len(bucket_list))

# To list out all of the buckets
for bucket in resource.buckets.all():
    print(bucket.name)
    

 
    
