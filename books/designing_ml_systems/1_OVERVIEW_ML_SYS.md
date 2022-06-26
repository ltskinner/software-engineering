# Chapter 1. Overview of Machine Learning Systems

- algorithm only small part of ML system in production
- other components:
  - business requirements
  - data stack
  - logic for: developing, monitoring, updating model
  - infrastructurer that enables delivery

Relationship between MLOps and the ML Systems Design

- Ops in MLOps comes from DevOps - deploying, monitoring, maintaining
  - MLOps is set of tools and best practices for bringing ML to production
- ML systems design takes a system approach to MLOps, which means that it considers an ML system holistsically to ensure that all the components and their stakeholders can work together to satisfy the specified objectives and requirements

## When to Use ML

ML is not a magic tool that can solve all problems

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

Traditional Software:

- Inputs + patterns go in => produces outputs

ML

- Inputs + outputs go in => patterns come out

### Some Use Cases

- Increasing customer satisfaction
- Generating customer insights/intelligence
- Reducing customer churn
- Filtering assets and content
- Predicting demand fluctuations
- Recommender systems
- Reducing costs
- Increasing long-term customer engagement
- Increasing conversion rates
- Building brand awareness
- Acquiring new customers
- Retaining customers
- Detecting fraud
- Increasing customer loyalty
- Interacting with customers
- Improving customer experience
- Internal processing automation

## Understanding ML Systems

### ML in Research vs Production

Key Differences between ML in research and ML in production

| Attribute | Research | Production |
| - | - | - |
| Requirements | State-of-the-art model performance on benchmark datasets | Different stakeholders have different requirements |
| Computational priority | Fast training, high throughput | Fast inference, low latency |
| Data | Static | Constantly shifting |
| Fairness | Often not a focus | Must be considered |
| Interpretability | Often not a focus | Must be considered |

#### Different stakeholders and requirements

Some stakeholders:

- ML engineers
- Sales team
- Product team
- ML platform teeam
- Manager

Ensembling is not widely used in production

- Does give your system a performance improvement, but makes system too complex to be effective in prod. Slower predictions and harder to interpret results
- Is a .1% improvement in thruput, or a .1% improvement in accuracy more valuable?

#### Computational priorities

- Novice designers spend too much time on model development, and not enough time on deployment and maintenance (yea heard dat lmao, blast from the past)
- Research prioritizes fast training, deployment prioritizes fast inference

`latency` = response time - a measure of the time from when a request is sent to the time a response is received. No futzing around with network vs compute, just bundle all together
`throughput` how many samples can be processed in a second

Batch processing may have higher latency, but also higher throughput

100ms delay can hurt conversion rates by 7%

Remember, latency is not a single number - it is a distribution. It helps to think of them in terms of percentiles

- High percentiles (bad slow responses) shouldnt be disregarded
  - Sometimes these are slow because lots of data on highly active user
  - Use high percentiles to specify performance requirements for system
    - 90th percentile latency of a system must be below a certain number

#### Data

- Real world data is messy
  - noisy, unstructured, constantly shifting
  - biased, and unknown by how much
  - Labels, if any, sparce, imbalanced, or incorrect. Might even have to update (bruh haha flashbacks)

Some funny graphic of a phd showing that 75% of his time was spent working on data haha seems low to me

#### Fairness

- There is no "state of the art" with respect to fairness
- "ML algorithms dont predict the future, but encode the past, thus perpetuating the biases in the data and more"

#### Interpretability

"Suppose you have cancer and you have to choose between a black box AI surgeon that cannot explain how it works, but has a 90% cure rate, and a human surgeon with an 80% cure rate. Do you want the AI surgeon to be illegal"

### Machine Learning Systems Versus Traditional Software

lol "ML production would be a much better place if ML experts were better software engineers"

- Many challances are unique to ML applications and require their own tools
  - In SWE, theres an underlying assuption that code and data are separated
  - In SWE, want to keep things as modular and separate as possible
- On the contrary:
  - ML systems are part code, part data, and part artifacts created from the two
  - applications developed from most/best data win
  - Instead of improving algorithms, many companies focus on improcing data
- In SWE, only need to test and version code
  - in ML need to test and version data, too
    - how to version large datasets
    - how to know if data sample is good or bad for system
- Size of ML models is challange as well
  - requires GBs of memory
  - dam, in a few years, might look at billion param model and say "Can you believe the computer that sent men to the moon only had 32 MB of RAM"

