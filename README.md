# A Serverless Workload to Perform CRUD Operations on DynamoDB

## Project Overview

This project provides a simple yet powerful setup for handling CRUD (Create, Read, Update, Delete) operations on DynamoDB using an API Gateway to trigger a Lambda Function. The entire infrastructure is defined and deployed using AWS CloudFormation. The Lambda Function is written in Python.

![Solution Overview](https://github.com/trsteinmetz/AWS-CrudApiToDynamoDb/blob/main/images/architecture.png "Architecture Diagram")

The solution works as follows. _Step 1:_ The user sends a CRUD (Create, Read, Update or Delete) request to the API Gateway. _Step 2:_ A Lambda Function is triggered to handle the request. _Step 3:_ The operation result (or it’s failure) is logged in Cloudwatch. _Step 4:_ One or more items are retrieved, updated or deleted, according to the requested operation in step 1.

## Prerequisites

Before you begin, ensure you have the following prerequisites:

- [AWS CLI](https://aws.amazon.com/cli/) installed and configured with the necessary access permissions.
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/) is nice to have, but not at all mandatory.

## Deployment Steps

Follow these steps to deploy the API Gateway, Lambda Function, and DynamoDB table:

1. Clone the repository to your local machine.

    ```bash
    git clone https://github.com/trsteinmetz/AWS-CrudApiToDynamoDb.git
    ```

2. Navigate to the project directory.

    ```bash
    cd your-repo
    ```

3. Deploy the CloudFormation stack using the AWS CLI.

    ```bash
    aws cloudformation create-stack --stack-name YourStackName --template-body file://HttpApi-Lambda-DynamoDb.yml --capabilities CAPABILITY_IAM
    ```

4. Wait for the stack to complete deployment. You can monitor the progress in the AWS CloudFormation console.

5. Once the stack is deployed successfully, go to the AWS CloudFormation console, select your stack, and navigate to the "Outputs" tab.

![Alt text](https://github.com/trsteinmetz/AWS-CrudApiToDynamoDb/blob/main/images/output.png "Find the Endpoint to Your API")

7. Find the `ApiEndpoint` value in the "Outputs" tab. This is the endpoint for your API Gateway.

## Usage

Now that your stack is deployed and the API Gateway endpoint is available, you can start making CRUD requests to your DynamoDB table using the provided endpoint.

Here's an example using `curl` for a GET request:

```bash
curl -X GET <ApiGatewayEndpoint>/items
```

## Cleanup

To avoid incurring unnecessary costs, it's important to clean up resources when they are no longer needed. Run the following AWS CLI command to delete the CloudFormation stack:

```bash
aws cloudformation delete-stack --stack-name YourStackName
```

I hope you liked this solution. Feel free to contact me if you need to clarify some aspects of this work.
