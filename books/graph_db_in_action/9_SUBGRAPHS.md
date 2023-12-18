# Chapter 9. Working with Subgraphs

This leads to personalization - say person a and person b have not many (if any) links to reach each other

Personalization is a process of filtering data based on the connections in the data in order to serve the most relevant content

Because the answer to our question is in only a well-defined subset of data, we just want to work exclusively with that data

The most efficient way to do this is to extract that subset of data from the global graph

## 9.1 Working with subgraphs

### 9.1.1 Extracting a subgraph

To create this subgraph, we need to develop a traversal that defines the vertices and edges

Depending on our choice of database engine, we can create subgraphs using one of two techniques:

- vertex-induced
- edge-induced

#### Vertex-Induced vs Edge-Induced Subgraphs

Vertex-induced is defined by a set of vertices and any shared edges

Edge-induced is defined by a set of edges but includes the incident vertices

Even though our subgraphs have the same vertices, these do not have identical edges

#### Defining our Subgraph

Edge-induced:

- 1. Get the Josh vertex (person_id=2)
- 2. Traverse the friends edges in either direction
- 3. Define a subgraph based on the edges traversed
- 4. Extract the edges and vertices in the subgraph
- 5. Return the results

```gremlin
g.V().has('person', 'person_id', 2).
  bothE('friends').
    subgraph('sg').
  cap('ag').
next()
```

- `.subgraph(sideEffectKey)` - defines an edge-induced subgraph within a larger set of graph data. The sideEffectKey is a reference to the full results of the side effect
- `.cap(sideEffectKey)` - iterates the traversal up to itself and emits the results of the side effect referenced by the sideEffectKey - basically returns the subgraph

### 9.1.2 Traversing a subgraph

Basically, the .cap('sg') returned subgraph is abstract. To use it, need to get a graphTraversalSource

`sg = subgraph.traversal()`

## 9.2 Building a subgraph for personalization

Actions:

- 1. Locate the person vertex, who is the subject of the subgraph
- 2. Traverse to the friends vertices of the subject person
- 3. Determine the review vertices for each friend
- 4. Find the review_ratings
- 5. Find the rests with the most highly-rated reviews

New step:

- `optional(traversal)` - attempts the traversal, and if there is a result it emits it, otherwise it issues the incoming element as with the identity() step

```gremlin
g.V().has('person', 'person_id', 2).
  bothE('friends').
    subgraph('sg').
      otherV().outE('wrote').
    subgraph('sg').
      inV().
      optional(
        hasLabel('review_rating').
          outE('about').
          subgraph('sg').inV()
      ).
      outE('about').subgraph('sg')
      inV().outE('within').
    subgraph('sg').
  cap('sg').next()
```

## 9.3 Building the traversal

### 9.3.1 Reversing the traversing direction

### 9.3.2 Evaluating the individualized results of the subgraph

## 9.4 Implementing a subgraph with a remote connection

## Summary

- Subgraphs are a subset of graph data that contain vertices and edges represented as a graph. Subgraphs are themselves graphs. This means that we can run traversals on these, but because these are constrained to a small subset of vertices and edges, subgraphs require less memory and computation power to process
- Subgraphs can be defined in one of two ways: verte-induced or edge-induced. Vertex-induced subgraphs are defined by specifying a set of vertices and include the incident edges. Edge-induced subgraphs are defined by specifying a set of edges and include the adjacent vertices. The database you choose determines which option is available
- Because subgraphs return as graphs, we can traverse these and perform all the other operations youve learned to do with graphs once youve created a graph traversal source for the subgraph
- Subgraphs can be reused and even modified, but any changes you make are done in isolation from the original graph. This means that any changes are not propagated back to the original graph data
