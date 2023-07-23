# Create a script that will stop instances with certain tags

import boto3

ec2 = boto3.client('ec2', region_name='us-east-1') # Insert the region of the instances

# Function takes an instance and returns True if Dev, otherwise False
def is_dev(instance):
    tag = {'Key':'Environment', 'Value':'Dev'}
    is_dev = False
    if tag in instance['Tags']:
        is_dev = True
    return is_dev

# Function takes an instance and returns True if running, otherwise False
def is_running(instance):
    is_running = False
    if instance['State']['Name'] == 'running':
        is_running = True
    return is_running

instance_attr = ec2.describe_instances() # Lists mulitple dictionaries of instance information

reservations = instance_attr['Reservations'] # Accessing Reservation values

for reservation in reservations: # Iterating through Reservation values
    for instance in reservation['Instances']: # Looking for Instances through the iterations
        if (is_dev(instance) and is_running(instance)): # If Dev present (see function) and instance running
            instance_id = instance['InstanceId'] # Defining instance ID variable
            ec2.stop_instances(InstanceIds=[instance_id]) # Stop instance ids who is_dev=True and is_running=True
            print("The following instance has stopped: " + instance_id) # Print instances that were stopped
            
