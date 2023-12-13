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
