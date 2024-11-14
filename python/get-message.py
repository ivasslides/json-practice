import boto3 
import json 
from credentials import * 

qurl = "https://sqs.us-east-2.amazonaws.com/440848399208/queue_36 "

response = sqs.receive_message(
    QueueUrl = qurl,
)

# print(response)
# going into Messages, going to the first index, and printing only the Body field (which contains the actual message string)
print(response['Messages'][0]['Body'])