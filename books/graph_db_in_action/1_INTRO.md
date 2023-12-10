# Chapter 1. Introduction to Graphs

For every 100 modern questions that apps anser, only 88 answered with relational db, leaving 12 where relational dbs struggle

## 1.1 What is a graph?

- `Graph` - A set of vertices (singular vertex) and edges
- `Vertex` A point in a graph where zero or more edges meet, also referred to as a node or entity
- `Edge` - A relationship between two vertices whthin a graph, sometimes called a relationship, link, or connection

Common data structures:

- linked lists
- trees

### Euler and origins of graph theory

"Seven Bridges of Konigsberg" how people could cross all bridges exactly once, old Prussian city

### 1.1.1 What is a graph database?

Data-storage engine that combines basic graph structures of vertices and edges with:

- persistence technology
- traversal (query) language

to create a database optimized for storage and fast retrieval of highly connected data

Unlike other db technologies, graph dbs are build on the concept that the relationships between entities are as or more important than entities within the data

Relational dbs use foreign keys as pointers, hard to compute inverse effectively

"edges are first-class citizens, just like the vertices"

### 1.1.2 Comparisoin with other types of databases

- Key-value (Berkley DB, RocksDB, Redis, Memcached)
- Wide-column or column-oriented (Apache HBase, Azure Table Storage, Cassandra, Bigtable)
- Document (MongoDB, CouchDB)
- Relational
- Graph (Neo4j, TinkerPop, JanusGraph, TigerGraph)

higher is simple data complexity, lower is complex data complexity

basically, graph databases are the most complex

Where graphs are more elegant:

- recursive queries (for example, an org hierarchy)
- different result types (orders and products for reporting)
- paths (river crossing puzzle)

#### Recursive Queries

- Executed multiple times in succession
- if doing in sql, requires excessive denormalization of data and complex queries

SQL Example:

```sql
WITH RECURSIVE org AS (
    SELECT
        employee_id,
        manager_employee_id
        employee_name
        1 as level
    FROM org_chart
UNION
    SELECT
        e.employee_id,
        e.manager_employee_id,
        e.employee_name
        m.level +1 AS level
    FROM org_chart AS e
        INNER JOIN
            org as M
        ON
            e.manager_employee_id = m.employee_id
)
SELECT
    employee_id,
    manager_employee_id,
    employee_name
FROM org
ORDER BY level ASC;
```

Graph Example:

```gremlin
g.V().repeat(
    'works_for'
).path.next()
```

#### Different Result Types

Have you ever needed to return several different data types from a db, all within a single result set

```sql
SELECT
    id,
    name,
    address,
    null AS product_name,
    null AS cost,
    'Order' AS object_type
FROM Orders
UNION
SELECT
    id,
    null AS name,
    null AS address,
    product_name,
    cost,
    'Product' AS object_type
FROM Products;
```

Produces a "sparse matrix"

```gremlin
g.V().valueMap(true)

==>[label:order, address:[], name:[], id:1]
==>[label:order, address:[], name:[], id:2]
==>[label:product, cost:[], id:234, product_name:[]]
==>[label:product, cost:[], id:123, product_name:[]]
```

#### Paths

We have a fox, a goose, and a bag of barlye that must be transported across a river by a farmer on a boat

Constraints:

- The boat can only carry one item in addition to the farmer on each trip
- The farmer must go on each trip
- The fox cannot be left alone with the goose or it will eat it
- The goose cannot be left alone with the barley or it will eat it

Model initial state of system as a vertex:

TGBF_

- T (the boat and farmer)
- G (the goose)
- F (the fox)
- B (the barley)
- _ (the river)

(TFGB_) -(take_goose)-> (FB_TTG)

Graph representation of the farmer using the boat (T) to take the goose (G) across the river (_), leaving the fox (F) with the barley (b)

- 1. produce graph with all possible states
- 2. remove any vertex (state) that violates a constraint, and the adjoining relationships (edges)
- 3. further simplify by removing any edge that connects back to a previous state (as this leads us to a previous state aka cycle)

```gremlin
'TFGB_'.
    repeat(
        out()
    ).until(hasId('_TGFB')).path.next()
```

Solution (2):

```gramlin
TFGB_ -take goose-> FB_TG
-take empty-> TFB_G
-take barley -> F_TGB
-return goose -> TFG_B
-take fox-> G_TBF 
-return empty-> TG_FB
-take goose-> _TGFB

not writing second
```

## 1.2 Is my problem a graph problem

- social network analysis
- reccomendation engines
- dependency analysis
- fraud detection
- master data management
- search problems
- research on the internet

Difficulty with these lists, is that unless your problem is one specified, hard to know if good fit

### 1.2.1 Explore the questions

"Just because a problem can be represented in a graph, doesnt neccesarily mean that a graph database is the best technology to choose to solve that problem"

- What is the problem we are trying to solve?
  - Selection/search
  - Related or recursive data
  - Aggregation
  - Pattern matching
  - Centrality, clustering, influence

#### Selection/Search

Finding a small set of entities that all share a common attribute, such as name, location or employer:

- Give me everyone who works at X?
- Who in my system has a first name like John?
- Locate all stores within X miles

These are too simple for graph

#### Related or Recursive Data

Questions that explore the relationships between entities add meaning and provide topological value to data:

- Whats the easiest way for me to be introduced to an executive at X?
- How do John and Paula know each other?
- Hows company X related to company Y?

"friends of friends"

#### Aggregation

Excellent use case for a relational db

- How many companies are in my system?
- What are my average sales for each day over the pasth month?
- Whats the number of transactions processed by my system each day?

#### Pattern Matching

How entities are related - the prime example of how to leverage power of graph databases

Typical use casess: reccomendation, fraud detection, intrusion detection

- Why in my system has a similar profile to me
- Does this transaction look like other known fraudulent transactions
- Is the user J. Smith the same as Johan S.

graph dbs have query language specific built in features to handle these queries

#### Centrality, Clustering, and Influence

The relative influence or impoartance of one entitiey compared to another is a typical graph db use case

- Who's the mose influential persion I am connected with on linkedin
- What equipment in my network has the most substantial impact if it breaks
- What parts tend to fail at the same time

### 1.2.2 Im still confused... Is this a graph problem?

Decision Tree:

- do I care about how things are related as much as the things themselves?
  - yes -> yes use graph
- does sql perform many joins on the same table or require recursion?
  - yes -> is this because of a bad relational model? no -> yes use graph
- how often does the data structure evolve?
  - frequently -> maybe use graph
- is my domain a natural frit for a graph
  -> maybe use graph

(note, implicit no to go down to next question)


