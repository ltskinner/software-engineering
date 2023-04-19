# Chapter 7. MLOps for AWS

Which cloud do I pick? - The safe choice is Amazon

- widest selection of technology
- largest market share
- once mastering, easier to master other cloud offerings (bc they assume you know AWS)

## Introduction to AWS

They say it is always "Day 1" at Amazon, meaning the same energy and enthusiasm that happens on Day 1 should happen every day

They also place the customer at "the heart of everything"

### Contrast to Google

"This type of culture is very different than Google, which has struggled in cloud computing"

The Google culture is research-oriented with heavy academic hiring.

The benefits of this culture are open source projects like Kubernetes and Tensorflow - both complex engineering marvels

The downside is that the customer is not first in the culture, which as hurt Google in the cloud computing market share

Many organizations balk at not buying professional services and supporting something as critical as cloud computing

### Getting Started with AWS Services

Like costco, prepared food costs more money, and raw ingredients cost less

Compare the opportunity cost of doing something yourself

Cloud9 is nice because it lets you develop in the exact location where all the action takes place

#### Serverless Cookbook

Serverless is a cruicial methodology for MLOps

#### AWS CaaS

`Fargate` is a Container as a Service offering from AWS that allows developers to focus on building containerized microservices

Advantages of containers:

- Allows the developers to mimic the production service locally on their desktop
- Allows easy software runtime distribution to customers through public container registries like Docker Hub, Github Container REgistry, and Amazon Elastic Container Registry
- Allows for GitHub or a source code repo to be "source of truth" and contain all aspects of a microservice: model, code, IaC, and runtime
- Allows for easy production deployment via CaaS services

#### Computer Vision

AWS DeepLens

### MLOps on AWS

When given a ML problem with three constraints:

- prediction accuracy
- explainability
- operations

Which two would you focus on to achieve success, and in what order?

If you focus on operationalizing the model, model accuracy can improve alongside improvements in the software system

The culture of AWS supports this concept in the leadership principles of "Bias for Action" and "Deliver Results"

- Bias for Action:
  - refers to defaulting to speed and delivery results
  - focusing on the critical inputs to a business
  - delivering results quickly

## MLOps Cookbook on AWS

- Github
  - Github acitons to build containers
  - GitHub Container Registry to host container
- ML Prediction
  - Flask webapp
  - Click CLI
  - Container
- Deploy Targets
  - AWS Fargate
  - Google cloud run
  - Azure app services
  - Development Environment

Useful Files:

- Makefile
  - Both a:
    - List of recipies
    - Way to invoke those recipies
- requirements.txt
- cli.py
  - Command line shows how a ML library can be invoked from the CLI, not just via a webapplication
  - [https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/cli.py](https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/cli.py)
- utilscli.py
  - A utility that allows the user to invoke different endpoints:
    - AWS, GCP, Azure, or any production environment
  - This tool simplifies scaling inputs and scaling back outputs
  - [https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/utilscli.py](https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/utilscli.py)
- app,py
  - Application file is the Flask web microservice with the /predict endpoint
- mlib.py
  - the modal handling library does much of the heavy lifting in a centralized location
  - intentinoally very basic, and doesnt solve more complicated issues like caching loading of the model, or other production issues
  - [https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/mlib.py](https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/mlib.py)
- htwtmlb.csv
  - A csv file is helpful for input scaling
  - [https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/htwtmlb.csv](https://github.com/noahgift/Python-MLOps-Cookbook/blob/main/htwtmlb.csv)
- model.joblib
  - This model is exported from sklearn, but could easily be any other format
  - Other real-world considerations could be keeping this model in a different location like S3, in a container, or even Sagemaker
- Dockerfile
- workflow.ipynb
  - a notebook for other developers interested in playing around with the model

### CLI Tools

### Flask Microservice

A Flask ML microservice can operate in many ways

#### AWS App Runner Flask Microservice

`AWS App Runner` is a high level service that dramatically simplifies MLOps

AWS App Runner points to a source code repo, and will auto-deploy on each change to GitHub

## AWS Lambda REcipies

SAM = AWS Serverless Application Model

[https://github.com/noahgift/Python-MLOps-Cookbook/tree/main/recipes/aws-lambda-sam](https://github.com/noahgift/Python-MLOps-Cookbook/tree/main/recipes/aws-lambda-sam)

### AWS Lambda-SAM Local

### AWS Lambda-SAM Containerized Deploy

## Applying AWS ML to the Real World

Partial List of Recommended ML patterns on AWS:

- Container as a Service (CaaS)
  - For organizations struggling to get something going, CaaS is a great place to start the MLOps journey
  - A reccomended service is AWS App Runner
- SageMaker
  - For larger organizations with different teams and big data, SageMaker is an excellent platform to focus on
  - Allows for fine-grained security
  - Enterprise-level deployment and training
- Serverless with AI APIs
  - For small startups that need to move very quickly
  - Excellent initial approach to doing MLOps is to use pretrained modes via an API
  - Along with a serverless technology like AWS lambda

## Case Study: Sports Social Network

Q: What are 3-5 of the most important things to be aware of deploying and maintaining ML systems at scale?

- ML is not a one and done process. You must be committed to continually evaluating the data and the models accuracy as these change over time
- Involve SMEs early and often
- Be sure to make the busines sproblem that you are attempting to solve with ML, AND the impact of solving that problem, are as straightforward as possible
  - This will help garner maximum support form critical stakeholders
- Find your critical metric for business impact

## Case Study: Career Advice from AWS ML Evangelist

Q: 3-5

- ML is software engineering
  - best practices like: traceability, versioning, testing, automation, documentation are not optional
- Code and datasets should be versioned and traced
- Code and models should be tested
- Models should be safely deployed in production, with quality gates, and well understood strategies (canary, blue-green, etc)
- Monitoring is also critical
  - infrastructure persepctive (throughput, latency)
  - ml perspective (prediction quality, data drift)
- models should also scale up and down according to trafic

Q: 3-5 career advice

- Learn as much as you can about the business problem that youre trying to solve
  - Unless you have a deep understanding, you wont be able to call the right shots
  - What do users really care about?
  - What are the key metrics you should be watching?
  - Whats the best cost versus performance versus time to market tradeoffs
- Technology is just a tool. Mastering it for its own sake or to beef up your resume is pointless
- Obsess over automation
- Make sure you have your security covered

## Conclusion

- Engage with AWS Enterprise Support
- Get your team certifies on AWS starting with AWS Solutions architect or Cloud Practicioner exam, and AWS Certified ML Specialty
- Obtain quick wins by using AI APIs like AWS comprehend, AWS Rekognition, and high-level PaaS offerings like AWS App Runner or AWS Lambda
- Focus on automation and ensure that you automate everything you can
  - From data ingestion and the feature store
  - To modeling and deployment of the ML model
- Start using SageMaker as an MLOps long-term investment and use it for longer term or more complex projects alongside more accessible solutions

## Exercises

- [x] Build a ML CD pipeline for a flask webservice using Elastic Beanstalk [link](https://github.com/noahgift/Flask-Elastic-Beanstalk)
  - OK so Elastic Beanstalk is good for deploying web applications and services
  - ECS is good for orchustrating containers
- [ ] Start an Amazon SageMaker instance and build and deploy the AWS example for "US census data for the population segmentation example"
- [ ] Build a CaaS ML prediction service using AWS Fargate [link](https://github.com/noahgift/eks-fargate-tutorial)
- [ ] Build a serverless data engineering prototype [link](https://github.com/noahgift/awslambda)
- [ ] Build a computer vision trigger that detects labels [link](https://github.com/noahgift/serverless-cookbook/blob/main/aws-lambda-image-label-s3-trigger.py)
- [ ] Use the MLOps Cookbook base project and deploy it to as many different targets as you can:
  - [ ] Containerized CLI
  - [ ] EKS
  - [ ] Elastic Beanstalk
  - [ ] Spot Instances
  - [ ] Anything else you can think of

## Critical Thinking Discussion Questions

- Why do organizations do ML using a datalake? What is the core problem they solve?
- What is a use case for using prebuild models like AWS Comprehend, versus training your sentiment analysis model?
- Why would an organization use AWS SageMaker vs Pandas, sklearn, Flask, and Elastic Beanstalk? What are the use cases for both?
- What are the advantages of a containerized machine learning model deployment process?
- A colleague says they are confused about where to start with ML on AWS due to the variety of offerings. How would you recommend they approach their search?
