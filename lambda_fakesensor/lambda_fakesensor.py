
import datetime as dt
import boto3
from decimal import Decimal
from boto3.dynamodb.conditions import Key, Attr
import numpy as np
import math

dynamodb = boto3.resource('dynamodb', region_name='us-east-1') 
def getMetaData(inputTag):
    metaWeatherDatatable = dynamodb.Table('metaWeatherDatatable')
    response = metaWeatherDatatable.get_item(
    Key={
        'tag':inputTag
    }
    )    
    return response['Item']
def updateMetaData(inputData):
    # TODO: Need to update the meta data only when the date is older than update date 
    metaWeatherDatatable = dynamodb.Table('metaWeatherDatatable')
    response=metaWeatherDatatable.query(
        KeyConditionExpression = Key('tag').eq(inputData['tag'])
    )
    try:        
        data = response['Items'][0]
    except:
        data = None
    if data:        
        metaWeatherDatatable.delete_item(
        Key={
            'tag':inputData['tag']        
        }
        )
        metaWeatherDatatable.put_item(
            Item=inputData
        )
        finalResponse = 'Updated Data'
    else:
        print("noData")
        finalResponse = metaWeatherDatatable.put_item(Item=inputData)
    return finalResponse
def putIntialData():
        timestamp = '2019-04-08 12:12:00'
        data = [
        {
            'tag':'Speed',
            'timestamp':timestamp,
            'value':Decimal(12.0)
        },
        {
            'tag':'SpeedError',
            'timestamp':timestamp,
            'value':Decimal(2.0)
        },
        {
            'tag':'Direction',
            'timestamp':timestamp,
            'value':Decimal(40)
        }
        
        ]

def sendDatatoDyanamo(i):
    weatherDatatable = dynamodb.Table('weatherData')
    # todo: check if the timestamp in the meta data is older than the timestamp working on now 
    updateMetaData(i)
    weatherDatatable.put_item(Item=i)

def getSensorData():    
    now = dt.datetime.now()
    sec = now.second
    minute = now.minute
    hour = now.hour
    stTimestamp = dt.datetime(now.year, now.month, now.day, hour,minute,sec)
    try:
        prevVal = getMetaData('Speed')['value'] #starting wind speed to seed the random function     
    except:
        prevVal=20.0
    try:
        prevOrientation = getMetaData('Direction')['value'] #starting orentation of the wind direction
    except:
        prevOrientation = 50
    if(round(prevVal) > 45):
        prevVal = int(math.floor(prevVal))
    elif(round(prevVal) < 10):
        prevVal = int(math.ceil(prevVal))
    else:
        prevVal = int(round(prevVal))


    Speed=np.random.normal(prevVal, 2, 1)[0]
    SpeedError = np.random.normal(round(prevVal/10), 1)
    timestamp = stTimestamp.strftime("%Y-%m-%d %H:%M:%S")

    if(minute % 5 == 0):
        Direction = np.random.uniform(prevOrientation-50,
                                                prevOrientation+50)
    else:
        Direction = np.random.uniform(prevOrientation-5,
                                                prevOrientation+5)
    data = [
        {
            'tag':'Speed',
            'timestamp':timestamp,
            'value':Decimal(str(Speed))
        },
        {
            'tag':'SpeedError',
            'timestamp':timestamp,
            'value':Decimal(str(SpeedError))
        },
        {
            'tag':'Direction',
            'timestamp':timestamp,
            'value':Decimal(str(Direction))
        }
        
    ]
    return data

def pushDataToDynamo(event=None,context=None):
    fakeSensorData=getSensorData()
    for i in fakeSensorData:
        sendDatatoDyanamo(i)

if __name__=="__main__":    
    import time
    while True:
        pushDataToDynamo()
        time.sleep(5)

