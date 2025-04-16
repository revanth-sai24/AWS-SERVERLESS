# awsgi
 We need to manually create a deployment package that includes your application code and all its dependencies

 # steps:
 - create the Flask app and install the dependencies in a virtual environment
 - Create a directory for your deployment package and copy your application code and dependencies into it.


 ## AWS Lambda Pros
    1. No Maintenance 
        AWS handles all the infrastructure management tasks like server and operating system maintenance, capacity provisioning, automatic scaling, code monitoring, logging, and security patching.
    2. pay only for what you use 
        you are charged based on the number of requests for your functions and the time your code executes
    3. High availability 
        there will be no downtime
    4. Scalability 
        AWS Lambda automatically scales your application by running code in response to each trigger. 
        Your code runs in parallel and processes each trigger individually, scaling precisely with the size of the workload. 
        we can send 1-1000 requests at a time and it will handle it. if we want to send more than 1000 requests at a time we need to request AWS to increase the limit.
        for each request, it will create a container and run the code and send the response and destroy the container.
    5. Monitoring:
        AWS Lambda automatically monitors Lambda functions on your behalf, reporting metrics through Amazon CloudWatch. ( we can check the request count, error count, duration, etc)
    6. Logging: AWS Lambda provide the logs for each request and we can check the logs in CloudWatch.
    - When a request comes in it will create a container and run the code after sending the response it will destroy the container.

 ## AWS Lambda Cons
    1. Cold Start
        When a request comes in, AWS Lambda creates a new container to run the code. This process is called a cold start. 
        The cold start can increase the latency of the first request. 
        The cold start time depends on the size of the deployment package and the amount of memory allocated to the function.
        example: 
            1. cold start time for a Python function with 128 MB of memory is around 1-2 seconds.
            2. cold start time for a Python function with 3 GB of memory is around 100-200 milliseconds.
    2. Execution Limits
        AWS Lambda has execution limits that you need to be aware of. 
        For example, the maximum execution time for a Lambda function is 15 minutes. 
        The maximum deployment package size is 250 MB. 
        The maximum memory allocation is 3 GB.
    3. Limited Runtime
        AWS Lambda supports a limited number of runtimes, including Node.js, Python, Ruby, Java, Go, .NET Core, and custom runtimes.
    4. Limited Environment
        AWS Lambda provides a limited execution environment. 
        For example, you can't access the file system directly, and you have limited control over the underlying infrastructure.
    5. Limited Deployment Options
        AWS Lambda has limited deployment options compared to traditional servers. 
        For example, you can't SSH into a Lambda function to debug it, and you can't install custom software on the underlying infrastructure.
    
# When to use AWS
    - When you have a small application that doesn't require a lot of resources.
    - When you want to build a serverless application that scales automatically and doesn't require any infrastructure management.
    - When you want to pay only for what you use, without any upfront costs or long-term commitments.


## AWS Lambda Pros
1. No Maintenance: AWS handles all infrastructure management tasks.
2. Pay Only for What You Use: Charged based on requests and execution time.
3. High Availability: No downtime.
4. Scalability: Automatically scales with workload.
5. Monitoring: Metrics reported through Amazon CloudWatch.
6. Logging: Logs available in CloudWatch.

## AWS Lambda Cons
1. Cold Start: Increased latency for the first request.
2. Execution Limits: Max execution time is 15 minutes, max package size is 250 MB, max memory is 3 GB.
3. Limited Runtime: Supports a limited number of runtimes.
4. Limited Environment: Limited execution environment and control.
5. Limited Deployment Options: Limited compared to traditional servers.

## When to Use AWS Lambda
- For small applications with minimal resource requirements.
- For serverless applications that scale automatically.
- To pay only for usage without upfront costs or long-term commitments.

## How to create a LAMBDA
- Create a Lambda function in the AWS Management Console.
- Click on Create function.
- Select the runtime and permissions [ select Python as runtime and selct the x84 intel processes and permissions for create a new role with basic permissions (to see logs on cloudwatch) ].
- AWS will create a new Lambda function with the selected runtime and permissions, with a default handler function.
- You can now edit the code for the Lambda function and test it using the Test button.
- Once you're satisfied with the code, you can deploy the Lambda function by clicking on the Deploy button.
- You can now invoke the Lambda function using the Invoke button, and view the logs in CloudWatch.

# Deploy python code to AWS Lambda
    - One way
        - copy the code and paste it in the lambda function and deploy it.
    - zip way:
        - create a zip file and name it as python with the code.
        - There are two ways to upload the zip file to AWS Lambda:
            - Upload the zip file directly in the AWS Lambda Console by clicking upload from button.
            - we can upload this to s3 bucket and provide the s3 bucket path in the lambda function. (more than 10mb we need to use this way)
        - Once the zip file is uploaded, you can deploy the Lambda function by clicking on the Deploy button.
        - there should be lambda_handler function in our main file.
        - we need to set the start point of the code in the lambda function. as 'lambda_handler.lambda_handler'
        <>filename.functionname</>
    - code with dependencies:
        - create a folder and name it as python
        - add the app.py and lambda_handler.py in the folder
        - add the dependencies in the folder (site-packages only)
        - create a zip file with the folder and upload it to the lambda function.
        - set the start point of the code in the lambda function. as 'lambda_handler.lambda_handler'
        - we can use the lambda_handler.py file as a start point for the code.
        - we can use the app.py file as a main file for the code.
## AWS Lambda Layers:
-  the dependencies that we use in code that we called as layers in lambdas
- we can create a layer and add the dependencies in the layer and use the layer in the lambda function.
- we can create a layer in the AWS Lambda by clicking on Layers and then Create layer.
- click on create layer and provide the name and description and and run time upload the zip file with the dependencies.
- create a python folder and add the site-package dependencies in the folder and create a zip file with the folder and upload it to the layer.
- after creating will get an arn number and we can use this arn number in the lambda function.
- Integrate it with the lambda function by clicking on the Layers tab in the Lambda function and then Add a layer.
- select the custom layer / arn number and select the layer that we created and click on Add.
- In the lambda function we can the layers as 1 like this we can add 5 layers to the lambda function. 
- each layer can take up to 250 mb.


Integrate the API gateway with the lambda function:
- click on the API gateway and create a new API.
- click on the create API and select the REST API and select the security either open/api-key and  click on Add.
- Once it was added we can see the API Gateway on lambda console and click on the resources and click on the Actions and create a new resource and provide the resource name and click on create resource.


- Serverless Framework:
    - To deploy a web app on AWS Lambda, and making them serverless we can use the serverless framework.
    - which is an open-source framework that makes it easy to deploy serverless applications on AWS, other cloud providers.
    - all we required is an yaml file and we can deploy the code to the AWS Lambda.
    - first we need to install the serverless framework by using the command 'npm install -g serverless'
    - install the required plugins by using the command 'serverless plugin install -n serverless-python-requirements' and 'serverless plugin install -n serverless-awsgi'
    - create a yaml file for the serverless framework and add the required configurations in the file.

    ```yaml
    service: my-service
    package:
        individually: true
        exclude:
            - .venv/**
    provider:
        name: aws
        runtime: python3.8
        stage: dev
        region: us-east-1
        environment:
            STRIP_STAGE_PATH: YES
    functions:
        app:
            handler: wsgi.handler
            events:
                - httpApi: '*'
    custom:
        wsgi:
            app: app.app
            packRequirements:
                zip: true
                slim: true
    plugins:    
        - serverless-python-requirements
        - serverless-awsgi
    ```
    - need to configure the aws with serverless 
    - deploy the code by using the command 'serverless deploy --aws-profile default'
    - it will dump our packages in the s3 bucket and create a lambda function and API gateway.