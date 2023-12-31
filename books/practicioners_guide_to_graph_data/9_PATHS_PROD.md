# Chapter 9. Finding Paths in Production

Next concept is to evolve the idea of distance. We do this by adding some type of weight or cost to the steps along a path. We refer to this type of problem as a *minimum cost path* or *shortest weighted path*

Shortest weighted paths are very popular optimization problems in cs and math. These types of problems tend to be multifaceted, complex optimization problems because they are tryng to combine more than one source of information into a cost metric for minimization

Need to understand edge weights. Want to create a bounded minimum optimization problem

## Weighted Paths and Search Algorithms

sacks() are how we maintain this variable at runtime

### Shortest Weighted Path Problem Definition

- Shortest Weighted Path: The shortest weighted path discovers the path between two vertices in a graph such that the total sum of the edges weights is the min

### Shortest Weighted Path Search Optimizations

Optimizations include:

- Lowest cost optimization: The lowest cost optimization excludes an edge if the edges destination is reachable via a lower cost path
- Supernode avoidance: Supernode avoidance excludes a vertex if its degree would increase the search space complexity over a threshold
- Global heuristic: A global heuristic excludes an edge if the edges weight causes the paths total weight to exceed a threshold

### Supernodes in graphs

Vertex with an extremely high number of edges

- Supernode: A supernode is a vertex with a disproportionately high degree

### Normalization of Edge Weights for Shortest Path Problems

### Normalizing the Edge Weights

- 1. Shift the scale to the interval [0, 1]
- 2. Frame the new scale as a shortest path problem
  - Use logarithms so that multiplication becomes addition
  - Multiply the result by -1 so that the max becomes a min
- 3. Decide how to handle modeling infinity

### Updating Our Graph

### Exploring the Normalized Edge Weights

### Some Thoughts Before Moving On to Shortest Weighted Path Queries

## Shortest Weighted Path Queries

- sideEffect(): The sideEffect() step allows the traversers state to proceed unchanged to the next step, but with some computational value from the provided traversal

## Weighted Paths and Trust in Production
