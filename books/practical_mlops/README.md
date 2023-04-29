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

## [Chapter 4. Continuous Delivery for Machine Learning Models](./4_CD_FOR_ML.md)

## [Chapter 5. AutoML and KaizenML](./5_AUTOML.md)

- Rules without Ideas is prison
- Ideas without Rules is chaos
- Bonsai teaches us balance
- Balancing rules against innovation is a pervasive problem in all of life

"Difficulty, or lack therof, doe snot equate with completeness or realness"

"MLOps: you dont need to build it to use it"

Dont self-handicap lmao

### AutoML Flavors

- Apple
- Google
- Azure
- AWS - SageMaker AutoPilot
- Open Source
  - Ludwig
  - FLAML - Fast and Lightweight AutoML

Yknow bro, id probably be much more rigorous in evaluating models if I wasnt so involved in building them haha

## [Chapter 6. Monitoring and Logging](./6_MONITORING_LOGGING.md)

"Before becoming a {something specific}, you must become a {general precursor}"

## [Chapter 7. MLOps for AWS](./7_MLOPS_FOR_AWS.md)\

"Compare the opportunity cost of doing something yourself"

## [Chapter 8. MLOps for Azure](./8_MLOPS_AZURE.md)

**ALWAYS ENSURE AUTHENTICATION IS DONE CORRECTLY. DO NOT TRY TO SKIP OR WORK AROUND THESE RESTRICTIONS, EVEN WHEN ITS AN OPTION**

### Troubleshooting Deployments

- Do not ever assume things.
- Question everything.
- Pay attention to deteails.
- Trust, but verify.

## [Chapter 9. MLOps for GCP](./9_MLOPS_GCP.md)

Cons:

- fewer practicioners
- part of "surveillance capitalism" - "sv and other corps mining users information to predict and shape behavior"
- google has reputation for:
  - poor user and customer experience
  - frequently abandons products (like hangouts and plus)
  - so, if gcp continues to be the third-best optoin, will they discontinue it?

Pros:

- good at creating things that work at "planet scale"

## [Chapter 10. ML Interoperability](./10_ML_INTEROPERABILITY.md)

Use ONNX

## [Chapter 11. Building MLOps Command Line Tools and Microservices](./11_MLOPS_CLI_MS.md)

## [Chapter 12. ML Engineering and MLOps Case Studies](./12_ML_CASE_STUDIES.md)

## Example Cleanup

- [ ] GCP
  - VertexAI - def do not forget about this lol
  - Absolutely NUKE **everything** in GCP, will never, ever use this and will actively avoid GCP shops when job hunting lmao
  - [how to delete](https://stackoverflow.com/questions/52408422/delete-all-resources-in-a-google-cloud-project#:~:text=Simply%20go%20to%20%22IAM%20%26%20Admin,%2C%20see%20the%20billing%2C%20etc.)
- [ ] Azure
  - [ ] App Service is biggest one
  - [ ] Then Pipelines
- [ ] AWS
  - [ ] [Sagemaker Resources](https://catalog.workshops.aws/sagemaker-studio-emr/en-US/08-clean-up)

## Some Closing Remarks

### Book Itself

Enjoyed the exercises and discussion questions thoroughly

The "personal stories" about stuff unrelated to work were inessential tho

### Cloud Platforms

GCP is cancer

AWS is still pog for most things, sagemaker is a whole ass beast tho

Azure ML ecosystem is much more user friendly, tho doesnt always work. The workflows are super intuitive, but it doesnt always work. I love the idea of Azure ML, and the automl is actually really good, but just enough hops, skips, and jumps to where I wouldnt feel comfortable migrating existing services on AWS over

The docs also seem to be like really, really up to date, which is a little concerning. Like the interfaces and sdks are definitely under constant development, which I dont love, I like things more stable. BUT, that said, with the rapid iteration, I think the Azure ML ecosystem long term will be better than sagemaker and I will certainly prioritize Azure ML for my next ML engagement

But for now, the simplicity and unified portal for AWS is unbeatable, truly. Much smaller delta from dev env to prod env with it
