# 2. Graph Data Modeling

4 step process to graph data modeling

## 2.1 The Data Modeling Process

High level:

- identifying and understanding the problem
- determinging the entities and relationships in that problem
- creating representation of that problem in the database

Big thing is to have an "entity AND relationship first" mindset

### 2.1.1 Data Modeling Terms

- Entity
  - commonly represented by nouns
  - describe things or type of thing
  - become vertex
- Relationship
  - verbs
  - how entities interact
  - become edges
- Attribute
  - like entities, also represented by a noun, but always in the context of an entity or relationship
  - **limit use of attributes cause can detract from omre critical parts of model**
- Access pattern
  - questions or methods of interaction in the domain
  - often become queries in logical model and implementation

Define your queries before the data model, like you need to know your use case before you do the dog n pony show

Approach here is designed to reduce risk and minimize data model changes

### 2.1.2 Four-step process for data moseling

- 1. Understand the problem
- 2. Create a whiteboard or conceptual model
  - codifying main entities and relationships
  - focused on the business perspective
- 3. Create logical data mosel
  - define vertices and edges, and specifying properties on those
- 4. Test the model
  - validate coherence of previous steps
  - "does this make sense"
  - "did we leave anything out"

## 2.2 Understand the Problem

### 2.2.1 Domoain and scope question

Boundary definitions, limit scope lol

- What will the app do for its users?
- What types of information does the application need to record to perform these tasks?
- Who are the users of our application?

### 2.2.2 Business Entity Questions

Goal is to identify the fundamental building blocks of our application, and how these things are related to one another

- What sort of items or things does the application utilize?
- How do these items interact with one another?
- What are the critical pieces of data you need to know about each entitiy?

### 2.2.3 Functionality Questions

Questioning how business entities interact produces relationshipg between entities

- How are people going to use the system?

## 2.3 Developing the whiteboard model

The first tangible picture of the system

### 2.3.1 Identifying and grouping entities

As a best practice, we should make all the names of our entities `singular`

Looking for `Nouns`

### 2.3.2 Identifying relationships between entities

Instead of looking for nouns, looking for `Verbs`

## 2.4 Constructing the logical data model

- 1. Translate entities to vertices
- 2. Translate relationships to edges
- 3. Find and assign properties to vertices and edges
- 4. Check your model

### 2.4.1 Translating Entities to Vertices

- Finding the conceptual entities
- Naming the vertex labels

### 2.4.3 Translating relationships to edges

- 1. Identifying the relevant relationships from the conceptual data model
- 2. Naming the edge in the form of a label to uniquely identify that relationsihp in our graph data model
- 3. Assigning a direction to the edge by defining the start and end vertex types
- 4. Specifying the uniqueness of the edge by deciding on the number of times this edge can exist between two specific instance vertices

Look at the functional questions list to guide

an edge that returns to source node is called a loop - this is fine

the direction of an edge should complement the edge label to make a sentence that sounds natural (and fits the needs of the use case)

play around with inverting and changing wording of edge

Uniqueness:

- describes the number of times an instance of a vertex is related to another instance of a vertex with an edge having the same label
- describes what is an allowable number of edges of a given label between two vertices
- the allowable number of edges of a given label between two vertices

#### Why uniqueness and not cartinality or multiplicity

The term cardinality is often used (wrongly) to refer to a many-to-many or one-to-many relationships

- Cardinality - the number of elements in a set
- Multiplicity - a specification of the maximum and minimum cardinality that set can have (like one-to-many, zero-to-many, many-to-many)

In our context, we are describing the characteristics of a group of edges - not a single edge

Data uniqueness describes the measure of duplication of identified data items within a data set - define uniqueness as the allowable number of edges of a given label between two vertices

Single uniqueness: there can only be one of a given edge label between two instance vertices

Multiple uniqueness: is like a collection, there can be one or more of the given edge label between two instance vertices

Single uniqueness is significantly more common than multiple uniqueness. As a rule, assume single uniqueness and think about multiple uniqueness only when there is a specific requirement dictating multiple instances of the same edge between two vertex instances

Improper uniqueness usually appears in one of three ways:

- Too little data returned
- Duplicated data returned
- Poor query performance

`IMPORTANT` - incorrect edge uniqueness is one of the most common problems in graph data modeling, and it is frequently a root cause of query issues

- First symptom of incorrect uniqueness is that too little data is returned from a query
- Second symptom is having duplicated data returned, occurs when we have multiple uniqueness edges but should only have one
- Third symptom

### 2.4.3 Finding and assigning properties

Default and null values in graph databases? app doesnt insert default or null values for graphs, unlike RDBMS where you need to have the right structure

Before assignging properties, ask:

- What properties are required
- How are we going to name them
- What is their data type

Some graphs are schemaless, some require a schema. For required schema, need to work with mechanics of schema definition to slam it in there

## 2.5 Checking our model

Questions:

- Do the vertices and edges read like a sentence? Yes
- Do I have different vertex or edge labels with the same properties? No
- Does my model make sense? Yes

## Summary

- Strong, early investment in understanding the problem, use cases, and common domain terminology are the foundation of building a good data model. Reduces risk of radical change later
- A conceptual data model provides an overarching view of the scope, entities, and application functionality from the pov of a business user
- Translating a conceptual data model to a logical data model requires four steps: translate entities to vertices, translate relationships to edges, assign properties, check the model
- Translating entities to vertices involves identifying the required conceptual entities, creating corresponding vertices, and providing those vertices with a label that is concise, descriptive, and generic
- Translating relationships to edges consists of identifying the required conceptual relationships, creating the corresponding edges, labeling each edge, assigning a direction to each edge, and determining the edge uniqueness
- Edge uniqueness defines the number of times an instance of a vertex can relate to another instance of a vertex with an edge with the same level. Incorrectly identifying edge uniqueness is a common problem in graph data modeling, which causes data and performance issues
- To validate a graph data model, verify against the requirements and conceptual model, check that the vertex and edge labels reqd like a sentence, and ensure that the model does not have duplicated edge or verte types. Finally, perform a "gut-check" to see that tht model makes sense
