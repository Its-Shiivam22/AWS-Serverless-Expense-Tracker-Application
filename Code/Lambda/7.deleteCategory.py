import json
import boto3
from urllib.parse import unquote

dynamodb = boto3.client("dynamodb")
TABLE_NAME = "Categories"

DEFAULT_CATEGORIES = [
    "Food & Dining",
    "Health & Medicine",
    "Entertainment",
    "Shopping",
    "Travel",
    "Bills & Utilities",
    "Education",
    "Investments",
    "Personal Care",
    "Others"
]

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
        name = unquote(event["pathParameters"]["name"])

        if name in DEFAULT_CATEGORIES:
            return response(400, {"error": "Default categories cannot be deleted"})

        dynamodb.delete_item(
            TableName=TABLE_NAME,
            Key={
                "userId": {"S": user_id},
                "categoryName": {"S": name}
            }
        )

        return response(200, {"message": "Category deleted"})

    except Exception as e:
        return response(500, {"error": str(e)})