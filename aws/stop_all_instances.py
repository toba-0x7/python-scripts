# Create a script that will stop all running instances

import boto3

region = 'us-east-1' # Insert the region of the instances
ec2 = boto3.client('ec2', region_name=region)
instance_attr = ec2.describe_instances() #Lists mulitple dictionaries of instance information

data = instance_attr["Reservations"] #Call the reservations key

instance_list = [] #Create an emppty list

for instances in data:
    instance = instances["Instances"] #Call the Instances key
    for ids in instance:
        instance_id = ids["InstanceId"] #Iterate through the instances' instance ids
        instance_list.append(instance_id) #Add the instance_id iterations to the empty list
      
ec2.stop_instances(InstanceIds=instance_list) # Stop the instances found in instance_list


    