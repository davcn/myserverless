import boto3
import pytest
from botocore.exceptions import ClientError
from moto import mock_dynamodb2
from compute import lambda_handler

TXNS_TABLE1 = "testTable1"

## Test Setup Functions

from contextlib import contextmanager

@contextmanager
def do_test_setup():
	with mock_dynamodb2():
		set_up_dynamodb()
		yield


def set_up_dynamodb():
  client = boto3.client('dynamodb', region_name='us-east-1')
  client.create_table(
    AttributeDefinitions=[
      {
        'AttributeName': 'id',
        'AttributeType': 'S'
      }
    ],
    KeySchema=[
      {
        'AttributeName': 'id',
        'KeyType': 'HASH'
      }
    ],
    TableName=TXNS_TABLE1,
    ProvisionedThroughput={
      'ReadCapacityUnits': 1,
      'WriteCapacityUnits': 1
    }
  )
  table = boto3.resource('dynamodb', region_name='us-east-1').Table(TXNS_TABLE1)
  table.put_item(
    Item={
	    'id' : 1234,
	    'speed' : 5
	}
  )
	
# tests

def test_lambda_handler():
  	with do_test_setup():
	  assert lambda_handler({"recordId": 1234}, None) == 100
