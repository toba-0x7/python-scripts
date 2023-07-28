import boto3

s3_resource = boto3.client("s3")
print(s3_resource)

# To bring name of bucket at index 0
print(s3_resource.list_buckets()["Buckets"][0]["Name"])

# To print creation date of bucket at index 0
creation_date = s3_resource.list_buckets()["Buckets"][0]["CreationDate"]
print(creation_date)

# print(creation_date.strftime("%d%m%y_%H:%M:s"))

# print name and creation date
for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])