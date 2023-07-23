# CODE WORKS
# Print # of VPCs and VPC Ids

import boto3

client = boto3.client("ec2")

x = client.describe_vpcs()

num_vpcs = x["Vpcs"]

print(len(num_vpcs))

for vpc in num_vpcs:
    print(vpc["VpcId"])
    
