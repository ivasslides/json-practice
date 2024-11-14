import boto3
import json
from credentials import * 

qurl = "https://sqs.us-east-2.amazonaws.com/440848399208/queue_36 "

response = sqs.send_message(
    #passing our url to the sqs variable
    QueueUrl = qurl,
    #lil message body 
    MessageBody = "Iliana saying ciao"
)

print(response)