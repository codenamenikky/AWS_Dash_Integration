# AWS_Dash_Integration
This repo is intended to be useful for anyone working in advanced energy to use both AWS infrastructure and dash. It is built on top of 
https://github.com/plotly/dash-wind-streaming so if you want to look into the original dash script please look into that. 

Below are the main objectives:
1. Use Dynamodb instead of sqllite
2. Create a basic wind sensor simulator as Lambda function
3. Use Lambda functions to push data from the simulator to dynamoDB
4. Host the dash app in AWS infrastructure. 

