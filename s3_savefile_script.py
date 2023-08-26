import boto3

def upload_file_to_s3(file_path, bucket_name, s3_file_name):
    """
    Upload a file to an S3 bucket.

    :param file_path: The path of the file on your EC2 instance to be uploaded.
    :param bucket_name: The name of the S3 bucket where the file will be uploaded.
    :param s3_file_name: The name of the file in the S3 bucket. Can be the same as file_path or different.
    """
    # Create an S3 client
    s3 = boto3.client('s3')

    # Uploads the given file to the S3 bucket
    s3.upload_file(file_path, bucket_name, s3_file_name)
    print(f"File {file_path} uploaded to {bucket_name}/{s3_file_name}")

# Example usage:
#file_path_on_ec2 = 'path_to_your_file_on_ec2.txt'
#bucket_name = 'your-s3-bucket-name'
#s3_file_name = 'desired_name_in_s3.txt'

file_path_on_ec2 = '/home/ubuntu/test.txt'
bucket_name = 'variances3bucket'
s3_file_name = 'test.txt'

upload_file_to_s3(file_path_on_ec2, bucket_name, s3_file_name)

"""
Replace 'path_to_your_file_on_ec2.txt', 'your-s3-bucket-name', and 'desired_name_in_s3.txt' with appropriate values.

When you run this script on your EC2 instance, it will upload the specified file to the given S3 bucket.

Remember, the EC2 instance must have permissions (through an IAM role or otherwise) to perform the s3:PutObject action on the specified bucket.
"""
