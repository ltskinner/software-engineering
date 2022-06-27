# Chapter 7: Model Deployment and Prediction Service

ML App Logic (stack):

- Data Engineering
- Feature Engineering
- Model
- Metrics

"Deploy" is a loose term that generally means making your model running and accessible.

"Production is a **spectrum**"

"Deploying is easy if you ignore all the hard parts"

The hard parts include:

- making model available to millions of users
- latency of milliseconds
- 99% uptime
- setting up infrastructure so correct person is immediately notified when something goes wrong
- figuring out what went wrong
- seamlessly deploying the updates to fix whats wrong

## Machine Learning Development myths

### Myth 1: You Only Deploy One or Two ML Models at a Time

- in reality, companies have many, many ML models
- an application might have many different features, and each feature might require its own model
- may need to generalize across regions of country, or globe, and different languages
  - 20 countries, 10 models = 200 models performing same task

### Myth 2: If We Dont Do Anything, Model Performance Remains the Same

HA "Software doesnt age like fine wine. It ages poorly"

The phenomenon in which a software program degrades over time even if nothing seems to have changed is known as "software rot" or "bit rot"

- data distribution shifts are expecially dangerous and real to ML systems

### Myth 3: You Wont Need to Update Your Models as Much

the question is NOT:

- How often **should** I update my models?

Rather, ask:

- How often **can** I update my models?

Since a models performance decause over time, want to update it as fast as possible

- etsy - deploy 50 times a day
- netflix - thousands of times per day
- aws - every 11.7 seconds (holy shit)

### Myth 4: Most ML Engineers Dont Need to Worry About Scale

## Batch Prediciton vs Online Prediction

- Online prediction:
  - predictions are generated and returned as soon as requests for these predictions arrive
  - on-demand prediction
  - REST APIs
  - synchronous predictions
- Batch prediction:
  - periodically, when triggered
  - predictions are stored somewhere
  - asynchronous predictions

Feature types:

- Batch features
- Streaming features
  - features computed exclusively fromo streaming data
- Online features
  - any feature used for online prediction, such as batch features stored in memory (like precomputed embeddings)

Key differences in batch and online prediction:

| Feature | Batch Prediction (async) | Online Prediction (synch) |
| - | - | - |
| Frequency | Periodical, some time interval | As soon as requests come |
| Useful for | Processing accumulated data when you dont need immediate results (like recommender systems) | When predictions are needed as soon as a data sample is generated (such as fraud detection) |
| Optimized for | High throughput | Low latency |

### From Batch Prediciton to Online Prediction

For real time, gotta use online

To overcome latency challange of online prediction, two components are required:

- A (near) real-time pipleine that can work with incoming data, extract streaming features (if needed), input them into a model, and return a prediction in near real time. A streaming pipeline with real-time transport and a stream computation engine can help with that
- A model that can generate predictions at a speed acceptable to its end users. For most consumer apps, this means ms

### Unifying Batch Pipeline and Streaming Pipeline

Having two different pipelines to process your data is a common cause for bugs in ML production

- one cause is when changes in one pipeline arent correctly replicated in the other, leading to two pipelines extracting two different sets of features
  - especially common if different teams maintain each pipeline

Apache Flink is good stream processor

## Model Compression

If the model you want to deploy takes too long to generate predictions, have three aproaches:

- Make it perform inference faster
- Make model smaller
- Make hardware its deployed on faster

### Low-Rank Factorization

Idea is to replace high dimensional tensors with low dimensional tensors

- one type is `compact convolutional filters`
  - over-parameterized conv filters are replaced with compact blocks to both reduce number of params and increase speed
  - replace 3x3 with 1x1
  - techniques are specific to model type, and required lots of arch knowledge to design

### Knowledge Distillation

Small model (the student) is trained to mimic larger model or ensemble of models (teacher)

Can work regardless of architectural differences between teacher and student

However, depends entirely on availability of teacher network

### Pruning

In context of nns:

- remove entire nodes of a nn
  - change arch and reduce number of parameters
- find parameters least useful to preds, and set them to zero

### Quantization

Most general and commonly used model compression method

- Use fewer bits to represent parameters
  - using 16 bits to represent float instead of 32
  - or use ints only (fixed point)
  - bruh, xnor-net, bought by apple for 200M
- reduces memory footprint and improves computation speed

Downsides:

- smaller range of values represented, have to round up and down

## ML on the Cloud and on the Edge

Cloud is, well, cloud

edge is like mobile devices, smartwatch, cameras, robots

Cloud downsides:

- compute intensive, compute expensive. why not have users pay for the compute?
- rely on internet connection
- data security, privacy regulation

But for edge, how to make models run on arbitrary hardware efficiently?

### Compiling and Optimization Models for Edge Devices

Intermediate Representation (IR) - middleman

- from original code for model, compilerrs generate a series of high and low level IRs before generating the code native to a hardware backend
- process is called *lowering*
  - as in, you lower your high level framework code into low-level ahrdware netive code

#### Model Optimization

- usually will run into performance issues
  - generated code may not take advantage of data locality and harware cashes, or available advanced features like vector or parallel operations
- individual dependencies have local optimizations that do not transfer well

Two ways to optimize ML models:

- locally
  - optimize an operator or set of operators in model
- globally
  - optimize the entire compute graph end to end

Standard techniques

- Vectorization
  - given a loop or nested loop, instead of executing one at a time, execute multiple elments contiguous in memory at same time to reduce latency cause by data io
- Parallelization
  - given an input arary, divide into different, independent work chunks, and do the operation on each chunk individually
- Loop tiling
  - Change the data accessing order in a loop to leverage hardwares memory layout and cache. this kind of optimization is hardware dependent. A good access pattern on CPUs is not a good access pattern on GPUs
- Operator fusion
  - fuse multiple operators into one to avoid redundant memory access

#### Using ML to optimize ML models

Hand designed heuristics are not guaranteed to be optimal. they are also nonadaptive

autoTVM is good general solution, and works with subgraphs instead of just an operator

- 1. it first breaks your computation graph into subgraphs
- 2. it predicts how big each subgraph is
- 3. it allocates time to search for the best possible path for each subgraph
- 4. it stitches the best possible way to run each subgraph together to execute the entire graph

This can be a very slow process to let run in entirety

### ML in Browsers

Javascript is main go to

WebAssembly (WASM) is easy to embed in JS. lets you run executable programs in browsers (lol a little scary doe)

But can be slow
