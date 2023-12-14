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
