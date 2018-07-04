import boto3
import pytest
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr
from moto import mock_dynamodb2
from compute import lambda_handler

DATA_TABLE = "dataTable"
CHECK_TABLE = "checkTable"
RESULTS_TABLE = "resultsTable"

## Test Setup Functions

from contextlib import contextmanager

@contextmanager
def do_test_setup():
	with mock_dynamodb2():
		set_up_dynamodb()
		yield


def set_up_dynamodb():
  client = boto3.client('dynamodb', region_name='us-east-1')
  
  attributeDefinitions = { 'AttributeName': 'id', 'AttributeType': 'S' }
  keySchema = { 'AttributeName': 'id', 'KeyType': 'HASH' }

  createTable(client, DATA_TABLE, attributeDefinitions, keySchema)
  table = boto3.resource('dynamodb', region_name='us-east-1').Table(DATA_TABLE)
  table.put_item(
    Item={
	    'id' : 1234,
	    'speed' : 5
	}
  )

  createTable(client, CHECK_TABLE, attributeDefinitions, keySchema)
  table = boto3.resource('dynamodb', region_name='us-east-1').Table(CHECK_TABLE)
  table.put_item(
    Item={
	    'id' : 5678,
	    'speed' : 8
	}
  )
  createTable(client, RESULTS_TABLE, attributeDefinitions, keySchema)
  	
def createTable(client, tableName, attributeDefinitions, keySchema):
	client.create_table(
	  AttributeDefinitions=[ attributeDefinitions ],
	  KeySchema=[ keySchema ],
	  TableName=tableName,
	  ProvisionedThroughput={
	    'ReadCapacityUnits': 1,
	    'WriteCapacityUnits': 1
	  }
	)

# tests

def test_lambda_handler():
  	with do_test_setup():
  	  lambda_handler({"recordId": 1234, "dataId": 5678}, None)
  	  table = boto3.resource('dynamodb', region_name='us-east-1').Table(RESULTS_TABLE)
  	  checkItem = table.scan(
    	FilterExpression=Attr('id').gt("0"),
    	Limit=1
  	  )	
	  assert checkItem["Items"][0]["speed"] == 400
