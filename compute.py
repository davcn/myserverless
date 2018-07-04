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
    dataItem  = dynamodb.findById('dataTable', recordId)
    checkItem = dynamodb.findById('checkTable', dataId)
    
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



