#!/usr/bin/env python3.7
# Create a script that will stop running instances

import boto3
region = 'us-east-1' # Insert the region of the instances
tag = { "Key":"Environment", "Value":"Dev"} # Identify the tags you want to sort by in a dictionary

ec2 = boto3.client('ec2', region_name=region)

list_instances = ec2.describe_instances()


def lambda_handler(event, context):
    for instance in list_instances:
        print("hello")
        # if (tag in instance['Tags'] and 'stopped' in instance['State']['Name']):
            #ec2.start_instances(InstanceIds=[instance['InstanceId']])
            
            

