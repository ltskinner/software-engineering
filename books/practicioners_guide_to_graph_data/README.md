# The Practicioners Guide to Graph Data

*Applying Graph Thinking and Graph Technologies to Solve Complex Problems*

[https://www.amazon.com/Practitioners-Guide-Graph-Data-Technologies-ebook/dp/B086BY8YQB/](https://www.amazon.com/Practitioners-Guide-Graph-Data-Technologies-ebook/dp/B086BY8YQB/)

[Github Repo](https://github.com/datastax/graph-book)

## [Chapter 1. Graph Thinking](./1_GRAPH_THINKING.md)

## [Chaptr 2. Evolving from Relational to Graph Thinking](./2_REL_TO_GRAPH.md)

## [Chapter 3. Getting Started: A Simple Customer 360](./3_GETTING_STARTED.md)

We like to think of querying a graph database, loosely, as the reverse of a SQL query.

- Relational sequence: `SELECT`-`FROM`-`WHERE`
- In graph, follow in reverse: `WHERE`-`JOIN`-`SELECT`

## [Chpapter 4. Exploring Nieghborhoods Development](./4_NEIGHBORHOODS.md)

Edges are the most important piece of the graph model. Edges are why you need graph technology in the first place

Map: Verbs to Edges, Nouns to Vertices. Think about Vertex-Edge-Vertex in terms of subject-verb-object

Rules of Thumb:

- 1. If you want to start your traversal on some piece of data, make that data a vertex
- 2. If you need the data to connect concepts, make that data an edge
- 3. Vertex-Edge-Vertex should read like a sentence or phrase from your queries
- 4. Nouns and Concepts should be vertex labels. Verbs should be edge labels
- 5. When in development, let the direction of your edges reflect how you would think about the data in your domain
- 6. If you need to use data to subselect a group, make it a property
- 7. Properties can be duplicated onto edges or vertices; use denormalization to reduce the number of elements you have to process in a query
- 8. Let the direction you want to walk through your edge labels determine the indexes you need on an edge label in your graph schema
- 9. Load your data; then apply your indexes
- 10. Keep only the edges and indexes that you need for your production queries
- 11. Time goes up onthe way up, and time goes down on the way down. When this rule of thumb isnt true, the path is invalid and should be filtered out of the results
- 12. Cluster your edges on disk so that you can sort through them in your queries and mitigate the effect of your datas branching factor

Pitfalls in Naming Conventions:

- 1. Using the word `has` as an edge label
- 2. Using the word `id` sa a property
- 3. Inconsistent use of casing
  - Capital `CamelCase` for vertex labels
  - Lowecase `snake_case` for edge labels, property keys, and example data

Note: If you could understand one concept about graph data modeling:

- Modeling data as a graph is just as much an art as it is engineering
- The art of the data modeling process involves creating and evolving your perspective on your data
- This evolution translates your mindset into the paradigm of relationship-first data modeling

When modeling cases, ask the following questions:

- 1. What does this concept mean to the end user of the application?
- 2. How are you going to read this data in your application?

Advice:

- 1. Focus on the data you have. It is easy to boil the ocean by modeling your industries entire graph problem - acoid this rabbit hole.
- 2. Second, apply the practice of query-driven design. Build your data model to accomodate only a predefined set of graph queries.
- 3. Consider what the data means to your end user

Spend time designing your data architecture, models and queries to present information that is most meaningful to them

Tip: If you ever question what object type you have in the middle of developing a gremlin traversal, add `.next().getClass()` to where you are in the traversal, this will inspect the objects

## [Chapter 5. Exploring Neighborhoods in Production](./5_NBHOODS_IN_PRODUCTION.md)

Cassandra stuff

## [Chapter 6. Using Trees in Development](./6_TREES.md)

## [Chapter 7. Using Trees in Production](./7_TREES_PRODUCTION.md)

## [Chapter 8. Finding Paths in Development](./8_PATHS.md)

## [Chapter 9. Finding Paths in Production](./9_PATHS_PROD.md)

## [Chapter 10. Recommendations in Development](./10_RECS_IN_DEV.md)

Types of recommender systems:

- Content-Based: Focused only on the preferences of the user
- Social Data Mining: Systems that do not need input from user. Only on popular historical trends
- Collaborative Filtering: Type of rec system that predicts new content (filtering) by matching the interests of the individual user with the preferences of many users (collaborating)
  - User-Based
  - Item-Based
  - Hybrid Models
- Hybrid Models (not a dupe)

## [Chapter 11. Simple Entity Resolution in Graphs](./11_ENTITY_RESOLUTION.md)

## [Chapter 12. Recommendations in Production](./12_RECS_IN_PROD.md)

## [Chapter 13. Epilogue](./13_EPILOGUE.md)
