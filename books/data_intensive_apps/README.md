# Designing Data-Intensive Applications

"we have to dig deeper than buzzwords"

[https://github.com/ept/ddia-references](https://github.com/ept/ddia-references)

## Part I. Foundations of Data Systems

### [Chapter 1. Reliable, Scalable, and Maintainable Applications](./1_1_RELIABLE_SCALABLE_MAINTAINABLE.md)

- Reliability
  - Tolerating hardware and software faults
  - Human error
- Scalability
  - Measuring load and performance
  - Latency percentiles throughput
  - Will likely need to rethink architecture on every order of magnitude load increase
- Maintainability
  - Operability, simplicity, and evolvability

It is impossible to reduce the probability of a fault ot zero, therefore it is usually best to design fault tolerance mechanisms that **prevent faults from causing failures**

### [Chapter 2. Data Models and Query Languages](./1_2_MODELS_LANGAUGES.md)

"Data models are perhaps the most important part of developing software, because they have such a profound effect: not only on how the software is written, but also on how we *think about the problem* that we are solving"

### [Chapter 3. Storage and Retrieval](./1_3_STORAGE_RETRIEVAL.md)

### [Chapter 4. Encoding and Evolution](./1_4_ENCODING_EVOLUTION.md)

Idea of evolvability: we should aim to build systems that make it easy to adapt to change

In order for a system to continue running smoothly, we need to maintain compatability in both directions:

- Backward compatability:
  - Newer code can read data that was written by older code
  - Normally not hard to achieve - as the author of newer code, you know the format of old code and can explicitly handle
- Forward compatability:
  - Older code can read data that was written by newer code
  - Trickier because requires older code to ignore additions made by newer versions of the code

"Data outlives code"

## Part II. Distributed Data

Various reasons why you want to distribute data across multiple machines:

- Scalability
- Fault tolerance/high availability
- Latency

Scaling to Higher Load:

- simple to vertical scale - just buy a more powerful machine
  - this is a `shared memory architecture`
  - linear cost growth
  - due to bottlenecks, 2x compute doesnt always mean handling 2x load
  - limited fault tolerance

Shared-Nothing Architecture

- scale horizontal - node oriented
- covered here mostly because they require the most caution by the developer
  - there are conmstraints and tradeoffs

Replication vs Partitioning - two common ways data is distributed across multiple nodes

- Replication
  - Keep a copy of the same data on several different nodes. Provides redundancy and can improve performance
- Partitioning
  - Splitting a big database into partitions (shards)

### [Chapter 5. Replication](./2_5_REPLICATION.md)

Replication can serve several purposes:

- High Availability
  - Keep the system running, when one machine (or several machines, or an entire datacenter) goes down
- Disconnected Operation
  - Allowing an application to continue working when there is a network interruption
- Latency
  - Placing data geographically close to users, so that users can interact with it faster
- Scalability
  - Being able to handle a higher volume of reads than a single machine could handle, by performing reads on replicas

Main approaches:

- Single-leader replication
  - client sends all writes to single node (leader), which are sent to other replicas
  - reads performed by any replica
- Multi-Leader replication
  - clients send writes to one of several leaders
  - leaders send changes to each other and to followers
- Leaderless replication
  - Clients send each write to several nodes, and read from several nodes in parallel in order to detect and correct nodes with stale data

Consistency models:

- Read-after-write consistency
  - Users should always see data that they submitted themselves
- Monotonic reads
  - After users have seen the data at one point in time, they shouldnt later see the data from some earlier point in time
- Consistent prefix reads
  - Users should see the data in a state that makes causal sense
