# Chapter 7. Advanced Data Modeling Techniques

- Increasing performance with generic data labels
- Simplified traversals by moving properties to edges
- Creating more efficient traversals with data denormalization

## 7.1 Reviewing our current data models

Builtt model with 4 step process:

- 1. Defining the problem
- 2. Creating the conceptual data model
- 3. Creating the logical data model
- 4. Testing the model

## 7.2 Extending out logical data model

Needs to support answering the following questions:

- What resturaount near me with a specific cuisine is the highest rated?
- What are the ten highest-rated resturaunts near me?
- What are the newest reviews for this restaraunt

### Known walk

In graph theory, a walk is a sequence of edges and verteces. Same as a path, but a path is a specific type of walk, which only contains distinct vertices. A known walk is a pattern in graph applicatinos where we have prior knowledge of the exact series of vertices and edges to traverse to get our answer

In pathfinding problems, we know the series of vertices and edges to traverse, but we do not know the number of times we must traverse these.

In known-walk problems, on the other hand, we know the series of vertices and edges to traverse and the number of times we need to traverse them

Prior knowledge about the depth of the traversal is one of the factors differentiating between the two patterns, pathfinding and known walks.

To decide if a traversal is a known walk, we use the following two questions:

- Do we know the exact definition of the steps (e.g. entities and relationships) needed to traverse from the starting vertex to the ending vertex
- Do we know the number of times we need to traverse these steps to get our results?

If yes, the traversal is likely a known walk

## 7.3 Translating entities to vertices

### 7.3.1 Using generic labels

#### Labeling with contact types

- `.union(traversal, traversal, ...)` - process each traversal separately and outputs the combined results as a single result set

Ex. "What are all the contact methods for Ted?

```gremlin
g.V().has('person', 'name', 'Ted').
union(
    out('has_phone').values('number'),
    out('has_email').values('address'),
    out('has_fax').values('number')
)
```

A union() step is a branching step that requires that the current traverser be copied to each branch of the union() in order to run. This means our final two traversals require three copies of the traverser in order to continue processing. In small graphs not a big issue but def snowballs

While it mmight be tempting to create a simple edge label called has or has_a to simplify our model, the reality is that labels such as these are too generic to provide any useful information

#### Labeling for recommendation engine vertices

### 7.3.2 Denormalizing graph data

Copying data into multiple locations at write time to increase performance at read time

Downsides:

- Increased disk usage
- Data synch issues (every time a value changes, it needs to be updated)
- Reduced write performance

Note: indexing is a form of denormalization

#### Using precalculated fields

#### Using duplicate data

If we expect to retrieve orders by ID frequently, to avoid overhead, can copy the order_date onto the placed edge and the order vertex

#### Evaluating the diningbyfriends logical model for denormalization

### 7.3.3 Translating relationships to edges

Required relationships:

- person-writes-review
- person-lives in-city
- review-are about-resturaunt
- rest-serves-cuising
- rest-within-city
- city-within-state

Edges:

- write
- about
- serves
- lives
- within

### 7.3.4 Finding and assigning properties

### 7.3.5 Moving properties to edges

Move a property from a vertex onto the incident edge to reduce the number of steps your traversal needs to process

While we use a single out() steps to do this, we think of it as as single operation. But in reality the out() step is effectively an alias for the outE().inV() combination

### 7.3.6 Checking out model

- Do the vertices and relations read like a sentence
- Do we have different vertex or edge labels with the same properties
- Does the model make sense

## 7.4 Extending our data model for personalization

## 7.5 Comparing the results

## Summary

- Generic data labels allow us to reuse labels to simplify our traversals by enabling us to group similar entities so that we create more prformant and scalable traversals
- Denormalizing data through precalculating fields or duplicating data reduces the complexity of our traversals by making the data available earlier in our traversal
- Precalculating fields is a great choice when the field to be calculated when read much more frequently than written
- Data duplication involves copying properties into multiple locations in our graph to optimize for multiple different traversal paths at the expense of keeping data in sync
- Moving properties from vertices to edges can reduce the complexity of our traversals by reducing the number of steps our traversal has to perform
- Applying these advanced modeling techniques allows us to create complex data models for real-world situations such as reccomendation and personalization use cases
