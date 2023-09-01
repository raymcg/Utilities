# Start EC2 Instance
"""
Because this is a python script, to run it within the normal python environment would need the instance to already be started
This means we include this script in the Lambda functionality of AWS
So it runs as a python script on Lamba rather than on our instance
Note: We do not have to be logged into AWS for it to run
Note: We can generate a scheduled running of the Lambda function via Cloudwatch

IMPORTANT NOTE: You need to grant the Lambda function the appropriate attach a role that has permissions to start EC2 instances
                You do this in the IAM section of AWS and click Roles, Create role, Lambda, Next:Permissions.
"""

import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    
    # Replace 'your_instance_id' with your EC2 instance ID
    instance = ec2.Instance('your_instance_id')
    instance.start()
