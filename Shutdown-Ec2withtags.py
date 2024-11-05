import boto3

def stop_instances_with_tag(key, value):
    ec2 = boto3.client('ec2')
    
    # Describe instances with the specified tag
    response = ec2.describe_instances(Filters=[
        {
            'Name': 'tag:' + key,
            'Values': [value]
        },
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ])

    # List of running instance IDs with the specified tag
    instance_ids = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]

    if instance_ids:
        # Stop running instances with the specified tag
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f'Stopped instances with IDs: {instance_ids}')
    else:
        print('No running instances found with the specified tag')

if __name__ == '__main__':
    tag_key = 'Environment'  # Replace with your tag key
    tag_value = 'Dev'  # Replace with your tag value
    stop_instances_with_tag(tag_key, tag_value)
