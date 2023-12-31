# Chapter 8. Finding Paths in Development

After neighborhood retrieval and unbounded hierarchies, pathfinding is next most important use

## Thinking About Trust: Three Examples

### How Much Do You Trust That Open Invitation

Think about social media friend requests

### How Defensible Is an Investigators Story

### How Do Companies Model Package Delivery

## Fundamental Concepts About Paths

### Shortest Paths

Find path with the smallest distance, or shortest walk, from one vertex to another

- Path: A path in a graph is a sequence of consecutive edges in a graph
- Length: The length of a path is the number of edges in the path
- Shortest path: The shortest path between two vertices is the path that connects the two vertices and has the shortest length or distance
- Distance: The distance between two vertices in a graph is the number of edges in a shortest path

Three types of shortest path problems:

- Shortest path: The goal of a shortest path problem is to discover the smallest distance walk from A to B
- Single-source shortest path: The goal of a single-source shortest path problem is to discover the smallest distance walk from A to all other vertices in the graph
- All-pairs shortest path: The goal of an all-pairs shortest path problem is to discover the smallest distance walk between any two vertices in the graph

Any solution relies on understanding how to procedurally walk through a graph data:

- Depth-first search: DFS explores a path as deep as possible along each branch before backtracking
- Breadth-First Search: BFS explores all of the neighbor vertices at the present depth prior to moving on to the vertices at the next depth level

### DFS and BFS

### Learning to See Application Features as Different Path Problems

## Finding Paths in a Trust Network

## Understanding Traversals with Our Bitcoin Trust Network

### Evaluation Strategies with the Gremlin Query Language

Gremlin is primarily a lazy stream-processing language. This means that Gremlin tries to process any traversers all the way through the traversal pipeline before getting more data from the start of the traversal. This is different from an eager evaluation strategy, which does the work right away before moving onto the next step

- Lazy evaluation: Lazy evaluation delays the evaluation of an expression until its value is needed
- Eager evaluation: Eager evaluation evaluates an expression as soon as it is bound to a variable

There are numerous situations in which the Gremlin language cannot use lazy evaluation

In Gremlin, the key to knowing when a traversal changes between lazy and eager eval is to recognize barrier steps. When a barrier step exists, a Gremlin traversal changes from lazy to eager eval

#### Barrier steps in Gremlin

- Barrier step: A barrier step is a function that turns the lazy traversal pipeline into a bulk-synchronous pipeline

Barrier steps change the behavior of a query to operate like BFS or DFS

Example barrier steps:

- dedup
- aggregate
- count
- order
- group
- groupCount
- cap
- iterate
- fold

## Shortest Path Queries

### Finding Paths of a Fixed Length

Basically, first do count, then do limit

### Finding Paths of Any Length

do count(local)

#### Connecting concepts: BFS and traversal strategies

If using BFS then we can guarantee that the first traverser that satisfies the stopping condition is the shortest path

The definitive way to answer is to inspect the explain() step to see what traversal strategies are applied

repeat().unitl() pattern uses barriers. This means it executes eagerly using BFS

### Augmenting Our Paths with Trust Scores

#### Using sack() to aggregate trust ratings

The definitions for sack constructs in Gremlin are:

- A traverser can contain a local data structure called a sack
- The sack() step is used to read and write sacks
- Each sack of each traverser is initialized when using withSack()

### Do You Trust This Person
