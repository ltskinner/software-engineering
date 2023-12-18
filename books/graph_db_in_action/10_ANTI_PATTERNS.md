# Chapter 10. Performance, Pitfalls, and Anti-Patterns

## 10.1 Slow-performing traversals

### 10.1.1 Explaining our traversal

- `explain()`

basically just tack on to the end and it walks thru the steps

### 10.1.2 Profiling our traversal

Lets say our slow traversal works perfectly fine for some users, but horribly for others

Instead of looking at the planned execution, we need to profile the actual operations. This allows us to compare good runs to the bad ones and to see the difference

In most graph dbs, done with profile() - runs the traversal and collects statistics on the performance characteristics during its execution

For each line of output:

- The count of the represented traversers (Count)
- The count of the actual traverser (Ts or Traversers)
- The time spent on that step (Time)
- The percentage of the traversal's total duration spent on that step (%Dur)

### 10.1.3 Indexes

Three areas where indexes can provide the most performance improvement:

- Properties frequently used for filtering on values or ranges. Indexes quickly reduce the number of traversers required to execute a perticular task, thereby reducing the work required of the databases. This is especially helpful early on in a traversal where a minimal number of traversers is desired
- Properties requiring a full-text search, such as finding words that start with, end with, or contain a specific phrase. Many databases require a particular type of index to perform a full-text search on a property because these warrant special handling to be indexed efficiently
- Spatial features needing to be searched if the database supports geospatial data. Spatial properties also fall into the category of requiring special indexing to perform all the appropriate queries such as "Find all rest within ten miles of here"

## 10.2 Dealing with supernodes

Supernodes are one of the most common data-related performance problems in graph databases. These are also particularly difficult to deal with because supernodes cant be removed. And because they are part of the data, we can only try to mitigate the problems caused by supernodes

Supernode: a vertex in a graph with a disproportionally high number of incident edges

Two main concepts when discussing a supernode:

- Instance data
- Underlying data structures

### 10.2.1 Its about instance data

Refers to an instance of a vertex with a dispopo number of edges

- specific instance of a vertex, not the generic node type

### 10.2.2 Its about the database

Different engines have different internal data structures and storage algorithms. Read the docs and really understand the distribution of relationships

### 10.2.3 What makes a supernode

### 10.2.4 Monitoring for supernodes

Use general rules to id

#### Monitor for growth (degree) of vertices

```gremlin
g.V().
  project('vertex', 'degree').
    by(identify()).
    by(bothE().count()).
  order().
    by(select('degree'), desc).
  limit(10)
```

Drawbacks:

- needs to remember to run on a regular basis
- long running bc visit every vertex, and every edge twice

#### Monitoring for outliers

Reactively monitor the performance of traversals and look for outliers

### 10.2.5 What to do if you have a supernode

- first, decide if its actually a problem

#### Is the supernode a problem

Try inverting traversals or doing it another way

#### Mitigating supernodes

Most common and universally applicable:

- refactor the model to remove or minimize the impact of the supernode

Employ data modeling strategies:

- Duplicating vertex properties on edges
- Making vertices into properties or properties into vertices
- Moving property locations
- Precalculating data
- Adding indexes

The goeal of this refactoring is to minimze the number of edges

#### Vertex-centric and edge indexes

Because supernodes are a common problem within graph databases, some db vendors include specific index types to help address this issue. Referred to as edge indexes or vertex-centric indexes

## 10.3 Application anti-patterns

Other problems:

- 1. Using graphs for non-graph use cases
- 2. "Dirty" data
- 3. Lack of adequate testing

### 10.3.1 Using graphs for non-graph use cases

"I want to use a grpah database, so lets find a use case for one"

### 10.3.2 Dirty data

Data that:

- contains errors
- duplicate records
- incomplete or outdated information
- missing data fields

#### ENTITY RESOLUTION

- de-duplicating
- linking
- grouping records

that are believed to represent the same entity together into a single canonical representation

## 10.3.3 Lack of adequate testing

- non-representative test data
- insufficient scale when testing

### Non-representative test data

Because of the connected nature of graphs and how we traverse these, ensuring that we test against representative samples of data is more important than with relational dbs

Unlike relational, performance of graph traversals is less dependent on the quantity of data in the graph. Instead, its more dependent on the connectedness of the data in the graph

### Lack of scale

Testing at an adequate scale means using sufficiently deep and sufficiently connected data, not just sufficiently large data

Testing at scale is especially paramount with highly recursive applications or those using a distributed db

For example, if the app involves an unbounded recursive traversal that performs acceptably on our test graph with a depth of 5, it might crap out at 10 levels

## 10.4 Traversal anti-patterns

Patterns:

- Not using parameterized traversals
- Using unlabeled filtering steps

Both of these represent either a security of performance risk

### 10.4.1 Not using parameterized traversals

Injection attacks or whatever

#### Preventing injection attacks

A parameterized traversal uses tokens to represent the input values in the query

### 10.4.2 Using unlabeled filtering steps

This is underdefined:

`g.V().has('first_name', 'Hank').next()`

This is proper and more secure (cause not checking every vertex type)

`g.V().has('person', 'first_name', 'Hank').next()`

## Summary

- Performance issues with graph traversals can be diagnosed using one of two commonmethods:
  - explain() - shows how a graph traversal is executed but does not run it
  - profile() - runs the traversal and collects statistics about what actually occured (more helpful)
- Graph databases use indexes to speed up traversals by allowing quick and direct access to data, similar to relational databases. However, there are multiple types of indexes offered. The index type available is dependent on the vendors specific database implementation
- Supernodes are vertices in a graph that have a disproportionately high number of edges. These can cause traversal performance problems, especially when running transactional traversals
- Supernodes can be found by monitoring the branching factor and the number of successor vertices, and by looking for outliers
- Supernodes can be mitigated by using data modeling tips and tricks to split up the edges across multiple, different vertices or by using features such as vertex-centric indexes available in some graph databases. These indexes are designed to help alleviate the side effects of supernodes
- Although supernodes arent desirable when running transactional queries, these can be critically important when running analytical algorithms, such as degree centrality
- When writing graph-backed applications, understanding the problem were trying to solve is critical to its success. This ensures that we use the right tools and use those in the right way
- The use of "dirty" data is a common anti-pattern that is particularly problematic in graph applications due to the highly connected nature of the data and questions. Dirty data can be addreseed by properly de-duplicating an dlinking data to facilitate better application performance
- You should avoid testing with unrepresentative data because the connectedness of the data dramatically impacts the performance of graph-backed applications
- When submitting strings of Gremlin, the only way supported by some graph db vendors, you should always parameterize graph traversals to prevent injection attacks from running malicious code
- When running transactional queries, always start a traversal with a filter traversal that specifies the vertex label (or labels) as well as the properties. Specifying a filter at the start of your traversal prevents a traversal from searching all of the vertices
