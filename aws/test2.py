# Create a script that will stop instances with certain tags

import boto3

region = 'us-east-1' # Insert the region of the instances
ec2 = boto3.client('ec2', region_name=region)
tag = {'Key':'Environment', 'Value':'Dev'}
instance_attr = ec2.describe_instances() #Lists mulitple dictionaries of instance information

data = instance_attr["Reservations"] #Call the reservations key

instance_list = [] #Create an emppty list

for instances in data:
    instance = instances["Instances"] #Call the Instances key
    for ids in instance:
        instance_id = ids["InstanceId"]
        instance_state = ids["State"]["Name"]
        instance_tags = ids["Tags"]
        if (tag in ids['Tags'] and 'running' in ids['State']['Name']):
            print(ids['InstanceId'])
            ec2.stop_instances(InstanceIds=[ids['InstanceId']])
            print("The following instance has stopped: " + instance_id)