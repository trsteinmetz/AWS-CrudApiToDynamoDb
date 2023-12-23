# API Gateway and Lambda Function for DynamoDB CRUD Operations

## Project Overview

This project provides a simple yet powerful setup for handling CRUD (Create, Read, Update, Delete) operations on DynamoDB using an API Gateway to trigger a Lambda Function. The entire infrastructure is defined and deployed using AWS CloudFormation. The Lambda Function is written in Python.

## Prerequisites

Before you begin, ensure you have the following prerequisites:

- [AWS CLI](https://aws.amazon.com/cli/) installed and configured with the necessary access permissions.
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/) familiarity.

## Deployment Steps

Follow these steps to deploy the API Gateway, Lambda Function, and DynamoDB table:

1. Clone the repository to your local machine.

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Navigate to the project directory.

    ```bash
    cd your-repo
    ```

3. Deploy the CloudFormation stack using the AWS CLI.

    ```bash
    aws cloudformation create-stack --stack-name YourStackName --template-body file://cloudformation-template.yml --capabilities CAPABILITY_IAM
    ```

4. Wait for the stack to complete deployment. You can monitor the progress in the AWS CloudFormation console.

5. Once the stack is deployed successfully, go to the AWS CloudFormation console, select your stack, and navigate to the "Outputs" tab.

6. Find the `ApiGatewayEndpoint` value in the "Outputs" tab. This is the endpoint for your API Gateway.

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

## Screenshots

Include screenshots or diagrams to visually guide users through the process. Place images in the `images` directory and reference them in the README:

```markdown
![CloudFormation Outputs](./images/cloudformation_outputs.png)
```

Feel free to replace the example image and adjust the content based on your specific project structure.
