### AWS SERVERLESS

- [AWS Serverless](https://aws.amazon.com/serverless/)

- Serverless architecture is a cloud computing model where the cloud provider dynamically manages the allocation and provisioning of servers. In this model, developers can focus on writing code without worrying about the underlying infrastructure.
- Serverless is a cloud computing model which lets you run applications without having to worry about managing and scaling servers.

- Components of a Simple AWS Serverless Architecture:

  - AWS Lambda:
    - Function as a Service (FaaS): AWS Lambda allows you to run code without managing servers. we write our code in a Lambda function, and AWS handles the execution in response to events.
    - Lambda functions are triggered by events such as HTTP requests, changes to data in an S3 bucket, or updates to a DynamoDB table.
  - Amazon API Gateway:
    - Amazon: API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale.
    - HTTP Requests: API Gateway can be used to create RESTful APIs that can be integrated with Lambda functions.
  - Amazon S3:
    - Amazon S3 is a scalable object storage service that allows you to store and retrieve data. It can be used to store static assets such as images, videos, and HTML files.

- I have come to known there are couple of tools where we can use to deploy serverless applications. Some of them are:

  - Serverless Framework
  - zappa
  - awsgi
    @REM - Chalice
    @REM - Claudia.js
    @REM - cloudformation
    @REM - Terraform
    @REM - AWS SAM (Serverless Application Model)
    @REM - AWS CDK (Cloud Development Kit)
    @REM - AWS Amplify

- Zappa:

  - Zappa is a Python library that makes it easy to deploy serverless applications on AWS Lambda. It allows you to deploy WSGI-compatible Python applications, such as Flask and Django, as serverless applications.
  - Zappa handles the deployment and configuration of the Lambda function, API Gateway, and other AWS resources required to run the application. It also provides features such as automatic scaling, logging, and monitoring.
  - Zappa is a popular choice for deploying Python applications on AWS Lambda because it simplifies the deployment process and provides a high-level abstraction that allows you to focus on writing code.

  Configuration with Zappa:

  - create a flask app [pip install flask]
  - create a virtual environment [python -m venv venv]
  - activate the virtual environment [.\venv\Scripts\activate]
  - install zappa [pip install zappa]
  - create a zappa configuration file [zappa init]: This will create a zappa_settings.json file that contains the configuration settings for the application.
  - deploy the application [zappa deploy dev]: This will create the Lambda function and other resources required to run the application.
  - update the application [zappa update dev]: This will update the Lambda function with the latest code changes.
  - undeploy the application [zappa undeploy dev]: This will remove the Lambda function and other resources created by Zappa.
  - view the logs [zappa tail dev]: This will display the logs from the Lambda function.
  - invoke the function [zappa invoke dev 'app.app']: This will invoke the Lambda function with the specified event data.
  - rollback to a previous version [`zappa rollback dev`]: This will rollback to a previous version of the Lambda function.
  - view the status `zappa status dev`: This will display the status of the deployment.
  - delete the application 'zappa delete dev': This will delete the application and all associated resources.
  - file structure:

  ```python
      my-flask-app/
      ├── app.py
      ├── wsgi.py
      ├── requirements.txt
      └── zappa_settings.json
  ```

  - code structure:
  - app.py:

  ```python
  from flask import Flask
  app = Flask(__name__)

  @app.route('/')
  def hello_world():
      return 'Hello, World!'
  ```

  - wsgi.py:

  ```python

  from app import app

  def lambda_handler(event, context):
      return app(event, context)

  ```

  -requirements.txt:

  ```python
  Flask==1.1.2
  zappa
  ```

  - zappa_settings.json:

  ```python
      {
      "dev": {
          "app_function": "wsgi.lambda_handler",
          "aws_region": "us-east-1",
          "profile_name": "default",
          "project_name": "my-zappa-app",
          "runtime": "python3.8",
          "s3_bucket": "my-zappa-app-bucket"
      }
      }

  ```

- Serverless Framework:

  - The Serverless Framework is an open-source framework that makes it easy to build serverless applications on AWS, Azure, and Google Cloud Platform. It provides a simple, yet powerful, way to define and deploy serverless applications using a configuration file.
  - The Serverless Framework supports multiple programming languages, including Node.js, Python, Java, and Go. It also provides a plugin system that allows you to extend its functionality with custom plugins.
  - The Serverless Framework is a popular choice for building serverless applications because it simplifies the process of deploying and managing serverless applications. It provides a high-level abstraction that allows you to focus on writing code, rather than managing infrastructure.

- Chalice:
  - Chalice is a Python library that makes it easy to build serverless applications on AWS Lambda. It provides a simple, yet powerful, way to define and deploy serverless applications using a configuration file.
  - Chalice supports multiple programming languages, including Python, Node.js, and Java. It also provides a plugin system that allows you to extend its functionality with custom plugins.
  - Chalice is a popular choice for building serverless applications because it simplifies the process of deploying and managing serverless applications. It provides a high-level abstraction that allows you to focus on writing code, rather than managing infrastructure.
- awsgi:
  - awsgi is a Python library that makes it easy to deploy WSGI-compatible Python applications on AWS Lambda. It allows you to deploy applications built with frameworks such as Flask and Django as serverless applications.
  - awsgi handles the deployment and configuration of the Lambda function, API Gateway, and other AWS resources required to run the application. It also provides features such as automatic scaling, logging, and monitoring.
  - awsgi is a popular choice for deploying Python applications on AWS Lambda because it simplifies the deployment process and provides a high-level abstraction that allows you to focus on writing code.
