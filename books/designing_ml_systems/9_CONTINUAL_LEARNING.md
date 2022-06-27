# Chapter 9: Continual Learning and Test in Production

How do we adapt out models to data distribution shifts? By continually updating our ML models

Continual learning is largely an infrastructural problem

## Continual Learning

Most people think of paradigm where the model updates itself with every incoming sample from production

Very few companies do that

- for nns, learning with every incoming sample makes it susceptible to catastrophic forgetting (forgetting stuff it once knew that is not seen often now)
- can make training more expensive
  - hardware backends designed for batches, not single samples

Basically, no need ot update every 5 or 10 minutes because:

- not enough new data is generated in that period
- models dont decay THAT fast

### Stateless Retraining vs Stateful Training

Continual learning is more about the manner in which the model is retrained, not the frequency of it occuring

Stateful: model continues learning on new data, aka fine-tuning, or incremental learning

Grubhub found that switching to daily stateful training reduced compute cost 45x and increased purchase-thru rate by 20%

With stateful training, is possible to avoid storing data altogether

- for stateless, data sample may be reused during multiple training iterations of a model
- for stateful, each data sample can be used and discarded once

Goal: setup infrastructure to allow both, then the training frequency to just be a parameter or button to push

Again, the primary goal is setting up infrastructure to succeed - how its used depends on the use case

How does stateful training work if I want to add a new feature or another layer?

There are two kinds of model updates:

- Model iteration:
  - A new feature is added to an existing model arch or the model arch is changed
- Data iteration:
  - Model arch and features remain the same, but is refreshed with new data

Stateful training mostly applied to data iterations

Model changes usually retraining from scratch, but look into `knowledge transfer` and `model surgery`

- Surgery transfers trained weights from one network to another after a seleciton process to determine which sections of the model are unchanged and which must be re-initialized

### Why Continual Learning

- combat data distribution shifts
- adapt to rare events
- to overcome *continuous cold start* problem
  - when model has to make preds for a new user without any historical data

### Continual Learning Challenges

- Fresh data access
  - if you want to update model every hour, need new data every hour
  - very much a data engineering problem
- Evaluation
  - how do you make sure the update is good enough to deploy?
  - the risks for catastrophic failure amplify with continual learning
    - First, the more frequently you update a model, the more opportunities there are for it to fail
    - Second, continual learning makes models more susceptible to coordinated manipulation and adversarial attack
  - Realistically, cant issue new updates until enough time has elapsed to collect the right eval data (fraud detection ~2 weeks to see how model has performed)
- Algorithms
  - nns are best to do stateful training
  - trees and matrix based may not benefit

### Four Stages of Continual Learning

#### Stage 1: Manual, stateless retraining

- If your team is developing a ton of models, already created models become backburner
- Only updated these existing models when: models performance has degraded severely AND the team has time to update it

Common, lmao

#### Stage 2: Automated retraining

Script to automatically execute all retraining steps

Interval done on gut instinct

Requirements:

- writing good scripts (lol) - see Airflow or Argo
- have stable access to data
- can version and store all artifacts necessary for repoducing

Feature reuse (log and wait)

- basically if data is coming hot off of prod (natural), the features were already processed to be fed to the prod model - save these and wait until next retrain

#### Stage 3: Automated, stateful training

Switch to locating previous verious checkpoint

Requirements:

- change in mindset

MODEL LINEAGE CAPACITY

#### Stage 4: Continual learning

What is the optimal schedule to retrain

- by change in data distribution?
- change in performance?

Holy grail: combinw continual learning with edge deployment

Requirements: need good triggers, which can be:

- Time based
- Performance based
- Volume based (when total amount of labeled data increases by 5%)
- Drift based

Must have solid monitoring solution in place to facilitate this

And need solid eval pipeline as well

### How Often to Update Your Models

If your model gains lots from the most fresh data, then wanna retrain asap. If fresh data doesnt matter that much, dont need to retrain frequently

#### Value of data freshness

To help determine, train models on different sections of data from specific time periods. If model does better on the most recent data, then fresh data is pog

#### Model iteration vs data iteration

Should do both, but one usually comes at cost of the other

- Figure out which one is more valuable and do that one more

## Test in Production

If you update a model to adapt to a new distribution, not sufficient to eval model on test splits from old distributoin

- test model on most recent (fresh) data that you have access to
- also prolly still use past distribution as sanity check

### Shadow Deployment

Safest way to deploy model or software update

- 1. Deploy candidate model in parallel with existing model
- 2. For each incoming request, route to both model to make predictions, but only serve existing models prediction to user
- 3. Log prediction from new model for analysis purposes

Can be expensive

### A/B Testing

- 1. Deploy the candidate model alongside the existing model
- 2. A % of trafic is routed to new model
  - make sure that the two models have no way to impact each other
  - like model As outputs wont update world state in a way that model B would be degraded or artificially improved
- 3. Monitor and see which model is pogger

Traffic routing must be truly random - there cannot be any form of selection bias

Also needs ot be done on enough samples to gain confidence in the outcome

### Canary Release

Roll out change to small subset of users before rolling out to entire userbase

- 1. Deploy candidate model alongside existing model. The candidate model is the canary
- 2. A portion of traffic is routed to the candidate model
- 3. If its performance is satisfactory, increase the traffic to the candidate model, else, abort
- 4. Stop when either the canary is serving all requests, or when canary is aborted

Doesnt require randomization

### Interleaving Experiments

For a user, show them recs or outputs from both models alongside

Must be cognicent of position of model outputs on page to minimize bias, or at least balance

### Bandits

Think multi-armed bandit, and the slot machines are each model

Facilitate request routing

Bandit is stateful: before routing a request to a model, you need to calculate all models current performance, requiring:

- model to be able to make online preds
- short feedback loops
- mechanisms to collect feedback

#### Contextual Bandits as an exploration strategy

Help balance showing what we *know* the users want, and stuff we wanna collect data on user response from

Also, a good eval pipeline is not just about the tests that are run. It matters who runs the tests. Designers are biased and wont use model same way as users. Different designers also lean toward different tests, which could have different outcomes

To mitigate: each team should outline clear pipleines on how models should be evaluated

- what test to run
- order to run tests
- thresholds that must be passed to be promoted to next state
- should be automated too
- process for reviewing results should be there as well
