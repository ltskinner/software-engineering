# Chapter 6. Reproducibility Design Patterns

## Design Pattern 21: Transform

Makes moving an ML model to production easier by keeping inputs, features, and transforms carefully separate

The problem is that inputs to a machine learning model are not the features that the ml model uses in its computations

Helpful to differentiate between:

- Instance level transformations
  - Can be part of the model directly
- Dataset level transformations
  - Which requier a full pass to compute overall statistics

## Design Pattern 22: Repeatable Splitting

To ensure sampling is repeatable and reproducible, it is necessary to use a well-distributed column and deterministic hash function to split the available data into training, validation, and test datasets

Want lightweight, repetable splitting of the data that works regardless of programming language or random seeds

Can automatically check the label distributions are similar across datasets using Kolomogorov-Smirnov test: just plot the cumulative distribution functions of the label in the three datasets and find the maximum distance between each pair. The smaller the max distance, the better the split

### Random split

What if the rows are not correlated? Want a random, repeatable split, but do not have a natural column to split by. In this case, we can hash the entire row of data by converting it to a string and hashing that string

Note, for identical records, they will always end up in the same split. If this is not desirable, add a unique identifier to the row

## Design Pattern 23: Bridged Schema

Provides a way to adapt the data used to train a model from its older, original data schema, to newer better data. Lets us augment new improved data with some older data to improve model accuracy

Ex. Have feature that originally was [card, cash]

Is now [gift card, debit card, credit card, cash]

- Probabilistic Method
  - Based on newer training data, estimate the distribution/proportion of original feature
  - like 10% gift, 30% debit, 60% credit
- Static Method
  - Like one hot encode
  - For old data, encode as [0, .1, .3, .6] corresponding to above based on new dist
  - For new data, encode as [0, 0, 1, 0] because we know for certain

The static method is recommended because it is effectively what happens when the probabilistic method runs for long enough

Also look at evaluation metrics while training to determine optimal portion of old data to include. For best results, choose the smallest number of older examples that we can get away with

ALSO, be sure to compare training with new data against models on entirely old data. Possible that there are no good signals in the new data

Also, dont just concat old features with new features. Because going forward, some old features will never be seen again that is just chaff

### Handling new features

For imputing missing values, use:

- The mean of the feature if the feature is numeric and normally distributed
- The median value of the feature if the feature is numeric and skewed or has lots of outliers
- The median value of the feature if the feature is categorical and sortable
- The mode of the feature if the feature is categorical and not sortable
- The frequency of the feature being true if it is boolean

## Design Pattern 24: Windowed Inference

Handles models that require an ongoing sequence of instances in order to run inference

This pattern works by externalizing the model state and invoking the model from a stream analytics pipleine. Also useful when a ml model requires features that need to be computed from aggreagtes over time windows

## Design Pattern 25: Workflow Pipeline

Address the problem of creating an end-to-end reproducible pipeline by containerizing and orchestrating the steps in our ml process. Containerization can be done explicitly or using a framework that simplifies the process

Core pipeline steps:

- Data collection
- Data validation
- Data analysis and preprocessing
- Model training
- Model deployment

DAGs again babyy

## Design Pattern 26: Feature Store

Simplifies management and reuse of features across projects by decoupling the feature creation process from the development of models using those features

Big value add is consistency in feature generation across training and inference

Feast is a good open source feature store

As datasets change over time, feast allows a few changes:

- adding new features
- removing existing features (more like tombstoned and not used, but remain on record)
- changing features schemas
- changing feature set source or max_age of feature set examples

Not allowed changes:

- Changes to feature set name
- Changes to entities
- Changes to names of existing features

The key operand here is that feature engineering is decoupled from feature usage, allowing constant feature development and experimentation separate from where the features may or may not be used

Primary components of a feature store:

- Tool to process large feature engineering jobs quickly
- Storage component to house feature sets
- Metadata layer to record feature version information, documentation and feature registry to simplify discovery and sharing
- An api for ingesting and retrieving features to and from the feature store

## Design Pattern 27: Model Versioning

Backward compatibility is achieved by deploying a changed model as a microservice with a different REST endpoint. This is a necessary prerequisite for many of the other patterns discussed here

This is useful if different subsets of users require different outputs from the model, specifically different metadata features (like explainability metadata), so we expose different versions of the modle to different users
