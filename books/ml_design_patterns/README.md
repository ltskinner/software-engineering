# Machine Learning Design Patterns: Solutions to Common Challenges in Data Preparation, Model Building, and MLOps

[https://github.com/GoogleCloudPlatform/ml-design-patterns](https://github.com/GoogleCloudPlatform/ml-design-patterns)

## Patterns Reference

| Chapter | Design Pattern | Problem Solved | Solution | NLP | CV | Pred. Analysis | IoT | Rec. Systems | Fraud and Anomaly Det. |
| - | - | - | - | - | - | - | - | - | - |
| Data Representation | Hashed feature | Problems associated with categorical features such as incomplete vocabulary, model size due to cardinality, and cold start | Bucket a deterministic and portable hash of string representation and accept the trade-off of collisions in the data representation | x | | | x | x | |
| | Embeddings | High-cardinality features where closeness relationships are important to preserve | Learn a data representation that maps high cardinality data into a lower-dimensional space in such a way that the information relevant to the learning problem is preserved | x | x | x | | x | x |
| | Feature Cross | Model complexity insufficient to learn feature relationshipts | Help models learn relationships between inputs faster by explicitly making each combination of input values a separate feature | | | x | | | x |
| | Multimodal Input | How to choose between several potential data representations | Concatenate all the available data representations | x | x | | | x | |
| Problem Representation | Reframing | Several problems including confidence for numerical prediction, ordinal categories, restricting prediciton range, and multitask learning | Change the representation of the output of a machine learning problem; for example, representing a regression problem as a classification (and vice versa) | | x | x | x | x | x|
| | Multilabel | More than one label applies to a given training example | Encode the label using a multi-hot array, and use k sigmoids as the output layer | | x | x | | x | |
| | Ensembles | Bias variance trade-off on small and medium scale problems | Combine multiple ml models and aggregate their results to make predictions | | | x | | x | x |
| | Cascade | Maintainability or drift issues when a ml problem is broken into a series of ML problems | Treat an ML system as a unified workflow for the purposes of training, evaluation, and prediction | x | x | x | x | | x |
| | Neutral Class | The class label for some subset of examples is essentially arbitrary | Introduce an additional label for a classification model, disjoint from the current labels | x | x | x | x | x | x |
| | Rebalancing | Heavily imbalanced data | Downsample, upsample, or use a weighted loss function depending on different considerations | | | | | | x |
| Patterns that Modify Model Training | Useful Overfitting | Using ML methods to learn a physics-based model or dynamical system | Forgo the usual generalization techniques in order to intentionally overfit on the training dataset | | | | | | |
| | Checkpoints | Lost progress during long-running training jobs due to machine failure | Streo the full state of the model perodically, so that partially trained models are available and can be used to resume training from an intermediate point, instead of starting from scratch | | | | | | |
| | Transfer Learning | Lack of large datasets that are needed to train complex ml models | Take part of a previously trained model, freeze the weights, and use these nontrainable layers in a new model that solves a similar problem | x | x | | | x | |
| | Distribution Strategy | Training large neural networks can take a very long time, which slows down experimentation | Carry the training loop out at scale over multiple workers, taking advantage of caching, hardware acceleration, and parallelization | | | | | | |
| | Hyperparameter Tuning | How to determine the optimal hyperparameters of a ml model | Insert the training loop intoa n optimization method to find the optimal set of hyperparameters | | | | | | |
| Resilience | Stateless Serving Function | Production ML system must be able to synchronously handle thousands to millions of production requests per second | Export the ml modal as a stateless function so that it can be shared by multiple clients in a scalable way | | | | x | | |
| | Batch Serving | Carrying out model predictions over large volumes of data using an endpoint that is designed to handle requests one at a time will overwhelm the model | Use software infrastructure commonly used for distributed data processing to carry out inference asynch on a large number of instances at once | | | x | | x | |
| | Continued Model Evaluation | Model performance of deployed models degrades over time either due to data drift, concept drift, or other changes to the pipelines which feed data to the model | Detect when a deployed model is no longer fit-for-purpose by continually monitoring model predictions and evaluating model performance | | | | | | |
| | Two-Phase Predictions | Large, complex models must be kept performant when they are deployed at the edge or on distributed devices | Split the use case into two phases with only the simpler phase being carried out on the edge | x | x | | x | x | x |
| | Keyed Predictions | How to map the model predictions that are returnedd to the corresponding model input when submitting large prediction jobs | Allow the model to pass througha  client-supported key during prediciotn that can be used to join model inputs to model predictions | | | | | | |
| Reproducibility | Transform | Teh inputs to a model must be transformed to create the features the model expects and that process must be consistent between training and serving | Explicitly capture and store the transformations applied to convert the model inputs into features | | | x | x | x | x |
| | Repeatable Splitting | When creating data splits, its important to have a method that is lightweight and repreatable regardless of the programming language or random seeds | Identify a column that captures the correlation relationship between rows and use the Farm Fingerprint hashing algorithm to split the available data into training, validation, and training dataset | | | | | | |
| | Bridged Schema | As new data ebcomes available, any changes to the data shcema could prevent using both the old and new data for retraining | Adapt the data from its older, original data schema to match the schema of the newer, better data | | | | | | |
| | Windowed Inference | Some models  require ongoing equence of instances to run inference or features must be aggregated across a time window in such a way that avoids training-serving skew | Externalize the model state and invoke the model from a stream analytics pipeline to ensure that features calculated in a dynamic, time-dependent way can be correctly repreated between training and serving | x | | x | x | x | |
| | Workflwo Pipeline | When scaling the ml workflow, run trials independently and track performance for each step of the pipeline | Make each step of the ml workflows a separate, containerized service that can be chained together to make a pipekine that can be run on a single REST call | | | | | | |
| | Feature Store | The ad hoc approach to feature engineering slows model development and leads to duplicated effort between teams as well as work stream inefficiency | Create a feature store, a centralized location to store and document feature datasets that will be used in building ml models and can be shared across projects and teams | | | x | x | x | x |
| | Model Versioning | It is difficult to carry outperformance monitoring and split test model changes while having a single model in produciton or to update models wihtout breaking existing users | Deploy a changed model as a microservice with a different REST endpoint to achieve backward compatability for deployed models | | | | | | |
| Responsible AI | Heuristic Benchmark | explaining model performance using complicated evaluation metrics does not provide the intuition that business decision makers need | Compare a ml model againast a single, easy-to-understand heuristic | | | | | | |
| | Explainable Predictions | Sometimes it is necessary to know **why** a model makes a certain prediction either for debugging or for regulatory and compliance standards | Apply model explainability techniques to understand how and why models make predicitons and improve user trust in ML systems | | | | | | |
| | Fairness Lens | Bias can cause ml models to not treat all users equally and can have adverse effects on some populations | Use tools to identify bias in datasets before training and evaluate trained models through a fairness lense to ensure model predictions are equitable across different groups of users and different scenarios | | | | | | |

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

### Design Pattern 4: Multimodal Input

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

### Design Pattern 20: Keyed Predictions

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

## [Chapter 7. Responsible AI](./7_RESPONSIBLE_AI.md)

### Design Pattern 28: Heuristic Benchmark

Compares a ML model against a simple, easy-to-understand heuristic in order to explain the models performance to business decision makers

### Design Pattern 29: Explainable Predictions

Increases user trust in ML system by providing users with an understanding of how and why models make certain decisions

## [Chapter 8: Connected Patterns](./8_CONNECTED_PATTERNS.md)

### ML Life Cycle

- Define Business Use Cases
- Data Exploration
- Select Algorithm
- Data Pipeline Feature Engineering
- Build ML Model
- Evaluate
- Present Results
- Plan for Development
- Operationalize Model
- Monitor Model

### Deployment Questions

- How should model retraining be managed?
- Will input data need to stream in?
- Should training happen on new batches of data or in real time?
- What about model inference? Should we plan for one-off batch inference jobs each week, or do we nee to support real-time prediction
- Are there special throughput or latency issues to consider?
- Is there a nmeed to handly spiky workloads?
- Is low latency a priority?
- Is network connectivity an issue?

[OK, there is a section on AI readiness that is actually super pog](./8_CONNECTED_PATTERNS.md#ai-readiness)
