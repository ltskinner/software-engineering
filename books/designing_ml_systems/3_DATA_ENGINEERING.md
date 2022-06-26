# Chapter 3: Data Engineering Fundamentals

Several services working together in production:

- Feature engineering service that computes features from raw data
- Prediction service to generate predictions based on these features
  - will need to exchange features between two

## Data Sources

### User Input Data

- if its possible for users to input wrong data, they will do it
- data will be malformed
  - text too long or too short
  - numerical values in place of text, text in place of numeric
  - upload wrong file formats

### System-Generated Data

- logs and system outputs like model predictions
- logs dont have to be processed instanteneously, can be done periodically depending on criticality of log
  - but must be processed fast enough to detect and notify when something interesting happens
- Is common to log literally everything you can
  - volume of logs grows quickly
  - problems:
    - hard to know where to look because signals get lost in noise

Some good logging tools:

- Logstash
- Datadog
- Logz.io

How to store logs?

- most cases, can only store for as long as it is useful, then discard
- if dont have to access frequently, can store in low access storage thats super cheap

### Internal Databases

### Third-Party Data

- first party: data your company collects
- second party: data collected by another company on their customers that iss shared
- third party: companies collect data on the public that arent direct consumers

## Data Formats

Some questions:

- How do i store multimodal data, e.g. a sample that contains both image and text?
- Where do I store my data so that its cheap and still fast to access?
- How do I store complex models so that they can be loaded and run correctly on different hardware?

`data serialization` the process of converting a data structure of object state into a format that can be stored or transmitted and reconstructed later

Some attributes to consider:

- human readability
- access pattterns
- based on text or binary

Common Data Formats and Where They are Used

| Format | Binary/Text | Human-readable | Example use cases |
| - | - | - | - |
| JSON | Text | Yes | Everywhere |
| CSV | Text | Yes | Everywhere |
| Parquet | Binary | No | Hadoop, Amazon Redshift |
| Avro | Binary primary | No | Hadoop |
| Protobuf | Binary primary | No | Google, Tensorflow (TFRecord) |
| Pickle | Binary | No | Python, PyTorch serialization |

### Row-Major vs Column Major format.

CSV is row major: consecutive elements in a row are stored next to each other in memory

Parquet is column major: consecutive elements in a column are stored next to each other

Computers process sequential data more efficiently than nonsequential data

- if a table is row major, accessingits rows will be faster than accessing columns

Uhhh bottom line:

- Use column major for accessing features (columns)
- Use row major for accessing individual samples

Row major allows faster writes

column major good for feature reads

#### Numpy vs Pandas

Hmm interesting, dfs are actually column major

The code sample here is a bit iffy but it is interesting its not row as I would have expected

### Text vs Binary Format

## Data Models

### Relational

#### From Declarative Data Systems to Declarative ML Systems

"Users only need to declare the features schema and the task, and the system will figure out the best model to perform that task with the given features. Users wont have to write code to construct, train and tune models"

Popular declarative ML frameworks:

- Ludwig
- H20 AutoML

### NoSql

#### Document Model

#### Graph Model

### Structured vs Unstructured Data

- `Data Warehouse` repository for storing structured data
  - Store data that has been processed into formats ready to be used
-`Data Lake` repository for storing unstructured data
  - Store raw data before processing

Key differences between structured and unstructured data

| Structured Data | Unstructured Data |
| - | - |
| Schema clearly defined | Data doesnt have to follow a schema |
| Easy to search and analyze | Fast arrival |
| Can only handle data with a specific schema | Can handle data from any source |
| Schema changes will cause a lot of troubles | No need to worry about schema changes (yet) as the worry is shifted to the downstream applications that use this data |
| Stored in data warehouses | Stored in data lakes |

## Data Storage Engines and Processing

### Transactional and Analytical Processing

`transaction` any kind of action: tweeting, ordering ride share, uploading new model, wathcing video

`online transaction processing (OLTP`

- transactions need to be processed fast (low latency) so that users arent kept waiting
- also needs to be high availability

Basically, all non shit relationals are ACID

- Atomicity
  - guarantee all steps in transaction completed perfectly - no partial completions
- Consistency
  - All the same rules were followed by every single transaction
- Isolation
  - Guarantee that two transactions happen at the same time as if they were isolated
    - Two users accessing the same data wont change it at the same time
- Durability
  - Guarantee that once a transaction has been committed, it will remain committed even in the case of a system failure

`online analytical processing (OLAP)`

kinda outdated

Transactional database taht handles analytical queries: CockroachDB

Analytical databases that can handle transactional queries: Apache Iceberg, DuckDB

In OLTP and OLAP paradigm, storage and processing are tightly coupled - how data is stored is also how data is processed

- can result in
  - same data being stored in multiple databases
  - using different processing engines to solve different types of queries

New paradigm: decouple storage from processing (compute)

- BigQuery, Snowflake, Teradata

For this, data can be stored in same place with processing layer on top that can be optimized for different types of queries

The term "online" once meant only connected to internet, now it also means "in production"

### ETL: Extract, Transform, Load

ETL done prior to going into DB

- extracted from source: csv, database, app exhaust
- transform into something
- load it into a relational dbms

"ETL refers ot the general purpose processing and aggregating of data into the shape and the format that you want"

- Extract
  - Is extracting the data you want form all your sources
  - some will be corrupted or malformatted
  - validate data and reject samples that dont meet requirements
    - may want to notify sources of failures
  - doing this properly saves tons of time downstream
- Transform
  - join data from multiple sources and clean it
  - standardize value ranges
  - operations: transposing, deduplicating, sorting, aggregating, deriving new feature, more data valudation
- Load
  - How and how often to load transformed data into the target destination
  - destinations: file, database, data warehouse

## Modes of Dataflow

How do we pass data between different processes that dont share memory

When data is passed from one process to another, we say that the dat flows from one process to another, which gives us a dataflow

3 main modes of dataflow:

- Data passing thru database
- Data passing thru services using requests (REST, RPC API, POST/GET)
- Data passing thru real-time transport like Apache Kafka and AWS Knesis

### Data Passing Through Databases

Easiest way

- Process A writes to database
- Process B reads from database

Doesnt always work tho:

- Both processes must be able to access the same database
- Both processes must read from a database, so slow read/write times may make it not feasible (almost all consumer facing applications)

### Data Passing Through Services

Send directly through network

`request-driven`

This mode of data passing is tightly coupled with the service-oriented architecture

- A service is a process that can be accessed remotely (thru a network)
- B is exposed to A as a service that A can send requests to
- For B to be able to request data from A, A will also need to be exposed to B as a service

Two services in communication with each other can be run b different companies in different applications

Two services in communication with each other can also be parts of the same application. Structuring different components of your application as separate services allows each component to be developed, tested, and maintained independently of one another. Structuring an application as separate services gives you the godchitecture of microservice architecture

Bro, this is not ground breaking shit I guess most AI people really are completely ignorant to SE fundamentals

### Data Passing Through Real-Time Transport

Have each service just talk to broker

In many ways like a DB, but messages instead of like a db

`event-driven`

- request-driven good for systems that rely more on logic than data
- event-driven works better for systems that are data heavy

Two most common types of real-time transports:

- pubsub (publish subscribe)
  - Any service can publish to different topics in real time transport
  - Any service can read all events from that topic
  - Services that produce data dont care about what services consume their data
  - Usually need retention policy
    - data retained for certain period of time before deletion or moved to permanent storage
- message queue
  - Event has intended consumers (an event with intended consumers is called a message)
  - message queue responsible for getting message to correct consumers

Pubsub:

- Apache kafka
- aws knesis

Message queues:

- Apache RocketMQ
- RabbitMQ

## Batch Processing Versus Stream Processing

`Historical Data` anything in a database, datalke, data warehouse

- Process this with batch jobs, periodically
- can use mapreduce and spark

`Streaming Data` anything that keeps working its way in lol

- process with stream processing
- stream processing can also be done periodically, but are done on much shorter period (five minutes instead of daily)
- best for low latency

Because batch processing happens much less frequently than stream processing, in ML, batch processing is used to compute features that change less often. `Batch features` are also known as `static features`

Stream processing is used to compute features that change quickly (how many rides in last minute). `Streaming features` are also known as `dynamic features`

Stream feature extraction logic can require complex queries with join and aggregation along different dimensions. See:

- Apache Flink
- KSQL
- Spark Streraming
