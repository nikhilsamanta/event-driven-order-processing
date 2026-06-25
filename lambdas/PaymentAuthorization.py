import json
import random

def lambda_handler(event, context):

    if random.randint(1,5) == 1:
        raise Exception("Payment Service Temporary Failure")

    return {
        "status": "Payment Approved"
    }
