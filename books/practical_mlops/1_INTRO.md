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
  - [x] automatically run this test when you push changes to a staging branch FROM LEFT FIELD THE SOLUTION APPEARS

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

## Critical Thinking Discussion Questions

### What Problems does a continuous integration system solve?

Solves several problems, the main one for me is you should never walk away from a codebase that is non-operable, and with ci you can automatically test your stuff and make sure the tests pass. Its no guarantee that you even have tests, or that the tests are good and applicable, or even still relevant, BUT it is one less thing to worry about. Plus, outside of the python-sphere if you actually have to build, like not having to run gcc deez nutz is really nice. Also, from this chapter, the resurfacing of the makefile as an abstraction to simple tasks like installing, linting, testing, etc is super nice because you dont have to off the top of your head type out all the syntax - you just have to remember the make recipie names, which are things you can keep common across multiple projects (all projects really, akin to std file structures). Plus, with true cloud integrated cicd, everything runs in one place and you dont have to worry about local compute. Scaling this to dev TEAMS, consolidating the work of everyone into one single indisputable environment is CRITICAL to ensure the software really is working as expected. The formalizaiton of envirionment creation is also a precursor to effective cd because you can just lift n shift the env and theoretically not worry about any differences between dev, test, and prod, though in actuality, automatically testing what you "deploy" to test and or "prod" is also underpinned by all the bits that make CI work

### Why is a CI system an essential part of both a SaaS software product and an ML system?

Under the premise that SaaS = web-based software, like your product is web and network enabled, so relying on the network to deploy your web product is not a far put. While it is not ESSENTIAL that you have a CI system to deploy SaaS, in many ways it lets you use the same tool that your end users will be using to reach your product. Breaking out of the SaaS nitty gritty, I would actually argue it is not essential to deploy SaaS software or an ML system, BUT to deploy it reliably, safely, consistenly, and with minimal hassle it is a precursor for certain. On one end of the spectrum, with no automation and no ci, you are EXPENSING developer hours to make changes and maintain/test/etc the system, whereas when you stand up proper CI you are INVESTING developer hours, which is a critical distinction

### Why are cloud compute platforms the ideal target for analytics applications?

Theres a couple good reasons, on the developer side of things, you can work from trash workstations but still get dank compute, and you can get every developer on the same compute. The opportunity to create automations that impact all developers is much greater in a shared environment (the cloud), though working from a non-aws, azure, gcp, datacenter you could still yield the same benefits. While cloud is technically a computing paradim and is by no means limited to aws et al, I believe in this context, and the context of the book, "the cloud" is in reference to the big three that have the descriminators of being dedicated compute providers with extensive software infrastructure to support developers. So, anyways, specialized teams of professionals who spend their entire workweeks optimizing and maintaining compute for you to use is much better than, basically anything a non-them company could muster realistically. OK, back to why they are good for analytics applications - on the operations side of things one of the big reasons cloud is apex is sCalAbiLItY. Analytics applications implicitly are data applications, and data can get quite large, so operating under the assumption that you wont run out of compute, storage, or io is a really nice assmuption to be able to make. Furthermore, all of the traditional application success measures, uptime, latency, etc are dramatically enhanced when run in the cloud because of redundancy, distribution of compute and all that jazz

### How do data engineering and DataOps assist in building cloud-based analytics applications?

Well, data engineering and dataops assist regardless of if you are in the cloud or not, and I assume in this context, data engineering and dataops refers more to the tools than the paradigm, so ill focus on that. Basically data engineering and dataops tools running in the cloud are nice because you can schedule jobs to run whenever, you have access to unlimited compute and storage, and you can have lots of people supporting different parts of the pipeline. Any analytics (and therefore data driven) applications are worthless without secure, reliable, trustworthy, correct, and timely data, and everything about the cloud supports these hard quality attribute requirements

### How does deep learning benefit from the cloud?

Uhh focusing on the scope of PURE deep learning, with no deployment considerations, cloud providers have dank compute and a wide spectrum of it. On one extreme, if you need minimal compute, you can use minimal compute, and on the other extreme if you need a ton of compute (32 GPUS for a month) you can just use it. By the time youre done training there will probably even be a better compute tier available ;p whereas if you bought the compute required (all of it) thats an asset your company has to manage and will want to milk roi on, and towards the end of life, milk at the expense of develors who need something different. Imagine buying those 32 gpus, and then it turns out you actually needed 64 to complete training in the month timeline, youre SOL and gotta deal with your 32 gpus for 2 months now, the whole deal is botched. Factoring in data considerations, blob stores are OP and automating your feature extraction pipelines to support round the clock training just isnt possible for that volume and availability from a local workstation realistically

### Is deep learning feasible without cloud computation?

Yes for sure but youre handicapped. I mean it def depends on the value proposition of the project you are doing, like there are absolutely use cases where you just wanna putz around local and let something run on your laptop while you go to the gym or something but thats kinda like 2020s deep learning, like the fatty models these days really really require the cloud

### Explain what MLOps is and how it can enhance a ml engineering project?

Honestly i probably didnt read the formal definition but mlops is basically an extension of DevOps into the ML domain for ML specific workflow tasks. Underpinned by automation and cloud tools, basically starting at the first steps of the workflow you can automate data management and wrangling stuff, including etl stacks, feature extraction pipelines, etc. It enables reproducible and hands off retraining of models and collection, storage, access of evaluation metrics, as well as model versioning and storing metadata on the training sets etc to support audits and all that. From a deployment standpoint, it enables batch and streaming workflows easily, and other web-dev driven concepts like ab testing, blue green testing, etc. Kinda dumb, but being in the cloud hugely enables teams of developers to all actively contribute, so under the kaizen umbrella, lots of people making minor improvements up and down the stack has a compounding positive impact. Again, this is all assuming MLOps as an extension of the core utility of DevOps, which manages the raw codebase and environment details so I wont rehash those
