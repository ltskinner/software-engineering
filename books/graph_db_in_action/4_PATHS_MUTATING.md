# Chapter 4. Pathfinding Traversals and Mutating Graphs

## 4.1 Mutating a graph

### 4.1.1 Creating vertices and edges

new vertex involves adding appropriate elements and properties

new edge is a bit more complicated - need to specify the vertex that belongs at each end of the edge

#### Adding vertices

#### Concerning mutations and graph steps

**DONT RUN** `g.V().addV('person)`

we would get a person vertex added for every existing vertex in the graph

vertex ids are generated automatically depending on the state of the db

#### Adding edges

- given a traversal source g
- add a new edge with a label friends
- assign the outbound vertx of the edge to the vertex with the key of first_name and the value of Ted
- assing the inbound vertex of the edge to the vertex with the key of first_name and the value of Hank

can do this pretty explicitly or can do with vertex variables as in script

### 4.1.2 Removing data from our graph

#### Removing a Vertex

- given a traversal source g
- find vertex with an id of 13
- remove (or drop) that vertex

`g.V(13).drop()`

#### Removing an Edge

- given a traversal source g
- find the edge with an ID of 15
- remove (or drop) that edge

`g.E(15L).drop()` - note need to specify L for Long (I believe)

### 4.1.3 Updating a graph

- given a traversal source g
- find the vertex with the key of first_name and the value of Dav
- update the property to that vertex with the key of first_name and the value of dave

#### Scripting Mutations

`.next()` causes the traversal to execute

`iterate()` is similar to next - the key difference being that iterate() does not return a result, while next does return a result

like for drops() because they dont return anything, iterate() is better to use than next()

Gremlin is a REPL loop - Read, Eval, Print Loop

#### Chaining Mutations

For composing complex opertions into a single statement, chaining steps is a fundamental strategy in Gremlin, as well as with other query languages. The concept is that each step takes data passed to it from the previous step, performs work on the data, and passes it on to the next step. Gremlin is able to do this because every step takes as input an iterable GraphTraversal, and nearly every step emits as its output a GraphTraversal. For those with functional programming experience, this should all be quite familliary

### 4.1.4 Extending our graph

## 4.2 Paths

Paths offer a description of te series of steps that a traverser takes to get from the start vertex to the end vertex

This means that not only can we find out which two vertices are connected, but we can also determing exactly how to get from the start to the end

When working with path algorithms, we begin by specifying a start vertex, and end vertex, and which edges to traverse between the two. The traversal returns all possible sets of direcitions that go from the start vertex to the end vertex

Steps of friends to go through to get ted introduced to denise:

- find the ted vertex
- traverse across each incoming and outogoing friends edge
- check to see if the vertex were on is the denise vertex
- repeat steps 2 and 3 until we reach denise
- return the path - the series of vertices and edges we traversed

Often discover that data has more connections than we anticipated

`.path()` is introduced - note that path() is expensive and slows shit down

```gremlin
g.V().has('person', 'first_name', 'Ted'
).until(
    has('person', 'first_name', 'Denise')
).repeat(
    both('friends').simplePath()
).path()
```

Above encounters cycles in the graph

`:clear` will clear the buffer and start over the traversal

### 4.2.1 Cycles in graphs

A cycle is a path of vertices and edges in a graph that contains one or more vertices that are reachable from themselves

So, how do we write a traversal without gettig stuck in an endless loop?

### 4.2.2 Finding the simple path

In graph theory, theres a concept known as the simple path. A simple path is a path that doesnt repeat any vertices, meaning that we only get results that are not cylical

`.simplePath()`

if it comes across an item it has already visited, it knows its in a cycle and removes itself

Why do we put this inside the repeat() instead of at the end? cause to see if were in a cycle, we eval current position and historical, so it needs to be within the loop

## 4.3 Traversing and filtering edges

To get the edge information as part of the path, we go from the vertex to edge to vertex

We must be explicit about stepping onto the edge and then stepping off of the edge

### 4.3.1 Introducing the E and V steps for traversing edges

"Who did Dave work with before the job he started in 2018

- given a traversal source g
- find the vertex with the key of first_name and the value of Dave
- traverse the works_with edges that have a start_year thats less than or equal to 2018
- traverse to the adjacent vertex
- return the first_name

what were missing is how to traverse from a vertex stop on the edge, filter based on a property on that edge, and then go to the adjacent vertex

The key is to traverse not from a vertex to the incident vertex, but to stop on the edge itself, look around a bit, then traverse to the next vertex

```gremmlin
g.V().has('person', 'first_name', 'Dave').
bothE('works_with').has('end_year', lte(2018)).
value('first_name')
```

#### Steps for Edges specifically

- `inE(label)` - traverses from the current vertex into incoming incident edges (if a label is specified, then it filters to only traverse to edges of that type)
- `outE(label)`
- `bothE(label)`

These steps each start on a vertex, traverse to an edge, and stop on the edge i.e returns an Edge i think

The location at the end of the step is the cruicial difference between out() and outE()

How do get back to a vertex:

- `inV()` - traverses from the current edge to the incoming vertex (and is commonly paired with the outE() step)
- `outV()` - traverses from the current edge to the outgoing vertex (commonly paired with inE())
- `otherV()` - traverses to the vertex that isnt the vertex thats used to traverse  onto the edge (commonly paired with bothE())
- `.bothV()` - traverses from the current edge to both of the incident vertices. Rarely used.

```gremlin
g.V().has('person', 'first_name', 'Dave').
bothE('works_with').otherV().values('first_name')

// which does the same as
g.V().has('person', 'first_name', 'Dave').
both('works_with').values('first_name')
```

Why would we ever use the E and V steps if we can do everything with the in(), out(), and both() steps - some use cases:

- filtering on edge properties using the has() filtering method
- including edges in path() results
- performant edge counts and denormalization

### 4.3.2 Filtering with edge properties

Filtering with edge properties usually comes in two flavors:

- time-based filters
- weight-based filters

```gremlin
g.V().has('person', 'first_name', 'Dave'),
bothE('works_with').has('end_year', lte(2018)).
value('first_name')

// another

g.V().has('person', 'first_name', 'Dave').
bothE('works_with').has('end_year', lte(2018)).
otherV().
values('first_name')
```

### 4.3.3 Include edges in path results

"When using the path() step, how do we also include the edges traversed?"

Need to use `bothE().otherV()` traversal pattern to explicitly traverse oto the edge

```gremlin
g.V().has('person', 'first_name', 'Ted').
until(
    has('person', 'first_name', 'Denise')
).repeat(
    bothE('works_with').otherV().simplePath()
).path()
```

### 4.3.4 Perormant edge counts and denormalization

We think that performance optimizations should only be applied after core functionality is established. We consider established to mean that the functionality is working, with good test coverage, and deployed with a production-similar data set

`g.V().bothE().count()`

does the same as:

`g.V().both().count()`, but this is more expensive

## Summary

- Adding vertices to a graph is similar to adding entities to a relational database
- Adding edges to a graph requires that we not only add the edge but also add or identify the vertex on each end
- Mutation operations in graph traversals allow for chaining together multiple mutation operations into a single operation, unlike SQL
- Paths in a graph represent the series of vertices and edges that connect two elements
- Cycles in a graph refer to a pth that has repeated vertices and are a common cause of long-running recursive and pathfinind queries in graph traversals
- A simple path is a path in a graph that does not repeat any vertices
- Edges can be traversed to and filtered on directly, without having to traverse to the adjacent vertex
