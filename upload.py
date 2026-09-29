import boto3

s3 = boto3.client("s3")

bucket_name = "my-internship-project-bucket"
file_name = "data.csv"

s3.upload_file(file_name, bucket_name, file_name)

print("File Uploaded Successfully")