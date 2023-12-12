# Chapter 3. Running Basic and Recursive Traversals

Powerful feature of graphs: the ability to easily write recursive queries

## 3.1 Setting up your environment

## Starting the console, connecting to server, loading data

## 3.2 Traversing a Graph

Lets answer "Who are Ted's freinds?"

### Traverse, traversal, traversal source, and traverser

- Traverse:
  - The process of moving from vertex to edge or edge to vertex as we navigate a graph
  - Traversing a graph is analogous to the act of querying in a relational database
- Traversal:
  - A specification of one or more steps or actions to perform on a graph, which either returns data or makes changes, or in some cases, does both
  - In a relational world, this would be the actual SQL query. In a graph world this is the set of operations, called steps, that are send to the server to be executed
- Traversal source:
  - The traversal source is a concept specific to TinkerPop
  - It represents the base or starting point from which steps traverse the graph
  - By this convention, this is usually represented with the variable g and is required to begin any traversal
- Traverser
  - The computing process associated with a specific branch of a traversals execution
  - A traverser maintains all the metadata about the current branch of the graph its moving through (e.g. current object, loop information, historical path data, etc)
  - A unique traverser represents each branch through the data

Another way to think about these terms is that a traversal begins at a traversal source by sending one traverser per branch to traverse a graph. The traverser can either be removed or returned with the results

### 3.2.1 Using a logical data model (schema) to plan traversals

#### Graph Elements

- Vertices
  - vertex label
  - vertex properties
  - connected edge labels
- Edges
  - edge labels
  - edge properties
  - edge direction
  - connected vertex labels

If we find that it is difficult to write traversals to address the use cases, then we likely missed something in our data modeling process

### 3.2.2 Planning the steps through the graph data

### 3.2.3 Fundamental concepts of traversing a graph

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

### 3.2.4 Writing traversals in Gremlin

Steps:

- given all the vertices in my graph
- find all `person` vertices with a `first_name` of `Ted`
- Walk the outgoing `friends` edges to the first incident vertex
- return the `first_name`

Better to see the answer first, and then break down what each step does

#### Traversal source

`g` is always the first step in every gremlin traversal

#### Gremlin key concepts: `g != graph`

There are two APIs

The predominant API is the Traversal API that starts, by convention, with a veriable defined by `g = graph.traversal()`

#### Global steps

The second step is `V()`

This returns an iterator that cintains every vertex in the graph

1 of 2 global graph steps

The other global graph step is `E()`

This returns an iterator that contains every edge in the graph

Rarely use `E()` step

#### Filtering Steps

`has()` is the first filtering step introduced

One of the most common because it only passes through any vertex or edge that:

- Matches the label specified, if a label is specified
- Has a key-value pair that matches the specified key-value pair

Common forms:

- `.hasLabel(label)`
  - Yields all vertices or edges of the specified `label` type
- `.has(key, value)`
  - Yields all vertices and edges with a property matching the specified `key` and `value`
- `.has(label, key, value)`
  - Yields all vertices and edges with both the specified `label` and with a property matching the specified `key` and `value`
  - Sameas `g.V().hasLabel('person').has('first_name', 'Ted')`

Can chain all these bois together

When working with a transactional graph, its vital to narrow down the number of starting traversers as quickly as possible - for load and performance

#### Traversal steps

`out(label)` traverses all outgoing edges to the incident vertex with a specified label

if a label is not specified, it traverses all outgoing edges

`in(label)` also works

`both(label)` --> does both in and out

### 3.2.5 Retrieving properties with values steps

Final step in traversal is the `values(keys)` step --> lists values

Returns the values of the elements `properties`

Another is `valueMap(keys)` --> lists keys and values

## 3.3 Recursive traversals

### 3.3.1 Using recursive logic

Exmaple problems:

- bill of materials
- map directions
- task dependency

Each of these requires traversing an unknown number of links

Lets find friends of teds friends:

- 1. Find all the Ted vertices
- 2. Traverse the outgoing `friends` edges to the incident edge
- 3. Traverse to the incoming vertex
- 4. Traverse the outgoing `friends` edges to the incident edge
- 5. Traverse to the incoming vertex
- 6. Return the `first_name` property value

### 3.3.2 Writing recursive traversals in Gremlin

- `.repeat(traversal)`

The `traversal` parameter represents the set of Gremlin steps to be repeated within the loop

- `.times(integer)` - a modifer for a `repeat()` loop - n times for loop to exe
- `.until(traversal)` - a modifier for a `repeat()` loop - represents the set of Gremlin steps that evaluate for each loop. When the traversal evals to `true` the `repeat()` step exits

When using `until(traversal)`, if condition not met, becomes an `unbounded traversal`

Reccomend providing:

- `times()`, or
- `timeLimit()`

To see intermediate steps: `emit()`

By placing `emit()` before `repeat()` our traversal yields not only our initial vertex, but avoids duplicating final vertex
