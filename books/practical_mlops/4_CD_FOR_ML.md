# Chapter 4. Continuous Delivery for Machine Learning Models

Injuries require a war strategy; giving up and quitting is not an option

There is always an option, and creativity is as important as trying to recover fully

Pain is not a foe - it is an indocator that helps you decide to keep doing what you are doing, or stop and rethink your current strategy

Constant evaluation, making changes and adapting to the feedback, and applying new strategies to achieve success is exactly what continuout integration and continuous delivery are about

## Packaging for ML MOdels

Containers

Characteristics of packaging ML models into containers:

- As long as a container runtime is installed, it is effortless to run a container locally
- There are plenty of options to deploy a container in the cloud, with the ability to scale up or down as needed
- Others can quickly try it out with ease and interact with the container

## Infrastructure as Code for Continuous Delivery of ML Models

"We tend to grow easily accustomed to things being manual (and complex!), but there is always an opportunity to automate"

Can mount model weights to azure (and likely aws and gcp), and then send those weights there from your ci pipelines

When building pipelines, identify *greedy steps* - ones that are trying to do too much and have lots of responsibility

### Steps for Packaging a model

- 1. Check out the current branch of the repository
- 2. Authenticate to Azure Cloud
- 3. Configure auto-install of Azure CLI extensions
- 4. Attach the folder to interact with the workspace
- 5. Download the ONYX model
- 6. Build the container for the current repo

## Using Cloud Pipelines

A pipeline is nothing more than a set of steps (or instructions) that can achieve a specific objective like publishing a model into production

Tip for operationalizing ML:

- Consider making any operation more straightforward for a future failure situation
- Avoid being tempted to go fast and get a pipeline deployed and running in a single step (because it is easier)
  - Take your time to reason about what would make it easier for you (and others) to build ML infrastructure
  - That way, when failures happen, it is easier to go find problems and fix them
- Apply tot concepts of CI/CD to improvement itself: continuous evaluation and improvement of processes is a sound strategy for robust environments

### Controlled Rollout of Models

Come from web service deployments

Two strategies:

- Blue-green deployment
- Canary deployment

#### Blue-green

- Incoming traffic either goes to the "new" blue version, or the "old" green version
- Dont go whole hog lol do some verification before routing everything to new
- Some issues tho, can be complicated to replicate production environments
- Basically, use k8s

#### Canary

- More involved and riskier
- Traffic is routed progressively to the newer model, at the same time the previous model is serving predictions

`from azureml.core.webservice import AksEndpoint` - does some canary stuff

### Testing Techniques for Model Deployment

When you send an HTTP request to the container, several software layers are required:

- Client sends an http request, with a json body, in the form of an array with a single string
- A specific http port and endpoint have to exist to get routed to
- The flask application has to receive the json payload and load it into native python
- The onyx runtime needs to consume the string and produce a prediction
- A json response with an http 200 response needs to contain the boolean value of the prediction

Every single one of these steps can (and should) be testes

#### Automated Checks

- valid json request
- json response
- invalid json request
- health endpoint
- port and endpoint

#### Linting

The earlier you can identify a code problem, the better

Linters catch the first instance of an issue

#### Continuous Improvement

## Exercises

- [x] Create your own Flask application in a container
  - [x] Publish it to a github repo
  - [x] Document it thoroughly
  - [x] Add GitHub Actions to ensure it builds correctly
- [x] Make changes to the ONNX container so that it pushes to DockerHub instead of GitHub Packages
- [ ] Modify a SageMaker pipeline so it prompts you before registering the model after training it
- [ ] Using the Azure SDK, create a Jupyter notebook that will increase the percentile of traffic going to a container

## Critical Thinking Discussion Questions

- Name at least four critical checks you can add to verify a packaged model in a container is built correctly
- What are the differences between a canary and blue-green deployments? Which one do you prefer? Why?
- Why are cloud pipelines useful versus github actions? Name at least three differences
- What does *packaging a container* mean? Why is it useful?
- What are three characteristics of package machine learning models?
