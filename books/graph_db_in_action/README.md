# Graph Databases in Action

Gremlin is a query language, that is allegedly turing complete, while cypher is not. Apparently cyper is supposed to be easier to use, but provides a subset of functionlity of Gremlin

Gremlin sits on top of Apache TinkerPop (a graph computing framework for OLTP and OLAP systems)

This book uses `labeled property graph database` instead of:

- RDF store
- triplestore database

Labeled property graph databases are most common seen in production (and have the most momentum behind them)

Why Gremlin was picked:

- Gremlin is a better tool for teaching how traversal works
- Gremlin is a common language of choice for enterprise applications
- Gremlin is the most portable language between property graph databases

## General Links

- [Gremlin](./_GREMLIN.md)
- [DiningByFriends](./_DININGBYFRIENDS.md)

## Part 1. Getting Started with Graph Databases

### [1. Introduction to Graphs](./1_INTRO.md)

"Just because a problem can be represented in a graph, doesnt neccesarily mean that a graph database is the best technology to choose to solve that problem"

- What is the problem we are trying to solve?
  - Selection/search - RDBMS
  - Related or recursive data - **Graph**
  - Aggregation - RDBMS
  - Pattern matching - **Graph**
    - Prime example of power of graph dbs
  - Centrality, clustering, influence - **Graph**

Should I use a graph?

- do I care about how things are related as much as the things themselves?
  - yes -> yes use graph
- does sql perform many joins on the same table or require recursion?
  - yes -> is this because of a bad relational model? no -> yes use graph
- how often does the data structure evolve?
  - frequently -> maybe use graph
- is my domain a natural frit for a graph
  -> maybe use graph

### [2. Graph Data Modeling](./2_GRAPH_DATA_MODELING.md)

High level:

- identifying and understanding the problem
- determinging the entities and relationships in that problem
- creating representation of that problem in the database

Big thing is to have an "entity AND relationship first" mindset

- Entity
- Relationship
- Attribute
  - **limit use of attributes cause can detract from omre critical parts of model**
- Access pattern

Define your queries before the data model, like you need to know your use case before you do the dog n pony show

#### Four-step Process

- 1. Understand the problem
- 2. Create a whiteboard or conceptual model
  - codifying main entities and relationships
  - focused on the business perspective
- 3. Create logical data mosel
  - define vertices and edges, and specifying properties on those
- 4. Test the model
  - validate coherence of previous steps
  - "does this make sense"
  - "did we leave anything out"

Naming conventions: be concise, descriptive, and generic

The direction of an edge should complement the edge label to make a sentence that sounds natural (and fits the needs of the use case)

Play around with inverting and changing wording of edge

Improper uniqueness usually appears in one of three ways:

- Too little data returned
- Duplicated data returned
- Poor query performance

### [3. Running Basic and Recursive Traversals](./3_TRAVERSAL.md)

Basic operations:

- find a starting vertex
- identify an edge to traverse
- traverse that edge
- complete the traversal by arriving at the destination vertex

Things to remember:

- Traversing is a series of steps
- Traversing requires knowing where we are
- Edge direction matters
- Traversals dont have history

#### Starting operators

`g = graph.traversal()`

#### Global Steps

- `V()` - iter all vertex
- `E()` - iter all edges - rarely use

#### Filtering Steps

- `.hasLabel(label)` - v and e with label
- `.has(key, value)` - v and e
- `.has(label, key, value)` - `g.V().hasLabel('person').has('first_name', 'Ted')`

#### Traversal Steps

- `.out(label)` e out
- `.in(label)` e in
- `.both(label)` e both out and in

### Value Retrieval Steps

- `.values(keys)` - returns values of `properties`
- `.valueMap(keys)` - returns keys and values

### Recursive Steps

- `.repeat(traversal)`
  - `.times(integer)`
  - `.until(traversal)` - Reccomend providing:
    - `times()`, or
    - `timeLimit()`
- `emit()` - to see intermediate steps
  - `.unitl().emit().repeat()` - shows start
  - `.until().repeat().emit()` - dupes last v