# Chapter 2. Evolving from Relational to Graph Thinking

Three core questions:

- 1. Is graph technology better for my problem than relational technology?
- 2. How do I think about my data as a graph?
- 3. How do I model a graphs schema?

## Chapter Preview: Translating Relational Concepts to Graph Terminology

## Relational vs Graph: Whats the Difference

## Relational Data Modeling

### Entities and Attributes

- Entity - an entity is an object such as a person, place, or thing that you need to track in your database
- Attribute - An attribute refers to a property of an entity such as names, dates, or other descriptive features

## Concepts in Graph Data

### Fundamental Elements of a Graph

- Graph - A graph is a representation of data with two distinct elements: vertices and edges
- Vertex - A vertex represents a concept or entity in data
- Edge - An edge represents a relationship or link from one vertex to another

Note, this book avoids the term nodes because node is overloaded in distributed systems, graph theory, and cs generally

### Adjacency

The mathematical term used to describe whether vertices are connected to each other. Formally:

- Adjacency - Two vertices are adjacent if they are connected by an edge

### Neighborhoods

Data that is connected forms communities

- Neighborhood - For a vertex v, all vertices that are adjacent to v are said to be within the neighborhood of v, written N(v). All vertices within a neighborhood are neighbors of v

The *second neighborhood* consists of those vertices that are two edges away

### Distance

Another way to talk about the connectedness of this sample data is to say how many steps it takes to walk from one vertex to another

- Distance - In graph data, distance refers to the number of edges that you have to walk through to get from one vertex to another

### Degree

For many applications, it is expecially useful to understand *how well* a piece of data is connected to its neighbors

- Degree - A vertex's degree is the number of edges that are incident to (i.e., touch) the vertex

We also break down a vertex's degree into two subcategories according to whether the edge starts or ends with that particular vertex

- In-degree - A vertex's in-degree is the total number of incoming edges that are incident to the vertex
- Out-degree - A vertex's out-degree is the total number of outgoing edges that are incident to the vertex

#### Implications of vertex degree

## The Graph Schema Language

### Vertex Labels and Edge Labels

- Vertex label - A vertex label is a set of objects that are semantically homogeneous. Taht is, a vertex label represents a class of objects that share the same relationships and attributes
- Edge label - An edge label names the type of relationship between vertex labels in your db schema

The terms vertices and edges are used in reference to data. To describe a databases schema, we use the terms vertex labels and edge labels

### Properties

- Property - A property describes features of a vertex label or an edge label, such as names, dates, or other descriptive features

### Edge Direction

Two ways can model:

- Directed - A directed edge foes one way: from one vertex label to the other vertex label
- Bidirectinoal - A bidirectional or bidirected edge goes in both directions between the vertex labels

Loosely speaking, the identification of the subject, predicate, and object of your description creates an edge labels direction

The subject is the first vertex label and is where an edge starts - this is a domain. The object of the destination or range of an edge label

- Domain - The domain of an edge label is the vertex label from which the edge label originates or starts
- Range - The range of an edge label is the vertex label to which the edge label points or ends

### Self-Referencing Edge Labels

If an edge starts and ends on the same vertex label, we say it is self referencing

- Self-referencing - A self-referencing edge label is where the edge labels domain and range are the same vertex label

### Multiplicity of Your Graph

- Multiplicity - Multiplicity is a specification of the range of allowable sizes that a group may assume. Namely, multiplicity describes the range of allowable sizes that the group of vertices adjacent to a given vertex along a particular edge label may assume

#### Modeling multiplicity in the GSL

- Set - A set is an abstract data type that stores unique values
- Collection - A collection is an abstract data type that stores nonunique values

The most likely occasion for needing to decide about the multiplicity type is when you are modeling time on your edges. Do you want only the most recent edge in your database? Then you are thinking of your edge as a set. Do you want all of your edges over time? Then you are thinking of your edges as a collection

## Relational Versus Graph: Decisions to Consider

### Data Modeling

Use Graphs if the relationships between your entities are the most important features of your data
