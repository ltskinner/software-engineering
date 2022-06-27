# Chapter 6: Model Devlopment and Offline Evaluation

## Model Development and Training

### Evaluating ML Models

Things to consider:

- model performance (accuracy, f1, log loss)
- how much data requires
- compute
- time to train
- inference latency
- interpretability

Six Tips for model selection:

- Avoid state of the art
  - sota only means it performed better than existing models on some static datasets
  - better to focus on solving your problem instead of blindly following some abstract benchmark performance
- Start with the simplest models
  - simple models are easier to deploy, and deploying early gets you quickest validation data on consistency between training and prediciton pipelines
  - starting with something simple and adding more complex components step-by-step makes it easier to understand your model and debug it
  - having a simple model as a baseline serves as a reference point for future iterations
- Avoid Human biases in selecting models
  - most models perform better under certain circumstances, so dont let opinions about architectures weigh on selecting the best solution for the production environment
- Evaluate good performance now vs good performance later
  - the best model now does not always mean the best model two months from now
  - e.g. in two months, have 2x more training data, so can move to different more data intensive model
    - loss and accuracy as function of the number of training samples used
    - this can be used to project optimal number of training samples
- Evaluate tradeoffs
  - false positive and false negative tradeoff
    - depends on the task, which is more dangerous
  - compute requirement and accuracy
    - a more accurate model may require much more compute and a GPU
  - more complex models are not as interpretable
- Understand your models assumptions
  - Does your data satisfy those assumptions?
  - Some assumptions
    - Prediction assumption: every model that aims to predict Y from X makes the assumption this is possible
    - IID: nns assume that examples are *independent and identically distributed*, which means all the examples are independently drawn from the same joint distribution
    - Smoothness: Every supervised machine learning method assumes that theres a set of functions that can transform inputs into outpouts such that similar inputs are transformed into similar outputs
    - Tractability: Let X be input and Z be latent representation of X. Every generative model makes the assumption that its tractable to compute the probability P(Z|X)
    - Boundaries: A linear classifier assumes that decision boundaries are linear
    - Conditional independence: A naive bayes classifier assumes that the attribute values are independent of each other given the class
    - Normally distributed: Many statistical methods assume that data is normally distributed

### Ensembles

Ensembling methods are less favored in produciton becaus ensembles are more complex to deploy and harder to maintain

However are still common for tasks where a small performance boost can lead to a huge financial gain

Three main approaches:

- bagging
  - `bootstrap aggregating` - reduces variance and avoids overfitting
  - create a bunch of different variants of the training set (sample with replacement)
  - train a distinct classifier
  - combine output of all classifiers to produce final
- boosting
  - For single dataset, train on same data
  - but for each iteration, weight each sample differently
  - future weak learners focus on examples that previous weak learners misclassified
  - Steps:
    - 1. Start by thraining the first weak classifier on original dataset
    - 2. Samples are reweighted based on how well the first classifier classifies them (misclassifications are given a higher weight)
    - 3. Train the second classifier on this reweighted dataset. Your ensemble now consists of first and second classifiers
    - 4. Samples are weighted based on how well the ensemble classifies them
    - 5. Train the third classifier on this reweighted dataset. Add to ensemble
    - 6. Repeat for as many iterations as needed
    - 7. Form the final strong classifier as a weighted combination of the existing classifiers - classifiers with smaller training errors have higher weights
- stacking
  - train base learners from training data, then create a meta- learner that combines outputs of the base learners to output final predictions
    - majority vote
    - average vote
    - its own model - logistic or linear regression

### Experiment Tracking and Versioning

Its important to keep track of all the definitions needed to re-create an experiment and its relevant artifacts. Artifact is a file generated during an experiment and show: loss curve, evaluation loss, logs, intermediate results

Tools:

- MLflow
- Weights & Biases
- DVC

#### Experiment Tracking

Things to consider:

- loss curve corresponding to the train split and each of the eval splits
- model performance metrics that you care about on all non-test splits, like accuracy, F1, and perplexity
- corresponding sample, prediciton, and ground truth label. this is handy for ad hoc analytics and sanity check
- speed of model - number of steps per second, number of tokens per second
- system performance metrics like memory and cpu usage - important for identifying bottlenecks and to help avoid wasting system resources
- values over time of parameter and hyperparameter, like learning rate, gradient norms (globally and per layer, weight notm)

#### Versioning

Imagine going to reproduce a new really promising model, and are unable to

ML systems are part code, part data, so need to version code and data

"Data versioning is like flossing. Everyone agrees its a good thing to do, but few do it"

Why Challenging:

- data is much larger than code, so cant use same versioning strategy
- what constitutes a diff? a new file is added or removed? a checksum of the repo changes? how to resolve merge conflicts
- data regulation might make you delete data on request, which can make reproducing a dataset down the road impossible

### Debuggin ML Models

Main reasons so challenging:

- models fail silently, will run but predict wrong
- slow and challenging to validate the defect has been removed
- cross-functional complexity - lots of people and components

Primary reasons for failure:

- Theoretical constraints
  - each model comes with own set of assumptions about data and features. The data a model learns from could not conform to assumptions
- Poor implementation of model:
  - framework specific misuse and general implementation issues
- Poor choice of hyperparameters
  - can have right model and right data, but hyperparamters are misconfigured
- Data problems
  - collection issues
  - feature engineering issues
- Poor choice of features
  - too many, too few, not useful

Debugging approach:

- Start simple and gradually add more components
- overfit a single batch
- set a random seed
  - randomness makes it hard to compare results across different experiments

### Distributed Training

- common to train a model using data that doesnt fit into memory
  - data preprocessing will need to run out of core and in parallel
- may have to use gradient checkpointing

#### Data parallelism

- now the norm to train ML models on multiple machines
  - split data on multiple machines, train model on them, and accumulate the gradients
  - how to accurately and effectively accumulate gradients from different machines?
    - stragglers will slow down entire system
    - if async, gradient staleness becomes issue
  - batch size can also get very large

#### Model parallelism

- each worker has own copy of the whole model, and does all the computation necessary for its copy of the model
  - machine 0 handles first two layers
  - machine 1 handles next two
  - some machines handle forward pass, others handle backward pass

Pipeline parallelism

- several variants
- key idea is to break each computation of machine into multiple parts
  - machine 1 can execute on output of machine 0 for first batch, while machine 0 begins on second batch

### AutoML

#### Soft AutoML: Hyperparameter tuning

HAHA "Graduate Student Descent" - technique in which grad student fiddles around with hyperparameters until model works

- random search
- grid search
- bayesian optimization

#### Hard AutoML: Architecture search and learned optimizer

- give algorithm building blocks, and let it figure out how to combine them

`Architectural search` or `Neural architecture search (NAS)`

Consists of three components:

- A search space
  - defines all possible model architectures
- A performance estimation strategy
  - To evaluate the performance of a candidate architecture without having to tran each candidate architecture from scratch until converge
- A search strategy
  - To explore the search space
  - random, reinforcement learning, evolution

Why AutoML is tank:

- resulting architectures and learned optimizers can allow ML algs to work off the shelf on multiple real-world tasks (saving production time and cost, both during training and inference)
- may be able to solve real world tasks previously thought impossible

Four Phases of ML Model Development:

- 1. Before machine learning
  - start with non-ml solution
  - "If you think that machine learning will give you a 100% boost, then a heuristic will get you 50% of the way there"
- 2. Simplest machine larning models
- 3. Optimizing simple models
- 4. Complex models

## Model Offline Evaluation

### Baselines

Evaluation metrics, by themselves, mean little. Must have baselines to compare against

- Random baselines
  - if the model just predicts at random, whats the expexted performance
- Simple heuristic
  - forget ml, if you just make predictions based on simple heuristics, what performance would you expect?
- Zero rule baseline
  - when the model just predicts the most common class
  - any model you build has to outperform this significantly to justify added comlexity
  - Ex. reccomending next app: just recommend most used app
- Human baseline
  - hwo well humans have performed on this task
- Existing solutions

### Evaluation Methods

Want models to be robust, fair, calibrated, and make sense

- Perturbation tests
  - make small changes to test splits and see how these impact models performance
  - adding noise
  - the more sensitive the model is to noise, the harder it will be to maintain
- Invariance tests
  - certain changes to inputs shouldnt lead to changes in the output
  - how to test: keep inputs the same, but change the sensitive information to see if outputs change
  - or just exclude sensitive info
- Directional expectation changes
  - certain changes to inputs should cause predictable changes in output
  - if the outputs change in the opposite expected direction, model might not be learning the right thing
- Model calibration
  - Someone makes a prediction that something will happen 70% of the time
  - predicted outcome same as actual outcome 70% of the time
  - if the actual is only 60%, the model isnt calibrated
  - basically, predicted likelihoods should be representative of actual lieklihoods
  - to measure calibration, a simple method is counting
    - count number of times model outputs probability X and frequency Y that prediciton is true
    - graph this - for perfectly calibrated, x and y should be linear diagonal
    - `sklearn.calibration.calibration_curve`, `sklearn.calibration.CalibratedClassifierCV`
- Confidence measurement
  - considered a way to think about usefulness threshold for each individual prediction
  - what is the certainly threshold at which predictions should be shown?
  - what to do with predictions that fall below? discard? loop to human? ask for more info from users?
- Slice-based evaluation
  - separate data into subsets and look at models performance on each subset separately
    - model should perform the same across all
    - easy one is have majority class heavy set, and a minority class heavy set
  - Simpsons paradox: a phenomenon in which a trend appears in several groups of data, but disappears or reversed when groups are combined
  - Determining critical slices:
    - Heuristics based
      - slice data using domain knowledge
    - Error analysis
      - Manually go through misclassified examples and find patterns among them
    - Slice finder
      - Research exists to systemize process of finding slices:
        - Chung - "Slice Finder: Automated Data Sclicing for Model Validation"
        - Helal - "Subgroup Discovery Algorithms: A Survey and Empirical Evaluation"
