# AWS SERVERLESS

- [AWS Serverless](https://aws.amazon.com/serverless/)

- Serverless architecture is a cloud computing model where the cloud provider dynamically manages the allocation and provisioning of servers. In this model, developers can focus on writing code without worrying about the underlying infrastructure.
- Serverless is a cloud computing model which lets you run applications without having to worry about managing and scaling servers.

## Components of a Simple AWS Serverless Architecture:

### AWS Lambda:
- Function as a Service (FaaS): AWS Lambda allows you to run code without managing servers. we write our code in a Lambda function, and AWS handles the execution in response to events.
- Lambda functions are triggered by events such as HTTP requests, changes to data in an S3 bucket, or updates to a DynamoDB table.
### Amazon API Gateway:
- Amazon: API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale.
- HTTP Requests: API Gateway can be used to create RESTful APIs that can be integrated with Lambda functions.
### Amazon S3:
- Amazon S3 is a scalable object storage service that allows you to store and retrieve data. It can be used to store static assets such as images, videos, and HTML files.

- I have come to known there are couple of tools where we can use to deploy serverless applications. Some of them are:

  - Serverless Framework
  - zappa
  - awsgi
  - Chalice

## Zappa:

  - Zappa is a Python library that makes it easy to deploy serverless applications on AWS Lambda. It allows you to deploy WSGI-compatible Python applications, such as Flask and Django, as serverless applications.
  - Zappa handles the deployment and configuration of the Lambda function, API Gateway, and other AWS resources required to run the application. It also provides features such as automatic scaling, logging, and monitoring.
  - Zappa is a popular choice for deploying Python applications on AWS Lambda because it simplifies the deployment process and provides a high-level abstraction that allows you to focus on writing code.

  Configuration with Zappa:

  - create a flask app
    ```bash 
    pip install flask
    ```
  - create a virtual environment
    ```bash
    python -m venv venv
    ```
  - install zappa
    ```bash
    pip install zappa
    ```
  - create a zappa configuration file
    ```bash
    zappa init
    ```
    This will create a zappa_settings.json file that contains the configuration settings for the application.
  - deploy the application
    ```bash
    zappa deploy dev
    ```
    This will deploy the application to AWS Lambda and create the necessary resources.
  - update the application
    ```bash
    zappa update dev
    ```
    This will update the application with any changes made to the code.
  - undeploy the application
    ```bash
    zappa undeploy dev
    ```
    This will undeploy the application and delete all associated resources.
  - view the logs
    ```bash
    zappa tail dev
    ```
    This will display the logs for the application.
  - invoke the function
    ```bash
    zappa invoke dev
    ```
    This will invoke the Lambda function.
  - rollback to a previous version 
    ```bash
    zappa rollback dev
    ```
    This will rollback to a previous version of the application.
  - view the status
    ```bash
    zappa status dev
    ```
    This will display the status of the application.
  - delete the application
    ```bash
    zappa delete dev
    ```
    This will delete the application and all associated resources.

- The following is an example of a simple Flask application that can be deployed to AWS Lambda with Zappa.

  - file structure:
  ```python
      my-flask-app/
      ├── app.py
      ├── requirements.txt
      └── zappa_settings.json
  ```

  ## Code Structure:
  ### app.py:

  ```python
  from flask import Flask
  app = Flask(__name__)

  @app.route('/')
  def hello_world():
      return 'Hello, World!'
  ```

  ### requirements.txt:

  ```python
  Flask==1.1.2
  zappa
  ```

  ### zappa_settings.json:

  ```python
      {
      "dev": {
          "app_function": "app.app",
          "aws_region": "us-east-1",
          "profile_name": "default",
          "project_name": "my-zappa-app",
          "runtime": "python3.8",
          "s3_bucket": "my-zappa-app-bucket"
      }
      }

  ```
  - The app_function key specifies the entry point for the application. In this case, it is app.app, which refers to the app object in the app.py file.
  - The aws_region key specifies the AWS region where the application will be deployed. In this case, it is us-east-1.
  - The profile_name key specifies the AWS profile to use when deploying the application. In this case, it is default.
  - The project_name key specifies the name of the project. In this case, it is my-zappa-app.
  - The runtime key specifies the Python runtime to use. In this case, it is python3.8.
  - The s3_bucket key specifies the name of the S3 bucket where the application will be deployed. In this case, it is my-zappa-app-bucket.

## Deploying a Flask Application to AWS Lambda with Zappa:
  - When deploying to AWS Lambda with Zappa, Zappa handles the WSGI interface and the Lambda function setup for you. You can deploy your Flask application to AWS Lambda with Zappa by running the following commands.
  - After the testing is done and the application is ready to deploy, run the following commands:
    ```bash
    zappa deploy dev
    ```
  - This will deploy the application to AWS Lambda and create the necessary resources. You can then access the application using the URL provided by Zappa.
  - To update the application with any changes made to the code, run the following command:
    ```bash
    zappa update dev
    ```



## Serverless Framework:

  - The Serverless Framework is an open-source framework that makes it easy to build serverless applications on AWS, Azure, and Google Cloud Platform. It provides a simple, yet powerful, way to define and deploy serverless applications using a configuration file.
  - The Serverless Framework supports multiple programming languages, including Node.js, Python, Java, and Go. It also provides a plugin system that allows you to extend its functionality with custom plugins.
  - The Serverless Framework is a popular choice for building serverless applications because it simplifies the process of deploying and managing serverless applications. It provides a high-level abstraction that allows you to focus on writing code, rather than managing infrastructure.

## Chalice:
  - Chalice is a Python library that makes it easy to build serverless applications on AWS Lambda. It provides a simple, yet powerful, way to define and deploy serverless applications using a configuration file.
  - Chalice supports multiple programming languages, including Python, Node.js, and Java. It also provides a plugin system that allows you to extend its functionality with custom plugins.
  - Chalice is a popular choice for building serverless applications because it simplifies the process of deploying and managing serverless applications. It provides a high-level abstraction that allows you to focus on writing code, rather than managing infrastructure.

## awsgi:
  - awsgi is a Python library that makes it easy to deploy WSGI-compatible Python applications on AWS Lambda. It allows you to deploy applications built with frameworks such as Flask and Django as serverless applications.
  - awsgi handles the deployment and configuration of the Lambda function, API Gateway, and other AWS resources required to run the application. It also provides features such as automatic scaling, logging, and monitoring.
  - awsgi is a popular choice for deploying Python applications on AWS Lambda because it simplifies the deployment process and provides a high-level abstraction that allows you to focus on writing code.
