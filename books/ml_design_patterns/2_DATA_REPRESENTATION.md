# Chapter 2. Data Representation Design Patterns

- input: real world data fed to the model (e.g. weight)
- feature: the representation f the transformed data that the model actaully operates on
  - process of creating feeatures to represent input data is feature engineering

`Embedding` design pattern is the canonical example of a data representation that deep neural networks are capable of learning on their own

- in an enbedding, the loearned representation is `dense` and `lower dimensional` than the input, which could be sparse

The process of learning features to represent the input data is feature extraction

## Simple Data Representations

### Numerical Inputs

#### Why scaling is desirable

- bc the -1, 1 range
- centering the data to lie in the range makes the error function more spherical
- so, models trained with transformed data tend to converge faster and are faster, cheaper to train
- also offers the highest floating point precision
- some ml algs are very sensitive to the relative magnitudes of the different features
  - k-means for example

#### Linear Scaling

- min-max xcaling
- clipping (in conjunction with min-max scaling)
  - helps reduce outliers by using "reasonable" values instead of estimating the max and min
- z-score normalization
  - addresses the problem of outliers without requiring prior knowledge of what the reasonable range is
  - `x1_scales = (x1 - mean_x1)/stddev_x1`
- winzorizing
  - uses empirical distribution in the training data to clip the bounds between the 10th and 90th percentile or whatever
  - also min-max scaled

#### Dont throw away "outliers"

- can expect to see outliers in production too

#### Nonlinear transformations

Waht if your data is skewed neither uniformly distributed nor distributed like a bell curve?

In this case, better to apply a non-linear transform to the input before scaling it

Common trick is to take the log of the input before, or sigmoid, or polynomial expansions (square, square root, cube, cube root, etc)

Bucketing is also good - `histogram equalization` which is based on the quantiles of the raw distribution

`Box-Cox transformation` - choose a single parameter, lambda, to control the heteroscedasity so the variance no longer depends on the magnitude

#### Array of Numbers

- Represent th input array in terms of its bulk statistics
  - ex. use the length, average, median, min, max, stc
- Represnting the input array in terms of its empirical distribution
  - percentile, etc
- If arary is ordered, represent the input array by the last three or some n items
  - for arrays of length less than n, pad to length

### Categorical Inputs

#### One-hot Encoding

Sometimes helpful to treat a numeric input as categorical and map it to a one-hot encoded col:

- When the numeric input is an index
- When the relationship between input and label is not continuous
- When advantageous to bucket the numeric variable
- When we want to treat different values of the numeric input as being independent when it comes to their effect on the label

#### Array of Categorical Variables

- Counting aka multi-hot encoding
  - Number of occurences of each category indexed in a list
- Relative frequency
  - to avoid large numbers, basically normalize sum to 1

## Design Pattern 1: Hashed Feature

Addresses three possible problems:

- incomplete vocabulary
- model size due to cardinality
- cold start

### Problem

One-hot encoding a categorical input variable requires knowing the vocabulary beforehand

Tons of categories (vocabulary)

New categories coming online in production (cold-start)

### Solution

- Convert categorical input to unique string
- Invoke a deterministic (no random seeds or salt) and portable (so that the same alg can be used in train and serving) hashing alg on the string
- Take the remainder when the hash result is divided by the desired number of buckets

Good rule of thumb is choose a number of hash buckets such that each bucket gets about 5 entries

### Trade-Offs and Alternatives

The key tradeoff here is we lose model accuracy

- Bucket Collision

## Design Pattern 2: Embeddings

### Problem

One hot encoding treats the categorical variables as being `independent`

### Solution

Addresses the problem of representing high-cardinality data densley in a lower dimension by passing the input data through an embedding layer that has trainable weights

A learned embedding allows us to extract inehrent similarities between two separate categories, so we can quanify the similarity between two categorical features

#### Image Embeddings

Take ResNet or whatever and then remove the last softmax layer - without this final layer, the model produces a feature vector

### Trade-Offs and Alternatives

Main tradeoff with using an embedding is the compromised representaiton of the data. There is a loss of information involved in going fro high-cardinality to lower dimensional

But, in return we gain information about closeness and context of the items

The lossiness of the representation is controlled by the size of the embedding layer

Rules of thumb:

- Use the fourth root of the total number of unique categorical elements
- Be appx 1.6x the square root of the number of the elements in the category, and no less than 600

#### Autoencoders

Training embeddings in a supervised way can be hard because it requires a lot of labeled data. Autoencoders provide a way around the need for a massive labeled dataset

## Design Pattern 3: Feature Cross

Helps models learn relationships between inputs faster by explicitly making each combination of input values a separate feature

Concatenate two categorical features

### Why It Works

Provide more complexity, more expressivity, and more capacity to simple models

### Trade-Offs and Alternatives

Can also be applied to numerical features

## Design Pattern 4: Multimodal Input

Addresses the problem of representing different types of data or data that can be expressed in complex ways by concatenating all the available data representations

### Problem

Say we have camera footage with metadata

### Solution

### Trade-Offs and Alternatives

### Multimodal Representation of Images

- pixel values
- sets of tiles (cnns)
- windowed sequences
