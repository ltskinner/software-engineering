# Chapter 2. Data Models and Query Languages

"Data models are perhaps the most important part of developing software, because they have such a profound effect: not only on how the software is written, but also on how we *think about the problem* that we are solving"

Most applications are built by layering one data model on top of another. For each layer, the key question is: hows is it *represented* in terms of the next-lower layer?

- 1. As an application developer, you look at the real world (people, orgs, goods, actions, money, sensors) and model it in terms of objects or data structures, and apis that manipulate those data structures
- 2. When you want to store those data structures, you express them in terms of a general-purpose data model, such as JSON, xml, tables, graph, etc
- 3. The engineers who built your database software decided on a way of representing that json/whatever in terms of bytes in memory, on disk, or on a network. The representation may allow the data to be queried, searched, manipulated, and processed in various ways
- 4. On yet lower levels, hardware engineers have figured out how to represent bytes in terms of electrical currents, pulses of light, magnetic fields, and more

## Relational Model vs Document Model

### The Birth of NoSQL

Several driving forces behind the adoption of NoSQL databases including:

- A need for greater scalability than relational databases can easily achieve, including very large datasets or very high write throughput
- A widespread preference for free and open source software over commercial database products
- Specialized query operations that are not well supported by the relational model
- Frustration with the restrictiveness of relational schemas, and a desire for a more dynamic and expressive data model

### The Object-Relational Mismatch

Currently, require an awkward translation layer to go between objects in application code and the database model of tables, rows, and columns - `impedance mismatch`

JSON has better `locality` than multi-table schema - dont need to perform multiple queries and joins to get the desired structure and info

### Many-to-One and Many-to-Many Relationships

There are advantages to having a user select from a drop-down list or autocompleter with standardized lists in the backend:

- Consistent syle and spelling across profiles
- Avoiding ambiguity (e.g. if there are several cities with the same name)
- Ease of updating - the name is stored in only one place, so it is easy to update across the board if it ever needs to be changed
- Localization support - when the site is translated into other languages, the standardized lists can be localized, so the region and industry can be displayerd in the viewers language
- Better search (because metadata on pre-defined options)

### Are Document Databases Repeating History

#### The Network Model

- a generalization of the hierarchical model
  - unlike hierarchical, where every record had exactly one parent
  - in network, records can have multiple parents
- the links between records were not foreign keys, but more like pointers - access path through chain of links
- this made code for querying and updating the database complicated and inflexible

#### The Relational Model

- dont have to change queries to take advantage of new index - query optimizer figures this out already

#### Comparison to Document Databases

- Document databases reverted back to the hierarchical model in one aspect: storing nested records within their parent record rather than in a separate table
- both document and relational have a unique identifier
  - `foreign key` in the relational model
  - `document reference` in the document model

### Relational vs Document Databases Today

Main arguments for document data model are:

- schema flexibility
- better performance due to locality
- some applications, it is closer to the data structure used by the application

Arguments for relational:

- better support for joins
- many-to-one and many-to-many relationships

#### Which Data Model Leads to Simpler Application Code

- if the data in your application has a document like structure, then probably use document model lol

Limitations:

- cannot refer directly to a nested item within a document
  - end up needing an access path like the hierarchical model
- poor support for joins
- many-to-many relationships are bad

#### Schema Flexibility in the Document Model

Document databases are sometimes called `schemaless`

But thats misleading, as the code reading the data structure usually assumes there is an implicit schema, its just not **enforces** by the db

A more accurate term is `schema-on-read` as opposed to `schema-on-write`

Schema-on-read is adventagious if the items in the collection dont all have the same structure for some reason

- there are many different types of objects, and it is not practical to put each type of object in its own table
- The structure of the data is determined by external systems over which you have no control and which may change at any time

In these cases, a schema may hurt more than it helps

#### Data Locality for Queries

If an application needs to access an **entire** document, there is a performance advantage to `storage locality`

If the data is split across multiple tables, multiple index lookups are required to retrieve it all, which may require more disk seeks and take more time

But if you only need part of a document, can be wasteful to load the whole thing

Generally recommended to keep documents fairly small and avoid writes that increase the size of the document

#### Convergence of Document and Relational Databases

Most relational database systems have supported XML for a while

- includes functions to make local modifications to xml documents
- ability to index and query inside xml docs

## Query Languages for Data

Imperative language tells the computer to perform certain operations in a certain order

Declarative language you specify the pattern of data, what conditions, and how you want data transformed, but not HOW to achieve the goal

- Declarative is attractive because it is typically more concise and easier to work with than an imperative api
- It also hides implementation details of the db engine, which lets you improve the db without modifying queries
- Lend themselves to parallel execution

### Declarative Queries on the Web

### MapReduce Querying

MapReduce is neither a declarative query language, nor a fully imperative query api, but somewhere in between:

- the logic of the query is expressed with snippets of code, which are called repeatedly by the processing framework

map and reduce functions are somewhat restricted in what they are allowed to do - they must be `pure` functions which means they can only use the data that is passed to them as input, they cannot perform additional database queries, and they must not have any side effects

## Graph-Like Data Models

Many-to-many relationships are an important distinguishing feature between data models. If your application has mostly one-to-many relationships (tree structured data) or no relationship between records, the document model is appropriate

But what if many-to-many relationships are very common in your data?

Graphs - vertices (nodes) and edges

Examples:

- social graphs
- web graphs
- road or rail networks

Note, nodes dont need to be homogenous - linking across different node types is super powerful

- Property graph model
  - neo4j, titan, infinitegraph
- triple-store
  - datomic, allegraph

### Property Graphs

Each vertex consists of:

- a unique identifier
- a set of outgoing edges
- a set of incoming edges
- a collection of properties (key-value pairs)

Each edge consists of:

- a unique identifier
- the vertex at which the edge starts (the tail vertex)
- the vertex at which the edge ends (the head vertex)
- a label to describe the kind of relationship between the two vertices
- a collection of properties (key-value pairs)

Some important aspects of this model are:

- any vertex can have an edge connecting it with any other vertex. there is no schema that restricts which kinds of things can or cannot be associated
- given any vertex, you can efficently find both its incoming and outgoing edges and thus traverse the graph, both forward and backward
- by using different labels for different kinds of relationships, you can store several different kinds of information in a single graph, while still maintaining a clean data model

### The Cypher Query Lanuguage

Declarative query language for property graphs

### Graph Queries in SQL

In a relational database, you usually know in advance which joins you need in your query

in graph query, its ok to not know the joins in advance

### Triple-Stores and SPARQL

(`subject`, `predicate`, `object`) - (jim, likes, banannas)

The subject of a triple is equivalent to a vertex in a graph. The object is one of two things:

- a value in a primitive datatype, such as a string or number - in this case, the predicate and object of the triple are equivalent to the key and value of a property on the subject vertex
- another vertex in the graph - in this case the predicate is an edge in the graph, the subject is the tail vertex, and the object is the head vertex

#### The Semantic Web

"If you read more about triple-stores, you may get sucked into a `maelstrom` of articles written about the semantic web" broo hahahah

### The RDF Data Model

Turtle language is human readable format for RDF data

### The SPARQL Query Language

query langauge for triple-stores using the RDF model

### The Foundation: Datalog
