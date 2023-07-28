# CODE WORKS
# Delete VPC based on VPC Id

import boto3

client = boto3.client("ec2")

response = client.delete_vpc(VpcId = "vpc-021cfc5f102183b56") # Sub VpcId with specific VPC you want to delete
