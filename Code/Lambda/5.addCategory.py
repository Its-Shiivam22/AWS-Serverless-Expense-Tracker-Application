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
        body = json.loads(event.get("body") or "{}")

        name = body.get("name", "").strip()

        if not name:
            return response(400, {"error": "Category name is required"})

        if name in DEFAULT_CATEGORIES:
            return response(400, {"error": "Default category already exists"})

        dynamodb.put_item(
            TableName=TABLE_NAME,
            Item={
                "userId": {"S": user_id},
                "categoryName": {"S": name}
            },
            ConditionExpression="attribute_not_exists(categoryName)"
        )

        return response(200, {"message": "Category added"})

    except dynamodb.exceptions.ConditionalCheckFailedException:
        return response(409, {"error": "Category already exists"})

    except Exception as e:
        return response(500, {"error": str(e)})