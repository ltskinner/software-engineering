# Chapter 5. Data Generation in Source Systems

Job of the data engineer is to take data from the source systems, do something with it, and make it helpful in serving downstream use cases

## Sources of Data: How is Data Created

- Analog Data
  - occurs in the real world, such as vocal speech, sign language, written on paper
- Digital Data
  - product of converting analog data to digital
  - or, is the natuve product of a digital system

## Source Systems: Main Ideas

### Files and Unstructured Data

- Applications often write data to files
  - parameters, events, logs, images, video

Some data engineering focused formats:

- Parquet
- ORC
- Avro

### APIs

- lotta time spent maintaining custom API connections

### Application Databases (OLTP systems)

- Application dbs store the state of an application
  - these are typically online transaction processing (OLTP)
    - read and write individual data records at ahigh rate
    - aka, tansactional databases
    - low latency, high concurrency
- OLTP and analytics
  - often, small companies run analytics directly on oltp
  - this works in short term, but doesnt scale

### Online Analyticsl Processing System (OLAP)

- good for running large analytics queries
- poor for handling lookups of individual records
- olap may serve data for:
  - training ML model
  - reverse etl workflow

### Change Data Capture

- method for extracting each change event (insert, update, delete) that occurs in a database
- often, event logs get generated that can be processed to create a stream

### Logs

Logs should capture:

- who
  - the human, system, or service, associated with the event
- what
  - the event and related metadata
- when
  - timestamp

### Database Logs

Important, lol

I guess in some cases they write the operation that is slated to occur, before it occurs, so that if something fails the expected state can be recovered

### Insert-Only

- uhh basically, records dont get updated or deleted, just new shit gets stacked on top of old with a timestamp
- has some disadvantages tho (obviously haha)

### Messages and Streams

- messages are raw data communicated
  - typically sent thru a message queue
  - publisher sends to consumer
  - once a message is delivered, it is removed from the queue
- streams are append only log of event records
  - streams are used to see what happened over a series of numerous events
  - stream records are persisted over a long time (weeks or months)

### Types of Time

- Event time: the time the event is generated
  - generated in the source system
- Ingestion time: when the event is ingested
- Process time: how long processing took

## Source System Practical Details

### Databases

#### Major Considerations for Understanding Database Technologies

- Database Management System
- Lookups
  - know whether db uses indexes and what the best patterns for designing and maintaining them are
- Query optimizer
- Scaling and distribution
- Modeling patterns
- CRUD
- Consistency

##### NoSql varieties

- key-value stores
  - in-memory key-value dbs are popular for caching session data for web and mobile applications (where ultra-fast lookup and high concurrency are required)
  - ecommerce is good as well
- document stores
- wide-column database
  - good for massive amounts of data
  - high transaction rates, extremely low latency
  - popular in ecommerce, fintech, ad tech, iot
  - do not support conplex queries
  - only have one index (the row key)
- graph databases
  - nodes and edges babyy
- search database
  - text search
    - exact, fuzzy, semantic
  - log analysis
    - anomaly detection, real-time monitoring, security analysis, operational analytics
- Time Series
  - Optimized for retrieval and statistical processing of time-series data

### APIs in depth

- REST
  - stateless babyy
  - can induce global state changes tho
- GraphQL
  - I guess more flexible than REST
  - returns data in JSON format? not sure how thats novel
- Webhooks
  - event-based data-transmission pattern
  - when events happen, a call is triggered to an HTTP endpoint hosted by the data consumer
  - aka: `reverse APIs`
- RPC and gRPC
  - Remote Procedure Call
  - common in distributed computing
  - protobufs

### Data Sharing

- row, column, and sensitive record data filtering

### Third-Party Data Sources

### Message Queues and Event-Streaming Platforms

Event driven architectures are ideal because events can both trigger work inthe application and feed near real-time analytics

#### Mesasge Queues

- mechanism to asynchronously send data between systems using a `publish and subscribe` model
- critical ingredient for decoupled microservices and event-driven architectures

Pay attention to:

- Message ordering and delivery
  - order in which messages are created, sent, and received
  - in general, dont assume messages will be in order. design accordingly
- Delivery frequency
  - messages can be sent exactly once, or at least once
    - exaclty once are deleted after the subscriber acknoledges it
    - at least once can be consumed by multiple subscribers or the same subscriber more than once
  - systems should be idempotent
    - outcome of processing a message once is identical to processing it multiple times
- Scalability

#### Event-Streaming Platforms

typically will have:

- key
- value
- timestamp

Some Characteristics:

- Topics
  - producers stream to topics, a collection of related events
  - fraud alers, orders, temperature readings
  - can be many to many
- Streaming Partitions
  - dividing a stream into multiple streams
  - allows for parallelism and higher throughput
  - partitione don partition key
  - want to make sure u dont hotspot - send disproportionately more or less to an individual partition
- Fault tolerance and resilience

## Whom Youll Work With

- Systems stakeholders
  - build and maintain the source system (engineers, developers, POs)
- Data stakeholders
  - own and control access to the data (IT, governance group)
- In some cases these are the same people

Can be benefitial to convey to the generators your system requirements and ask they meet your requirements. Along the lines of 99% uptime or something like that

## Undercurrents

### Security

- Is the source sytem architected so data is secure and encrypted, both with data at rest and while data is transmitted?
- Do you have to access the source system over the public internet, or are you using a vpn?
- Keep passwords, tokens, and credentials to the source system locked away
- Do you trust the source system? Trust but verify and make sure youre not on the receiving end of data from a bad actor

### Data Management

- Data Governance
  - Are upstream data and systems governed in a reliable, easy-to-understand fashion? Who manages the data?
- Data Quality
  - How do you ensure data quality and integrity in upstream systems?
  - Work with source system teams to set expectations on data and communication
- Schema
  - Expect that upstream schemas will change. Where possible, collaborate with source system teams to be notified of looming schema changes
- Master data management
  - Is the creation of upstream records controlled by a master data management practice or system?
- Privacy and ethics
  - Do you have access to raw data, or will the data be obfuscated?
  - What are the implications of the source data?
  - How long is it retained?
  - Does it shift locations based on retention policies?
- Regulatory
  - Based upon regulations, are you supposed to access the data?

### DataOps

- Automation
  - Theres automation impacting the source system
  - Does an issue in the source sytems automation impact my data workflow automation?
- Observability
  - How will I know when theres an issue in the source system?
  - How will I know if the data sent over is good?
- Incident response
  - How will my system respond if the source system goes offline?
  - Whats the plan to backfill data once the source system gets back online?

### Data Architecture

- Reliability
  - Does the system produce predictable outputs?
  - How often can we expect the system to fail?
  - Whats the MTTR to get the system back online?
- Durability
  - How does the source system handle data loss from hardware failures or network outages?
  - Whats the plan for handling outages for an extended period?
  - How to minimize the "blast radius" of an outage?
- Availability
  - What guarantees that the source system is up, running, and available when its supposed to be?
- People
  - Whose in charge of the source system design, and how will you know if breaking changes are made in teh architecture?

### Orchestration

- Cadence and frequency
  - Is the data available on a fixed schedule, or can you access the new data whenever you want?
- Common frameworks
  - Do software and data engineers use the same container manager?
  - Would it make sense to integrate application and data workloads into the same K8s cluster?
  - If using Airflow, does it make sense to integrate it with the upstream application team?

### Software Engineering

- Networking
  - Make sure code can access the network where source systems reside
  - Do secure networking too - HTTPS and SSH or use a VPN
- Authentication and Authorization
  - make sure to have proper credentials
  - use secret managers
  - use IAM roles
- Acces spatterns
  - How are retries and timeouts handled
- Orchestration
  - Does code integrate with orchestration framework?
  - Can it be executed as an orchestrated workflow?
- Parallelization
  - How are you managing and scaling parallel access to source systems?
- Deployment
  - How are you handling the deployment of source code changes?


