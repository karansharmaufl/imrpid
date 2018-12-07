from flask import Flask
import config
import boto3
from botocore.exceptions import ClientError
import time
import calendar

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
@app.route("/upload")
def upload():
    #file_key = datetime.datetime.now() + '_sample_stl.stl'
    file_key = str(calendar.timegm(time.gmtime())) + '_sample_stl.stl'
    try:
        print "DEBUG HERE"
        s3_client = boto3.client('s3', aws_access_key_id=config.aws_access_key_id, aws_secret_access_key=config.aws_secret_access_key)
        print "CLIENT CREATED SUCESSFULLY"
        print s3_client
    except ClientError as ce:
        cerror_message = ce.response['Error']['Message']
        print "ERROR: "+cerror_message
    s3_client.upload_file('sample_stl.stl',config.bucket_name,file_key)
    return "IMPLEMENT UPLOAD API"


# The route() decorator to binds a function to a URL.
@app.route("/alluploads")
def alluploads():
    return "IMPLEMENT ALLUPLOADS API"



if __name__ == '__main__':
    app.run(debug = True)
