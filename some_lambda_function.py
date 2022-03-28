# some lambda function using API gateway

from __future__ import print_function
import boto3
import json

def handler(event, context):
    return{
      "statusCode": 200,
       "body": json.dumps({
           "message": "hello my friend",
        }),
    }        
    
  
