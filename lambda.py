import json
import boto3

def handler(event,context):
    print("***************Event Start************")
    print(event)
    body = json.loads(event['body'])
    message = body['raw_text']
    client = boto3.client(service_name='sns')
    arn="<<SNS ARN GOES HERE>>"
    response = client.publish(
        TargetArn=arn,
        Message=message
    )
    print("***************Event End************")
    return {"statuscode": 200, "body":"sent"}