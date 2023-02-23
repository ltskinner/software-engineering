# Chapter 7.Ingestion

## What is Data Ingestion?

`Data ingestion` is the process of moving data from one place to another - from point a to b

`Data integration` combines disparate sources into a new dataset

`Data ingestion` is also different from `internal ingestion` within a system

### Data Pipelines

Begin in source systems, but ingestion is the stage where data engineers begin actually designing the pipeline

"A data pipeline is the combination of architecture, systems, and processes that move data through the stages of the data engineering lifecycle"

## Key Engineering Considerations for the Ingestion Phase

- Whats the use case for the data im ingesting?
- Can I reuse this data and avoid ingesting multiple versions of the same dataset?
- Where is the data going? Whats the destination?
- How often should the data be updated from the source?
- What is the expected data volume?
- What format is the data in? Can downstream storage and transformation accept this format?
- Is the source data in good shape for immediate downstream use (aka good quality)?
- What post-processing is required to serve it? What are data-quality risks?
- Does the data require in-flight processing for downstream ingestion if the data is from a streaming source?

Regardless of how often data is ingested, will need to consider these:

### Bounded vs unbounded

- unbounded data is as it exists in the real world - sporatic or continuous
- bounded is bucketing

"all data is unbounded until its bounded"

### Frequency

- ingestion processes can be batch, micro-batch, or real time
- real time, near real time, and streaming interchangeable
- streaming architectures generally coexist with batch processing

### Synchronous vs Synchronous Ingestion

- synchronous - the source, ingestion, and destination have complex dependencies and are tightly coupled
  - if proces A fails, all downstream cannot start
- asynchronous ingestion - dependencies operate at level of individual events
  - basically the paradigm is that you can run your entire pipeline in parallel, as opposed to like a "master status" like from batching

### Serialization and deserialization

### Throughput and Scalability

Design your systems to scale and shrink to match desired data throughput

Theoretically, ingestion should never be a bottleneck, but in practice it can become one

- think about edge cases of source systems, what kinds of surges or lapses could you expect to see and what would their impacts be on your system?
- use managed services to handle thruput scaling

### Reliability and Durability

- reliability - high uptime
- durability - make sure data isnt lost or corrupted
- build an appropriate level of redundancy and self-healing as a proportion of the impact and cost of losing data

### Payload

Payload - the dataset youre ingestion, which has characteristics

- kind:
  - tabular, image, video, etc
- shape:
  - tabular
  - semistructured json
  - unstructured text
  - images (width, height, rgb)
  - uncompressed audio (some noise stats)
- size:
  - number of bytes of the payload
  - use zippy stuff if things get too big
  - chunking is cool too
- schema and data types:
  - things to look for:
    - adding a new column
    - changing a column type
    - creating a new table
    - renaming a column
  - schema registries of metadata of schema history
    - applies to both relational and streaming stuff (message formats are pre-structured)
- metadata:
  - critical

### Push vs Pull vs Poll Patterns

- push:
  - source system forces itself on destination
- pull:
  - destination system requests data from source
- poll:
  - destination checks for a change, and then pulls

## Batch Ingestion Considerations

- time-interval batch ingestion
  - do on some time interval - nightly, whatever
- size-based batch ingestion
  - common for streaming
  - by size (bytes) or by number of events
- snapshot or differential extraction:
  - incremental vs full
  - incremental good for minimizing network traffic
  - full still widely used bc how simple
- file-based export and ingestion
  - like basically, things are written to files and the files are exchanged
  - advantages over direct db connections:
    - dont have to give db access (security)
    - export is run entirely on source system, giving source engineers full control over what is exported and how data is preprocessed
  - sftp, edi, scp
- etl vs elt
  - extract: getting data from source system
  - load: once extracted, can either be transformed first or after loaded
- inserts, updates, batch-size
  - batch-oriented systems often perform poorly when users attempt to perform many small-batch operations, rather than a small number of large operations
  - tools are designed to be better at one or the other, so know the characteristics
- data migration:
  - not common
  - usually MASSIVE ammounts of data
  - main hurdles are usually migrating the pipelines, not the data itself

## Message and Stream Ingestion Considerations

- schema evolution:
  - fields may be added or removed
  - value type might change
  - these usually have unintended consequences
  - be sure to version schema changes
  - use a `dead-letter queue`
  - regularly communicate with upstream stakeholders about potential changes - be proactive not reactive
- late-arriving data
  - consiously figure out how this might impact downstream systems
  - set a cutoff time for when late data will no longer be processed
- ordering and multiple delivery
  - because streaming systems are usually distributed, there can be complications
  - out of order messages, and multiple message delivery can be a problem
- replay
  - allows readers to request a range of messages from the history
- time to live
  - how long will you preserve your event record
  - key parameter is `maximum message retention time` or `ttl`
  - how long events live before they are acknowledged and ingested
  - any unacknowledged event thats not ingested before the ttl expires will disappear
  - dont want too long or too short
- message size
  - must ensure that the streaming framework can handle maximum expected message size
- error handling and dead-letter queues
  - some event arent successfully ingested
    - event sent to nonexistent topic or message queue
    - message too large
    - event has expired ttl
  - events that cannot be ingested need to be rerouted and stored in separate location called a `dead-letter queue`
    - segregates problematic events
    - erroneous messages risk other messages from being processed
    - useful for diagnosing defects
- consumer pull and push
  - pull are the default for most applications
  - push useful for specialized applications
- location
  - the closer ingestion happens to where data originates, the better bandwidth and latency

## Ways to Ingest Data

- direct database connection
- change data capture
  - process of ingesting changes from a source database system
  - batch-oriented cdc
    - if table has `updated at` field, then can query against some time in the past to see all updated rows
    - but, this doesnt capture all the changes that have happened
    - so like, if multiple changes happened, only see the most recent
  - continuous cdc
    - treat each write to the db as an event
  - cdc and database replication
    - can be used to replicate between databases - just stream the events log
  - cdc considerations:
    - incurs compute overhead
- apis
  - "the bulk of software engineering is just plumbing"
  - reserve custom connection work for apis that arent well supported by existing frameworks
    - re: dont build one unless you gotta, and the expense of maintaining is lower than dealing with an alternate solution
    - that said, apis are really nice
- message queues and event streaming platforms
- managed data connectors
  - if youre writing an ingestion connector to a database or api, ask yourself: "has this already been created?"
  - is there a service that will manage the nitty gritty details of this connection for me?
- moving data with object storage
  - object storage is the most optimal and secure way to handle file exchange
- edi
  - electronic data interchange
  - usually refers to archaic means of file exchange: email or flash drive (lmao)
- databases and file export
  - be aware of how source database systems handle file export
  - can you do exports without negatively impacting other users of the db
- practical issues with common file formats
  - more robust and expressive export formats include:
    - parquet, avro, arrow, orc, json
- data sharing
  - data providers provide datasets to third-party subscribers, either free or at cost
  - read only
  - can disappear tho

## Who Youll Work With

- Upstream stakeholders
  - teams managing data generating sources
  - bring them in so they can see how their exhause gets used by you
  - they also might have ideas for ways to get value out of their work
- Downstream stakeholders
  - communicate communicate communicate

## Undercurrents

- security
  - the act of moving data creates vulnurability
  - be consious
  - encrypt
- data management
  - schema changes
    - something something git
  - data ethics privacy and compliance
    - first ask, can we just not transfer this data (esp if its sensitive)
    - drop sensitive data before it can become an issue
    - if you must work on sensitive data, dev on unsensitive identically structured data - touchless production
    - if you have to look at the data itself, make sure thats done at the approval of more than one person - broken-glass process
    - beware of naive technological solutions to human problems
- dataops
  - reliable data pipleines are key - make sure they are monitored
  - monitor:
    - uptime
    - latency
    - data volume
  - data-quality tests
- orchestration
  - ingestion usually sits at the beginning of a large and complex data graph
- software eingineering
