# Chapter 12. The Future of Data Systems

"If the highest aim of a captain was to preserve his ship, he would keep it in port forever"

## Data Integration

### Combining Specialized Tools by Deriving Data

"In my experienct, 99% of people only need X" or "dont need X" - such statements speak about the experience of the speaker, not the actual usefulness of a technology. What one person considers to be an obscure and pointless feature may well be a central requirement for someone else

#### Reasoning About Workflows

#### Derived Data vs Distributed Transactions

#### The Limits of Total Ordering

- In most cases, constructing a totally ordered log requires all event sot pass through a single leader node that decides theordering
  - If the throughput of events is greater than a single machine can handle, you need to partition the log across multiple machines
- If the servers are spread across multiple geographically distributed datacenters, youll typically have a separate leader in each datacenter, which implies an udefined ordering of events that originate in two different datacenters
- When apps are deployed as microservices, cant determine order between events from one service to another (if they perform the same fn)
- Some apps maintain client-side state that is updated immediately on user input - with these, very likely to see events in different orders

#### Ordering Events to Capture Causality

Places to start:

- Logical timestamps can provide total ordering without coordination, but still require recipients to handle events that are delivered out of order, and require additional metadata to be passed around
- If you can log an event to record the state of the system that the user saw before making a decision, and it gave that event a unique identifier, then any later events can reference that event identifier in order to record the causal dependency
- Conflict resolution algorithms - useful for maintaining state, but do not help if actions have external side effects (like sending notifications)

### Batch and Stream Processing

#### Maintaining Derived State

Derived data systems could be maintained synchronously, but asynchrony is what makes systems based on event logs robust - they allow a fault in one part of the system to be contained locally

#### Reprocessing Data for Application Evolution

##### Schema Migrations on Railways

In england, used to be two different width rails, and trains couldnt ride on both

So a "third" rail was introduced, which allowed for gradual migration

"Reprocessing" the existing tracks in this way allowed old and new versions to exist side by side

#### The Lambda Architecture

In lambda approach, the stream processor consumes the events and quickly produces an approximate update to the view

The batch processor later consumes the same set of events, and produces a corrected version of the derived view

The reasoning behind this design is that batch processing is simpler and less prone to bugs

While stream processors are thought to be less reliable and harder to make fault tolerant - moreover `the stream process can use fast approximate algorithms while the batch process uses slower exact algorithms`

#### Unifying Batch and Stream Processing

Unifying batch and stream processing in one system requires the following features:

- The ability to replay historical events though the same processing engine that handles the stream of recent events
- Exactly-once semantics for stream processors - that is ensuring that the output is the same as if no faults had occurred, even if faults did in fact occur
  - Like batch processing, requires discarding partial output of failed tasks
- Tools for windowing by event time, not processing time, since processing time is meaningless when reporcessing historical events

## Unbundling Databases

### Composing Data Storage Technologies

#### Creating an Index

#### The Meta-Database of Everything

- Federated Databases: Unifying Reads
  - if it was possible to provide a unified query interface to a wide variety of underlying storage engines and processing methods
- Unbundled Database: Unifying Writes
  - Making it easier to reliably plug together storage systems (e.g. though cdc and event logs) is like unbundling a dbs index-maintenance features in a way that can synchronize writes across disparate technologies

#### Making Unbundling Work

Federation and unbundling are two sides of the same coin: composing a reliable, scalable, and maintainable system out of diverse components

The big advantage of log-based integration is loose coupling between the various components

Its about breadth, not depth

#### Unbundled vs Integrated System

#### Whats Missing

### Designing Applications Around Dataflow

#### Application Code as a Derivation Function

When one dataset is derived from another, it goes through some kind of transformation function

#### Separation of Application Code and State

#### Dataflow: Interplay Between State Changes and Application Code

#### Stream Processors and Services

### Observing Derived State

#### Materialized Views and Caching

#### Stateful, Offling-Capable Clients

#### Pushing State Changes to Clients

#### End-to-End Event Streams

#### Reads are Events Too

#### Multi-Partition Data Processing

## Aiming for Correctness

### The End-To-End Argument for Databases

#### Exactly-Once Execution of an Operation

#### Duplicate Suppression

#### Uniquely Identifiying Requests

#### The End-to-End Argument

#### Applying End-to-End thinking in Data Systems

### Enforcing Constraints

#### Uniqueness Constraints Require Consensus

#### Uniqueness in Log-Based Messaging

#### Multi-Partition Request Processing

### Timeliness and Integrity

#### Loosely Interpreted Constraints

Basically, in some cases can correct things at the human level - if two users book same seat on plane, go back and tell one of em ya goofed

In many business contexts, it is acceptable to temporarily violate a constraint and fix it up later by apologizing

#### Coordination-Avoiding Data Systems

### Trust, but Verify

#### Maintaining Integrity in the Face of Software Bugs

#### Dont Just Blindly Trust What They Promise

#### A Culture of Verification

#### Designing for Auditability

#### Tools for Auditable Data Systems

Some interesting lessons from blockchain

## Doing the Right Thing

### Predictive Analytics

#### Bias and Descrimination

#### Responsibility and Accountability

#### Feedback Loops

### Privacy and Tracking

#### Surveillance

#### Consent and Freedom of Choice

#### Privacy and Use of Data

#### Data as Assets and Power

#### Remembering the Industrial Revolution

#### Legislation and Self-Regulation

## Summary
