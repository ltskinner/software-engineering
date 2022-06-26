# Chapter 4: Training Data

The term "training data" is used instead of "training dataset" because "dataset" denotes a set that is finite and stationary

Data in production is neither finite nor stationary

## Sampling

One case: dont have access to all possible data in the real world, the data you use to train is subset of real world data

Another case: infeasible to process all the data one has access to - too much time or too many resources

Sampling is also helpful to accomplish a task faster and cheaper (for experimentation and stuff like that)

### Nonprobability Sampling

Nonprobability sampling is when the selection of data isnt based on any probability criteria

- Convenience sampling:
  - Samples of data are selected based on their availability. Popular because convenient
- Snowball sampling:
  - Future samples are selected based on existing samples
  - Ex. scrape legit twitter accounts without having access to twitter api, then scrape the accounts they follow, and so on
- Judgement sampling
  - Experts decide what samples to include
  - lmao
- Quota sampling
  - You select samples based on quotas for certain slices of data without any randomization
  - Ex. when doing a survey, you might want 100 responses from each age group:
  under 30, 30-60, over 60, regardless of actual age distribution

Samples selected by any of these are not representative of real world data and are riddled with selection biases

Goddamn wikipedia and common crawl, love and hate

Self driving cars not immune either, most data from phoenix or the bay lol

### Simple Random Sampling

In simplest form of random sampling, you give all samples in the population equal probabilities of being selected

- easy to implement
- rare categories may not be picked up

### Stratified sampling

Group by class, then for each class randomly sample from that grouping (each group called stratum if you wanna split hairs)

- inst always possible, such as when impossible to divide all samples into groups
- for multilabel data this can be a pain

### Weighted Sampling

Each sample is given a weight, which determines probability of it being selected

- if you have 3 samples A, B, C, give them weights of .5, .3, .2
- This method allows you to leverage domain expertise
  - If you know subpopulation of the data is more valuable (more recent, better labelers, etc) you want to see more of that
- This can also help when data you have comes from a different distribution compared to the true data
  - easy to do with `random.choice`

### Resivoir Sampling

Useful for streaming data

- imagine incoming stream of tweets
- want to sample k to train a model on
- unknown how many tweets
- certainly cannot fit them all in memory
  - no way to know in advance the probability a tweet should be selected at

You want:

- Every tweet to have an equal probability of being selected
- Can stop the alg at any time and the tweets are sampled with the correct probability

Enter resivour, which is an array, and has 3 steps:

- 1. put the first k elements into the resivoir
- 2. For each incoming nth element, generate a random number i such that 1 <= i <= n
- 3. if 1 <= i <= k: replace the ith element in the resivoir with the nth element. Else, do nothing

This means that each incoming nth element has a k/n probability of being in the resivoir

### Importance Sampling

Allows us to sample from a distribution when we only have access to another distribution

- commonly used in policy-based reinforcement learning
- yeah that checks out

## Labeling

Despite the promise of unsupervised ML, most ML models in production today are supervised

Damn dude this guy at Tesla

Got himself a full time data labeling team, thats so pog

### Hand Labels

Problems:

- expensive, especially if SME is required
- data privay is annoying
- slow

Slow labeling leads to slow iteration speeds, and makes model less adaptive to changing environments and requirements

#### Label multiplicity

Often, to obtain enough labeled data, companies have to use data from multiple sources and rely on multiple annotators who have different levels of expertise. Different annotators have different levels of accuracy, lmao preach

This leads to the problem of label `ambiguity` or label `multiplicity`: what to do when there are multiple conflicting labels for a data instance

`must have clear problem definition`

#### Data Lineage

Indescriminately using data from multiple sources, generated with different annotators, without examining their quality can cause your model to fail mysteriously. bro thats so brutal

- keep track of origin of each sample, as well as its labels
- damn dude its crazy seeing all this shit I just whipped up off the cuff back in the day haha

### Natural Labels

Models predictions can be automatically evaluated or partially evaluated by the system

- ex. model that estimates arrival time for certain route on maps
  - by end of trip, gmaps knows exactly how long you were stuck in traffic for
- ex. stock market

Many tasks can be framed as recommendation tasks

Basically, there just needs to be a native (natural) feedback mechanism in the macro problem being solved

Quick chart on companies surveyed:

- 62% use hand labels
- 63% use natural labels
- 30% use programmatic labels (risky risky)

#### Feedback loop length

The time it takes for a prediction to eb served until the feedback on it is provided

- short window length means capture labels faster, and can use these to detect issues with models and address quickly
  - but too short, and you might prematurely label a recommendation as bad
- long window length
  - like fraud and stuff

Basically, just dont jump the gun on labeling the scenario. If possible, use an actual event as a marker to determine closure of the engagement

### Handling the Lack of Labels

Summaries of four techniques for handling the lack of hand-labeled data

| Method | How | Ground truth required? |
| - | - | - |
| Weak supervision | Leverages (often noisy) heuristics to generate labels | No, but a small number of labels are recommended to guide the development of heuristics |
| Semi-supervision | Leverages structural assumptions to generate labels | Yes, a small number of initial labels as seeds to generate more labels |
| Transfer learning | Leverages models rpetrained on another task for your new task | No for zero shot learning, Yes for fine-tuning, though the number of ground truths required is often much smaller than what would be needed if you train the model from scratch |
| Active learning | Labels data samples that are most useful to your model (???) | Yes |

#### Weak supervision

- heuristics to label data (imo better to centaur this and narrow down samples to give to sme)

```python
def label_function(note):
    if "deez nuts" in note:
      return "GOT EEM"
```

Some lfs:

- Keyword heuristic
- Regex
- Database lookup (followed by stringmatch)
- Outputs of other modes (as an undeclared comsumer lmao)

This can be useful when dataset has strict privacy

Easy to version subject matter expertise

Also, using LFs is known as `programmatic labeling`

Advantages of programmatic labeling over hand labeling

| Hand Labeling | Programmatic labeling |
| - | - |
| Expensive: Especially when SMEs required | Cost saving: Expertise can be versioned, shared, and reused across an org |
| Lack of privacy: Need to ship data to human annotators | Privacy: Create LFs using a cleared data subsample and then apply LFs to other data without looking at individual samples |
| Slow: time required scales linearly with number of labels needed | Fast: Easily scale from 1K to 1M samples |
| Nonadaptive: Every change requires relabeling the data | Adaptive: When changes happen, just reapply LFs |

#### Semi-supervision

Weak supervision leverages heuristics to obtain noisy labels

Semi-supervised leverages structural assumptions to generate new labels based on small set of initial labels. **Requires initial set of labels**

Classic semi-supervision is **self-training**:

- Train a model with the data you have
- Use this to label unseen before data
- Take high confidence samples to be new training set
- Repeat until happy with model

Perturbation

- basically make random benign changes so the same sample is no longer the "same sample"

#### Transfer Learning

#### Active Learning

Method for improving the efficieny of data labels. The hope is that ML models can achieve greater accuracy using less samples if they choose the data to be trained next with

aka `Query learning`

Instead of randomly labeling data samples, label samples that are most helpful to your models according to some metrics or heuristics

- label examples the model is least certain about
  - will help learn decision boundary

## Class Imbalance

### Challanges of Class Imbalance

Class imbalance can mean there is insufficent signal for the model to learn to detect the minority class

Model can rut itself by exploiting a simple heuristic instead of learning a real pattern

Because minority classes are rare, failure to predict these can be proportionally more expensive than others

### Handling Class Imbalance

- choose correct metrics for problem
- data-level methods
- algorithm-level methods

#### Using the right evaluation metrics

Wrong metrics will give you wrong ideas of how models are doing

- overall accuracy is super misleading

#### Data-level methods: Resampling

- Oversampling:
  - adding (duplicating) more instances from the minority class
  - Runs risk of overfitting
- Undersampling:
  - Remove samples from biggie class
  - Runs risk of losing important data

Two-phase learning:

- 1. Train model on resampled data
- 2. Then fine-tune on original data

#### Algorithm-Level Methods

- Give training instances we care about a higher loss weight, which will make the model focus on improving that

Cost-sensitive learning

- define a cost matrix for predicted neg, pos and actual neg, pos

Class balanced loss

- Class weight = W = total samples / n for low count class

Focal loss

- Incentivize the model to focus on learning the samples is has difficulty classifiying

## Data Augmentation

Family of techniques that are used to increase the amount of training data

- simple label-preserving transformations
- perturbation
- data synthesis

### Simple Label-Preserving Transformations

In CV, easiest technique is to randomly modify images while preserving the label

- cropping
- flipping
- rotating
- inverting
- erasing

In NLP

- replace word with similar word

### Perturbation

- adding small amounts of noise to images really fuck things up
- adversarial stuff

### Data Synthesis

In NLP, can create templates

"Find me a [CUISINE] resturaunt within [NUMBER] of miles of [LOCATION]"

In CV, synthesize new data by combining existing samples with discrete labels to generate continuous labels

called `mixup`
