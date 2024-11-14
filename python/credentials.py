import boto3

# creating a boto3 client for the sqs service -> communitcation service -> messages are wrapped in json 
sqs = boto3.client('sqs', region_name = 'us-east-2',
    aws_access_key_id='AKIAWNJE4XNUMNELGYVO',
    aws_secret_access_key='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'
    )

