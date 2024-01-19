import requests
import boto3
import os

os.environ.setdefault('AWS_DEFAULT','user name')

s3_client = boto3.client('s3')
def dowmload(file):
    print("Downloading...")
    result = requests.get(file)
    file_name = file[65:69]

    upload = s3_client.put_object(
        Bucket = 'balancesheet10',
        Key = file_name + ".json",
        Body = result.content
    )

    print(upload)
    return upload

