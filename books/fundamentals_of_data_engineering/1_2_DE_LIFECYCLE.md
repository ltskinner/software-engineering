# Chapter 2. The Data Engineering Lifecycle

Basically, the next evolution of Data Engineers is to become Data Lifecycle Engineers (as tools become more abstracted)

## What is the Data Engineering Lifecycle

### Five Stages

- Generation
- Storage
- Ingestion
- Transformation
- Serving Data

Not always a neat, continuous flow

Various stages of the lifecycle may

- repeat themselves
- occur out of order
- overlap
- weave together in weird ways

### The Data Lifecycle vs Data Engineering Lifecycle

- data engineering lifecycle is subset of the whole data lifecycle

### Generation: Source Systems

`source system` - the origin of the data used in the data engineering lifecycle

- iot device
- application message queue
- transactional database

Data engineers consume from, but likely dont have control over

Data engineer needs to understand:

- way source systems work
- way they generate data
- frequency of the data
- velocity of the data
- variety of the data

Should also keep open comms line with system owners about changes that may break pipelines or analytics

#### Evaluating source systems: Key engineering considerations

- What are the essential characteristics of the data source? Is it an application? A swarm of IoT devices?
- How is data persisted in the source system? Is data persisted long term, or is it temporary and quickly deleted?
- At what rate is data generated? How many events per second? How many gigabytes per hour?
- What level of consistency can data engineers expect from the output data? If youre running data-quality checks against the output data, how often do data inconsistencies occur - nulls where they arent expected, lousy formatting, etc.?
- How often do errors occur?
- Will the data contain duplicates?
- Will some data values arrive late, possibly much later than other messages produced simultaneously?
- What is the schema of the ingested data? Will data engineers need to join across several tables or even several systems to get a complete picture of the data?
- If schema changes (say, a new column is added), how is this dealt with and communicated to downstream stakeholders?
- How frequently should data be pulled from the source system?
- For stateful systems (e.g., a database tracking customer account information), is data provided as periodic snapshots or update eventds from change data capture (CDC)? Whats the logic for how changes are performed, and how are these tracked in the source database?
- Who/what is the data provider that will transmit the data for downstream consumption?
- Will reading from a data source impact its performance?
- Does the source system have upstream data dependencies? What are the characteristics of these upstream systems?
- Are data-quality checks in place to check for late or missing data?

The data engineer should know the unique volume and cadence of data generation from each source, as well as relevant quirks or nuances, and limitations

#### Handling Schemas

Two options: `schemaless` and `fixed schema`

- `schemaless`
  - Does **NOT** mean absence of schema
  - Means: application defines the schema as data is written (whether to message queue, flat file, blob, document db)
- `fixed schema`
  - relational database paradigm
  - applications must conform to the schema enforced by the db

Schema evolution is ok, its ok for them to change over time

## Storage

Choosing a storage solution is key to success in the rest of the data lifecycle

- Data architects in the could often leverage *several* storage solutions
- Few data storage solutions function purely as storage (many can perform transformation queries)
- Storage frequently touches on other stages (like ingestion, transformation, serving)

Streaming frameworks like `Kafka` and `Pulsar` can function simultaneously as ingestion, storage, and query systems for messages

### Evaluating Storage Systems: Key Engineering Considerations

For a data warehouse, data lakehouse, database, or object store:

- Is this storage solution compatible with the architectures required write and read speeds?
- Will storage create a bottleneck for downstream processes?
- Do you understand how this storage technology works? Are you utilizing the storage system optimally or committing unnatural acts? For instance, are you applying a high rate of random access updates in an object storage system? (As an example of antipattern with performance overhead)
- Will this storage system handle anticipated future scale? Consider all capacity limits on the storage system: total available storage, read operation rate, write volume, etc
- Will downstream users and processes be able to retrieve data in the required service-level agreement (SLA?)
- Are you capturing metadata about schema evolution, data flows, data lineage, ..., etc? Metadata is an investment in the future - enhancing discoverability and institutional knowledge
- Is this a pure storage solution (object storage) or does it support complex query patterns (i.e., a cloud data warehouse)?
- Is the storage system schema-agnostic (object storage)? Flexible schema (Cassandra)? Enforced schema (cloud data warehouse)?
- How are you tracking master data, golden records data quality, and data lineage for data governance?
- How are you handling regulatory compliance and data sovereignty?

### Understanding Data Access Frequency

"Retrieval patterns"

Data access frequency will determine the `temperature` of your data

- `hot data` - retrieved many times per day, per second, etc - should be stored in fast retrieval
- `lukewarm data` - accessed every month or week
- `cold data` - often retained for compliance purposes or in case of failure of other systems

### Selecting a Storage System

Depends on:

- Use cases
- Data volumes
- Frequency of ingestion
- Format
- Size of data being ingested

## Ingestion

Source systems and ingestion represent the most difficult bottlenecks of the data engineering lifecycle

### Key Engineering Considerations for Ingestion

- What are the use cases for the data im ingesting? Can I reuse this data rather than create multiple versions of the same dataset?
- Are the systems generating and ingesting this data reliably, and is the data avilable when I need it?
- What is the data destination after ingestion?
- How frequently will I need to access the data?
- In what volume will the data typically arrive?
- What format is the data in? Can my downstream storage and transformation systes handle this format?
- Is the source data in good shape for immediate downstream use? If so, for how long, and what might cause it to become unusable?
- If the data is from a streaming source, dows it need to be transformed before reaching its destination? Would an in-flight transformation be appropriate, where the data is transformed within the stream itself?

### Batch versus Streaming

- virtually all data we deal with is inherently `streaming`
  - It is produced and updated continually at it source
- `batch ingestion` is a specialized and convenient way of processing this stream in large chunks - like doing all the data from one day at once

Streaming allows us to provide data to downstream services in real-time or near real-time - aka data is available to downstream systems a short time after it is produced. Note, latency required to qualify as real-time varies by domain and requirements

Batch processing is still popular, "particularly in analytics and ML"

### Key Considerations for `batch` vs `stream` ingestion

- If I ingest the data in real time, can downstream storage systems handle the rate of data flow?
- Do I need millisecond real-time data ingestion? Or would a micro-batch approach work, accumulating and ingesting data on a minutely interval?
- What are my use cases for streaming ingestion? What specific benefits do I realize by implementing streaming? If I get data in real time, what actions can I take on that data that would be an improvement upon batch?
- Will my streaming-first approach cost more in terms of time, money, maintenance, downtime, and oppotunity cost than simply doing batch?
- Are my streaming pipeline and systems reliable and redundant if infrastructure fails?
- What tools are most appropriate for the use case? Should I use a managed service, or stand up my own instance? Who will manage the self admined? What are the costs and trade-offs?
- If im deploying an ML model, what benefits do I have with online predictions and possibly continuous training?
- Am I getting data from a live production instance? If so, whats the impact of my ingestion process on this source system?

Adopt true real-time streaming only after identifying a business use case that justifies the trade-offs against using batch

### Push versus Pull

- `push` model - source system writes data out to a target
- `pull` model - data is retrieved from the source system

In context of Extract, Transform, Load:

- Extract clarifies we are dealing with a `pull` ingestion model
  - Ingestion system queries a current source table snapshot on a fixed schedule

Consider Continuous CDC:

- A common method triggers a message every time a row is changed in the source database
  - This message is `pushed` to a queue, where the ingestion system picks it up
- Another common method is to record every commit to binary logs
  - The database `pushes` to its logs
- Some version of batch CDC use `pull`

## Transformation

Changing data from its original form into something useful for downstream use cases

Without proper transformations, data will:

- sit inert
- not be in a useful form for reports, analysis, ML

The transformation stage is typically where data begins to create value for downstream user consumption

### Key Considerations for the Transformation Phase

- What is the cost and ROI of the transformation? What is the associated business value?
- Is the transformation as simple and self isolated as possible?
- What business rules to the transformations support?

Can perform the transforms in batch or while streaming in flight

Things like:

- basic transformations
- correct data type mapping
- putting records into standard formats
- removing bad records
- general data preparation
- data wrangling
- cleaning
- etc

All fall into bucket of transformations

Also, be sure to have standard approach for implementing business logic across transformations

#### Data Featurization

Key for ML

- Extract and enhance features useful for training ML models
- Can be a dark art, combines:
  - Domain expertise
  - With extensive experience in data science

## Serving Data

Now its time to get value from the data

Data has value when its used for practical purposes. Data that is not consumed or queried is simply inert

Inert data and data vanity projects are a major risk for companies

### Analytics

Types of analytics:

- BI, ad hoc
- Operational
- Embdded

#### BI Analytics

"logic-on-read" is becoming popular - here, data is stored in a clean but fairly raw form, then business logic is used to query the data

Evolution of analytics is going from ad hoc analysis to self service analytics, where everyone can access data without needing IT to intervene. As good as it sounds, very difficult to successfully execute on lol

### Operational Analytics

Focuses on the fine-grained details of operations. Want actionable insight that can be used immediately

Things like:

- live view of inventory
- real time dashboard of website or application health

Data is consumed in real time

### Embedded Analytics

Customer facing analytics (as opposed to internally facing BI)

Now, because customer facing, report request rates increase, and burden on system increases as well. Access control becomes an issue as well

Basically data security and ensuring there are no data leaks or spills (like one customer seeing another customers data)

### Machine Learning

Setting up domains of responsibility and relevant reporting structures are critical organizational decisions

#### Feature Stores

- combine data engineering and ML engineering
- maintain feature history and versions
- support feature sharing among teams
- provide basic operational and orchestration capabilities

Some considerations specific to serving for ML:

- Is the data of sufficient quality to performa reliable feature engineering? Quality requirements and assessments are developed in close collaboration with teams consuming the data
- Is the data discoverable? Can data scientists and ML engineers easily find valuable data?
- Where are the technical and organizational boundaries between data engineering an ML engineering? This organizational question has significant architectural implications
- Does the dataset properly represent ground truth? Is it unfairly biased?

Definitely worthwhile to invest into data foundations prior to investing in ML specifically

- setting up best systems and architecture across data engineering and ML lifecyycle
- develop competence in analytics before moving into ML

### Reverse ETL

Takes processed data from the output side of the data engineering lifecycle, and feeds it back into the source systems

- benefitial and often necessary
- allows us to take analytics, scored models, etc, and feed them back into production systems or saas platforms

Some tools: `Hightouch` and `Census`

## Major Undercurrents Across the Data Engineering Lifecycle

Rapidly maturing, specifically with better abstractions and simplifications, and is moving it up the value chain

### High Level Undercurrents

- Security
  - Access control to:
    - Data
    - Systems
- Data management
  - Data governance
    - Discoverability
    - Definitions
    - Accountability
  - Data modeling
  - Data integrity
- DataOps
  - Data governance
  - Observability and monitoring
  - Incident reporting
- Data architecture
  - Analyze tradeoffs
  - Design for agility
  - Add value to the business
- Orchestration
  - Coordinate workflows
  - Schedule jobs
  - Manage tasks
- Software engineering
  - Programming and coding skills
  - Software design patterns
  - Testing and debugging

### Security

- must be top of mind
- access control, with principle of least priviledge
  - giving user or system access to only the essential data and resources required to perform an intended function
- there is a cultural aspect to this as well
- timing is key too
  - only giving people access for the duration necessary to perform their work
- data needs to be protected from unwanted visibility, in flight and at rest
  - encryption
  - tokenization
  - data maskin
  - obfuscation
  - simple, robus access controls

### Data Management

"Data management is the development, execution, and supervision of plans, policies, programs and practices that deliver, control, protect, and enhance the value of data and information assets throughout their lifecycle"

- data engineers need a broader perspective of datas utility across the organization
  - from the source systems to the C-suite, and everywhere in between

### Key facets

#### Data governance, including discoverability and accountability

- be intentional about this
- unintentional actions result in unintentional consequences
- a common symptom of poor governance is people trying to answer questions sifting through tables and guessing which fields are relevant

##### `discoverability`

- data must be available and discoverable
- end users should have quick and reliable means to access the data they need to do their jobs
- metadata management is key for this
  - two categories: autogenerated and human generated
  - often, metadata collection is manual and error prone
  - data catalogues, data-lineage tracking systems, and dedicated metadata management tools are growing in popularity though
- data has a social element - each org accumulates social capital and knowledge around processes, datasets, and pipelines
  - documentation and `internal wikis` are key foundations for this

###### Main categories of metadata

- `Business` metadata
  - way data is used in the business
  - definitions
  - rules
  - logic
  - how data is used
  - data owners
  - answer nontechnical questions about who, what, where, how
- `Technical` metadata
  - data model and schema
    - structure of data stored in system (databases, data warehouse, data lake, filesystem)
  - data lineage
    - origin of changes
    - data dependencies
    - all over time - provides an audit trail
  - field mappings
  - pipeline workflows
    - workflow schedule
    - system and data dependencies
    - configurations
    - connection details
    - etc
- `Operational` metadata
  - describes operational results of various systems
  - stats about processes
  - job ids
  - application runtime logs
  - data used in a process
  - error logs
- `Reference` metadata
  - data used to classify other data
  - referred to as `lookup data`
  - internal codes, geo codes, units of measurement, internal calendars etc

##### Misc attrebutes

- Data Accountability
  - assigning a person to govern a portion of data (note, dont have to be data engineers)
  - they do a lot of coordination activity
- Data Quality
  - "can I trust this data"
  - assessed on three main characteristics:
    - `Accuracy`
      - Is the collected data factually correct? Are there duplicate values? Are the numeric values accurate?
    - `Completeness`
      - Are the records complete?
      - Do all required fields contain valid values?
    - `Timeliness`
      - Are records available in a timely fashion?
- Master Data Management
  - is data about business entities
    - employees
    - customers
    - products
    - locations
  - practice of building consistent entity definitions known as `golden records`
    - typically, these are harmonizing records that can be accessed from a single standard point

#### Data modeling and design

lmao: "murmurs of the write once, read never `WORN` access model, or reference to a `data swamp`

Basically, there is no shortage of new formats and ways to capture and encode data. Modeling the data is the grease that keeps everything working. **Document data formats**.

#### Data lineage

As data moves through its lifecycle, how do you know what system affected the data or what the data is composed of as it gets passed around and transformed?

Make your data auditable and traceable

Check out: Data Observability Driven Development `DODD`

#### Storage and operations

#### Data integration and interoperability

The process of integrating data across tools and processes

Lots of this is done through general purpose APIs, rather than custom db connections

Example:

- data pipeline pulls data from Salesforce API
- Store in S3
- call snowflake api to load into table
- call api again to run a query
- export results to S3
- spark consumes results

Python is excellent for writing glue code at the abstract system level instead of touching data directly

#### Data lifecycle management

Advent of data lakes encouraged organizations to ignore data archiving and destruction

Data engineers must kniw what consumer data they retain, and must have procedures to destroy data in response to requests and compliance requirements

#### Data systems for advanced analytics and ML

#### Ethics and privacy

### DataOps

DataOps maps the best practices of agile, devops, and statistical process control `SPC`

DataOps is a collection of technical practices, workflows, cultural norms, and architectural patterns that enable:

- Rapid innovation and experimentation delivering new insights to customers with increasing velocity
- Extremely high data quality and very low error rates
- Collaboration across complex arrays of people, technology, and environments
- Clear measurement, monitoring, and transperency of results

Very much a set of cultural habits:

- lots of communication and collaboration
- breaking down silos
- continuously learning from successes and mistakes
- rapid iteration

Start first with:

- Observability and Monitoring

With the goal to get as much visibility into the system performance as possible, then

- Automation
- Incident response

#### Automation

- enables reliability and consistency in the dataops processes
- facilitates quickly deploying new product features
- continuous workflow improvements

Orchustration frameworks: `Airflow` and `Dagster`

Embrace goal oriented change - per DataOps Manifesto

#### Observability and Monitoring

"Data is a silent killer" - bad data tends to linger, and continues to be trusted and used

Critical for getting ahead of problems in the data engineering lifecycle:

- observability
- monitoring
- logging
- alerting
- tracing

SPC is critical to this

DODD is much like test-driven development - "the purpose of DODD is to give everyone involved in the data chain visibility into the data and data applications so that everyone involved in the data chain ahs the ability to identify changes to the data or data applications at every step - from ingestion to transformation to analysis - to help troubpleshoot or prevent data issues. DODD focuses on making data observability a first-class consideration in the data engineering lifecycle"

#### Incident Response

Incident response is about using the automation and observability capabilities from above to rapidly identify root causes of an incident and resolve it as reliably and quickly as possible

"Everything breaks all the time"

Data engineers should proactively find issues before the businesses report them.

Trust takes a long time to build, and can be lost in minutes

Just because DataOps is not perfect doesnt mean it shouldnt be a priority. When it sorts itself out, organizations that are familliar with the paradigms will be in a much better position to adopt and integrate new tools

### Data Architecture

Have to understand needs of the business and gather requirements for use cases

Then, translate those use cases into designs for ways to capture and serve data, balancing cost and operational simplicity

Must know tradeoffs with design patterns, technologies, and tools in:

- source systems
- ingestion
- storage
- transformation
- serving data

### Orchestration

The process of coordinating many jobs to run as quickly and efficiently as possible on a scheduled cadence

NOT just schedulers

`Airflow` is pretty dank, but there are alternatives like `Prefect`, `Dagster`, `Argo`, `Pulsar`, `Metaflow`

### Software Engineering

#### Core Data Processing Code

#### Development of Open Source Frameworks

Before data engineers begine engineering new internal tools, be sure to check publically available ones

Internal tools have a Total Cost of Ownership cost, including opportunity cost of implementing a tool

#### Streaming

- ability to write effective *windowing* methods is critical
  - *windowing* allows real-time systems to calculate valuable metrics like `trailing statistics`

#### Infrastructure as Code

#### Pipelines as Code
