# Chapter 6. Partitioning

For very large datasets, or very high query thruput: we need to break the data up into `partitions`, also known as `sharding`

Normally, partitions are defined in such a way that each piece of data (each record, row, or document) belongs to exactly one partition

The main reason for wanting to partition data is `scalability`

A large dataset can be distributed across many disks and the query load can be distributed across many processors

For queries that operate on a single partition, each node can independenly execute the queries for its own partition, so the query throughput can be scaled by adding more nodes

## Partitioning and Replication

Partitioning is usually combined with replication so that copies of each partition are stored on multiple nodes - so even though each record belongs to exactly one partition, it may still be stored on several different nodes for fault tolerance

## Partitioning of Key-Value Data

How do you decide which records to store on which nodes?

Our goal with partitioning is to spread the data and the query load evenly across nodes - in theory, if balanced, 10 nodes should be able to handle 10x as much data and 10x the read and write thruput of a single node (ignoring replication)

If partitioning is unfair, then it is `skewed` - a partition is a disproportionately high load is called a `hot spot`

### Partitioning by Key Range

One way of partitioning is to assign a continuous range of keys (from some minimum to some maximum) to eacdh partition (like volumes of an encyclopedia)

- if you know the boundaries between the ranges, you can easily determine which partition contains a given key

The ranges of keys are not necessarily evenly spaced, because your data may not be evenly distributed. Partition boundaries may be chosen manually, or the db can choose them automatically

Downside of key range partitioning is that certain access patterns can lead to hotspots. If the key is a timestamp, then the partitions correspond to ranges of time - one partition per day. So if we write real time, all writes go to same partition (todays partition) which overloads it while other sit idele

Use something other than time to partition

### Partitioning by Hash of Key

A good hash function takes skewed data and makes it uniformly distributed

### Skewed Workloads and Relieving Hot Spots

Hashing helps but cannot avoid them entirely - re: socail media site, a celebrity user with millions of followers causes a storm of activity when they do something

A simple mitigation technique is for hot keys, assign a random number to beginning or end which splits the hot key across n number of keys - BUT this incurs write overhead as now readers have to read data from all 100 keys and combine it

## Partitioning and Secondary Indexes

A secondary index usually doesnt identify a record uniquely but rather is a way of searching for occurences of a partiular value

Problem is they dont map neatly to partitions

### Partitioning Secondary Indexes by Document

Here, each partition is completely separate and each partition maintains its own secondary index

docment-partitioned index is also known as a `local index` as opposed to a `global index`

reading from these requires care - uless you have done something special with the document ids, there is no reason why all cars with a particular color or make would be in the same partition. so, you need to send the query to all partitions and combine the results

This approach to querying a partitioned database is sometimes known as `scatter/gather` and can make read queries on secondary indexes quite expensive

DB vendors recommend that you structure your partitioning scheme so that secondary index queries can be served form a single partition

### Partitioning Secondary Indexes by Term

Construct a `global index` that covers data in all partitions

A global index must also be partitioned, but it can be partitioned differently from the primary key index

Downside is writes are slower and more complicated, because a write to a single document may now affect multiple aprtitions of the index (every term in the document might be on a different partition, on a different node)

In practice, updates to global secondary indexes are often asynchronous

## Rebalancing Partitions

Over time, things change in a database:

- The query throughput increases, so you want to add more CPUs to handle the load
- The dataset size increases, so you want to add more disks and RAM to store it
- A machine fails, and other machines need to take over the failed machines responsibilities

The process of moving load from one node in the cluster to another is called `rebalancing`

Rebalancing us usually expected to meet some minimum requirements:

- After rebalancing, the load (data storage, read and write requests) should be shared fairly between the nodes in the cluster
- While rebalancing is happening, the database should continue accepting reads and writes
- No more data than necessary should be moved between nodes, to make rebalancing fast and to minimize the network and disk io load

### Strategies for REbalancing

#### How NOT to do it: Hash Mod N

If the number N nodes changes, most keys will need to be moved from one node to another

#### Fixed Number of Partitions

Create many more partitions than there are nodes, and assign several partitions to each node - e.g. a db may run a 10 node cluster and be split into 1000 partitions

Now, if a node is added to the cluster, the new node can `steal` a few partitions from every existing node until partitions are fairly distributed once again - only entire partitions are moved between nodes

In principle, you can even account for mismatched hardware in your cluster: by assigning more partitions to nodes that are more powerful, you can force those nodes to take a greater share of the load

#### Dynamic Partitioning

For databases that use key range partitioning, a fixed number of partitions with fixed boundaries would be very inconvenient: if you got the boundaries wrong, you could end up with all of the data in one partition, and all of the other partitions empty

When a partition grows to exceed a configured size, it is split into two partitions so that approximately half of the data ends up on each side of the split

Conversely, if lots of data is deleted and a partition shrinks below some threshold, it can be merged with an adjacent partition

Caveat is that in empty databases, they start with a single partition. some dbs will pre-split an empty db

#### Partitioning Proportionally to Nodes

Make number of partitions proportional to number of nodes - to have a fixed number of partitions per node

### Operations: Automatic of Manual Rebalancing

Does rebalancing happen automatically or manually?

Some dbs generate a suggested partition automatically, but require an admin to commit it before it takes effect

Fully atomated rebalancing can be convenient, because there is less operational work to do for normal maintenance, but can be unpredictable and rebalancing is an expensive operation

Such automation can be dangerous in combination with automatic failure detection - say one node is overloaded and temporarily slow. other nodes conclude the node is dead, and automatically rebalance the cluster to move away from it. this puts additional load on the overloaded node, other nodes, and the network

Good thing to have a human in the loop for rebalancing. Slower than fully automatic, but can help prevent operational surprises

## Request Routing

When a client wants to make a request, how does it know which node to connect to?

This is an instance of a more general problem called `service discovery`

High level approaches:

- Allow clients to contact any node (e.g. via round robin load balancer)
  - If that node coincidentally owns the partition to which the request applies, it can handle the request directly
  - If not, forward the request to the appropriate node
- Send all requests from client to a routing tier first, which determines the node that should handle each request
  - the routing tier does not handle the request - it only acts as a partition aware load balancer
- Require that clients be aware of the partitioning and the assignment of partitions to nodes
  - In this case, a client can connect directly to the appropriate node, without any intermediary

In all cases, the key problem is: how does the component making the routing decision learn about changes in the assignment of partitions to nodes?

This is a problem because all participants must agree

Many distributed systems rely on separate coordination services such as ZooKeeper to keep track of this cluster metadata

### Parallel Query Execution

For massively parallel processing (MPP) are much more sophisticated in the types of queries they support

They will revisit this in a future section

## Summary

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
