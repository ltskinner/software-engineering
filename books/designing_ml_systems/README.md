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
