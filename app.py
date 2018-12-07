from flask import Flask, request, jsonify
import config
import boto3
from botocore.exceptions import ClientError
import time
import calendar
import data_helpers
import aws_helpers
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
@app.route("/upload", methods = ['GET','POST'])
def upload():
    s3_client = aws_helpers.init_botoclient()
    obj_res = ''
    if request.method == 'POST':
        file_upload = request.files['file']
        file_name = file_upload.filename
        file_key = str(calendar.timegm(time.gmtime())) + '_' +file_name
        
        try:
            s3_client.upload_fileobj(file_upload,config.bucket_name,file_key)
            file_url = '{}/{}/{}'.format(s3_client.meta.endpoint_url, config.bucket_name, file_key)

            print "file_url here:  "
            print file_url
            
            samp_response = s3_client.head_object(Bucket=config.bucket_name, Key=file_key)

        # THE METHOD CAN BE USED LATER ---- USING JSONIFY INSTEAD
        #res_json = data_helpers.create_json(samp_response)
        except Exception as e:
            print "EXCEPTION OCCURED"
            print e

        obj_res=jsonify(samp_response)

    else:
        print "INIT GET ALL FILES"
        all_files = s3_client.
        obj_res = 'IN GET METHOD'
        
    
    return obj_res
            


# The route() decorator to binds a function to a URL.
@app.route("/alluploads")
def alluploads():
    return "IMPLEMENT ALLUPLOADS API"

if __name__ == '__main__':
    app.run(debug = True)
