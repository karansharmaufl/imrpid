import boto3
from botocore.exceptions import ClientError
import config

def init_botoclient():
    try:
        #print "DEBUG HERE"
        s3_client = boto3.client('s3', aws_access_key_id=config.aws_access_key_id, aws_secret_access_key=config.aws_secret_access_key)
        #print "CLIENT CREATED SUCESSFULLY"
        #print s3_client
    except ClientError as ce:
        cerror_message = ce.response['Error']['Message']
        print "ERROR: "+cerror_message

    return s3_client
