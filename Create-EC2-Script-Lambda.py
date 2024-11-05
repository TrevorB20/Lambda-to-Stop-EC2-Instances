import boto3
# Create an EC2 instance client
ec2 = boto3.client('ec2')

def create_instances():
    instances = ec2.run_instances(
        ImageId='ami-06b21ccaeff8cd686',  # Replace the ami ID with your own 
        InstanceType='t2.micro',  # We leave instance type as it is in the free tier
        MinCount=3,
        MaxCount=3,
        KeyName='Ec2-Lambda',  # Replace with your key pair name
        SecurityGroupIds=['sg-0ecc07d16d83bbd95'],  # Replace with your security group ID
        SubnetId='subnet-06173f2b1015e31bf'  # Replace with your subnet ID
    )

    for instance in instances['Instances']:
        print(f"Created instance with ID: {instance['InstanceId']}")

if __name__ == '__main__':
    create_instances()