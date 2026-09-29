import boto3
import pandas as pd

s3 = boto3.client("s3")

obj = s3.get_object(
    Bucket="my-internship-project-bucket", 
    Key="data.csv"
)

df = pd.read_csv(obj["Body"])

print(df)