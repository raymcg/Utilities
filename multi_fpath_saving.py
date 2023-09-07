def write_to_csv_func():
    """
    Function to write generated files to csv taking into account windows and AWS environemtns
    Assumes if running in a Windows environment we are running from my PC and so saves to Dropbox
    Assumes if running in a Linux environment we are running on EC2 instance so saves to S3 Bucket
    """
    test_df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': ['a', 'b', 'c']
    }) 

    # Name for file to be saved as
    output_fname = f"testfile.csv"

    # If running on Windows, save to dropbox
    if platform.system() == "Windows":
        path_name = "C:\Dropbox\Variance\Data Files\\"

    # If running on Linux AWS, save file to the S3 bucket
    if platform.system() == "Linux":
        path_name = f"s3://variances3bucket/Scraping/datafiles/"

    # Add filepath to filename
    full_output_fname = f"{path_name}{output_fname}"

    # Write desired file to specified filepath (S3 bucket or Dropbox)
    test_df.to_csv(full_output_fname, index = False)

    print(f"{full_output_fname} written to csv")

    return path_name