# Chapter 3. Designing Good Data Architecture

## What is Data Architecture?

Successful data engineering is built on top of rock-solid data architecture

### Enterprise Archtecture Defined

Generally has 4 sub-sections:

- Business Architecture
- Technical Architecture
- Application Architecture
- Data Architecture

Enterprise architecture is the design of systems to support change in the enterprise, achieved by flexible and reversible decisions reached through careful evaluations of trade-offs

The reversible thing is interesting. Like, not everything can be reversible (or should be for that matter), but when it comes to prototyping new technology and just seeing how it works like being able to try a system out and hit ctl+z is important

### Data Architecture Defined

Data architecture is the design of systems to support the evolving data needs of an enterprise, achieved by flexible and reversible decisions reached through a careful evaluation of trade-offs

- Operational architecture: the `what`
  - Includes functional requirements of what needs to happen with people, processes, technology
- Technical architecture: - the `how`
  - Outlines how data is ingested, stored, transformed, and served

### "Good" Data Architecture

Good data architecture:

- serve business requirements
- common, reusable building blocks
- flexible and easily maintainable
- evolves with changes in the business environment

Bad data architcture:

- authoritarian
- one-size-fits-all decisions
- tightly coupled, rigid, overly centralized, uses wrong tools

## Principles of Good Data Architecture

### AWS Well-Architected Framework

- Operational excellence
- Security
- Reliability
- Performance efficiency
- Cost Optimization
- Sustainability

### Googles Five Principles for Cloud-Native Architecture

- Design for automation
- Be smart with state
- Favor managed services
- Practice defense in depth
- Always be architecting

### Author Suggestions

- 1. Choose common components wisely
- 2. Plan for failure
- 3. Archiect for scalability
- 4. Architecture is leadership
- 5. Always be architecting
- 6. Build loosely coupled systems
- 7. Make reversible decisions
- 8. Prioritize security
- 9. Embrace FinOps

#### 1. Choose common components wisely

Things like:

- object storage
- version control
- observability and monitoring
- orchustration

Should be accessible to everyone with an appropriate use case

#### 2. Plan for failure

Evaluating failure scenarios by:

- Availability
- Reliability
- Mean Recovery time, recovery time objective (max acceptible service outage)
- Recovery point objective (acceptable state after a recovery)

#### 3. Archiect for scalability

- should be able to scale up to serve needs
- but also scale down to conserve costs
  - elastic system
  - some also scale to zero

#### 4. Architecture is leadership

- the best leaders empower others, or something like that
- if you have highly competent people around you, then you wont become a bottleneck

#### 5. Always be architecting

- data architects donw serve their role to maintain an existing state
  - they are always designing new (exciting things) in response to changes in business and technology
- responsibilities:
  - develop baseline architecture (current state)
  - develop target architecture
  - map out sequencing plan (including prioritization and order or changes)

#### 6. Build loosely coupled systems

"When the architecture of the system is designed to enable teams to test, deploy, and change systems without dependencies on other teams, teams require little communication to get work done. Both the architecture and the teams are loosely coupled"

Bezos API Mandat (actually pretty sweet):

- 1. All teams will expose their data and functionality through service interfaces
- 2. Teams must communicate with each other through these interfaces
- 3. There will be no other form of interprocess communication allowed: no direct linking, no direct reads of another teams data store, no shared memory model, no back doors whatsoever. The only communication allowed is via service interface calls over the network
- 4. It doesnt matter what technology they use. HTTP, Corba, Pubsub, custom protocols - doesnt matter
- 5. All service interfaces, without exception, must be designed from the ground up to be externalizable. That is to say, the team must plan and design to be able to expose the interface to developers in the outside world

#### 7. Make reversible decisions

Reversible decisinos tend to simplify architecture and keep it agile

#### 8. Prioritize security

Must assume responsibility for the security of the systems built and maintained

##### Hardened-perimeter and Zero-Trust security models

Basically, there is no such thing as a "safe zone" and an "other" zone, each system needs to take care of itself

##### Shared Responsibility Model

- security of the cloud
  - aws secures the cloud
- security in the cloud
  - users secure things they use in the cloud

##### Data Engineers as Security Engineers

Failure to assume the responsibility will have dire consequences

#### 9. Embrace FinOps

This is a pretty cancerous FlyingMonkeyOps term but basically use data to make good decisions on where you spend money

## Major Architecture Concepts

Main goal: to take data and transform it into something useful for downstream consumption

### Domains and Services

- domain: real world subject area for which you are architecting
- service: set of functinoality whose goal is to accomplish a task
- domains can contain multiple services
  - two domains can share a common service

### Distributed Systems, Scalability, and Designing for Failure

- Plan for failure
- Architect for scalability

Attributes:

- Acalability
  - Allows us to increase the capacity of a system to improve performance and handle the demand
- Elasticity
  - Ability of a scalable system to scale dynamically - scaling up and down
- Availability
  - Percentage of time a service is in an operable state
- Reliability
  - Systems probability of meeting defined standards in performing its intended function during a specified interval

### Tight Versus Loose Coupling: Tiers, Monoliths, and Microservices

#### Architecture tiers

- architectures have layers, and appropriate decoupling of them is cruicial

##### Single Tier

The database and application are tightly coupled, residing both on the same server. Here, if the db, the app, or the server fail, the whole architecture fails

Note, these are fine for prototyping and development but def not for production

##### Multitier

Several Layers:

- data
- application
- business logic
- presentation
- etc

Common is the `Three-Tier Architecture`

- Presentation Layer
- Application/Logic Layer
- Data Layer

##### Monoliths

Monliths include as much as possible under one roof - single codebase running on single machine to provide both the application logic and user interface

Coupling:

- Technical coupling
- Domain coupling

Big problem is maintaining becomes a game of whack-a-mole - one component is improved, tho often at the expense of unknown consequences with other areas of the monolith

##### Microservices

- separate, decentralized, loosely coupled services

##### Considerations for Data Architecture

- recognize when its reasonable to totally decouple, and various real world limitations
- incorporate reversible technology
- its ok to start with monoliths, as long as everyone is prepared to break it into smaller pieces eventually - dont get too comfortable

### User Access: Single Versus Multitenant

### Event-Driven Architecture

`events` will typically change the `state` of something

Three areas of event-driven workflow:

- event production
- routing
- consumption

An event must be produced and routed to something that consumes it without tightly coupled dependencies among the producer, event router, and consumer

### Brownfield vs Greenfield Projects

Before starting architecture, need to know whether starting with a clean slate, or redesigning an existing architecture

#### Brownfield

- refactoring and reorganizing an existing architecture
- require thorough understanding of legacy architecture
  - easy to criticize a teams previous decisions
  - hard to dig deep, ask questions, and understand why decisinos were made
- Remember: your job is to make reversible, high-roi decisions
  - NOT be right

lmao: "Legacy is a condescending way to describe something that makes money"

Several ways to depreciate:

- can dive in and just do a complete overhaul, but a ton of work, risky, and big-bang like
- or, can "strangle" the old architecture. Get new services online that replace old ones. Eventually, old will cease to exist

#### Greenfield Projects

Here, get to start from scratch, no old shit to contend with

- Be careful to not get carried away with trying out new shit
  - Watch out for shiny blue objects lol
- Watch out for `resume-driven development`
  - that is, stacking up impressive new technologies without prioritizing the projects ultimate goals

## Examples and Types of Data Architecture

### Data Warehouse

- Central hub used for reporting and analysis
- Highly formatted and structured

#### Organizational Data Warehouse Architecture

- Separates online analytical processing (OLAP) from production databases (online transaction processing)
  - Moving data into separate physical systems directs load away from production systems and improves analytical performance
- Centralizes and Organizes data

#### Technical Data Warehouse Architecture

#### ETL and ELT

- Basically, sometimes doing transformation last (aka transofrm on read) makes sense because of compute available in warehouse

#### The Cloud Data Warehouse

#### Data Marts

Refined suybset of warehouse designed to serve `analytics and reporting`, with a focus on serving a single organization and their specific needs

- Basically, they sit after the data warehouse as a subset

### Data Lake

Lets dump all data, structured and unstructured, into one place :)

"The first generaionm data lake made solid contributions but generally failed to deliver on its promise"

"The data lake became a dumping ground: terms such as *data swamp, datk data, and WORN* were coined as projects failed"

Ya so if you got discipline and ways to discover and know whats in the datalake like its fine

#### Convergence, Next Generation Data Lakes, and the Data Platform

Databricks introduced the `data lakehouse`

- incorporates controls, data management, and data structure like you would find in a data warehouse
- support ACID transactions

### Modern Data Stack

Trendy analytics architecture that highlights the type of abstraction that will become more commonplace in coming years

- Main objective is to use cloud-based, plug-and-play, easy to use, off the shelf components

Key outcomes:

- self service analytics and pipelines
- agile data management
- open source tools and or transperently priced services

### Lambda Architecture

Systems operating independently of each other - batch, streaming, and serving

Source system is ideally immutable and append only

Uhhh seems like the big thing here is that both data that is transformed in flight on a stream, as well as data that was processed in batch (usually NoSQL), are served from the same server service

### Kappa Architecture

Response to Lambda architecture

"Why not just use a stream processing platform as the backbone for all data handling - ingestion, storage, and serving?"

Streaming is still a mystery to many companies

Easy to talk about, hard to execute

### The Dataflow Model and Unified Batch and Streaming

Central problem of unifying batch data and streaming data is still there

Core idea of `Dataflow model` is to view all data as events, as the aggregation is performed over `various types of windows`

- Ongoing, real-time event streams are *unbounded data*
- Batch data are simply bounded event streams, where the boundaries provide a window
- Engineers can choose from various windows for real time aggregation
  - sliding
  - tumbling

### Architecture for IoT

#### Devices

Should know:

- what the device does
- the data it collects
- any edge computations or ml it runs before transmitting data
- how often it sends data
- consequences of device or internet outage
- environmental or external factors affecting data collection

#### Inferfacing with Devices

- IoT gateway
  - hub for connecting devices and routing devices to appropriate destinations on the internet
- Ingestion
  - uhh from the gateways, events and measurements flow into an event ingestion architecture
- Storage
  - storage requirements depends on latency requirement for devices in the system
- Serving
  - In a lot of cases, reverse ETL is super common cause source systems rely on readings from the sensors right
- Scratching the surface of the IoT

### Data mesh

In order to decentralize the monolithic data platform, we need to reverse how we thing oabout data, its locality, and ownership. Instead of flowing the data from domains into a centrally owned data lake or platform, domains need to host and serve their domain datasets in an easily consumable way

- Domain-oriented decentralized data ownership and architecture
- Data as a product
- Self-serve data infrastructure as a platofmr
- Federated computational governance
