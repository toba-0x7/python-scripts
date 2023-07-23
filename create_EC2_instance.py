import boto3

ec2_resource = boto3.resource("ec2")

ec2_resource.create_instances(ImageId = "ami-0cc87e5027adcdca8", InstanceType = "t2.micro", MaxCount = 1, MinCount = 1)
# Sub ami id for the id of an ami in your Region 
