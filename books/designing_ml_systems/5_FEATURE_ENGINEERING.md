# Chapter 5: Feature Engineering:

Facebook says having right features is most important thing in developing ML models

More testimony states that having the right features gives them the biggest performance boost compared to clever algorithmic techniques like hyper tuning

## Learned Features vs Engineered FEatures

"The promise of deep learning is that we wont have to handcraft features. For this reason, deep learning is sometimes called feature learning"

Majority of ML applications in production arent deep learning

Damn scrot, TikTok video suggestions - millions of features

## Common Feature Engineering Operations

### Handling Misisng Values

Covered this a bunch in Algs at JHU

Not all types of missing values are equal lol

- Missing not at random (MNAR)
  - value is missing because that is the true value - there is no info
- Missing at random (MAR)
  - missing not due to the value itself, but due to another observed variable
  - HAHA "age calues are often missing for respondents of gender A because people of gender A in this survey dont like dislosing their age"
- Missing completely at Random (MCAR)
  - no pattern in when the value is missing

#### Deletion

- Column Deletion:
  - just get rid of the feature if too many gone
- Row deletion:
  - remove the sample
  - good for MCAR
  - but can also remove important info
    - especially if MNAR...
    - introduce biases if not known exactly why value is missing

#### Imputation

- use defaults for forms
- mean, median, mode
- can use multiple techniques in tandem

No perfect way

### Scaling

- if normal distribution, minmax normalize, *standardization*

### Discretization

lmao guy in book says hes rarely seen it help, can confirm

### Encoding Categorical Categorical Features

problem is if new categoris come online

"wabbit" trick aka "hashing trick" just encode the hash across a known bitspace that is much larger than number of possible values

Not 100% foolproof but take on case by case basis

### Feature Crossing

Combine multiple features to make new feature

- helps model nonlinear relationships
  - essential for models that are bad or cant learn nonlinearities
    - linear regression
    - logistic regression
    - tree-based models
  - not critical for nns
- downside is increase number of features into the model and can lead to overfitting

### Discrete and Continuous Positional Embeddings

Basically, attention

## Data Leakage

Bro haha (covid) "researchers trained their model on a mix of scans taken when patients were lying down and standing up. Because patients scanned while lying down were more likely to be seriously ill, the model learned to predict serious covid risk from a persons position"

`data leakage` refers to phenomenon when a form of the label "leaks" into the input features. Naturally this auxilliary information is absent during inference, or is present and causes red herrings

(should be called label leakage)

### Common Causes for Data Leakage

#### Splitting time-correlated data randomly instead of by time

- the time the data is generated affects its label distribution
  - "information from the future leaked into the training process"

#### Scaling before splitting

- scaling requires global stats of data
- common mistake is to use entire training data to generate stats before splitting, which leaks the mean and variance of the test samples into the training process
  - basically, the test samples could impact stats, but will not be present during training
- split before scale, then use training stats to scale all other data
- some suggest split data prior to exploratory data analysis to be extra safe

#### Filling in missing data with statistics from the test split

- when imputing, make sure to not use data from eventual test set

#### Poor handling of data duplication before splitting

- if you have dupes or near dupes in data, failing to remove them before splitting will cause same sample to appear in both set
  - oversampling can introduce this
  - so only oversample after the split

#### Group leakage

So if you have a picture of a lung, theres two of em. Make sure left isnt in train and right isnt in test

Or for other pictures, like from a movie, make sure frame A isnt in train and frame B isnt in test right?

#### Leakage from data generation process

Basically, however the data was generated does matter especially if all data is not sourced from the same source

### Detecting Data Leakage

Monitor all stages of lifecycle for leakage

Measure predictive power of each feature, or a set of features

- If a feature has an unusually high correlaiton, look into it more
  - sometimes its not that a single feature leaked
  - but the combination of the features introduced a leak

Do "ablation" studies

- remove feature and see if model performance tanks
  - figure out exactly why that feature is so important

Pay extra attention to newly added features that seem too good to be true

And just be really careful with the test split

## Engineering Good Features

Generally, adding more features leads to better model performance. But not always. Having too many features can be bad both during training and serving:

- The more features you have, the more opportunities there are for data leakage
- Too many features can cause overfitting
- Too many features can increase memory required to serve model, which, in turn, might require you to use a more expensive machine/instance to serve your model
- Too many features can increase inference latency when doing online prediction, especially if you need to extract these features from raw data for predicitons online
- useless features become technical debts. Whenever your data pipeline changes, all the affected features need to be adjusted accordingly. For example, if one day your application decides to no longer take in information about users age, all features that use users age need to be updates.

In theory, if a feature doesnt help a model make good rpedictions, regularization techniques like L1 regularization should reduce that features weight to 0. However, inpractice it might help models learn faster if the features that are no longer useful (and even possibly harmful) are removed, prioritizing good features

Save em off, can always add back later

Two factors to consider in a feature:

- importance to the model
- generalization to unseen data

### Feature Importance

- trees, use xgboost
- SHAP, (Shapley Additive exPlanations)
- InterpretML

Generally tho, a features importance to a model is measure by how much that models performance deteriorates if that feature or a set of features containing that feature is removed from the model

facebook found that top 10 features accounted for more than 50% of models feature importance. last 300 account for less than 1%

### Feature Generalization

"lot less scientific than measureing feature importance, and it requires both intuition and sme on top of statistical knowledge

Two things to consider

#### Feature coverage

`coverage` is the percentage of the samples that has values for this feature in the data

- so the fewer values that are missing, the higher the coverage

General rule of thumb: if this feature appears in a very small portion of data, its not going to generalize very well

BUT sometimes these can be real gold nuggies, just have to play around with it

#### Distribution of feature values

Coverage of a feature can differ wildly between difference slices of data, and even in the same slice of data over time. If there are large discrepancies between train and test, this indicates that train and test dont come from the same distribution

#### Interesting example

- Taxi company, want to use leading 6 days to predict 7th
- Have feature `DAY_OF_WEEK`
- rationale is that weekday traffic is worse than weekend
- feature coverage is 100%, because in every feature
- but, bruh
- train set values are monday to saturday
- test set value is sunday only
