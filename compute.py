import os
import uuid
import decimal
from contextlib import closing
from boto3.dynamodb.conditions import Key, Attr
import boto3
import botocore

def lambda_handler(event, context):

    recordId = event["Records"][0]["Sns"]["Message"]
    print "RecordId: " + recordId

    # Retrieving information about the sonda from DynamoDB table
    dynamodb = boto3.resource('dynamodb')
    tableData = dynamodb.Table(os.environ['DB_SONDA_TABLE_NAME'])
    dataItem = tableData.query(
        KeyConditionExpression=Key('id').eq(recordId)
    )
    tableCheck = dynamodb.Table(os.environ['DB_CHECK_TABLE_NAME'])
    checkItem = tableCheck.scan(
        FilterExpression=Attr('timestamp').gt("0"),
        Limit=1
    )

    sondaSpeed = dataItem["Items"][0]["speed"]
    checkSpeed = checkItem["Items"][0]["speed"]

    result = calc(sondaSpeed, checkSpeed)
    id = str(uuid.uuid4())
    #Creating new record in DynamoDB table
    table = dynamodb.Table(os.environ['DB_RESULTS_TABLE_NAME'])
    table.put_item(
      Item={
        'id' : id,
        'speed' : result
      }
    )
    
    return id

def calc(sonda, real):
    return sonda * real * decimal.Decimal(0.1234)
