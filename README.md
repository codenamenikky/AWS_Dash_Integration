# AWS_Dash_Integration
This repo is intended to be useful for anyone working in advanced energy to use both AWS infrastructure and dash. It is built on top of 
https://github.com/plotly/dash-wind-streaming so if you want to look into the original dash script please look into that. 

Below are the main objectives:
1. Use Dynamodb instead of sqllite
2. Create a basic wind sensor simulator and run it on EC2 nano
3. Use EC2 to push data from the simulator to dynamoDB
4. Host the dash app in Elastic BeanStack. 

Development Machine set up. Below are the major steps to get a development machine setup. Linux is preferred 

1. [install code editor](https://code.visualstudio.com/download) - Visual studio code
2. [install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) - `$pip3 install awscli --upgrade --user` 
3. [install SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-additional.html#serverless-sam-cli-install-using-pip) - `$pip install --user aws-sam-cli`
4. [install docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) and [pull  dynamobd](https://hub.docker.com/r/amazon/dynamodb-local/) - to run dynamodb locally
5. get IAM credential set up , download the configuration file. 
6. [Configure AWS](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
7. run `$docker run -p 8000:8000 amazon/dynamodb-local`
8. create a [virtualenv with pip](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) or conda
9. [pip install boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
10. make the virtualenv kernal available for the [Jupyter notebook](https://anbasile.github.io/programming/2017/06/25/jupyter-venv/)
11. prototype in jupyter notebook
12. push to git
13. deploy using AWS CLI tools like eb, sam and aws

