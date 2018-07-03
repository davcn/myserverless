import os
import uuid
import decimal
from contextlib import closing
from boto3.dynamodb.conditions import Key, Attr
import boto3
import botocore

def lambda_handler(event, context):
    recordId = event["recordId"]

    # Retrieving information about the sonda from DynamoDB table
    dynamodb = boto3.resource('dynamodb')
    tableData = dynamodb.Table('testTable1')
    dataItem = tableData.query(
        KeyConditionExpression=Key('id').eq(recordId)
    )
    sondaSpeed = dataItem["Items"][0]["speed"]

    return calc(sondaSpeed, 2)

def calc(sonda, real):
    return sonda * real * decimal.Decimal(10)
