# Chapter 5. Design Patterns for Resilient Serving

## Design Pattern 16: Stateless Serving Function

Makes it possible for production ML systems to synchronously handle thousands to millions of prediciton requests per second

A stateless function is a function whose outputs are determined purely by its inputs

Because stateless components dont have any state, they can be shared by multiple clients

Tensorflow uses TensorFlow Serving

PyTorch uses TorchServe

### Prediction Library

So instead of having one endpoint serve one model, have one endpoint import the appropriate model from a library to perform inference with

Here, a library function is better than a microservice if the model cannot becalled over the network. Note this places computational burden on the client

## Design Pattern 17: Batch Serving

Uses software infrastructure commonly used for distributed data processing to carry out inference on a large number of instances all at once

Typically asynch

## Design Pattern 18: Continued Model Evaluation

Handles the common problem of needing to detect and take action when a deployed model is no longer fit-for-purpose

- How do you know your model is working as expected in the wild?
- What if there are unexpected changes in the incoming data?
- What if the model no longer produces accurate or useful predictions?
- How will these changes be detected?

Two main reasons models degrade over time:

- Concept drift: when the relationship between model inputs and targets have changed
  - often happens because underlying assumptions of the model have changed
- Data Drift: any change that has occured to the data being fed to the model for prediction as compated to the data that was used for training
  - input data schema changes (fields added or removed)
  - feature distributions change over time
  - meaning of data has changed

The most direct way to identify model deterioration is to continuously monitor model predictive performance over time, and assess that performance with the same eval metrics used during development

Important to keep in mind how the feedback loop of model predicitons and capturing ground truth might affect training data down the road - do not violate assumptions of the context in which the model will make predictions in the wild

Trigger retrains when accuracy falls below some threshold

Or, schedule retrains

## Design Pattern 19: Two-Phase Predictions

Provides a way to address the problem of keeping large, complex models performant when they have to be deployed on distributed devices by splitting the use cases into two phases, with only the simpler phase being carried out on the edge

Example:

- phase 1: "hey google" or "ok google"
- phase 2: "can you schedule a meeting with Sara at 10 am?"

Typically, the phase 1 model is really light and meant to be executed at the edge, like a phone or whatever. Must operate in an offline manner, while phase 2 could be online and rely on cloud infrastructure accessed via network

## Design Pattern 20: Keyed Predictions

Normally, you train a model on the same set of input features that the model will be supplied in realtime when it is deployed. However, it can be advantageous for you model to pass though a client-supplied key

Have the client supply a key associated with each input

- so, clients supply
  - (key, f1, f2, f3)
- and get back
  - (key, pred)

The client will now be able to figure out which output instance corresponds to which input instance. Handles cases where reponses are sent out of order, like in asynch applications
