# Practical ML Ops

Current problems with ML:

- Focus on the "code" and technical details vs the business problem
- Lack of automation
- HiPPO (Highest Paid Persons Opinions)
- Not cloud native
- Lack of urgency to solve solvable problems

## [Chapter 1. Introduction to MLOps](./1_INTRO.md)

Example repo: [https://github.com/ltskinner/pml_1_adder](https://github.com/ltskinner/pml_1_adder)

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

**Clear pattern of ML is how deeply tied it is to cloud computing**

"if it is not automated, its broken"

DevOps is a set of technical **and** management practices that aim to increase an organizations velocity in releasing high-quality software

"A well maintained CICD system is a form of investment in the future of the team and company"

### MLOps Feedback Loop

- Create and retrain models with reusable ML pipelines
- Continuous Delivery of ML Models
- Audit trail for MLOps pipeline
- Observe model data drift, use to improve future models

### MLOps Rule of 25%

- 25% DevOps
- 25% Data
- 25% Models
- 25% Business

## [Chapter 2. MLOps Foundations](./2_FOUNDATIONS.md)

### Bash and the Linux Terminal

Better way to think about the terminal is the "advanced settings" of the environment you are working on: the cloud, ml, or programming - if you need to do the advanced tasks, it is the way to perform it

## [Chapter 3. MLOps for Containers and Edge Devices](./3_CONTAINERS_EDGE.md)

Containers are the secret ingredient for MLOps

Containers increase the entire ML architecture quality by reducing complexity since the images are already "baked"

Intellectual horsepower can shift to other problems like data drift, analyzing the feature store for suitable candidates for a newer model, or evaluating whether the new model solves customer needs

### Containers in Monetizing MLOps

Container as a product - sell it on SageMaker marketplace

In companies looking to monetize ML, the container is an ideal package for delivering both models and algorithms to customers
