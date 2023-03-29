# Chapter 1. Introduction to MLOps

## Rise of the Machine Learning Engineer and MLOps

"DevOps is behavior" bro preach

Critical tools and processes for ML Engineering:

- Cloud native ML platforms
  - Sagemaker, Azure ML Studio, GCP AI Platform
- Containerized workflows
  - Docker format containers, Kubernetes, private and public container registries
- Serverless technology
  - AWS Lambda, AWS Athena, Google Cloud Functions, Azure Functions
- Specialized hardware for ML
  - GPU, AWS Inferentia Elastic Inference
- Big data platforms and tools
  - Databricks, Hadoop/Spark, Snowflake, Amazon EMR, Big Query

Clear pattern of ML is how deeply tied it is to cloud computing

## What is MLOps

"if it is not automated, its broken"

The history of automation shows that humans are the least valuable doing repetitive tasks, but are the most valuable using technology as architects and practicioners

With MLOps, not only do the software engineering processes need full automation, but so do the data and modeling. The model training and development is a new wrinkle added to the traditional DevOps lifecycle. Finally, additional monitoring and instrumentation muct account for new things that can break, like data drift - the delta between changes in the data from the last time the model training occured

## DevOps and MLOps

DevOps is a set of technical and management practices that aim to increase an organizations velocity in releasing high-quality software

Benefits:

- Speed
- Reliability
- Scale
- Security

These benefits occur through adherence to the following best practices:

- Continuous Integration (CI)
  - CI is the process of continuously testing a software project and improving the quality based on these tests results. It is automated testing using open source and SaaS build dervers like GH Actions, Jenkins, Gitlab, CircleCI or cloud native build systems like AWS Code Build
- Continuous Delivery
  - This method delivers code to a new environment without human intervention. CD is the process of deploying code automatically, often though the use of IaC
- Microservices
  - Software service with a distinct function that has little to no dependencies
  - Flask is sick (FastAPI these days i reckon)
  - Containers big too
- Infrastructure as Code (IaC)
  - Process of checking the infrastructure into a source code repository and "deploying" it ot push changes to that repository
  - Allows for idempotent behavior and ensures the infrastructure doesnt require humans to build it out
  - A cloud environment defined purely in code and checked into source control is a good example use case
  - AWS Cloud Formation and AWS SAM (Serverless Application Model)
  - Multicloud services are: Pulumi and Terraform
- Monitoring and Instrumentation
  - The processes and techniques used that allow an organization to make decisions about a software systems performance and reliability
  - Through logging and other app performance monitoring tools like New Relic, Data Dog, or Stackdriver
  - These essentially collect data about the behavior of an app in production
  - This data informs how to make things better daily or weekly
- Effective Technical Communication
  - This skill involves the ability to create effective, repeatable, and efficient communication methods
- Effective Technical Project Management
  - This process can efficiently use human and technology solutions, like ticket systems and spreadsheets, to manage projects
  - Also, must be able to break down problems into small, discrete chunks of work
  - An antipattern in ml is often when a team works on one production model that solves a problem "perfectly"
  - Instead, smaller wins delivered daily or weekly is more scalable and prudent approach to model building

CI and CD are two of the most critical pillars of DevOps

- CI involves merging code into a source control repo that automatically checks the codes quality throught testing
- CD is when code changes are automatically tested and deployed, either to a staging environment or production

"A well maintained CICD system is a form of investment in the future of the team and company"

## An MLOps Hierarchy of Needs

Top

- MLOps
- Platform Automation
- Data Automation
- DevOps

Bottom

One of the major things holding back ML projects is the necessary foundation of DevOps

### Implementing DevOps

Python project scaffold

- Makefile
  - install (pip install)
  - lint (pylint)
  - test
  - run_script.py

Really should be using venv - though not exactly sure where this fits with conda

### Configuring CI with Github Actions

### DataOps and Data Engineering

- Apache Airflow
- AWS Data Pipeline, AWS Glue (serverless ETL)

Many orgs use a centralized data lake as the hub of activity around data engineering - helpful because it provides "near infinite" scale in terms of I/O coupled with high durability and availability

Data engineers build systems to handle:

- Periodic collection of data and running jobs
- Processing streaming data
- Serverless and event-driven data
- Big data jobs
- Data and model versioning for ML engineering tasks

### Platform Automation

### MLOps

#### DevOps and MLOps Combined Best Practices

The feedback loop:

- Create and retrain models with reusable ML pipelines
  - Creating a model just once isnt enough. The data can change, the customers can change, and the people making the models can change. The solution is to have reusable ML pipelines that are versioned
- Continuous Delivery of ML Models
  - Continuous delivery of ML Models is similar to CD of software. When all of the steps are outomated, including the infrastructure, using IaC, the model is deployable at any time to a new environment, including production
- Autid trail for MLOps pipeline
  - Critical
  - No shortage of problems in ML - security, bias, accuracy
  - Having an audit trail is invaluable, just like having a logging trail for regular software
- Observe model data drift, use to improve future models
  - One of the unique aspects of ml is that data can literally "shift" beneath the model
  - By monitoring data drift (the delta of changes from the last time a model train occured) it is possible to prevent accuracy problems before causing production issues

The ability to build once and deploy many times is a critical feature in modern ML operations

## MLOps Rule of 25%

- 25% DevOps
- 25% Data
- 25% Models
- 25% Business

## Exercises

[https://github.com/ltskinner/pml_1_adder](https://github.com/ltskinner/pml_1_adder)

- [x] Create a new Github repo with necessary python scaffolding using
  - [x] Makefile
  - [x] linting
  - [x] testing
  - [x] Then, perform additional steps such as code formatting in your Makefile
- [x] Using GitHub Actions, test a Github project with two or more python versions
- [x] Using a cloud native build server (AWS Code Build, Azure DevOps pipelines), perform continuous integration for your project
- [x] Containerize a Github project by integrating a Dockerfile and automatically registering new containers to a Container Registry
- [x] Create a simple load test for your application using a load test framework such as
  - [x] locust (or loader io)
  - [ ] automatically run this test when you push changes to a staging branch

## Useful Links

- Github Actions to DockerHub:
  - https://github.com/marketplace/actions/build-and-push-docker-images
  - https://docs.github.com/en/actions/publishing-packages/publishing-docker-images
- AWS ECR:
  - https://docs.aws.amazon.com/codebuild/latest/userguide/sample-docker.html
  - https://docs.aws.amazon.com/codebuild/latest/userguide/sample-ecr.html
- Locust:
  - https://github.com/marketplace/actions/locust-load-test
  - for FastAPI: https://medium.com/@ashmi_banerjee/3-step-tutorial-to-performance-test-ml-serving-apis-using-locust-and-fastapi-40e6cc580adc
- Github Actions Sequencing Jobs:
  - `need` - https://stackoverflow.com/questions/63148639/create-dependencies-between-jobs-in-github-actions
