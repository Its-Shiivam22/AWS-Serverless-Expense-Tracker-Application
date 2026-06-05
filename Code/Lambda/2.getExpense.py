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

        result = dynamodb.query(
            TableName=TABLE_NAME,
            KeyConditionExpression="userId = :u",
            ExpressionAttributeValues={
                ":u": {"S": user_id}
            }
        )

        expenses = []

        for item in result.get("Items", []):
            expenses.append({
                "expenseId": item["expenseId"]["S"],
                "title": item["title"]["S"],
                "amount": float(item["amount"]["N"]),
                "category": item["category"]["S"],
                "date": item.get("date", {}).get("S", "")
            })

        return response(200, expenses)

    except Exception as e:
        return response(500, {"error": str(e)})