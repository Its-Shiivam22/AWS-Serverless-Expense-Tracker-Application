import json
import boto3

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

        result = dynamodb.query(
            TableName=TABLE_NAME,
            KeyConditionExpression="userId = :u",
            ExpressionAttributeValues={
                ":u": {"S": user_id}
            }
        )

        categories = []

        for cat in DEFAULT_CATEGORIES:
            categories.append({
                "name": cat,
                "isDefault": True
            })

        for item in result.get("Items", []):
            name = item["categoryName"]["S"]

            if name not in DEFAULT_CATEGORIES:
                categories.append({
                    "name": name,
                    "isDefault": False
                })

        return response(200, categories)

    except Exception as e:
        return response(500, {"error": str(e)})