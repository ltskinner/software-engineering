# Chapter 10: Infrastructure and Tooling for MLOps

Main layers:

- Storage and compute
- Resource management
- ML platform
- Development environment

## Storage and Compute

Storage layer: hdd, ssd, s3, snowflake, on prem, private data center, cloud

Compute layer: single cpu core, single gpu core

Compute can be sliced into smaller compute units to be used concurrently

There are compute layers that abstract away notions of cores, and use other units of computation:

- "job" for Spark and Ray
- "pod" for kubernetes (a wrapper around containers)
  - can have multiple containers in a pod, but cant start and stop containers independently within a pod

Compute units are primarily characterized by:

- how much memory
- how fast it runs an operation

Use MLPerf, benchmarks hardware vendors

### Public Cloud vs Private Data Centers

- multicloud strategy is goood for mitigating dependence on sole providor

## Development Environment

### Dev Environment Setup

Standard stack:

- git for code
- DVC for versioning data
- Weights & Biases or Comet.ml to track experiments
- MLFlow to track artifacts of models
- Claypot AI working on becoming one stop shop

#### IDE specific stuff

Infrastructure tools for making notebooks more useful:

- Papermill:
  - spawns multiple notebooks with different parameter sets
- Commuter:
  - notebook hub for viewing, finding, sharing notebooks within an org

### Standardizing Dev Environments

### From Dev to Prod: Containers

Lol, i guess this stuff really isnt intuitive for most ml people

## Resource Management

### Cron, Schedulers, Orchestrators

Key characteristics: repetitiveness and dependencies

Schedulers are cron programs that can handle workflow dependencies, actions taken for certain conditions

Use Kubernetes

### Data Science Workflow Management

Generally, alow you to specify workflows as DAGs

- python or yaml (config files)

Most common tools: Airflow, Argo, Prefect, Kubeflow, Metaflow

## ML Platform

General aspects to keep in mind when selecting:

- Whether tool works with your cloud provider or allows you to use on your own datacenter
- Whether its open source or a managed service

### Model Deployment

- a deployment service can help with both pushing out models and dependencies, as well as exposing models as endpoints
  - AWS Sagemaker
  - GCP with Vertex AI
  - Azure with Azure ML
  - Alibaba with Machine Learning Studio

### Model Store

Artifacts should store (model card)

- Model definition
  - create model shape, loss function, hidden layers, params per layer
- Model parameters
  - actual parameters of the model
  - combined with models shape to re-create the model
- Featurize and predict functions
  - given a prediction request, how do you extract features and input these features into the model to get back a prediction
  - usually wrapped in endpoints
- Dependencies
  - software
- Data
  - pointers to data location and stuff like that
- Model generation code
  - specific code for how model was created
    - framework
    - how trained
    - details on train/valid/test split
    - number of experiments run
    - range of hyperparameters considered
    - actual set of hyperparameters in final model
- Experiment artifacts
  - graphs like loss curve
  - raw numbers on performance against test set
- Tags
  - help with model discovery and filtering
  - owner, task, stakeholders

### Feature Store

Feature store solution should address:

- Feature management:
  - often, features used for one model may be useful in another model
  - think of as a `feature catalogue`
- Feature computation
  - actual logic, english or actual executables
  - notes on how expensive and complex
  - feature store can act as a data warehouse if actually performs calcs
- Feature consistency
  - validate calcs

Feast is best open source feature store, but batch only

## Build vs Buy

Things to consider when performing eval:

- The stage your company is at
  - Are you a noob or more mature?
- What you believe to be the focus, or the competitive advantage of the company
  - "if its something we want to be really good at, then make. else, vendor"
- The maturity of available tools
  - if cots is kinda buns and doesnt really solve your problem, look into building
  - avoid "integration hell" - spending more time integrating an external platform than it would have taken to build internal
