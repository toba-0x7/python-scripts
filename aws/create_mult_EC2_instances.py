import boto3

ec2_resource = boto3.resource("ec2")

ec2_resource.create_instances(ImageId = "ami-0cc87e5027adcdca8", InstanceType = "t2.micro", MaxCount = 3, MinCount = 2)
# Sub ami id for the id of an ami in your Region 
