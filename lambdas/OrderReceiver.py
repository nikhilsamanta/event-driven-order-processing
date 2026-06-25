
import json
import boto3

sqs = boto3.client('sqs')

QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/959222626247/order-processing.fifo'

def lambda_handler(event, context):

    if 'body' in event:
        body = json.loads(event['body'])
    else:
        body = event

    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(body),
        MessageGroupId='orders'
    )

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Order queued successfully',
            'messageId': response['MessageId']
        })
    }
