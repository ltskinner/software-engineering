# Chapter 3. Problem Representation Design Patterns

## Design Pattern 5: Reframing

Changing the representatino of the output of the ml problem - i.e. take a regression problem and pose it as a classification problem (and vice versa)

## Design Pattern 6: Multilabel

Problems where we can assign more than one label to a given training sample

### Handling Hierarchical Labels

- Use a flat approach and put every lable in the same output array regardless of hierarchy, making sure you have enough examples of each "leaf node" label
- Use Cascade design pattern. Build one model to identify higher-level labels. Based on the high-level classification, send the example to a separate model for a more specific classification task

#### One vs Rest

Training multiple binary classifiers instead of one multi-label model

Benefit is that we can use it with model architectures that only do binary classifications (like svms)

Can also be useful for rare categories

#### Summarizing

Use Multilabel when data falls into any of these scenarios:

- A single training example can be associated with mutually exclusive labels
- A single training example can have many hierarchical labels
- Labelers describe the same item in different ways, and each interpretation is accurate

Use Multilabel when data falls into any of these scenarios:

- A single training example can be associated with mutually exclusive labels
- A single training example can have many hierarchical labels
- Labelers describe the same item in different ways, and each interpretation is accurate

## Design Pattern 7: Ensembles

Combining multiple machine learning models and aggregate their results to make predictions

Can be an effective means to improve performance and produce predictions that are better than any single model

By building several models with different inductive biases and aggregating their outputs, we hope to get a model with better performance

### Sources of Error

- Irreducible error
  - Inherent error resulting from noise in the dataset, framing of problem, or bad training examples
- Error due to bias
  - Bias is inability to learn about relationship between model features and labels
  - High bias is underfit
- Error due to variance
  - Models inability to generalize to new, unseen samples
  - High variance is overfit

### Solutions

#### Bagging

Short for bootstrap aggregating

- Parallel ensembling method
- Addresses high variance
- Train different models with different subsets of the data

#### Boosting

Constructs an ensemble model with more capacity than individual member models

- Addresses reducing bias
- Idea of boosting is to build successive models where each moewl focuses on learning the examples that the previous model got wrong
- Takes a sequence of weak learnings and take a weighted average to yield a strong learner

#### Stacking

Combines the outputs of a collection of models to make a prediction

### Trade-Offs and Alternatives

- Increased training and design time (bad)
- Decreased model interpretability

## Design Pattern 8: Cascade

Situations where a ml problem can broken up into a series of ml problems

Convert into hierarchical situation

Unlike other design patterns, Cascade is not necessarily a best practice

Cascade pattern addresses the unusual scenario where we do not have a categorical input, and for which extreme values need to be learned from multiple inputs

## Design Pattern 9: Neutral Class

Good situations for neutral classes:

- When human experts disagree
  - A model that outpus a neutral determination is often more acceptable to experts than a model that is wrongly confident
- Customer satisfaction
- As a way to improve embeddings

## Design Pattern 10: Rebalancing

Approaches for handling datasets where one label makes up the majority of the dataset

- Downsampling - decrease number of examples from majority class
  - Note - commonly combined with Ensembles - have unique model for each downsample group. During inference, take median output of ensemble models
- Weighting (classes) - treat specific label classes as being more important
- Upsampling - duplicate minority class examples

For reframing specifically:

- Changing to regression task
- Analyzing model errors for each example
- Clustering
