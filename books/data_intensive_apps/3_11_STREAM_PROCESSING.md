# Chapter 11. Stream Processing

A big assumption of batch processing is that the input is bounded: it has a known and finite size, which allows the batch process to know when it has finished readin gits input

## Transmitting Event Streams

A record is more commonly known as an event: a small, self-contained, immutable object containing the details of something that happened at some point in time

The more often you poll, the lower percentage of requests that return new events, and thus the higher the overheads become

Instead, it is better for consumers to be notified when new events appear

### Mesasging Systems

Helpful to answer two questions:

- What happens if the producers send messages faster than the consumers can process them? Three options:
  - System drops messages
  - Buffers messages in a queue
  - Apply `backpressure` which blocks the producer from sending more messages
- What happens if a node crashes or temporarily goes offline - are any messages lost?

#### Direct Messaging from Producers to Consumers

- UDP multicast use when low latency is important
- Brokerless messaging libraries over TCP or IP

Although direct messaging work well in situations for which they were designed, they generally require the application code to be aware of the possibility of a message lost

#### Message Brokers

A widely used alternative - essentially a kind of database that is optimized for handling message streams

By centralizing the dat ain the broker, these systems can more easily tolerate clients that come and co (connect, disconnect, crash)

#### Mesasge Brokers Compared to Databases

- Dbs usually keep data until it is explicitly deleted, message brokers delete when a message has been successfully delivered to its consumers
- Because messages are quickly deleted, their queues are short
- DBs often support secondary indexes, while message brokers support some way of suscribing to a subset of topics matching some pattern
- When querying a database, the result is typically based on a point in time snapshot of the data, by contrast message brokers do not support arbitrary queries, but they do notify clients when data changes (a new message becomes available)

#### Multiple Consumers

When multiple consumers read messages in the same topic, two main patterns of messaging are used:

- Load balancing
  - Each message is delivered to `one` of the consuemrs so the consumers can share the work of processing the messages in the topic
  - This pattern is useful when th emessages are expensive to process so you want to be able to add consumers to parallelize the processing
- Fan-out
  - Each message is delivered to `all` of the consumers
  - Allows several independent consumers to each "tune in" to the same broadcast without affecting each other

#### Acknowledgements and Redelivery

A client must explicitly tell the broker when it has finished processing a message so that the broker can remove it from the queue

If message order matters, gotta be careful how you use queues and redeliery

### Partitioned Logs

#### Using Logs for Message Storing

In the context of a message broker:

- a producer sends a message by appengin it to the end of the log
- a consumer receives messages by reading the log sequentially

In order to scale to higher throughput than a single disk can offer, the log can be `partitioned`

A topic can be described as a group of partitions that all carry mesasges of the same type

#### Logs Compared to Traditional Messaging

#### Consumer Offsets

very similar to the `log sequence number`

#### Disk Space Usage

To reclaim disk space, the log is divided into segments, and from time to time old segments are deleted or moved to archive storage

#### When Consumers Cannot Keep Up with Producers

#### Replaying Old Messages

## Databases and Streams

### Keeping Systems in Sync

### Change Data Capture

The process of observing all data changes written to a database, and extracting them in a form in which they can be replicated to other systems

CDC is especially interesting if changes are made available as a stream, immediately as they are written

#### Implementing Change Data Capture

#### Initial Snapshot

The snapshot of the db must correspond to a known position or offset in the change log, so that you know at which point to start applying changes after the snapshot has been processed

#### Log Compaction

#### API Support for Change Streams

### Event Sourcing

Similar to CDC but applies the idea at a different level of abstraction:

- In cdc, application used the database in a mutable way, updating and deleting records at will
  - the log of changes is extracted from the db at a low level, which ensures that the order of writes extracted from the db matches the order in which they were actually written
- In event sourcing, the application logic is explicitly built on the basis of immutable events that are written to an event log
  - In this case, the event store is append only and updates or deletes are discouraged or prohibited

Event sourcing is a powerful technique for data modeling: from an application point of view, it is more meaningful to record the users actions as immutable events, rather than recording the effect of those actions on a mutable database

#### Deriving Current State from the Event Log

#### Commands and Events

### State, Streams, and Immutability

Whenever you have a state that changes, that state is the result of the events that mutated it over time

The log of all changes represents the evolution of state over time

"Transaction logs record all the changes made to the database. High-speed appends are the only way to change the log. From this perspective, the contents of the database hold a cache of the latest record values in the logs. The truth is the log. The database is a cache of a subset of the log. That cached subset happens to be the latest valuue of each record and index value form the log

#### Advantages of Immutable Events

#### Deriving Several Views from the Same Event Log

Good to separate mutable state from the immutable event log

Allows you to derive several different read-oriented representations from the same log of events

#### Concurrency Control

#### Limitations of Immutability

## Processing Streams

What do you do with a stream once you have it:

- You can take the data in the events and write it to a database, cache, search index, or similar storage system - from where it can then be queried by other clients
  - Good way of keeping a db in sync with changes happening in other parts of the system, especially if the stream consumer is the only client writing to the db
- You can push the events to users in some way, like email or alerts, or streaming events to a real time dashboard
- You canprocess one or more input streams to produce more output streams

### Uses of Stream Processing

Long been used for monitoring:

- Fraud detection
- Trading systems
- Manufacturing systems
- Military and intelligence systems

#### Complex Event Processing

Geared towards the kind of application that requires searching for certain event patterns, kinda like what regex provides

#### Stream Analytics

Another area in which stream processing is used is for analytics on streams

Boundary between CEP and stream analytics is blurry, but as a general rule, analytics tends to be less interested in specific event sequences. Instead more oriented toward aggregations and statistical metrics over a large nubmer of events:

- Measuring the rate of some type of event
- Calculating the rolling average of a value over some time period
- Comparing current stats to previous time intervals

#### Maintaining Materialized Views

#### Search on Streams

Formaulate the search query in advance, and then continually match the stream of items agains the query

#### Message Passing and RPC

### Reasoning About Time

#### Event Time vs Processing Time

Confusing event time and processing time leads to bad data

#### Knowing When Youre Ready

A tricky problem when defining windows in terms of event time is that you can never be sure whn you have received all of the events for a particular window, or whether there are some events still to come

You have twooptions:

- Ignore straggler events, as they are probably a small percentage of events in normal circumstances
  - Then track number of dropped events as a metric, and alert if you start dropping a significant amount of data
- Publish a `correction`, an updated value for the window with stragglers included

#### Whose Clock Are You Using, Anyway

Assigning timestamps to events is even more difficult when events can be buffered at several points in the system

To adjust for incorrect device clocks, one approach is to log three timestamps:

- The time at which the event occured, according to the device clock
- The time at which the event was sent to the server, according to the device clock
- The time at which the event was received by the server, according to the server clock

#### Types of Windows

Once you know how the timestamp of an event should be determined, the next step is to decide how windows over its time periods should be defined

- Tumbling window
  - Window has a fixed length, and every event belongs to exactly one window
  - Like 1 min sequential
- Hopping window
  - fixed length
  - but allows minor overlap to provide smoothing
  - 5min window with 1min hop size
- Sliding window
- Session window
  - no fixed duration
  - defined by grouping together all events for the same user that occur closely together in time
  - common for website analytics

### Stream Joins

Three types

- Stream-Stream Join (Window Join)
  - To implement, a stream processor needs to maintain state
- Stream-Table Join (Stream Enrichment)
- Table-Table Join (materialized view maintenance)

#### Time-Dependence of Joins

If the state changes over time, and you join with some state, at what point in time do you use for the join

If the ordering of events across sterams is undetermined, the join becomes nondeterministic, which means you cannot rerun the same job on the same input and necessarily get the same result: the events on the input streams may be interleaved in a different way when you run the job again

In data warehouses, this issue is known as a `slowly changing dimension (SCD)` and is often addressed by using a unique identifier for a particular version of a joined record - this change makes the jion deterministic, but has the consequence that log compation is not possible, since all versions of the records in the table need to be retained

### Fault Tolerance

Same issue arises in stream processing, but less straightforward to handle: waiting until a task is finished before making its output visible is not an option, because a stream is infinite so you can never finish processing it

#### Microbatching and Checkpointing

One solution is to break the stream into small blocks - microbatching

Implicitly provides a tumbling window

#### Atomic Commit Revisited

#### Idempotance

#### Rebuilding State After a Failure

## Summary

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
