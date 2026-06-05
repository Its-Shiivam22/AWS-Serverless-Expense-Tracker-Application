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
        body = json.loads(event.get("body") or "{}")

        title = body.get("title")
        amount = body.get("amount")
        category = body.get("category")
        date = body.get("date")

        if not title or not amount or not category or not date:
            return response(400, {"error": "title, amount, category and date are required"})

        dynamodb.update_item(
            TableName=TABLE_NAME,
            Key={
                "userId": {"S": user_id},
                "expenseId": {"S": expense_id}
            },
            UpdateExpression="SET title = :t, amount = :a, category = :c, #d = :d",
            ExpressionAttributeNames={
                "#d": "date"
            },
            ExpressionAttributeValues={
                ":t": {"S": title},
                ":a": {"N": str(amount)},
                ":c": {"S": category},
                ":d": {"S": date}
            }
        )

        return response(200, {"message": "Expense updated"})

    except Exception as e:
        return response(500, {"error": str(e)})