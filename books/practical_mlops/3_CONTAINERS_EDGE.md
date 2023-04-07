# Chapter 3. MLOps for Containers and Edge Devices

## Containers

Microservice eh

"In short, containers are all about the application itself, and only what the application IS, versus what it needs to run (like dbs, etc)"

### Container Runtime

So there are docker containers, and red hat containers. Docker is just really nice cross platform

## Creating a Containers

If you want a long-running container, use `ENTRYPOINT`

### Best Practices

Checkout `hadolint`

`&&`s in a single line chain commands together in a single RUN layer

Be on lookout for vulnurabilities - use `grype` for this

### Serving a Trained Model Over HTTP

```Dockerfile
FROM python:3.7

ARG VERSION

LABEL org.label-schema.version=$VERSION

COPY ./requirements.txt /webapp/requirements.txt

WORKDIR /webapp

RUN pip install -r requirements.txt

COPY webapp/* /webapp

ENTRYPOINT [ "python "]

CMD [ "app.py" ]
```

Project Structure:

```txt
/webapp
    app.py
    model.joblib
Dockerfile
```

## Edge Devices

The general idea is that the closer the computational resources are to the user, the faster the user experience will be

### Coral

The Coral Project is a platform that helps build local (on-device) inferencing that captures the essense of edge deployments: fast, close to the user, and offline

[https://coral.ai/](https://coral.ai/)

USB Accelerator - [https://coral.ai/products/accelerator](https://coral.ai/products/accelerator)

### Azure Percept

Microsofts offering, same core concepts of Coral

### TFHub

Great resource for finding pretrained models, like ones that are designed for the edge

## Containers for Managed ML Systems

At the heart of next-gen MLOps workflows are managed ML systems like:

- AWS Sagemaker
- Azure ML Studio
- Google Vertex AI

Containers are the secret ingredient for MLOps

Containers increase the entire ML architecture quality by reducing complexity since the images are already "baked"

Intellectual horsepower can shift to other problems like data drift, analyzing the feature store for suitable candidates for a newer model, or evaluating whether the new model solves customer needs

### Containers in Monetizing MLOps

Container as a product - sell it on SageMaker marketplace

In companies looking to monetize ML, the container is an ideal package for delivering both models and algorithms to customers

### Build Once, Run Many MLOps Workflow

- Container registry (with ML microservice container)
  - Monetization
  - CLI via public container registry
  - SaaS product
  - ML Platforms (SageMaker, et al)
  - Inference
  - Training
  - Edge devices and mobile

## Exercises

- [ ] Recompile a model to work with Coral Edge TPU from TFHub
  - Use this one: https://tfhub.dev/tensorflow/mask_rcnn/inception_resnet_v2_1024x1024/1
- [ ] Use the MobileNet V2 model to perform inference on other objects and get accurate results
  - Use this: https://tfhub.dev/google/lite-model/qat/mobilenet_v2_retinanet_256/1
- [ ] Create a new container image, based on the Flask example, that serves a model and that provides examples on a GET request to interact with the model
  - [ ] Create another endpoint that provides useful metadata about the model
- [ ] Publish the newly created image to a container registry (DockerHub)

## Critical Thinking Discussion Questions

### Would it be possible to use a container to perform online predictions with an edge TPU device like Coral? How? or Why not?

### What is a container runtime, and how does it relate to Docker?

### Name three good practices when creating a Dockerfile

### What are two critical concepts of DevOps mentioned in this chapter? Why are they useful?

### Create a definition, in your own words, of what the "edge" is. Give some ML examples that can be applied
