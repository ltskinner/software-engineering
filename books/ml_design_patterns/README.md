# Machine Learning Design Patterns: Solutions to Common Challenges in Data Preparation, Model Building, and MLOps

[https://github.com/GoogleCloudPlatform/ml-design-patterns](https://github.com/GoogleCloudPlatform/ml-design-patterns)

## [Chapter 1. The Need for Machine Learning Design Patterns](./1_NEED_FOR_ML_DESIGN.md)

## [Chapter 2. Data Representation Design Patterns](./2_DATA_REPRESENTATION.md)

### Design Pattern 1: Hashed Feature

Addresses:

- Incomplete vocabulary
- Model size due to cardinality
- Cold start

Instead of one-hot encoding:

- Convert categorical input to unique string
- Invoke a deterministic (no random seeds or salt) and portable (so that the same alg can be used in train and serving) hashing alg on the string
- Take the remainder when the hash result is divided by the desired number of buckets

Good rule of thumb is choose a number of hash buckets such that each bucket gets about 5 entries

### Design Pattern 2: Embeddings

Addresses the problem of representing high-cardinality data densley in a lower dimension by passing the input data through an embedding layer that has trainable weights

Rules of thumb to embedding size:

- Use the fourth root of the total number of unique categorical elements
- Be appx 1.6x the square root of the number of the elements in the category, and no less than 600

### Design Pattern 3: Feature Cross

Helps models learn relationships between inputs faster by explicitly making each combination of input values a separate feature

Concatenate two categorical features

## Design Pattern 4: Multimodal Input

Addresses the problem of representing different types of data or data that can be expressed in complex ways by concatenating all the available data representations

## [Chapter 3. Problem Representation Design Patterns](./3_PROBLEM_REPRESENTATION.md)

### Design Pattern 5: Reframing

Changing the representation of the output of the ml problem - i.e. take a regression problem and pose it as a classification problem (and vice versa)

### Design Pattern 6: Multilabel

Problems where we can assign more than one label to a given training sample

### Design Pattern 7: Ensembles

Combining multiple machine learning models and aggregate their results to make predictions

Can be an effective means to improve performance and produce predictions that are better than any single model

By building several models with different inductive biases and aggregating their outputs, we hope to get a model with better performance

- Bagging
- Boosting
- Stacking

### Design Pattern 8: Cascade

Situations where a ml problem can broken up into a series of ml problems

Convert into hierarchical situation

### Design Pattern 9: Neutral Class

### Design Pattern 10: Rebalancing

## [Chpater 4. Model Training Patterns](./4_TRAINING_PATTERNS.md)

### Design Pattern 11: Useful Overfitting

Overfitting is useful when these conditions met:

- There is no noise, so the labels are accurate for all instances
- You have the complete dataset, thus, overfitting becomes interpolating the dataset

Overfitting is also a good sanity check - complex models should be able to overfit on a small enough batch of data. If you train a NN that isnt capable of overfitting the training set, you should be using a bigger one

### Design Pattern 12: Checkpoints

Here we store the full state of the model periodically so that we have partially trained models available

### Design Pattern 13: Transfer Learning

Take part of a previously trained model, freeze the weights, and incorporate the non-trainable layers into a new model that solves a similar problem, but on a smaller dataset

### Design Pattern 14: Distribution Strategy

The training loop is carried out over multiple workers, often with caching, hardware acceleration, and parallelization

### Design Pattern 15: Hyperparameter Tuning

The training loop itself is inserted into an optimization method to find the optimal set of model hyperparameters

## [Chapter 5. Design Patterns for Resilient Serving](./5_RESILIENT_SERVING.md)

### Design Pattern 16: Stateless Serving Function

### Design Pattern 17: Batch Serving

### Design Pattern 18: Continued Model Evaluation

Basically, keep an eye on production predicitons and retrain as necessary, being conscious of the impact of stale training data

### Design Pattern 19: Two-Phase Predictions

Provides a way to address the problem of keeping large, complex models performant when they have to be deployed on distributed devices by splitting the use cases into two phases, with only the simpler phase being carried out on the edge

## Design Pattern 20: Keyed Predictions

Normally, you train a model on the same set of input features that the model will be supplied in realtime when it is deployed. However, it can be advantageous for you model to pass though a client-supplied key.

Basically lets you associate inputs and output results in asynch settings where results may be unordered

## [Chapter 6. Reproducibility Design Patterns](./6_REPRODUCIBILITY.md)

### Design Pattern 21: Transform

Makes moving an ML model to production easier by keeping inputs, features, and transforms carefully separate

### Design Pattern 22: Repeatable Splitting

### Design Pattern 23: Bridged Schema

Provides a way to adapt the data used to train a model from its older, original data schema, to newer better data. Lets us augment new improved data with some older data to improve model accuracy

### Design Pattern 24: Windowed Inference

### Design Pattern 25: Workflow Pipeline

### Design Pattern 26: Feature Store

Simplifies management and reuse of features across projects by decoupling the feature creation process from the development of models using those features

### Design Pattern 27: Model Versioning
