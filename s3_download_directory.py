import boto3
import os

s3 = boto3.client('s3')

def download_directory(bucket, s3_folder, local_directory):
    # Create local directory if it doesn't exist
    if not os.path.exists(local_directory):
        os.makedirs(local_directory)

    # List the objects in the S3 directory
    result = s3.list_objects(Bucket=bucket, Prefix=s3_folder)
    for content in result.get('Contents', []):
        # Get the S3 object key and construct the local file path
        s3_key = content['Key']

        # If the S3 key ends with a '/', it's a directory; skip downloading
        if s3_key.endswith('/'):
            continue
        
        local_path = os.path.join(local_directory, s3_key[len(s3_folder):].lstrip('/'))
        
        # Create local subdirectories if they don't exist
        if not os.path.exists(os.path.dirname(local_path)):
            os.makedirs(os.path.dirname(local_path))
        
        # Download the file
        s3.download_file(bucket, s3_key, local_path)
        print(f"{bucket}/{s3_key} downloaded to {local_path}")


# Example usage:
bucket_name = 'variances3bucket'
s3_folder_name = 'Trading/programs/Main/'  # Ensure it ends with a '/' to indicate it's a directory
local_path_on_ec2 = '/home/ubuntu/Trading/Main/' #EC2 Instance Path

download_directory(bucket_name, s3_folder_name, local_path_on_ec2)
