#!/usr/bin/env python3.7
# Create a script that will stop running instances

import boto3
region = 'us-east-1' # Insert the region of the instances
instances = ['i-0e65067ca437333c6', 'i-0c9b6b48aad6ff695', 'i-04381eba18b8755f3'] # Insert instance ids
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print("Stopped the following instances: " + str(instances))
