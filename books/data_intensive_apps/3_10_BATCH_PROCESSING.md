# Chapter 10. Batch Processing

"A system cannot be successful it it is too strongly influenced by a single person. Once the initial design is complete and fairly robust, the real test begins as people with many different viewpoints undertake their own experiments"

Three types of systems:

- Services (online systems)
  - A service waits for a request or instruction from a client to arrive
  - The service tries to handle it as quickly as possible
  - Response time is the primary measure of performance, and availability is often important
- Batch Processing Systems (offline systems)
  - Runs a job over a large amount of data
  - Usually scheduled
  - Measured by throughput
- Stream Processing Systems (near-real-time systems)
  - Unlike batch, consumes inputs and produces outputs shortly after event shappen

## Batch Processing with Unix Tools

### Simple Log Analytics

#### Chain of Commands vs Custom Program

#### Sorting vs In-Memory Aggregation

### The Unix Philosophy

- Make each program do one thing well. To do a new job, build afresh rather than complicate old programs by adding new "features"
- Expect the output of every program to become the input to another, as yet unknown, program. Dont clutter output with extraneous information. Avoid stringently columnar or binary input formats. Dont insist on interactive input
- Design and build software, even operating systems, to be tried early, within weeks. Dont hesitate to throw away the clumsy parts and rebuild them
- Use tools in preference to unskilled help to lighten a programming task, even if you have to detour to build the tools and expect to throw some of them out after youve finished using them

The approach: automation, rapid prototyping, incremental iteration, friendly to experimentation, breaking large projects into manageable chunks

#### Uniform Interface

#### Separation of Logic and Wiring

#### Transperency and Experimentation

## MapReduce and Distributed Filesystems

### MapReduce Job Execution

- Read a set of input files, and break it up into records
- Call the mapper function to extract a key and value from each input record
- Sort all of the key-value pairs by key
- Call the reducer function to iterate over the sorted key-value pairs
  - Iff there are multiple occurences of the same key, the sorting has made them adjacent in the list, so it is easy to combine those values without having to keep a lot of state in memory

Mapper:

- The mapper si called once for every input record, and its job is to extract the key and value from the input record
- For each input, it may generate any number of key-value pairs (including none)
- It does not keep any state from one input record to the next, so each record is handled independently

Reducer:

- Take the key-value pairs produced by the mappers, collects all the values belonging to the same key, and calls the reducer with an iterator over that collection of values
- The reducer can produce output records (such as number of occuences of same url)

#### Distributed Execution of MapReduce

MapReduce scheduler teis to run each mapper on one of th emachines that stores a replica of the input file - principle of `putting the computation near the data` - saves copying the file over the network, reducing network load and increasing locality

#### MapReduce Workflows

Very common for MapReduct jobs to be chained together into workflows

Workflows consisting of 50-100 mapreduce jobs are common when building recommendatino systems

### Reduce-Side Joins and Grouping

#### Sort-Merge Joins

#### Bringing Related Data Together in the Same Place

#### GROUP BY

#### Handling Skew

### Map-Side Joins

#### Broadcast Hash Joins

#### Partitioned Hash Joins

#### Map-Side Merge Joins

#### MapReduce Workflows with Map-Side Joins

### The Output of Batch Workflows

#### Building Search INdexes

Google orgininally built MapReduce to build indexes for its search engine

#### Key-Value Stores as Batch Process Output

Technically, you can write the batch job direclty to the db server, one record at a time, but usually a bad idea:

- Making a network request for every single record is much slower than the normal throughput of the batch task
- MapReduce jobs run maky tasks in parallel - if all mappers or reducers concurrently write to the same output database, with a rate expected of a batch process, that db can easily be overwhelmed
- MapReduce provides a clean all or nothing guarantee - when writing to a db you have to worry about results from partial jobs

A better solution is to build a brand new database inside the batch job as it writes files to the jobs output directory

Those files are then immutable once written, and can be loaded in bulk into servers that handle read only queries

#### Philosophy of Batch Process Outputs

By treating inputs as immutable and avoiding side effects, batch jobs not only achieve good performance but also become much easier to maintain:

- if you introduce a defect to the code and the output is wrong or corrupted, you can roll back to previous version of the code and rerun the job, and the output will be correct again.
  - Or, you can keep the old output in a different directory, and switch back to it
- A consequence of the ease of rolling back, feature development can proceed more quickly than in an environment where mistakes mean irreversible damage
  - The principle of `minimizing irreversibility` is useful
- If a map reduce or task fails, the MapReduce framework automatically re-schedules it and runs it again
- The same set of files can be used as input for various different jobs
- Logic is separated from the wiring

### Comparing Hadoop to Distributed Databases

#### Diversity of Storage

#### Diversity of Processing Models

#### Designing for Frequent Faults

## Beyond MapReduce

### Materialization of Intermediate State

The process of writing out an intermediate state is called materialization

#### Dataflow Engines

#### Fault Tolerance

#### Discussion of Materialization

### Graphs and Iterative Processing

Iterative style:

- and external scheduler runs a batch process to calcualte one step of the algorithm
- when the batch process completes, the scheduler checks whether the iterative algorithm has finished
- if the algorithm has not yet finished, the scheduler goes back to step 1 and runs another round of the batch process

#### The Pregel Processing Model

#### Fault Tolerance

#### Parallel Execution

### High-Level APIs and Languages

#### The Move Toward Declarative Query Languages

#### Specialization for Different Domains

## Summary

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
