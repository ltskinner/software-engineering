# Chapter 1. Graph Thinking

## Why Now? Putting Database Technologies in Context

Previous technologies and dbs focused on how to **most efficiently** store data

Now we want to know how we can get the **most value** out of data

History of dbs can be loosely divided into three eras:

- hierarchical
- relational
- NoSQL

### 1960s-1980s: Hierarchical Data

"hierarchical" or "navigational - irrispective of the label, the thinking during this era aimed to organize data in treelike structures

### 1980s-2000s

Separate organization of data from its retrieval system - entity-relationship databases

Relational systems organize your data into sets. These sets focus on the storage and retrieval of real-world entities, such as people, places, and things. Similar entities, such as people, are grouped together in a table. in these tables, each record is a row. An individual record is accessed from the table by its primary key

For better or for worse, this era introduced and ingrained the mentality that all data maps to a table

### 2000s-2020s: NoSQL

Addresses different shapes and volumes of data

The message of the NoSQL era was quite clear: storing, managing, and querying data at scale in tables doesnt work for everything

Three main needs:

- data serialization standards
- specialized tooling
- horizontal scalability

Clusters became a thing

### 2020s-?: Graph

#### Why the 2020s?

#### Connecting the dots

## What is Graph Thinking

Most high-value business problems and opportunities are complex problems

### Complex Problems and Complex Systems

- Complex problems - complex problems are the individual problems that are observable and measureable within complex systems
- Complex systems - complex systems are composed of many individual components that are interconnected in various ways such that the behavior of the overall system is not just a simple aggregate of the individual components behavior (called "emergent behavior")

### Comple Problems in Business

- LinkedIn - bought for $26B on $1B of rev
- Github - bought for $7.8B on $300M of rev

26x multiplier on data that models a domains complex system

## Making Technology Decisions to Solve Complex Problems

The difficulty with learning and applying graph begins with recognizing where relatinoships do or do not add value within your data

### Question 1: Does your problem need graph data

| Data Description | Data Shape | Usage | DB Rec |
| - | - | - | - |
| Spreadsheets or tables | Relational | Retrieved by a primary key | RDBMS datbases |
| Collections of files or documents | Hierarchical or nested | Root identified by an ID | Document DBs |
| Relationships or links | Graph | Queried by a pattern | Graph DBs |

### Question 2: Do relationships within your data help you understand your problem

The most common problem we advise teams to break down is *entity resolution*, or knowing who-is-who in your data

#### Common missteps in understanding your data

### Question 3: What are you going to do with the relationshiops in your data

Two main things youll need to do:

- analyze it
- query it

Divide is data analysis vs data management

### Question 4: Qhat do you need the results for

Topics in graph analysis can range from udnerstanding specific distributions acrss the relationships to running algs across the entire structure

This is the area for algorithms such as:

- connected components
- clique detection
- triangle counting
- calculating a graphs degree distribution
- page rank
- reasoners
- collaborative filtering
- many others

Three different goals for the results:

- reports
- research
- retrieval

#### Reports

Traditional need for intelligence and insights into business data

#### Research

Some books explore the tools and ifnrastrucutre needed for researching graph-structured data

#### Retrieval

Providing service to an end user - data driven products that serve customers

### Seeing the Bigger Picture

The path to understanding the strategic importance of your businesses data is synonymous with finding where (and whether) graph technology fits into your applciation

## Getting Started on Your Journey with Graph Thinking
