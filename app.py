from flask import Flask, request
import config
import boto3
from botocore.exceptions import ClientError
import time
import calendar
import data_helpers

app = Flask(__name__)


# The route() decorator to binds a function to a URL.
@app.route("/")
def hello():
    return "WELCOME TO IMRPID"

# The route() decorator to binds a function to a URL.
@app.route("/register")
def register():
    return "IMPLEMENT REGISTER API"


# The route() decorator to binds a function to a URL.
@app.route("/login")
def login():
    return "IMPLEMENT LOGIN API"

# The route() decorator to binds a function to a URL.
@app.route("/upload", methods = ['POST'])
def upload():
    file_upload = request.files['file']
    file_name = file_upload.filename
    file_key = str(calendar.timegm(time.gmtime())) + '_' +file_name
    try:
        #print "DEBUG HERE"
        s3_client = boto3.client('s3', aws_access_key_id=config.aws_access_key_id, aws_secret_access_key=config.aws_secret_access_key)
        #print "CLIENT CREATED SUCESSFULLY"
        #print s3_client
    except ClientError as ce:
        cerror_message = ce.response['Error']['Message']
        print "ERROR: "+cerror_message
    
    try:
        s3_client.upload_fileobj(file_upload,config.bucket_name,file_key)
        #time.sleep(10)
        samp_response = s3_client.head_object(Bucket=config.bucket_name, Key=file_key)
        res_json = data_helpers.create_json(samp_response)
        #print "RESPONSE_HERE"
        #print str(samp_response)
    
    except Exception as e:
        print "EXCEPTION OCCURED"
        print e

    
    return res_json



# The route() decorator to binds a function to a URL.
@app.route("/alluploads")
def alluploads():
    return "IMPLEMENT ALLUPLOADS API"



if __name__ == '__main__':
    app.run(debug = True)
