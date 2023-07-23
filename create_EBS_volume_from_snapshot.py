# CREATE A SNAPSHOT OF AN EXISTING VOLUME
# import boto3
# ec2 = boto3.client("ec2")
# ec2 = create_snapshot(Description = "Enter description", VolumeID = "id of existing volume")

# CREATE A VOLUME FROM A SNAPSHOT
# import boto3
# ec2 = boto3.client("ec2")
# ec2.create_volume(AvailabilityZone = "us=east-2", Encrypted = True, Size = 12, SnapshotId = "<enter snapshot id>", VolumeType = "gp2")

# DELETE EBS VOLUME
# import boto3
# ec2 = boto3.client("ec2")
# ec2 = delete_snapshot(SnapshotId = "<enter id of snapshot you want to delete>")

# DESCRIBE EBS VOLUME
# import boto3
# ec2 = boto3.client("ec2")
# ec2 = describe_snapshots(SnapshotIds = "<enter id of snapshot you want to describe>")

