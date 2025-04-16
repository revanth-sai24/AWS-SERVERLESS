# lambda_handler.py
import os
import boto3
import zipfile
import sys
import awsgi
from app import app

def download_dependencies():
    s3 = boto3.client('s3')
    bucket_name = 'your-s3-bucket-name'
    zip_key = 'my_flask_dependencies.zip'
    download_path = '/tmp/' + zip_key

    s3.download_file(bucket_name, zip_key, download_path)

    with zipfile.ZipFile(download_path, 'r') as zip_ref:
        zip_ref.extractall('/tmp/')

    sys.path.append('/tmp/python')

def handler(event, context):
    download_dependencies()
    return awsgi.response(app, event, context)
