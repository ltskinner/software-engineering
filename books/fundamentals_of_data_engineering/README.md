# Fundamentals of Data Engineering

"Success or failure is rarely a technology issue. Knowing how to navigate an organization, scope and gather requirements, control costs, and continuously learn are key descriminators."

## Data Engineering Lifecycle

- data generation
- storage
- ingestion
- transformation
- serving

## Part I. Foundation and Building Blocks

### [Chapter 1. Data Engineering Described](./1_1_DATA_ENGINEERING.md)

"Once a new technology rolls over you, if youre not part of the steamroller, youre part of the road"

"Business never sleeps"

"Companies dont hire engineers to simply hack code in isolation. To be worth of their title, engineers should develop a deep understanding of the problems theyre tasked with solving, the technology tools at their disposal, and the people they work with and serve"

#### Simplified Data Maturity Model

- 1. Starting with data
- 2. Scaling with data
- 3. Leading with data

### [Chapter 2. The Data Engineering Lifecycle](./1_2_DE_LIFECYCLE.md)

- Generation
- Ttorage
- Ingestion
- Transformation
- Serving

#### Underpinned by (at all stages)

- Security
- Data management
- DataOps
- Data architecture
- Orchestration
- Software engineering

Also, use DAGs to document and orchustrate

### [Chapter 3. Designing Good Data Architecture](./1_3_DESIGNING_GOOD_ARCH.md)

- 1. Choose common components wisely
- 2. Plan for failure
- 3. Archiect for scalability
- 4. Architecture is leadership
- 5. Always be architecting
- 6. Build loosely coupled systems
- 7. Make reversible decisions
- 8. Prioritize security
- 9. Embrace FinOps

#### Terms

- `MPP system` - Massively Parallel Processing
- `OLAP` - Online-Analytical Porcessing
- `CDC process` - Change Data Capture (identifies and tracks changes to data in a db)

#### On Addressing "Brownfield" Projects - aka Fixing Legacy

- Require thorough understanding of legacy architecture
  - Easy to criticize a teams previous decisions
  - Hard to dig deep, ask questions, and understand why decisinos were made
- **Remember: your job is to make reversible, high-roi decisions**
  - NOT be right

### [Chapter 4. Choosing Technologies Across the Data Engineering Lifecycyle](./1_4_CHOOSING_TECH.md)

Architecture first, technology second:

- Architecture is strategic - the what, why, and when
- Tools are tactical - the how

Considerations:

- Team size and capabilities
- Speed to market
- Interoperability
- Cost optimization and business value
- Today versus the future: immutable vs transitory technologies
- Location (cloud, on-prem, hybrid cloud, multicloud)
- Build vs buy
- Monolith vs modular
- Serverless versus servers
- Optimization, performance, and the benchmark wars
- The undercurrents of the data engineering lifecycle

## Part II. The Data Engineering Lifecycle in Depth

### [Chapter 5. Data Generation in Source Systems](./2_5_DATA_GENERATION.md)

Event driven architectures are ideal because events can both trigger work inthe application and feed near real-time analytics

Dont treat source systems as "someone elses problem" - not saying be nosy, but dont be a mouse

### [Chapter 6. Storage](./2_6_STORAGE.md)

### [Chapter 7. Ingestion](./2_7_STORAGE.md)

"the bulk of software engineering is just plumbing"

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

- Bounded vs unbounded
- Frequency
- Synchronous vs asynchronous
- Serialization and deserialization
- Throughput and scalability
- Reliability and durability
- Payload
- Push vs pull vs poll patterns

Monitor data pipelines as you would the applications they support:

- monitor
  - uptime
  - latency
  - data volume
  - various rates - things you can do statistical analysis on
- perform data quality tests as well

### [Chapter 8. Queries, Modeling, and Transformation](./2_8_TRANSFORMATION.md)

"Ingesting data without a plan is a great recipe for a data swamp"

#### Data Modeling

When modeling data, critical to focus on translating the model to business outcomes

##### Conceptual, Logical, Physical Data Models

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
