# Chapter 8: Data Distribution Shifts and Monitoring

"Deploying the model isnt the end of the process"

## Causes of ML System FAiilures

Failure state: when one or more expectations of the system is violated

In traditional software, generally onely care whether system executes its logic within the expected operational metrics (latency, thruput)

For ML system, care about operational metrics as well as ML performance metrics

Operational expectation violations are easier to detect

ML violations are hard because gotta measure and monitor

### Software System Failures

Failures that would have happened to non ML systems

- Dependency failure:
  - Software package or codebase that your system depends on breaks, which leads your system to break
  - Common when dependency is managed by a third party
- Deployment failure
  - Causes by deployment errors, like when accidentally deploy old version of binaries, or wwhen systems dont have correct read/write access
- Hardware failures
  - When cpus or gpus shit out
- Downtime or crashing
  - If a component of the system runs on a server, and the server is down, the whole system is down

### ML-Specific Failures

- data collection and processing problems
- poor hyperparameters
- changes in training pipeline not replicated in the inference pipeline (and vice versa)
- data distribution shifts, causing models performance to deteriorate over time
- edge cases
- degenerate feedback loops

Three new ones focused on (the last 3)

#### Production data differing from training data

The assumption is that unseen data comes from a *stationary* distribution that is *the same* as the training data distribution

BAD assumption - training sampling can and usually is biased, and the real world is certainly not stationary

Shifts can happen suddenly, gradually, or seasonally. They can be:

- even driven (news, brand change, new products, etc)
- socially driven (new norms, new trends)
- seasonal

#### Edge Cases

Blue Whalesss

Edge Cases vs Outliers:

- outlier: a sample that differs significantly from other examples
- edge cases: refer to performance, an example where a model performs significantly worse than other examples

Outliers can become edge cases, but not all outliers are edge cases

#### Degenerate feedback loops

When predictions themselves influence the feedback, which in turn, influences the next iteration of the model

These are created when a systems outputs are used to generate the systems future inputs

These are **especially** common in tasks with natural labels (recommenders, and click thru predictions)

##### Detecting degenerate feedback loops

Hard, lol

For recommenders, measure popularity diversity of a systems outputs even when the system is offline

- aggregate diversity
- average coverage of long-tail items

Low scores mean that outputs of the system are homogenous, which might be caused by popularity bias

##### Correcting degenerate feedback loops

First, use randomization

- improves diversity, but at cost of user experience
- can use intelligent exploration strategy to increase item diversity with an acceptable prediciton accuracy loss

Second, use positional features

- if the position in which a prediction is shown affects its feedback, encode how this is shown as a feature
  - some people always click first vid, even if 2-4 are actually more to their taste
- a more sophisticated approach would be to use two different models
  - first model predicts proba that user will see and consider rec taking into account position
  - second model predicts probability user will click given they did see and consider it (dont use position)

## Data Distribution Shifts

`source distribution` and `target distribution`

### Types of Data Distribution Shifts

- Covariate shift:
  - When P(X) changes but P(Y|X) remains the same.
  - This refers to the first decomposition and of the joint distribution
- Label shift:
  - When P(Y) changes but P(X|Y) remains the same.
  - This refers to the second decomposition of the joint distribution
- Concept drift:
  - When P(Y|X) changes but P(X) remains the same.
  - This refers to the first decomposition of the joint distribution

#### Covariate shift

`Covariate` is independent variable that can influence the outcome of a given statistical trial, but is not of direct interest

- how does location affect housing price?
  - house price is direct variable
  - square footage affects this
  - sf is a covariate

In supervised ML, the label is the variable of direct interest, and input features are covariate variables

Causes:

- sample selection bias
- when training data is artificially alered to make easier for model to learn (over, undersampling)
- learning process, expecially through active learning

In production, usually due to:

- changes in the environment
- changes in how application is used

If you know in advance how the real-world input distribution will differ from training input distribution, can leverage techniques such as `importance weighting` to train model better for real world data

- estimate density ratio of real world input distribution and training input distribution
- then, weight the training data according to this ratio
- train model on weighted data

However, this is difficult because can be challenging to get good real world distribution

#### Label shift

aka `prior shift`, `prior probability shift`, or `target shift`

When the output distribution changes, but for each possible output, the input distribution stays the same

#### Concept drift

aka `posterior shift`

When input distribution stays the same, but the conditional distribution of the output given an input changes - "same input, different output"

- cyclic
- seasonal

ex.

- rideshare prices on weekends vs weekdays
- flight prices holidays, vs non holidays

### General Data Distribution Shifts

- Feature change
  - when new features are added, older features are removed, set of possible values for a feature change
- Label schema change
  - when set of possible values for Y change
  - regression - range changes
  - classification - new classes

### Detecting Data Distribution Shifts

Really only problemmatic if they casuse the models performance to degrade

- First thing to do is monitor models accuracy related metrics
  - accuracy
  - F1
  - recall
  - ROC-AUC

In this context, "change" usually means "decrease", though increases are also of interest lol

These metrics work by comparing models predictions to ground truth labels

- having access to labels within a reasonable time window will vastly help give cisibility to models performance

When ground truth labels are unavailable, or too delayed to be useful, can monitor other distributions of interest instead

- input distribution P(X)
- label distribution P(Y)
- conditional distributions P(X|Y) and P(Y|X)

#### Satistical methods

A simple method to detect changes in distributions:

- compare statistics:
  - min, max, mean, median, variance, various quantiles (5th, 25th, 75th), skewness, kurtosis
- however, this is only useful when these statistical values are actually useful summaries

A more sophisticated solutoin is to use a two-sample hypothesis test

Also note that just because a difference is statistically significant, doesnt mean it is practically important

However, a good heuristic is:

- if you are able to detect the difference from a relatively small sample, then it is probabily a serious difference
- if it takes a large number of samples to detect, then the difference is probably not worth worrying about

Basic two-sample test: Kolomogorov-Smirnov test, K-S, KS

- nonparametric statistical test
- can only be used for 1D data
- they can also be expensive and produce too many false positives

Least-Squares Density Difference. Popular in research, but not bled its way into industry yet

#### Time scale windows for detecting shifts

Shifts can happen across two dimensions: spatial or temporal

Spatial shifts happen across an access point

- application gets new group of users
- app served on different, new, device

Temporal shifts happen over time

- treat input data to ml applications as time-series data

The time scale window of the data we use affects the shifts we can detect

- if data has weekly cycle, a window of less than a week wont detec tth cycle

Differentiate between `cumulative` and `sliding` statistics

- sliding computed within a single window (like 1hr)
- cumulative are continually updated

The shorter the time scale window, the faster can detect changes. BUT too short can lead to false alarms

Advanced monitoring platforms attempt a root cause analysis (RCA) feature

### Addressing Data Distribution Shifts

To make a model work with a new distribution, there are three main approaches:

- train models using massive datasets
  - the hope here is that if the training dataset is large enough, the model will be able to learn such a comprehensive solution that whatever data the model encouters in the wild will come out of this distribution
- adapt a trained model to a target distribution without requiring new labels
- retrain model using labeled data from the target distribution (most common)
  - do you start from scratch? (stateless training)
  - do you continue training from last checkpoint? (stateful training)
  - what data to use? (specifically, time period of data, will likely need to experiment)

Addressing shifts doesnt have to start after the shift has happened - can be more proactive and make system more robust to shifts

Different features shift at different rates

- consider tradeoffs between performance (high value features) and stable features (less important, but change less)

## Monitoring and Observability

`Monitoring`: tracking, measuring, logging different metrics to facilitate determining problems

- Designed to convey health of system. Three levels:
  - network the system is run on
  - machine the system is run on
  - application the system runs on

`Observability`: setting up our system in a way that gives visibility into the system to help investigate issues. The process is known as *instrumentation*

### ML-Specific Metrics

- accuracy-related metrics
- predictions
- features
- raw input

#### Monitoring accuracy-related metrics

- log and track all user feedback, implicit or explicit - actions
  - even if not used to infer natural labels

#### Monitoring predictions

- these are usually easy to visualize
- easy to monitor for distribution shifts
  - this is usually a proxy for input distribution shifts

#### Monitoring features

- raw inputs and at various stages of transformation
- first step is doing feature validation: making sure features follow expected schema

Things you can check

- min, max, median within acceptable range
- if value of feature satisfy a regex format
- values belong to a predefined set
- values of feature always greater than values of another feature

Some good tools for basic feature validation: Great Expectations and Deequ

Four major concerns:

- A company might have hundreds of models in production, and each model uses hundreds, if not thousands, of features
  - collecting too much data from too many sources can bog the system as a whole
- While tracking features is useful for debugging, its not very useful for detecting model performance degredation
  - Feature distreibutions shift al the time, and most changes are benign
  - Avoid alert fatigue
- Feature extraction is often done in multiple steps, using multiple libraries, on multiple services
  - is the error due to data itself or how it was processed?
- The schema that your features follow can change over time

#### Monitor raw inputs

- usually becomes burden for the data engineers, not the ml engineers

### Monitoring Toolbox

Trifecta: metrics, logs, traces

lol "traces are a form of logs, and metrics can be computed from logs"

Buddy focuses on set of tools from the perspective of users of the monitoring systems: logs, dashboards, alerts

#### Logs

- make easy to find later
  - distinct process ids
  - get all necessary metadata as well

Bruh, log management market estimated to be 2.3B, and 4.1B by 2026 holy fuck

Basically, want to do anomaly detection as quickly as possible after log is generated

#### Dashboards

"A picture is worth a thousand words"

Makes monitoring accessible to non-engineers - product managers, bus dev guys

Excessive metrics on a dashboard that dont convey anything truly meaningful and distinct leads to `dashboard rot`

#### Alerts

An alert consistes of three components:

- An alerts policy
  - The condition for an alert to occur
- Notification channels
  - Who and how observers are notified
- Description
  - Should be as detailed as possible
  - If possible, automatically provide mitigation instructions

### Observability

Concept drawn from control theory: bring "better visibility into understanding the complex behavior of software using outputs collected from the system at runtime"

`Telemetry`: a systems output collected at runtime

When something goes wrong in an observable system, we should be able to figure out what went wrong by looking at the systems logs and metrics without having to ship new code to the system.
