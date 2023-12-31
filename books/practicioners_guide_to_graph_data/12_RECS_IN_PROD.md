# Chapter 12. Recommendations in Production

We dont think a user of Nikes apparel app is going to wait the multiple seconds required to process and end-to-end NPS inspured collaborative-filtering graph query. And neither should you

Instead, we encourage you to think like a production engineer. Set up procedures that prioritize the end users in-app experience and then figure out how to connect a longer running query

## Shortcut Edges for Recommendations in Real Time

### Where Our Development Process Doesnt Scale

- branching factor
- supernodes

### How We Fix Scaling Issues: Shortcut Edges

Shortcut edges are one of the most popular tricks

- Shortcut edge: A shortcut edge contains precomputed results of a multi-hop query from vertex a to vertex n to be stored as an edge directly from a to n

### Seeing What We Designed to Deliver in Production

### Pruning: Different Ways to Precompute Shortcut Edges

The main tricks when using shortcut edges come down to what and how often you precompute the aggregations they hop over

There are three ways to limit the total amount of data that is considered for a shortcut edge:

- total score
- total number of results
- domain knowledge expectations

#### Pruning by score thresholds

- predefined score threshold
- only include a shortcut edge for a rec if the score you calc is above some threshold

#### Pruning with hard limits on total recommendations

- deifne total number of edges you are going to include in production
- like, say only keep highest 100 rec scores

More popular than score thresh. Easier to readon about effects, can pre-calc total amount of disk space required

#### Pruning by applying domain knowledge filters

### Considerations for Updating Your Recommendations

Computing a shortcut edge across all your users ratings is very expensive. Will need to reduce the scope of how often your team does these calcs. Three tips:

- 1. Updating the shortcut edges only for the content that has changed
- 2. Building data pipelines that account for successful recommendations
- 3. Creating robust computational processes (decompose and harden subroutines)

## Calculating Shortcut Edges for Our Movie Data

### Breaking Down the Complex Problem of Precalculating Shortcut Edges

Use parallelism

### Addressing the Elephant in the Room: Batch Computation

## Production Schema and Data Loading for Movie Recommendations

## Recommendation Queries with Shortcut Edges

### Understanding Response Time in Production by Counting Edge Partitions

### Final Thoughts on Reasoning about Distributed Graph Query Performance

- Partitions
- Connectivity
