# Practical ML Ops

Current problems with ML:

- Focus on the "code" and technical details vs the business problem
- Lack of automation
- HiPPO (Highest Paid Persons Opinions)
- Not cloud native
- Lack of urgency to solve solvable problems

## [Chapter 1. Introduction to MLOps](./1_INTRO.md)

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
