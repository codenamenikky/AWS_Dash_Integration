import boto3

dynamodb = boto3.resource('dynamodb',region_name='us-east-1') 
dynamodb.create_table(
    TableName='weatherData',
    KeySchema=[
        {
            'AttributeName': 'tag',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'timestamp',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'tag',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'timestamp',
            'AttributeType': 'S'
        },
    ],
    
        ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
dynamodb.create_table(
    TableName='metaWeatherDatatable',
    KeySchema=[
        {
            'AttributeName': 'tag',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'tag',
            'AttributeType': 'S'
        }
    ],
    
        ProvisionedThroughput={
        'ReadCapacityUnits': 2,
        'WriteCapacityUnits': 2
    }
)

