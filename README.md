# Devops Technical Interview #1

### 1. Write an example of AWS CloudFormation YAML template to create an S3 bucket and an EC2 instance

The [file](./sc-ec2-s3.yaml) contains a sample template when uploaded to the aws cloud formation creates both EC2 and S3 bucket instances.

The template creates an EC2 instance ScriptChainEC2 in the availability zone coded "ap-south-1a" and instance type "t2.micro" with the image ID of an ubuntu 24.04. Along with it the template also creates an S3 bucket instance ScriptChainS3 with all the public access policies set to false. 

### 2. Write a sample GitLab CI/CD YAML configuration to build, test, and deploy a Node.js application.

The [gitlab ci/cd pipeline yml file](./.gitlab-ci.yml) contains different components like image, stages, and cache. Each stage contains relevent instructions to build, test and deploy a simple nodejs application.

[Link](https://gitlab.com/interview2711622/nodejs_cicd) to the gitlab repository.

### 3. Write a sample package configuration in python to build an AWS lambda function

The [python file](./aws_lambda.py) contains the defination of a lambda function along with importing basic libraries like json and os. This when zipped and uploaded to the AWS Lambda builds an AWS lambda function.
