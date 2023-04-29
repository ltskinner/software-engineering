# Chapter 8. MLOps for Azure

## Azure CLI and Python SDK

## Authentication

Authentication should be one of the core pieces of automation when dealing with services

Azure has a *service principal* for access (and access control) to resources

When automating services and workflows, people tend to overlook or even attempt to simplify authenticating in general. Common to hear reccos like:

- just use root user
- just change file permissions so anyone can write an execute

ALWAYS ENSURE AUTHENTICATION IS DONE CORRECTLY. DO NOT TRY TO SKIP OR WORK AROUND THESE RESTRICTIONS, EVEN WHEN ITS AN OPTION

### Service Principal

### Authenticating API Services

Other envs might not benefit from a service principal account (like services exposed to the internet, providing interaction with deployed models via HTTP) - in these cases, need to decide the type of auth to be enabled

Before deploing a model or even configuring any settings for getting amodel into production, you need to have a good idea about the different security features available to you

Azure offers different ways to authenticate, essentially:

- keys
- tokens

Azure Kubernetes Service (AKS) and Azure Container Instances (ACI)

- Key-based auth:
  - AKS has key-based auth enabled by default
  - ACI has key-based auth disabled by default (but can be enabled). No authentication is enabled by default
- Token-based authentication:
  - AKS has token-based auth disabled by default
  - ACI does not support token-based auth

## Compute Instances

Azure has a definition for compute instances that describes them as a "managed cloud-based workstation for scientists"

- lets you get started very quickly with everything you might need for performing MLOps in the cloud

## Deploying

### Registering Models

Versioning is very git-like and natural

- identify which model version you are using
- can quickly select from the various versions, with clarity from descriptions
- you can rool back and select a different model without effort

### Versioning Datasets

Similar to registering models, the ability to version a dataset solves one of the biggest problems in ML today: enormous datasetst that differ slightly are hard to version nicely

## Deploying Models to a Compute Cluster

### Configuring a Cluster

Two types:

- Inference cluster
  - k8s behind the scenes
- Compute cluster
  - virtual machines

Typically use compute cluster to try different strategies

Cruicial to match workload to the size (and quantity) of machines doing the work

For ex. in a compute cluster, you must determine the min number and max nubmer of nodes

For the test run, best to start with less, and create clusters with more power as needed

Tip: choose 0 as min number to prevent getting charged for idle nodes

### Deploying a Model

Azure Container Instance (ACI)

- best for testing and test environments in general
  - specifically if under 1gb in size

Azure Kubernetes Service (AKS)

- all benefits of k8s (scaling in particular)
  - good for models larger than 1gb

## Troubleshooting Deployment Issues

- Do not ever assume things.
- Question everything.
- Pay attention to deteails.
- Trust, but verify.

### Retrieving Logs

Application Insights

### Debugging Locally

Want to avoid situations where the only option is to "log into prod and see whats goin on"

## Azure ML Pipelines

Azure describes its ML pipelines as a good fit for:

- machine learning
- data preparation
- application orchustration

### Publishing Pipelines

### Azure ML Designer

## ML Lifecycle

## Exercises

- [ ] Retrieve and ONNX model from a public source and register it in Azure with the python sdk
- [ ] Deploy a model to ACI and create a python script that returns the models response, as it comes back from the HTTP API
- [ ] Deploy a container locally, using Azures pythong sdk, and produce some HTTP requests for live inferencing
- [ ] Publish a new pipeline, and then trigger it. The trigger should show the output of the run_id after a successful request
- [ ] Train a model using Azure AutoML from the python sdk by grabbing a dataset from kaggle

**Did modified workflow that checked functional boxes I wanted to learn/practice**

## Critical Thinking Discussion Questions

- There are many ways to train models on the Azure platform: Azure ML Studio Designer, Azure Python SDK, Azure notebooks, and Azure AutoML. What are the advantages and disadvantages of each?
- Why is it a good idea to enable authentication?
- How can reproducible environments help deliver models?
- Describe two aspects of good debugging techniques and why they are useful?
- What are some benefits of versioning models?
- Why is versioning datasets important?
