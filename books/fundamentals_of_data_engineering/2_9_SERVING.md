# Chapter 9. Serving Data for Analytics, Machine Learning, and Reverse ETL

## General Considerations for Serving Data

### Trust

"It takes 20 years to build a reputation and five minutes to ruin it. If you think about that, youll do things differently"

Above all else, trust is the root consideration in serving data. /end users need to trust the data theyre receiving

### Whats the Use Case, and Whos the User

Can be useful to work backwards from the end user

### Data Products

Making data products is a full-contact sport, involving a mix of product and business alongside technology

Keep in mind:

- When someone uses the data product, what do they hope to accomplish? All too often, data products are made with out a clear uderstanding of the outcome expected by the user
- Will the data product serve internal or external users?
- What are the outcomes and ROI of the data product youre building?

### Self-Service or Not

How will users interface with the data product?

Today, most self-service BI and data science is mostly aspirational

The executive probably just wants a predefined dashboard of clear and actionable metrics

### Data Definitions and Logic

### Data Mesh

## Analytics

Discovering, exploring, identifying, and making visible key insights and patterns within data

- is the user looking at historical trends?
- should users be immediately and automatically notified of an anomaly?
- is someone consuming a real-time dashboard on a mobile application?

### Business Analytics

Use historical and current data to make strategic and actionable decisions

- dashboards
- reports
- ad hoc analysis

KPIs and Objectives and Key Results (OKRs)

Goal of reports is to use data to drive insight and action

Ad hoc is "dig into this I have a question"

### Operational Analytics

Data used to take *immediate action*

Should be real time, like application monitoring

Real-time data without action is an unrelenting distraction

### Embedded Analytics

external facing analytics

- low latency
- fast query performance
- concurrency

## Machine Learning

## What a Data Engineer Should Know About ML

## Ways to Serve Data for Analytics and ML

### File Exchange

Ways you serve files depends on several factors:

- use case - business analytics, operational analytics, embedded analytics
- data consumers data handling processes
- size and number of individual files in storage
- who is accessing this file
- data type - structured, semistructured, or unstructured

### Databases

Serving data from database carries variety of benefits

- databases impose order and structure
- databases offer fine-grained permission control
- databases offer high serving performance for large, computationally intensive queries and high query concurrency

### Streaming Systems

- *emitted metrics*

### Query Federation

way to serve queries without going through trouble of centralizing data in an OLAP system

### Data Sharing

- generally turns data serving into a security and access control problem

### Semantic and Metrics Layers

- metrics layer: tool for maintaining and computing business logic
- semantic layer: similar, but lives in a tool or software that builds transformation queries

### Serving Data in Notebooks

- datafrmes lol inherently memory based

## Reverse ETL

Serving data by loading it from an OLAP database back into a source system

`bidirectional load and transform (BTL)`

## Whom Youll Work With

- data analysts
- data scientists
- mlops/ml engineers
- the business - nondata or nontechnical stakeholders, managers, executives

## Undercurrents

"data is a silent killer" and the undercurrents come to a head in the serving stage

### Security

### Data Management

Primary concern is ensuring people can access high quality and trustworthy data

untrusted data will go unused

### DataOps

things to monitor:

- data health and data downtime
- latency of systems serving data - dashboards, databases, etc
- data quality
- data system security and access
- data and model versions being served
- uptime to achieve an SLO

### Data Architecture

feedback loops must be fast and tight

encourage users to migrate from local use to cloud based

### Orchestration

Will orchestration be centralized or decentralized?

- A decentralized approach allows small teams to manage their data flows, but can increase burden of cross team coordination
- Centralized is easier to coordinate, but significant gatekeeping must also exist to protect a single production asset

Who will own the orchestration?

### Software Engineering

Listen to your stakeholders, use as an opportunity to learn whats working and what can be improved

- build
- learn
- improve
