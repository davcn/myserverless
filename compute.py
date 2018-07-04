import os
import uuid
import decimal
from contextlib import closing
import dynamodb
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    recordId = event["recordId"]
    dataId = event["dataId"]

    # Retrieving information about the sonda from DynamoDB table
    tableData = dynamodb.getTable('dataTable')
    dataItem = tableData.query(
        KeyConditionExpression=Key('id').eq(recordId)
    )


    tableCheck = dynamodb.getTable('checkTable')
    checkItem = tableCheck.query(
        KeyConditionExpression=Key('id').eq(dataId)
    )

    sondaSpeed = dataItem["Items"][0]["speed"]
    checkSpeed = checkItem["Items"][0]["speed"]

    result = calc(sondaSpeed, checkSpeed)
    
    #Creating new record in DynamoDB table
    id = str(uuid.uuid4())
    table = dynamodb.getTable('resultsTable')
    table.put_item(
      Item={
        'id' : id,
        'speed' : result
      }
    )
    


def calc(sonda, real):
    return sonda * real * decimal.Decimal(10)



