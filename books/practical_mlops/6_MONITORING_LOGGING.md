# Chapter 6. Monitoring and Logging

Both logging and monitoring are core pillars of DevOps that are cruicial to robust ML practices

## Observability for Cloud MLOps

## Introduciton to Logging

Ngix webserver comes with default configuration for:

- access logs at `/var/log/ngix/access.log`
- error logs at `/var/log/ngix/error.log`

## Logging in Python

### Modifying Log Levels

Fine tuning between info or error is only something you can do progressively

### Logging Different Applications

Whats useful today can be information overload tomorrow

## Monitoring and Observability

### Basics of Model Monitoring

Types of metrics found in most metric-capturing systems:

- Counter
  - Counting any type of item
- Timer
  - How long something will take
- Value
  - Just saving the literal value of something

Two operations specific to ML that cloud providers should monitor and capture useful metrics on:

- target dataset
- baseline dataset

### Monitoring Drift with AWS SageMaker

### Monitoring Drift with Azure ML

"Before becoming a {something specific}, you must become a {general precursor}"

## Exercises

- [ ] Use a different dataset and create a drift report with violations using AWS SageMaker
- [x] Add Python logging to a script that will log errors to STDERR, info statements to STDOUT, and all levels to a file
- [x] Create a time-series dataset on Azure ML Studio
- [x] Configure a dataset monitor in Azure ML Studio that will send an email when a drift is detected beyond the acceptable threshold
  - To analyze existing data, cannot greater than 31 calendar days
  - Also, must have at least 50 samples in range
  - Implies >2 samples per day to work

## Critical Thinking Discussion Questions

- Why might it be desirable to log to multiple sources at the same time?
- Why is it critical to monitor data drift?
- Name three advantages of using logging facilities vs print() or echo statements
- List the five most common log levels, from least to most verbose
  - critical
  - error
  - warning
  - info
  - debug
- What are three common metric types found in metric capturing systems?
