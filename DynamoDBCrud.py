import json
import boto3
from decimal import Decimal
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['DYNAMODB_TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    http_method = event['requestContext']['http']['method']

    if http_method == 'GET':
        path_parameters = event.get('pathParameters', {})
        id = path_parameters.get('id')
        if id is not None: return get_item(id)
        return get_items()
    elif http_method == 'POST':
        return create_item(json.loads(event['body']))
    elif http_method == 'PUT':
        return update_item(json.loads(event['body']))
    elif http_method == 'DELETE':
        return delete_item(id=json.loads(event['pathParameters']['id']))
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Unsupported HTTP method')
        }

def get_items():
    try:
        response = table.scan()
        items = json.dumps(response['Items'], default=handle_decimal_type)
        return {
            'statusCode': 200,
            'body': items
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

def get_item(id):    
    try:
        key = str(id)
        response = table.get_item(Key={'pk': key})
        item = json.dumps(response['Item'], default=handle_decimal_type)
        return {
            'statusCode': 200,
            'body': item
        }
    except Exception as e:
        print("exception")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

def create_item(item):
    try:
        table.put_item(Item=item)
        return {
            'statusCode': 201,
            'body': json.dumps('Item created successfully')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

def update_item(item):
    try:
        key = item.get('pk')
        update_expression = "SET #attrName = :attrValue"
        expression_attribute_names = {"#attrName": "name"}
        expression_attribute_values = {":attrValue": item.get('name')}

        table.update_item(
            Key={'pk': key},
            UpdateExpression=update_expression,
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues=expression_attribute_values
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Item updated successfully')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

def delete_item(id):
    try:
        key = str(id)
        print(key)
        table.delete_item(Key={'pk': key})
        return {
            'statusCode': 200,
            'body': json.dumps('Item deleted successfully')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

def handle_decimal_type(obj):
    """
    Helper function to process decimal data to prevent errors 
    when composing JSON to return values.

    Parameters:
    - obj (Any): data retrieved from DynamoDB. If such data 
      is of class Decimal, it will be converted to either 
      integer or float.

    Returns:
    - int: if whole number
    - float: otherwise
    """
    if isinstance(obj, Decimal):
        if float(obj).is_integer():
            return int(obj)
        else:
            return float(obj)
    raise TypeError
