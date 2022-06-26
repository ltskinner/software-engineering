# Chapter 2: Introduction to ML Systems Design

Four primary requirements (focused on in this book):

- reliability
- scalability
- maintainability
- adaptability

Processes for iteratively designing systems to meet these reqs will be covered

## Business and ML Objectives

ML objectives: the metrics they can measure about performance of models

- accuracy
- F1
- inference latency, etc

The company doesnt care about these. Unless it changes a business metric, a change in accuracy matters not

Business metrics must be understood

The goal of any project within a business, is to increase profits (directly or indirectly)

- increasing sales, coversions
- cutting costs

What business performance metrics is the new ML system supposed to influence?

Many companies will do A/B testing and then based on how business metrics respond, use that to select final model - outside of scope of any ML metric

ROI on ML depends on matrurity stage of adoption

Of companies that have production models for 5+ years, almost 75% can deploy a new model in under 30 days, newer companies are at abou 60%

## Requirements fo ML systems

### Reliability

The system should continue to perform the correct function at the desired level of perfomance even in the face of adversity (hardware, software faults, human error)

- with traditional software, will get warning, 404
- ML fails silently
  - users dont know system has failed, and will continue to use as if it had not

### Scalability

There are multiple ways an ML system can grow

- grow in complexity
- grow in traffic volume
- grow in model count
  - managing 100 models is very different from managing 1 model
  - monitoring and retaining needs to be automated
  - need to manage code generation so that can adequately reproduce a model when need to

Need reasonable ways for dealing with that growth

Most people think of resource scaling, number of GPUs

### Maintainability

Many differnt people work on ML systems:

- ML engineers
- DevOps engineers
- SMEs

different backgrounds, different languages and tools, and own different parts of process

- structure workloads and infrastructure so contributors can work using tools they are comfortable with
  - Instead of one group of contributors forcing their tools onto other groups
- code needs to be documented
- models should be reproducible such that all contributors can reproduce if authors are not there

### Adaptability

To adapt to shifting data distributions and business requirements, system should have a capacity forr:

- discovering aspects of performance improvement
- allowing updates without service distruption

## Iterative process

Iterative and never ending process

Example workflow: predict whether an ad should be shown when users enter a search query

- 1. Choose a metric to optimize (impressions - number of times an ad is shown)
- 2. Collect data and obtain labels
- 3. Engineer features
- 4. Train models
- 5. During error analysis, realize errors are caused by the wrong labels, so relabel again
- 6. Train model again
- 7. During error analysis, realize model always predicts an ad that shouldnt be shown, the reason is 99.99% of data you have contain NEGATIVE labels. Collect more data of ads that should be shown
- 8. Train model again
- 9. The model performs well on existing data, which is two months old. Performs poorly on data collected yesterday, model is now stale. need to update on more recent data
- 10. Train model again
- 11. Deplow the model
- 12. The model seems to be performing well, but then business people come knocking. Ads are being shown, but few people click. Change model to optimize for ad click-thru rate instead
- 13. Go to step 1

A more concise cycle:

- 1. Project scoping
- 2. Data engineering
- 3. ML model development
- 4. Deployment
- 5. Monitoring and continual learning
- 6. Business analysis

But, basically all steps talk to all other steps lol

#### Step 1: Project Scoping

- lay out goals, objectives, constraints
- resources estimated, allocated

#### Step 2: Data Engineering

- handling data from different sources and in different formats
- curating training data
  - sampling
  - generating labels

#### Step 3: ML model development

- extract features and develop initial models on these features

#### Step 4: Deployment

- ML is like writing - you will never be done

#### Step 5: Monitoring and continual learning

- Once in production, monitor for performance decay
- maintained to be adaptive to changing environments and changing requirements

#### Step 6: Business analysis

- model performance needs to be evaluated against business goals and analyzed to generate business insights
- insights can be used to:
  - eliminate unproductive projects
  - scope out new projects (life begins anew)

## Framing ML Problems

want 100 examples from each class, bear minimum. if you have 1000 classes, minimum of 100,000 samples. For high number of classes, consider hierarchical classification

For classes that can be expected to change, be added, or be deleted - dont frame as multiclass or multilabel, instead have series of binary predicitons for each class

### Objective Functions

#### Decoupling objectives EXAMPLE

Imagine building system to rank items on users newsfeeds. Original goal: maximize users engagement. You want to achieve this goal through the following objectives:

- Filter out spam
- Filter NSFW content
- Rank posts by engagement: how likely users will click on it

Quickly learn that optimizing for engagement alone can lead to questionable ethical concerns. Extreme posts get more engagement. extremistbot.exe. You want a more wholesome, watered down soylent feed

New goal: maximize engagement while minimizing the spread of extreme views and disinfo. New goals:

- Filter spam
- Filter NSFW
- filter disinfo
- rank post quality
- rank post engagement: how likely users will click on it

Now, two objectives are in conflict with each other: if a post is engaging, but of questionable quality, should that post rank high or low?

An objective is represented by an objective function. To rank posts by quality, you first need to predict posts' quality, and you want posts predicted quality to be as close to their actual quality as possible. Essentially: minimize *quality_loss*: the difference between each posts predicted quality and its true quality.

Similarly, to rank posts by engagement, you first need to predict the number of clicks each post will get. You want to minimize *engagement_loss*: the idfference between each posts predicted clicks and its actua number of clicks.

**Approach 1** is to combine these two losse into one loss and train one model to minimize that loss:

`loss = alpha*quality_loss + beta*engagement_loss`

You can randomly test out different values of alpha and beta to find values that work best. Or just use Pareto optimization

But, with these static parameters, will need to be retaining if engagement or quality changes are reflected to user

**Approach 2** is to train two different models, each optimizing one loss. So you have two models:

- quality_model
- engagement model

Then you combine the models outputs and rank posts by their combined scores:

(use formula from above)

alpha and beta are now decoupled from the model (as a parameter in loss calculation) and you can tune finished product without retraining models

In general, when there are multiple objectives, its a good idea to decouple them first because it makes model development and maintenance easier.

- easier to twak system without retraining models
- easier to maintain since different objective might have difference maintenance schedules

## Mind versus Data

Uhh, basically theres two camps:

- The make models and algs better
- The just add more data camp

### Data Science Hierarchy of Needs

TOP

- AI, deep learning
- Learn/Optimize: A/B testing, experimentation, simple ML algorithms
- Aggregate/Label: Analytics, metrics, segments, aggregates, features, trainingdata
- Explore/Transform: Cleaning, anomaly detection, prep
- Move/Store: Reliable data flow, infrastructure, pipelines, ETL, structured and unstructured data storage
- Collect: Instrumentation, logging, sensors, external data, user-generated content

BOTTOM
