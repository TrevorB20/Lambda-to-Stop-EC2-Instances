import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

def create_instances():
    # Create 3 new EC2 instances
    instances = ec2.run_instances(
        ImageId='ami-06b21ccaeff8cd686', # Replace the ami ID with your own 
        InstanceType='t2.micro',   # We leave instance type as it is in the free tier
        MinCount=3,
        MaxCount=3,
        KeyName='Ec2-Lambda',  # Replace with your key pair name
        SecurityGroupIds=['sg-0ecc07d16d83bbd95'],  # Replace with your security group ID
        SubnetId='subnet-0edd6edcade98bcac'  # Replace with your subnet ID
    )

    instance_ids = [instance['InstanceId'] for instance in instances['Instances']]

    # Add "Environment: Dev" tag to the new instances
    ec2.create_tags(
        Resources=instance_ids,
        Tags=[
            {
                'Key': 'Environment',
                'Value': 'Dev'
            }
        ]
    )
    
    print(f"Started instances with IDs: {instance_ids} and tagged them with 'Environment: Dev'")

if __name__ == '__main__':
    create_instances()
