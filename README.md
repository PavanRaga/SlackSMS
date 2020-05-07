This is a simple serverless project to get messages from a specific slack channel to SMS.

Usecases : Could be get notified of the developments even when offline(no slack access)  OR you want to be notified via SMS only when your manager messgaes in the channel.

Steps:

1) Zapier to get messages from channel and send it to API gateway endpoint via webhook call from the zap action.
2) Have API Gateway as a trigger for above lambda function.
3) Create an SNS Topic to have SMS as the subscription without any filters(you can add filters here but have to send message attributes in the lambda function)
4) Add SNS arn in the lambda code. 