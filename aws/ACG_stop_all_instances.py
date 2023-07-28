# Import the boto3 library, which allows interaction with AWS services.
import boto3

# The lambda_handler function is the entry point for the AWS Lambda function.
# It takes two arguments: 'event' and 'context'.
def lambda_handler(event, context):
    # Get a list of all AWS regions using the EC2 client.
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    
    # Iterate over each region.
    for region in regions:
        # Create an EC2 resource object for the specific region.
        ec2 = boto3.resource('ec2', region_name=region)
        print("Region: ", region)
        
        # Get only the running EC2 instances in the current region.
        instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        
        # Stop the running instances in the current region.
        for instance in instances:
            instance.stop()
            print("Stopped instance: ", instance.id)
