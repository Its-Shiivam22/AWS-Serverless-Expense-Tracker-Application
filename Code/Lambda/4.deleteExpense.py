import json
import boto3

dynamodb = boto3.client("dynamodb")
TABLE_NAME = "Expenses"

def cors():
    return {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type,Authorization",
        "Access-Control-Allow-Methods": "GET,POST,PUT,DELETE,OPTIONS"
    }

def response(status, body):
    return {
        "statusCode": status,
        "headers": cors(),
        "body": json.dumps(body)
    }

def get_user_id(event):
    return event["requestContext"]["authorizer"]["jwt"]["claims"]["sub"]

def lambda_handler(event, context):
    try:
        user_id = get_user_id(event)
        expense_id = event["pathParameters"]["id"]

        dynamodb.delete_item(
            TableName=TABLE_NAME,
            Key={
                "userId": {"S": user_id},
                "expenseId": {"S": expense_id}
            }
        )

        return response(200, {"message": "Expense deleted"})

    except Exception as e:
        return response(500, {"error": str(e)})