import os
import uuid
import decimal
from contextlib import closing
from boto3.dynamodb.conditions import Key, Attr
import boto3
import botocore

def getDynamoResource():
	return boto3.resource('dynamodb')

def getTable(tableName):
	return getDynamoResource().Table(tableName)

def findById(tableName, id):
	return getTable(tableName).query(KeyConditionExpression=Key('id').eq(id))
