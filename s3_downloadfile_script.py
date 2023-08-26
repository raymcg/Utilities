import boto3

def download_file_from_s3(bucket_name, s3_file_name, local_file_path):
    """
    Download a file from an S3 bucket.

    :param bucket_name: The name of the S3 bucket from where the file will be downloaded.
    :param s3_file_name: The name of the file in the S3 bucket.
    :param local_file_path: The path where the file will be saved on your EC2 instance.
    """
    # Create an S3 client
    s3 = boto3.client('s3')

    # Download the file from the S3 bucket to the specified path on EC2
    s3.download_file(bucket_name, s3_file_name, local_file_path)
    print(f"File {s3_file_name} downloaded from {bucket_name} to {local_file_path}")

# Example usage:
#bucket_name = 'your-s3-bucket-name'
#s3_file_name = 'name_of_file_in_s3.txt'
#local_path_on_ec2 = 'path_where_you_want_to_save_on_ec2.txt'

local_path_on_ec2 = '/home/ubuntu/Trading/test.txt'
bucket_name = 'variances3bucket'
s3_file_name = 'test.txt'

download_file_from_s3(bucket_name, s3_file_name, local_path_on_ec2)
