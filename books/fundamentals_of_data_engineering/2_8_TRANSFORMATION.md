# Chapter 8. Queries, Modeling, and Transformation

## Queries

### What Is a Query?

- query - allows you to retrieve and act on data
  - CRUD stuff

#### Data Definition Language

- ddl commands are used to perform operations on database objects
  - objects like db itself, schemas, tables, users, etc
  - ddl defines the state of objects in the db
- common expressions
  - `CREATE`
  - `DROP`
  - `UPDATE`

#### Data Manipulation Language

- after using ddl to define database objects, need to add and alter data within them
- dml does this
- common commands:
  - `SELECT`
  - `INSERT`
  - `UPDATE`
  - `DELETE`
  - `COPY`
  - `MERGE`

#### Data Control Language

- dcl lets you control access to database objects (literal db objects)
- commands:
  - `GRANT`
  - `DENY`
  - `REVOKE`

#### Transaction Control Language

- tcl lets you define commit checkpoints, comditions when actions will be rolled back, etc
- commands:
  - `COMMIT`
  - `ROLLBACK`

### The Life of a Query

- db engine compiles sql
  - checks for proper semantics
  - verify db objects exist
  - verify user access
- sql converted to bytecode
  - express steps to be executed by the db engine
- query optimizer analyzes bytecode to determine how to execute query
  - reorder and refactor various steps to use resources efficiently
- query is executed
- results are produced

### The Query Optimizer

Queries can have wildly different execution times depending on how theyre executed

- goal is to minimize cost
- assess joins, indexes, data scan sizes, etc

### Improving Query Performance

- Will inevitably encounter poor performing queries
- Invaluable to know how to identify and fix these
- Dont fight the database
  - learn to work with its strengths
  - and augment its weaknesses

#### Optimize your join strategy and schema

- a common technique for improving query performance is to `prejoin` data
  - analytics queries are joining same data repeatedly
    - makes sense to join data in advance, and have queries read from prejoined version
    - relaxing normalization to widen tables
- improve performance of complex joins
  - many row-oriented databases allow you to index a result computed from a row
  - can also create a new derived column for joining
- use common table expressions (ctes) instead of nested subqueries or temporary tables
  - ctes allow users to compose complex queries in a readable fashion
  - let you understand the flow of the query
  - in many cases, will have better performance than a script that creates intermediate tables

#### Use the explain plan and understand your querys performance

- can access with `EXPLAIN` command or in some cases there is a visual representation
- also can provide metrics on resource consumption

Things to monitor:

- Usage of key resources such as disk, memory, and network
- Data loading time versus processing time
- Query execution time, number of records, the size of the data scanned, the quantity of data shuffled
- Competing queries that might cause resource contention in your database
- Number of concurrent connections used versus connections available. Oversubscribed concurrent connections can have negative effects on your users who may not be able to connect to the database

#### Avoid full table scans

- general rule of thumb: only query data you need
  - use predicates, not select *s lmao
- use pruning to reduce quantity of data scanned

#### Know how your database handles commits

- commit: change within a database, like creating, updating, deleting record, table or other db object
- transactions: a notion of committing several operations simulaneously in a way that maintains a consistent state
  - the purpose here is to keep a consistent state of a database both:
    - while its active
    - in event of failure
  - without transactions, users would get potentially conflicting information when querying a database

Examples:

- postgres
  - requires row locking
    - blocks reads and writes to certain rows
    - degrades performance in various ways
    - not optimized for large scans or massive amounts of data appropriate for large scale analytics applications
- bigquery
  - utilizes a point in time full table commit model
    - when query is issued, read from latest committed snapshot of table
    - whether query runs for one second or two hours, only reads from that snapshot
    - that table, however, is not locked - it can accept write operations
    - but, only allows one write operation at a time - no concurrency whatsoever
- mongodb
  - a `variable-consistency database`
  - celebrated for extraordinary scalability and write concurrency
  - but, notorious for issues that arise when engineers abuse it
  - e.g. sometimes it will "unceremoniously and silently discard writes" if it gets overwhelmed - suitable for applications that can stand to lose some data (like iot)

#### Vacuum dead records

- transactions incur the overhead of creating new records during certain operations
- these old records are pointers to last state of database
- however, they accumulate - remove these dead records
  - can do on per table, multi-table, all-table basis

#### Leveraging cached query results

- many olap databases cache query results

### Queries on Streaming Data

#### Basic query patterns on streams

- continuous cdc makes for an analytics database as a "fast follower" to a production database
- basically, query the analytics database and retrieve the statistical results and aggregations
  - Couldnt we accomplish the same thing simply by running our queries on the production database?
    - in theory, yes
    - in practice no
  - Production databases generally arent equipped to handle production workloads AND run analytics scans

#### Windows, triggers, emitted statistics, and late-arriving data

Windows are small batches that are processed based on dynamic triggers

- session window: groups events that occur close together, and filters out periods of inactivity when no events occur
  - e.g. a "user sesion" is any time interval with no inactivity gap of five min or more
- fixed-time windows: fixed time periods on fixed schedule, all data that has occured since previous window closed is processed
  - e.g. every 20 sec a window is closed and processed
- sliding windows:
  - e.g. generate a new 60 second window every 30 seconds
- watermarks
  - data is sometimes ingested out of the order from which itoriginated
  - a watermark is a threshold used by a window to determine whether data in a window is within the established time interval, or late

#### Combining Streams with other data

- Conventional table joins
- Enrichment
  - join a stream to other data
  - typically, done to provide enhanced data into another stream
- stream-to-stream joining

## Data Modeling

Data modeling involves deliberately choosing a coherent structure for data and is a critical step to make data useful for the business

Lack of rigorous data modeling created data swamps, along with redundant, mismatched, or simply wrong data

### What Is a Data Model?

a `data model` represents the way data relates to the real world

- reflects how data must be structured and standardized to best reflect an orgs:
  - processes
  - definitions
  - workflows
  - logic
- a good data model captures how communication and work naturally flow within the org
- a poor (or nonexistant) data model is haphazard, confusing, and incoherent

When modeling data, critical to focus on translating the model to business outcomes

- `customer` might mean different things to different departments
  - carefully defining and modeling customer data can have a massive impact on downstream reports

### Conceptual, Logical, Physical Data Models

When modeling data, the idea is to move from abstract modeling concepts to concrete implementation

- Conceptual
  - contains business logic and rules
  - describes systems data (schemas, tables, fields)
  - often helpful to visualize in an entity relationship diagram
- Logical
  - details how conceptual model will actually get implemented
  - add information on types of customer ids, names, custom addresses etc
  - map out primary and foreign keys
- Physical
  - defines how the logical model will be implemented in a database system
  - note specific databases, schemas, talbes

Consider the `grain` of the data - which is the resolution at which data is stored and queried. Typically at the level of a primary key in a table, accompanied by a timestamp

### Normalization

Enforces strict control over the relationships of tables and columns within a database

The goal of normalization is to remove the redundancy of data within a database, and ensure referential integrity

Main objectives of normalization:

- to free the collection of relations from undesirable insertion, update, and deletion dependencies
- to reduce the need for restructuring the collection of relations, as new types of data are introduced, and thus increase the lifespan of application programs
- to make the relational model more informative to users
- to make the collection of relations neutral to the query statistics, where these statistics are liable to change as time goes by

Normal forms:

- Denormalized
  - no normalization
  - nested and redundant data is allowed
- First normal form (1NF)
  - each column is unique and has a single value
  - the table has a unique primary key
- Second normal form (2NF)
  - the requirement of 1NF
  - partial dependencies are removed
- Third normal form (3NF)
  - the requirement of 2NF
  - each table contains only relevant fields related to its primary key
  - has no transitive dependencies

Terms:

- Unique primary key
  - single field or set of multiple fields that uniquely determines rows in the table
- Partial dependency
  - occurs when a subset of fields in a composite key can be used to determine a nonkey column of the table
- Transitive dependency
  - occurs when a nonkey field depends on another nonkey field

### Techniiques for Modeling Batch Analytical Data

In some cases, these can be combined

#### Inmon

data warehouse definition:

"A data warehouse is a subject-oriented, integrated, nonvolatile, and time-variant collection of data in support of managements decisions. The data warehouse contains granular corporate data. Data in the data warehouse is able to be used for many different purposes, including sitting and waiting for future requirements which are unknown today"

- subject-oriented
  - The data warehouse focuses on a specfuc subject area, such as sales or marketing
- integrated
  - data from disparate sources is consolidated and normalized
- nonvolatile
  - data remains unchanged after data is stored in a data warehouse
- time-variant
  - varying time ranges can be queried

Integration is critical for data warehouses. Once data resides in the data warehouse it has a single physical corporate image

Data warehouses are highly normalized

#### Kimball

Opposite of Inmon

- basically, bottom up
- model and serve department or business analytics in the data warehouse itself
- effectively makes the data mart the data warehouse itself

Data is modeled with two general types of tables:

- facts: table of numbers, events, etc. immutable - typically very tall
- dimensions: qualitative data referencing a fact
  - occur around a single fact table in a relationship called a `star schema`

Slowly Changing Dimension (SCD) - necessary to track changes in dimensions:

- type 1:
  - overwrite existing dimensino records
  - simple, and means no access to deleted historical dimension record
- type 2:
  - keep full history of dimension records
  - when record changes, that specific record is flagged as changed, and new dimension record is created
- type 3:
  - similar to type 2
  - instead of creating a new row, create a new field

Results in fewer joins which speeds up query performance

Arguably easier for business users to understand and use

### Data Vault

Separates the structural aspects of a source systems data from its attributes

Instead of representing busines slogic in facts, dimensions, or highly normalized tables, a data vault simply loads data from source systems directly into a handful of purpose-built tables in an insert-only manner

Goal of methodology is to keep the data as closely aligned to the business as possible, even while the businesses data evolves

Consist of 3 main types of tables:

- hub: store business keys
- link: maintains relationships among business keys
- satellite: represents a business keys attributes and context

#### Hubs

Queries often involve searching by a business key, like cutomer id or order id

A hub is the central entity of a data vault that retains a record of all unique business keys loaded into the data vault

These always contain the following standard fields:

- Hash key
  - primary key used to join data between systems
- Load date
  - the date the data was loaded into the hub
- Record source
  - the source from which the unique record was obtained
- Business key
  - the key used to identify a unique record

When designing a hub, identifying the business key is critical. Ask "what is the identifiable business element" aka "how do users commonly look for data"

#### Links

Tracks the relationships of business keys betweenhubs (deally at the lowest possible grain)

#### Satellites

Satellites are descriptive attributes that give meaning and context to hubs

- can connect to either hubs or links
- only required fields in a satellite are a primary key consisting of the business key of the parent hub and a load date

### Wide Denormalized Tables

lol

Criticisms:

- as you blend data you lose the business logic in your analytics
- another downside is theperformance of updates to things like an element in an array

### Modeling Streaming Data

Anticipate changes in source data and keep a flexible schema

- means no rigid model in the analytical database
- instead, assume the source systems are providing the correct data with the right business definition and logic

## Transformations

The net result of transforming data si the ability to unify and integrate data. Once data is transformed, the data can be viewed as a single entity. But without transforming data, you cannot have a unified view of data across the organization

A `query` retrieves the data from various sources based on filtering and join logic

A `transformation` persists the results for consumption by additional transformations or queries (and can be stored ephemerally or permanently)

Transformations rely on orchestration (which is a benefit)

### Batch Transformations

- Broadcast join
  - generally asymmetric, with one large table distributed across nodes, and one small table that can easily fit on a single node
  - the query engine "broadcasts" the small table to all nodes, where it gets joined in on the shard
- Shuffle hash join
  - if neither table is small enough to fit on single node, use a shuffle hash join
  - basically shard both tables and do many to many join

#### ETL, ELT, and data pipelines

#### SQL and code-based transformation tools

When determining whether to use native spark or pyspark code instead of spark sql or another sql engine:

- How difficult is it to code the transform in sql?
- How readable and maintainable will the resulting sql code be?
- Should some of the transformation code be pushed into a custom library for future reuse across the organization?

Notes for coding in native spark:

- filter early and often
- rely heavily on the core spark api and learn to understand the spark native way of doing things
  - try to rely on well-maintained public libraries if the native spark api doesnt support your use case
  - good spark code is substantially declarative
- be careful with udfs
- consider intermixing sql
