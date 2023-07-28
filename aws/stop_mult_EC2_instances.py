# THIS CODE IS NOT FINISHED
import boto3

ec2 = boto3.client("ec2")

x = ec2.describe_instances()

data = x["Reservations"]

data_list = []

DONT STOP YOUR CLOUD9 INSTANCE

for instances in data:
    instance = instances["Instances"]
    for ids in instance:
        instance_id = ids["InstanceId"]
        data_list.append(instance_id)

ec2.stop_instances(InstanceIds = data_list)
        
