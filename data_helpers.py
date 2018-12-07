import json
import datetime
import boto3


def create_json(obj_dict):
    print "DICT HERE"
    print obj_dict

    print "STARTING CONVERSION TO JSON"

    obj_dict = json.dumps(obj_dict, default=datetime_handler)
    res_json = json.loads(obj_dict)

    print "Resulting JSON"
    print res_json
    return obj_dict

# This is the handler for Datetime serialisation
# REF: <https://stackoverflow.com/questions/35869985/datetime-datetime-is-not-json-serializable>

def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")
    

# THIS FUNCTION IS TO RETURN ENDPOINT URL
# def get_url(s3_client):
#     url = '{}/{}/{}'.format(s3_client.meta.endpoint_url,)