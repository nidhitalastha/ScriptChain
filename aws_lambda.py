import json
import os

def lambda_handler(event, context):
    # TODO implement
    region = os.environ['AWS_REGION']
    print("REGION: ", region)
    print("EVENT: ", event)
    return {
        "body": json.dumps({
            "REGION": region,
            "EVENT": event
        }, default=str)
    }