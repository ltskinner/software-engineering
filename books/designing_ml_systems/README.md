# Designing Machine Learning Systems

[Accompanying Github Repo](https://github.com/chiphuyen/dmls-book)

## [Chapter 1. Overview of ML Systems](./1_OVERVIEW_ML_SYS.md)

What ML solutions generally do:

- 1. Learn: the system has the capacity to learn
- 2. Complex patterns: there are patterns to learn, and they are complex
  - many times, wont know if pattern exists until have experimented with developing a model
- 3. Existing data: data is available, or its possible to collect data
- 4. Predictions: its a predictive problem
- 5. Unseen data: unseen data shares the same patterns that exist with the training data

X factors that make a solution extra juicy:

- 6. The task is very repetitive
- 7. The cost of incorrect predictions is cheap
- 8. Its at scale - lots of predictions need to be made
- 9. The **patterns are constantly changing** (adaptability expected)

When ML should **NOT** be used

- When its unethical
- When more simple solutions will achieve the same outcome
- It is not cost effective, to develop or deploy

Research prioritizes fast training, deployment prioritizes fast inference

## [Chapter 2. Introduction to ML Systems Design](./2_INTRO_ML_SYS_DESIGN.md)

Primary requirements:

- reliability
  - the show must go on
  - WE need to know when model fails, because end user may not even notice. no 404s for ML
- scalability
  - grow in complexity
  - grow in traffic volume
  - grow in model count
- maintainability
  - different people, different backgrounds
  - facilitate people working with tools they are best at
  - developing, deploying, monitoring, testing - all needs to be done in absence of original author
- adaptability
  - discovering aspects of performance improvement
  - allowing updates without service distruption

Breakouts of these become dedicated chapters I believe

High Level Development Cycle:

- 1. Project scoping
- 2. Data engineering
- 3. ML model development
- 4. Deployment
- 5. Monitoring and continual learning
- 6. Business analysis

Decouple objective functions: have one model for one metric that can be optimized. If there are several, train several models and develop a heuristic or dedicated model for producing a combined output

## [Chapter 3. Data Engineering Fundamentals](./2_DATA_ENGINEERING.md)

"ETL refers to the general purpose processing and aggregating of data into the shape and the format that you want"

3 main modes of dataflow:

- Data passing thru database
  - Easiest
- Data passing thru services using requests (REST, RPC API, POST/GET)
  - Aka `request-driven`
  - Best for systems that rely more on logic than data
- Data passing thru real-time transport like Apache Kafka and AWS Knesis
  - Aka `event driven`
  - Better for systems that rely more on data than logic (data heavy is literal term used)

`Historical Data` anything in a database, datalke, data warehouse

- Process this with batch jobs, periodically
- Because batch processing happens much less frequently than stream processing, in ML, batch processing is used to compute features that change less often. `Batch features` are also known as `static features`

`Streaming Data` anything that keeps working its way in lol

- process with stream processing
- best for low latency
- Stream processing is used to compute features that change quickly (how many rides in last minute). `Streaming features` are also known as `dynamic features`

## [Chapter 4. Training Data](./4_TRAINING_DATA.md)

Handling labeling without hand(ling) labeling:

- Weak supervision (heuristic rule labelers)
- Semi-supervised
- Transfer learning
- Active learning

Handling class imbalance:

- choose correct metrics for problem
- data-level methods
- algorithm-level methods

## [Chapter 5. Feature Engineering](./5_FEATURE_ENGINEERING.md)

Best Practices Summary:

- Split dat by time into train/valid/test splits instead of doing it randomly
- If you oversample, do it after splitting
- Scale and normalize data after splitting to avoid leakage
- Use statistics ONLY from the train split, isntead of the entire data, to scale your features and handle missing values
- Understand how the data is generated, collected, and processed. Involve domain experts if possible
- Keep track of your datas lineage
- Understand feature importance to your model
- Use features that generalize well
- Remove no longer useful features from your models

## [Chapter 6. Model Development and Offline Evaluation](./6_MODELS_EVAL.md)

Tips for Model Selection:

- Avoid state of the art
- Start with the simplest models
- Avoid Human biases in selecting models
- Evaluate good performance now vs good performance later
- Evaluate tradeoffs
- Understand your models assumptions

Ensembling approaches:

- bagging
- boosting
- stacking

Things to track when experimenting:

- loss curve
- model performance
- corresponding sample, prediction, and ground truth
- speed of model
- system hardware performance
- parameter and hyperparemeter values

Primary reasons models fail:

- Not meeting theoretical constraints
- Poor implementation of model
- Poor choice of hyperparameters
- Data problems
- Poor choice of features

Debugging approach:

- Start simple and gradually add more components
- overfit a single batch
- set a random seed

### Model Offline Evaluation

Baselines - evaluation metrics, by themselves, mean little. Must have baselines to compare against

- Random baselines
- Simple heuristic
- Zero rule baseline
- Human baseline
- Existing solutions

Evaluation Methods - want models to be robust, fair, calibrated, and make sense

- Perturbation tests
- Invariance tests
- Directional expectation changes
- Model calibration
- Confidence measurement
- Slice-based evaluation

## [Chapter 7. Model Deployment and Prediction Service](./7_DEPLOYMENT_PREDS.md)

Basically, dont count out model optimization and compression. Not easy but will improve thruput

## [Chapter 8. Data Distribution Shifts and Monitoring](./8_DATA_DIST_SHIFT.md)

"Deploying the model isnt the end of the process" - model performance WILL degrade

Software System Failures

- Dependency failure:
- Deployment failure
- Hardware failures
- Downtime or crashing

ML-Specific Failures

- data collection and processing problems
- poor hyperparameters
- changes in training pipeline not replicated in the inference pipeline (and vice versa)
- data distribution shifts, causing models performance to deteriorate over time
- edge cases
- degenerate feedback loops (primarily in naturally labeled data)

Types of Data Distribution Shifts

- Covariate shift
- Label shift
- Concept drift

General Data Distribution Shifts

- Feature change
- Label schema change

Addressing Data Distribution Shifts

- train models using massive datasets
- adapt a trained model to a target distribution without requiring new labels
- retrain model using labeled data from the target distribution (most common)

Monitoring and Observability

`Monitoring`: tracking, measuring, logging different metrics to facilitate determining problems

- ML-Specific Metrics
  - accuracy-related metrics
  - predictions
  - features
  - raw input

`Observability`: setting up our system in a way that gives visibility into the system to help investigate issues. The process is known as *instrumentation*

## [Chapter 9. Continual Learning and Test in Production](./9_CONTINUAL_LEARNING.md)

Why Continual Learning

- combat data distribution shifts
- adapt to rare events
- to overcome *continuous cold start* problem

Continual Learning Challenges

- Fresh data access
- Evaluation
- Algorithms

How to improve evaluation - have explicit set of protocols for:

- what test to run
- order to run tests
- thresholds that must be passed to be promoted to next state
- should be automated too
- process for reviewing results should be there as well

## [Chapter 10. Infrastructure and Tooling for MLOps](./10_INFRASTRUCTURE_AND_TOOLING.md)

- Storage and compute
- Resource management
- ML platform
- Development environment

## [Chapter 11. The Human Side of Machine Learning](./11_HUMANS_AND_ML.md)

Full Stack Data Scientists:

```txt
Things id prioritize learning if I was to study to become a ML engineer again:

1. Version control
2. SQL+NoSQL
3. Python
4. Pandas/Dask
5. Data structures
6. Prob & stats
7. ML algos
8. Parallel computing
9. REST API
10. Kubernetes + Airflow
11. Unit/integration tests
```
