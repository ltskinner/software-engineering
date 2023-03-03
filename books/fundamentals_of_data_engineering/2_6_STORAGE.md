# Chapter 6. Storage

## Raw Ingredients of Data Storage

- HDD
  - disk transfer speed (read and write rate)
  - find speed, seek time
- SSD
- RAM
  - attached to cpu and mapped into cpu address space
- Networking and CPU
- Serialization
  - Apache Parquet
  - Apache Hudi
  - Apache Arrow
- Compression
- Caching

## Data Storage Systems

### Single Machine vs Distributed Storage

Distributed good for `redunancy` and `scalability`

#### Eventual vs Strong Consistency

Takes time to replicate changes across nodes

BASE is basis of eventual consistency:

- Basically Available
  - Consistency is not guaranteed, but database reads and writes are made on a best-effort basis, meaning consistent data is available most of the time
- Soft-state
  - The state of the transaction is fuzzy, and its uncertain whether the transaction is committed or uncommitted
- Eventual consistency
  - At some point, reading data will return consistent values

Consistency is the price you pay for horizontal scaling

Use strong consistency when you can tolerate higher query latency, and require correct data every time you read from the database

Many databases have configurations for how strong of consistency - selecting them is both an organizational (decision) and technical problem

### File Storage

Files can be modified in place, objects cannot

### Blocks

`block` - the smallest addressable unit of data supported by a disk

- the type of raw storage provided by SSDs and magnetic disk
- allow for abstract control of storage size, scalability, and data durability beyond that offered by raw disks

Think elastic block storage

### Object Stores

object stores are key-value stores for immutable data objects

object stores can house any binary data with no constraints on type or structure, and frequently play a role in ML pipelines for raw text, imnages, video and audio

not a bad idea to write metadata from the object insert to an actual database (strongly consistent). with this, you can verify that the object youre reading matches latest metadata in consistent db

## Data Engineering Storage Abstractions

Considerations:

- Purpose and use case
  - Must first identify the purpose of storing the data - what is it used for?
- Update patterns
  - Is the abstraction optimized for bulk updates, streaming inserts, or upsets?
- Cost
  - What are the direct and indirect financial costs?
  - The time to value?
  - The opportunity costs?
- Separate storage and compute
  - There is a trend toward separating storage and compute

### The Data Warehouse

- Standard OLAP data architecture

### The Data Lake

### The Data Lakehouse

- combines aspects of data warehouse and data lake
- intends to create an engineering experience similar to a data warehouse
  - robust table and schema support
  - managing incremental updates and deletes
  - support history and rollback

### Data Platforms

- vendors creating ecosystems of interoperable tools with tight integrations to the core data storage layer

### Stream-to-Batch Storage Architecture

## Big Ideas and Trends in Storage

### Data Catalog

- centralized metadata store for all data across an organization
  - integrate data lineage
  - present data relationships
  - allow user to edit data descriptions

Some things:

- Catalog application and integration
  - data applications are designed to integrate with catalog apis to handle their metadata and updates directly
- Automated scanning
  - cataloguing systems typically need to rely on an automated scanning layer that collects metadata from various systems
  - can collect existing metadata and use scanning tools to infer metadata
- Data Portal and social layer
  - human interface
  - wiki
- Data Catalog use cases
  - easy to access metadata
  - search for data, discoverability

### Data Sharing

Allows organizations and individuals to share specific data and carefully defined permissions with specific entities

### Schema

Just document this lol

### Separation of Compute from Storage

- data is stored as objects
- compute is spooled up to read and  process it

Considerations:

- Colocation of compute and storage
  - low latency disk reads, high bandwidth
- Separation of compute and storage
  - "ephemerable" - lasting for a very short time
  - scalable
  - durability and availability

Hybrid example:

- stand up hdfs on ssd
- pull from s3
- save data from intermediate processing steps on local hdfs
- write results back to s3
- other consumers read from s3

Zero Copy Cloning - a shallow copy

### Data Storage Lifycycle and Data Retention

| feature | hot | warm | cold |
| - | - | - | - |
| access | very frequent | infrequent | infrequent |
| storage cost | high | medium | cheap |
| retrieval cost | cheap | medium | high |

Data retention thoughts:

- value (of the data)
- time (expire data after some point)
- compliance
- cost (there should be an ROI for this data)
