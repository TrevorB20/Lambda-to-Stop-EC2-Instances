import boto3

def lambda_handler(event, context):
    # Create an EC2 client
    ec2 = boto3.client('ec2')
    
    # List of instance IDs to stop Ec2
    instance_ids = ['i-0e266168430a269b7', 'i-0a7d72ce4cd1090ab', 'i-01fcb586b8391f97d']  # Replace it with your actual instance IDs

    # Stop the instances
    response = ec2.stop_instances(InstanceIds=instance_ids)
    
    return {
        'statusCode': 200,
        'body': f'Stopped instances: {instance_ids}'
    }
