## This method requires an additional pandas library be installed called s3fs
# pip install pandas s3fs

import pandas as pd

def read_s3_csv_to_dataframe(bucket_name, s3_file_key):
    """
    Reads a CSV from S3 into a pandas DataFrame
    Args:
    - bucket_name (str): Name of the S3 bucket
    - s3_file_key (str): Key (path) of the CSV file in the S3 bucket
    
    Returns:
    - DataFrame: The CSV data as a pandas DataFrame
    """
    # Construct the full S3 URL for the file
    s3_url = f"s3://{bucket_name}/{s3_file_key}"

    # Use pandas to read the CSV directly from S3
    df = pd.read_csv(s3_url)
    
    return df

if __name__ == "__main__":
    BUCKET_NAME = 'variances3bucket'
    S3_FILE_KEY = 'Trading/datafiles/dividends_2023.csv'
    
    dataframe = read_s3_csv_to_dataframe(BUCKET_NAME, S3_FILE_KEY)
    print(dataframe.head())  # Display the first 5 rows of the dataframe