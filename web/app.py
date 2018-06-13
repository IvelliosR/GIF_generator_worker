import boto3
import time
import os

### Bucket config ###
bucket_name = os.environ["APP_BUCKET_NAME"]
bucket_url = 'https://s3.eu-central-1.amazonaws.com/'
s3 = boto3.resource('s3')
bucket= s3.Bucket(bucket_name)

def get_from_sqs(queue_name):
    sqs = boto3.resource('sqs', region_name="eu-central-1")
    orders = sqs.get_queue_by_name(QueueName=queue_name)

    while True:
        for message in orders.receive_messages():
            print('Message body: %s' % message.body)
            message.delete()
        time.sleep(1)

get_from_sqs(os.environ["QUEUE_NAME"])
