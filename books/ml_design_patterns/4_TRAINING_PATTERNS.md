# Chapter 4. Model Training Patterns

## Typical Training Loop

### Stochastic Gradient Descent

Extensions like Adam and Adagrad

### Training Design Patterns

Have something to do with modifying the typical training loop

## Design Pattern 11: Useful Overfitting

Where we dont generalize the model because we want to intentionally overfit on the dataset

Do by not regularizing, not using dropout, and not using validation for early stopping

Physical systems where you can model the system mathematically make for good overfitting. Using a precise model can be too slow, and a ML model might be a good enough approximation

In the scenario where you can generate training data over the entire state space, there will be no "unseen" data

Overfitting is useful when these conditions met:

- There is no noise, so the labels are accurate for all instances
- You have the complete dataset, thus, overfitting becomes interpolating the dataset

Can also be useful in distilling the knowledge of a large model to a smaller more compact one. Here, the small model learns from data labeled by the large model

Overfitting is also a good sanity check - complex models should be able to overfit on a small enough batch of data

Overfitting goes beyond a batch. From a more holistic perspective, overfitting allows the general advice given wrt regularization: The best fitting model is a large model that has been properly regularized. So, if your NN cant overfit the training set, you should be using a larger one. Then, once you have a large model that overfits the training set, you can apply regularization to improve the validation accuracy, even though training accuracy may decrease

## Design Pattern 12: Checkpoints

Here we store the full state of the model periodically so that we have partially trained models available

Using regularization instead of early stopping is good because early stopping requires you to sacrifice 10-20% of your dataset to decide when to stop training

## Design Pattern 13: Transfer Learning

Take part of a previously trained model, freeze the weights, and incorporate the non-trainable layers into a new model that solves a similar problem, but on a smaller dataset

## Design Pattern 14: Distribution Strategy

The training loop is carried out over multiple workers, often with caching, hardware acceleration, and parallelization

Accomplished via data parallelization, or model parallelism

### Synchronous Training

- Workers train on different slices o finput data in parallel, and the gradient values are aggregated at the end of each training step
  - A central server holds the most up to date copy of the model aprameters, and performs the gradient step according to the gradients received from the multiple workers

### Asynch Training

Workers train on different slices of input dataindependently

Model weights and parameters are updated asynch, typically through a `parameter server architecture`

The key difference is that the parameter server does not do an all-reduce. Instead, it computes the new model parameters periodically based on whichever gradient updates it received since the last computation

Typically, asynch achieves higher throughput than synch because dont have to wait for slow shards

### Model Parallelism

- For when you have a nn too large to fit in the memory of a single device

## Design Pattern 15: Hyperparameter Tuning

The training loop itself is inserted into an optimization method to find the optimal set of model hyperparameters
