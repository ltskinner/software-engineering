# Chapter 5. Exploring Neighborhoods in Production

## Working with Graph Data in Apache Cassandra

Concepts of graph data structures in Cassandra:

- primary keys
- partition keys
- clustering columns
- materialized views

Vertices: primary keys and partition keys

Edges: clustering columns, materialized views

### The Most Important Topic to Understand: Primary Keys

A major challenge of ubilding a good data model within a distributes system is determining how to uniquely identify data with primary keys

Simple form of primary keys: the partition key

- Partition key: The partition key is the first element of a primary key in Cassandra. The partition key is part of the primary key that identifies the location of the data in a distributed environment

Aka the first part of the primary key

- Primary key: The primary key describes a unique piece of data in the system. Can be made up of one or more properties

```groovy
schema.vertexLabel("Customer").
  ifNotExists().
  partitionBy("customer_id", Text).  // basic primary key: one partition key
  property("name", Text).
  create();
```

From a developers perspective, the decision to use customer_id as the full primary AND partition key:

- value of customer_id uniquely identifies the data
- app needs the value for customer_id to read the data about the customer
- A vertex labels partition key assigns your graph data to a host within a distributed environment. Partition keys also give you different ways you can colocate your graph data

### Partitioning graph data ccording to access pattern

Strategies exist for designing your partition keys to minimize the latency

To minimize jumping around machines in your cluster, consider pertitioning strategy that keeps all the data related to your query within the same partition

```groovy
schema.vertexLabel("Customer").
  ifNotExists().
  partitionBy("customer_id", Text).  // basic primary key: one partition key
  clusterBy("acct_id", Text). // to be defined
  property("name", Text).
  create();
```

### Understanding Edges, Part 1: Edges in Adjacency Lists

Three main data structures:

- Edge list: An edge list is a list of pairs in which every pair contains two adjacent vertices. The first element in the pair is the source (from) vertex, and the second element is the destination (to) vertex
- Adjacency list: An adjacency list is an object that stores keys and values. Each key is a vertex, and the value is a list of the vertices that are adjacent to the key
- Adjacency matrix: An adjacency matrix represents the full graph as a table. There is a row and column for each vertex in the graph. An entry in the matrix indicates whether there is an edge between the vertices represented by the row and column

### Understanding Edges, Part 2: Clustering Columns

- Clustering column: A clustering column determines a sorting order of your data in tables on disk

```groovy
schema.edgeLabel("owns").
  ifNotExists().
  from("Customer").  // the edge labels partition key
  to("Account").  // the edge labels clustering column
  property("role", Text).
  create()
```

### Understanding Edges, Part 3: Materialized Views for Traversals

The main area in which you are going to feel the effects of an edges primary key design comes into how you access your edges. To use an edge, you have to know its partition key

Because of this, we cannot yet traverse our edges in the reverse direction. This is because there are no edges in the system that start with the partition key from the incoming vertex labels in our examples

#### Materialized views for bidirectional edges

- Materialized view: A materialized view creates and maintains a copy of the data in a separate table with a different primary key structure, rather than requiring your application to manually write the same data multiple times to create the access patterns you need

```groovy
schema.edgeLabel("deposit_to").
  from("Transaction").
  to("Account").
  materializedView("Transaction_Account_inv").
  ifNotExists().
  inverse().
  create()
```

## Graph Data Modeling 201

Rule of Thumb 7: Properties can be duplicated onto edges or vertices; use denormalization to reduce the number of elements you have to process in a query

- Denormalization: Denormalization is the strategy of trying to improve the read performance of a database, at the expense of losing some write performance, by adding redundant copies of data grouped differently

Rule of Thumb 8: Let the direction you want to walk through your edge labels determine the indexes you need on an edge label in your graph schema

Rule of Thumb 9: Load your data; then apply your indexes

```groovy
// basically do the regular schema.eddgeLabel stuff
// then,
.materialilzedView()
```

Rule of Thumb 10: Keep only the edges and indexes that you need for your production queries

## Production Implementation Details

### Bulk Loading Graph Data

Load all data into graph from .csv files

csv file for each vertex and edge label

Vertex csvs:

- Accounts.csv - account ids, one per line
- CreditCards.csv - cc id, one per line
- Customers.csv - customer details, one per line
- Loans.csv - loan id, one per line
- Transactions.csv - transaction details, one per line
- Vendors.csv - vendor details, one per line

Edge csvs:

- charge.csv - charge edges from Transactions to a CreditCard
- deposit_to.csv - the deposit_to edges from a Transaction to an Account
- owes.csv - the owes edges from a Customer to a Loan
- owns.csv - the owns edges from a Customer to an Account
- pay_loan.csv - the pay edges from a Transaction to a Loan
- pay_vendor.csv - the pay edges from a Transaction to a Vendor
- uses.csv - the uses edges from a Customer to a CreditCard
- withdraw_from.csv - the withdraw_from edges from a Transaction to an Account
