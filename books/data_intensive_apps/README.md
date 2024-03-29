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

### [Chapter 6. Partitioning](./2_6_PARTITIONING.md)

Two main approaches to partitioning:

- Key range partitioning
  - Keys are sorted and a partition owns all keys from some minimum up to some maximum
  - Sorting has the advantage that efficient range queries are possible
  - Risk of hotspots if the application often accesses keys that are close together in the sorted order
  - Partitions are rebalanced dynamically by splitting the range into two subranges when a partition gets too big
- Hash partitioning
  - Hash function applied to each key, and a partition owns a range of hashes
  - Makes range queries inefficient, but may distribute the load more evenly
  - Common to create a fixed number of partitions in advance, and assign several partitions to each node - dynamic partitioning can also be used

Secondary index partitioning:

- Document-partitioned indexes (local indexes)
  - Secondary indexes are stored in the same partition as the primary key and value
  - Measn that only a single partition needs to be updated on write, but a read of the secondary index requires a scatter/gather across all partitions
- Term-partitioned indexes (global indexes)
  - Where the secondary indexes are partitioned separately, using the indexed values
  - When a document is written, several partitions of the secondary index need to be updated
  - But, a read can be served from a single partition

### [Chapter 7. Transactions](./2_7_TRANSACTIONS.md)

Transactions are an abstraction layer that allows an applicatio to pretend that certain concurrency problems and certain kinds of hardware and software faults dont exist

Isolation levels:

- read committed
- snapshot isolation (repeatable read)
- serializable

Race Conditions:

- Dirty reads
  - One client reads another clients write before they have been committed. The read committed isolation level and stronger levels prevent dirty reads
- Dirty writes
  - One client overwrites data that another client has written, but not yet committed. Almost all transaction implementations prevents dirty writes
- Read skew
  - A client sees different parts of the db at different points in time. Some cases of read skew are also known as `nonrepeatable reads`. Commonly prevented with snapshot isolation and is usually implemented with `multi-version concurrency control (MVCC)`
- Lost updates
  - Two clients concurrently perform a read-modify-write cycle. One overwrites the others write without incorporating its changes, so data is lost. Some implementations prevent this anomaly automatically, while others require a manual lock (SELECT FOR UPDATE)
- Write skew
  - A transaction reads something, makes a decision based on the value it saw, and writes the decision back to the db. However, by the time the write is made, the premise of the decision is no longer true. Only serializable isolation prevents this anomaly
- Phantom reads
  - A transaction reads the object that matches some search condition. Another client makes a write that affects the results of that search. Snapshot isolation prevents straightforward phantom reads, but phantoms in the context of write skew require special treatment, such as index-range locks

Approaches to implementing serializable transactions:

- Literally executing transactions in a serial order
  - If you can make each transaction very fast to execute, and the transaction thruput is low enough to process on a single cpu core, this is a simple and effective option
- Two-phase locking
  - For decades, this has been the standard way of implementing serializability, but many applications avoid using it because of its performance characteristics
- Serializable snapshot isolation (SSI)
  - A fairly new algorithm that avoids most of the downsides of previous approaches. It uses an optimistic approach, allowing transactions to proceed without blocking. When a transaction wants to commit, it is checked, and it is aborted if the execution was not serializable

### [Chapter 8. The Trouble with Distributed Systems](./2_8_TROUBLE_DISTRIBUTED.md)

Some problems:

- Packets may be lost or delayed, so you have no idea if the message got thru
- A nodes clock may be significantly out of synch
- A process may pause for a substantial amount of time

Build tolerance of partial failures, so that the system as a whole may continue to function

- First, must be able to detect faults (but can be hard)
- Then, have to handle - but not easy considering no shared memory or common knowledge, and all info must be exchanged over the unreliable network. Use quorums

### [Chapter 9. Consistency and Concensus](./2_9_CONSISTENCY_CONCENSUS.md)

Best way of building fault-tolerant systems is to find some general purpose abstractions with useful guarantees, implement them once, and then let applications rely on those guarantees

## Part III. Derived Data

Systems of Record - holds authoritative versions of the data - commonly normalized

Derived Data Systems - result of taking some existing data form another system, and transforming or procesisng it in some way (recreatable) - commonly denormalized

### [Chapter 10. Batch Processing](./3_10_BATCH_PROCESSING.md)

"A system cannot be successful it it is too strongly influenced by a single person. Once the initial design is complete and fairly robust, the real test begins as people with many different viewpoints undertake their own experiments"

#### The Unix Philosophy

- Make each program do one thing well. To do a new job, build afresh rather than complicate old programs by adding new "features"
- Expect the output of every program to become the input to another, as yet unknown, program. Dont clutter output with extraneous information. Avoid stringently columnar or binary input formats. Dont insist on interactive input
- Design and build software, even operating systems, to be tried early, within weeks. Dont hesitate to throw away the clumsy parts and rebuild them
- Use tools in preference to unskilled help to lighten a programming task, even if you have to detour to build the tools and expect to throw some of them out after youve finished using them

The approach: automation, rapid prototyping, incremental iteration, friendly to experimentation, breaking large projects into manageable chunks

#### Summary

Two main problems that distributed batch processing frameworks need to solve are:

- Partitioning
- Fault Tolerance

How partitioned algorithms work:

- Sort-merge Jions
  - Each of the inputs being joined goes throught a mapper that extracts the join key
  - By partitioning, sorting, and marging, all the records with the same key end up going to the same call of the reducer - this function can then output the joined records
- Broadcast hash joins
  - One of the two join inputs is small, so it is not partitioned and can be entirely loaded into a hash table
  - Then, you can start a mapper for each partition of the large join input, load the hash table for the small input into each mapper, and then scan over the large input one record at a time, querying the hash table for each record
- Partitioned hash joins
  - If the two join inputs are partitioned in the same way (using the same key, same hash function, and same number of partitions), then the hash table approach can eb used independently for each partitions

Distributed batch processing engines have a deliberately restricted programming model:

- callback functions (mappers and reducers) are assumed to be stateless and to have no externally visible side effects besides their designated output
- this restriction allows the framework to hide some of the hard distributed system problem behind its abstraction

The framework allows you do guarantee that the final output of a job is the same as if no faults have occured (though faults could have occured internally, and were retried)

### [Chapter 11. Stream Processing](./3_11_STREAM_PROCESSING.md)

Types of Brokers

- AMPQ/JMS-style message broker
  - Assigns individual messages to consumers, and consumers acknowledge individual messages when they have been successfully processed
  - Messages are deleted from the broker once they have been ackd
- Log-based messge broker
  - The broker assigns all messages in a partition to the same consumer node, and always delivers messages in the same order
  - Parallelism is achieved through partitioning, and consumers track their progress by checkpointing the offset of the last message they have processed
  - The broker retains messages on disk, so it is possible to jump back and reread old messages if necessary

Types of Joins

- Stream-stream joins
  - Both input streams consiste of activity events, and the join operator searches for related events that occur within some window of time
- Stream-table joins
  - One input stream consistes of activity events, while the other is a database changelog
- Table-table joins
  - Both input streams are db changelogs
  - The result is a stream of changes to the materialized view of the join between the two tables

### [Chapter 12. The Future of Data Systems](./3_12_FUTURE.md)

"If the highest aim of a captain was to preserve his ship, he would keep it in port forever"

"In my experienct, 99% of people only need X" or "dont need X" - such statements speak about the experience of the speaker, not the actual usefulness of a technology. What one person considers to be an obscure and pointless feature may well be a central requirement for someone else

"In many business contexts, it is acceptable to temporarily violate a constraint and fix it up later by apologizing"

#### The Lambda Architecture

In lambda approach, the stream processor consumes the events and quickly produces an approximate update to the view

The batch processor later consumes the same set of events, and produces a corrected version of the derived view

The reasoning behind this design is that batch processing is simpler and less prone to bugs

While stream processors are thought to be less reliable and harder to make fault tolerant - moreover `the stream process can use fast approximate algorithms while the batch process uses slower exact algorithms`
