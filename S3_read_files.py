import boto3

def get_s3_file_content(bucket_name, s3_file_key):
    """
    Fetches content of a file from S3
    Args:
    - bucket_name (str): Name of the S3 bucket
    - s3_file_key (str): Key (path) of the file in the S3 bucket
    
    Returns:
    - (str): Content of the file
    """
    # Create an S3 client
    s3 = boto3.client('s3')

    # Get object from S3
    response = s3.get_object(Bucket=bucket_name, Key=s3_file_key)
    
    # Read content from the S3 object
    file_content = response['Body'].read().decode('utf-8')

    return file_content

if __name__ == "__main__":
    BUCKET_NAME = 'variances3bucket'
    
    # List of S3 file keys you want to read
    S3_FILE_KEYS = [
        'Trading/datafiles/test1.txt',
        'Trading/datafiles/test2.txt',
        'Trading/datafiles/test3.txt'
    ]

    for s3_file_key in S3_FILE_KEYS:
        content = get_s3_file_content(BUCKET_NAME, s3_file_key)
        print(f"Content of {s3_file_key}:\n{content}\n{'-'*50}\n")
