# Chapter 11. Whats Next: Graph Analytics, Machine Learning, and Resources

Graph analytics and ml are two of the most common areas where exploration of graphs might take you next

## 11.1 Graph analytics

Thus far, only simple transactional questions with limited scope:

- Who are the friends of my friends?
- What are the newest reviews for this rest?

As opposed to:

- Who is the most connected person in my graph?
- Which person is the most centrally located?

For these, need to investigate most or all of the data in the graph

Algorithms that require using most or all of the data in our graph fall into a category of problems that use algorithms known as graph analytics

- fraud detection
- supply chain optimization
- epidemic migration prediction

### Graph analytics and graph databases

There are many frameworks and databases built specifically to perform these computationally intensive calculations. They have optimizations specifically tailored to performing the long running computations that most of the algorithms require

- AnzoGraph
- Apache Giraph

### 11.1.1 Pathfinding

Used analytically to explore the routes between vertices to identify optimal paths in a graph

Use cases:

- Direction finding - grographic mapping tools
- Optimization problems - pathfinding algs can optimize various problems that deal with a large number of interdependent entities, from managing supply chains to optimizing financial trades to determining bottlenecks and points of failure in computer networks
- Fraud detection - many fraud detection algorithms use cycle detection finding groups of entities that connect to themselves, to look for closely connected subgraphs as a measure of potentially fraudulent accounts

Most common pathfinding algs use shorted path algorithms. There are two fundamental approaches:

- Unweighted approach treats all paths as equal, calculating the shortest path based on the number of edges traversed.
- Weighted approach assigns relative weights to all paths, and these weights are then used in the computation

#### Unweighted shortest path algorithm

Great choice when the relative cost of traversing all edges is the same or is not a concern

Social networks are a great example of use case

Each friend connection is equal to every other friend connection

#### Weighted shortest path algorithm

In many scenarios, the relative cost, or weight, of moving from one vertex to another differs - goal is to find the overall relative cost

### 11.1.2 Centrality

Use centrality to identify the importance of a vertex within a graph

Invented for social network questions, but have many other applications:

- Finding the most critical components in a computer network that can cause the most disruption if lost
- Finding the importance of a person within an organization
- Estimating the optimal timing and routing for telecomm packets
- Finding outliers in a graph as a measurement of likely fraud

#### Degree

Degree - number of incident edges associated with a vertex, so degree centrality ranks vertices based on their edge count

Can be further broken down by measuring the:

- in degree
- out degree

Often used as a baseline for determining how connected a graph is, especially when calculating the mean, min, and max values

#### Betweenness

Betweenness centrality is a calculation of the number of times a vertex is used in the shortest path between all pairs of nodes in the graph

Betweenness centrality is effective at finding the critical points that connect different groups of vertices. The larger the number, the more important the vertex

#### Closeness

Closeness centrality is a measurement of the average length of the shortest path from a vertex to all other vertices, indicating which vertices are the most centrally located with respect to all other vertices. The smaller the returnn value, the more important the vertex

#### Eigenvector

Eigenvector centrality is a complex measurement of a centrality that uses the relative importance of the adjacent vertices as an input to calculate the importance of a given vertex

Just because a vertex is connected to many other vertixes does not necessarily mean it is important. Instead, the importance of the vertexs neighbors is used to compute a vertexs overall significance

If a vertex has many adjacent vertices, but those vertices are relatively unconnected, then it receives a lower score than a vertex with fewer adjacent vertices, each of which is highly connected

#### Pagerank

Works similarly to eigenvector centrality, as it uses the relative importance of the adjacent vertices to aid in determining the overall importance of a vertex. But it also includes a dampening value (commonly set to .85) to indicate a diminishing of the influence as the network is traversed. The higher the PageRank return value for a vertex, the more important the vertex

#### Centrality Comparisons

### 11.1.3 Community Detection

We use community detection algorithms to uncover groups or communities of vertices that are tightly connected to one another but loosely connected to other vertices within the graph

Some other use cases:

- Finding communities of potentially similar accounts within an e-commerce site to find distinct families within the graph
- Identifying potential fraud by looking for tightly connected components such as groups of accounts known to commit deceptive activities
- Identifying similar groups of users to provide product recommendations

Two most common

#### Triangle counting

Find communities by finding the groups of people who all know each other

Count the number of triangles within a given subset of nodes

Useful in capturing how cohesive or how closely related the network of vertices are in a graph. Graphs that contain closely associated networks or communities have a higher triangle count, and grpahs with loosely connected networks have a lower triangle count

#### Connected components

Instead of triangle counting, what if we want to find groups of people who are well-connected to one another, but who are not connected to other groups?

In graph theory, any subgraph in which every vertex has a path to every other vertex in the subgraph is known as a component. The connected components alg finds all these components within a graph

Connected components discover clusters of related data within a global graph, which can be helpful in finding items such as families within a social graph or groups of associated or possibly duplicate accounts within an e-commerce site. It does not consider the direction of the edges between the vertices, so it iss known as a weakly connected components algorithm

Strongly connected components take into acount direction (bidirectional)

### 11.1.4 Graphs and Machine Learning

While ML uses graphs to accomplish learning, these:

- dont allow for graphs as input
- doesnt provide graphs as an outputs

How does the flexible data structure of a graph get applied to the rigid data structure of an ML model?

- feature extractions
- graph embeddings

#### Feature Extractions

Often the simplest method for using graphs in ML is to extract features

- Shortest path - takes the shortest path between a person and a known bad actor as a predictive measurement for a fraudulet ML model
- Triangle count - uses a triangle count in a social network to determine how social or anti-social a particular user might be
- Degree - uses the degree of connections of a vertex to determine how critical a sensor is within a sensor network

#### Graph embedding

Graph embeddings turn sparse data into much more compact vector representations

Much of the research in this area is driven by work done in NLP, it is now being applied more generically to graphs to provide inputs into tasks such as predicting new friendships and finding fraudulent activity. Graph embeddings tend to come in one of two forms:

- Vertex embeddings - represents each vertex as a single vector/matrix. Used to compare items on a vertex level
- Graph embedding - represents the entire graph/subgraph as a single vector/matrix. Used to compare entire graphs against one another

Vector operations are more simple and faster

### 11.1.5 Additional resources

- Graph theory
  - Sarada Herke, Graph Theory Channel (YouTube)
  - Richard J. Trudeau, Introduction to Graph Theory (math focused)
  - Douglas B. West, Introduction to Graph Theory (deep mathematics)
- Graph databases
  - Ian Robinson, Graph Databases (go to book for neo4j)
  - Denise gosnesll and Matthias Broecheler, The Practicioners Guide to Graph Data (more focused on concepts than language syntax)
- Graph data sets
- Graph algorithms

## Summary

- We use pathfinding algorithms, such as unweighted or weighted shortest path, to describe the connectedness within a graph
- We use centrality algorithms such as degree, betweenness, closeness, eigenvector, and PageRank to describe how important or influential a vertex is within a graph
- The output of centrality algorithms can vary significantly, so understanding how each one works is important to selecting the appropriate one for your use case
- We use community detection algorithms such as triangle counting, connected components, and strongly connected components to detect unique clusters (or communities) of highly connected vertices within a graph
- Graph features such as shortest path, PageRank, and triangle count can be extracted from a graph to use as input into a feature set in ML
- Graph embeddings are a mechanism that represents the sparse multi-dimensional structure of a graph as a vector or matrix
