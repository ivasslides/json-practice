import boto3

# creating a boto3 client for the sqs service -> communitcation service -> messages are wrapped in json 
sqs = boto3.client('sqs', region_name = 'us-east-2',
    
    )

