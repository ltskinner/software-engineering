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
