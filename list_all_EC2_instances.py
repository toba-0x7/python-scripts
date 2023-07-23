import boto3

ec2 = boto3.client("ec2")

x = ec2.describe_instances()

data = x["Reservations"]
data_instance = data["Instances"]

for i in range(len(data_instance)):
    print(f"Instance Id is {data_instance[i]['InstanceId']}")