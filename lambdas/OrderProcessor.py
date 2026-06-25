import json
import boto3

sf = boto3.client('stepfunctions')

STATE_MACHINE_ARN = 'arn:aws:states:us-east-1:959222626247:stateMachine:OrderProcessingWorkflow'

def lambda_handler(event, context):

    for record in event['Records']:

        sf.start_execution(
            stateMachineArn=STATE_MACHINE_ARN,
            input=record['body']
        )

    return {
        'statusCode': 200
    }
