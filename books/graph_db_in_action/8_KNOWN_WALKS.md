# Chapter 8. Building Traversals Using Known Walks

## 8.1 Preparing to develop our traversals

Need two things:

- requirements of our use case
- need graph data model

Use cases:

- What rest near me with a specific cuising is the highest rated?
- What are the ten highest-rated rest near me?
- What are the newest reviews for this rest?

### 8.1.1 Identifying the required elements

three questions in our use case:

- 1. Examine each requirement and break it into the components needed to answer the question
- 2. Identify the required vertex labels
- 3. Identify the required edge labels

What we have/need:

- rest - the core piece of information returned
- city
- cuisine
- review

Note: pronouns are easily overlooked when translating business questions into technical requirements and implementation. These tend to hide additional and more subtle requirements. Pay attention to pronouns when identifying required elements. In the current example, note how we called out the phrase "near me" (with an emphasis on "me" as an example of a potentially hidden element)

Edges:

- rest-within-city
- rest-serves-cuising
- review-about-rest
- person-lives-city

Next vertexes:

- rest
- person
- city
- review

Edges:

- rest-within-city
- person-lives-city
- review-about-rest

### 8.1.2 Selecting a starting place

### 8.1.3 Setting up test data

## 8.2 Writing our first traversal

- 1. id vertex labels and edge labels required to answer the question
- 2. find the starting location for the traversal
- 3. find the end location for the traversal
- 4. write out the steps in plain english
- 5. code each step, one at a time

### 8.2.1 Designing out traversal

### 8.2.2 Developing the traversal code

#### Extending our traversal with the id

Using the internal id results in a leaky abstraction that tightly couples application logic to the underlying database implementation

#### Adding this traversal to our application

## 8.3 Pagination and graph databases

- `.range(startNumber, endNumber)`

### Importance of Ordering Inputs before calling range

Like the reason we sort sets before iterating

### Ordering is an expensive operation

When adding pagination, need to make the following changes:

- 1. replace the limit() step with a range() step
- 2. define a limit variable with a value of 3
- 3. define an offset variable and increment it by the limit value for each call

```gremlin
g.V().has('rest', 'rest_id', rid).
  in('about').
  order().by('created_date', decr).
  range(offset, offset+limit)
```

## 8.4 Reccomending the highest-rated rest

### 8.4.1 Designing our traversal

### 8.4.2 Developing the traversal code

- `.mean()` - aggregation to compute the mean or average of a set of values. most commonly used in the `.group().by().by()` step pattern

#### Troubleshooting errors while developing a traversal

#### Mid-traversal filtering

Want to filter out rest that dont have ratings, which is to say, do not have any `about` edges

- `.where(traversal)` - filters incoming objects based on a traversal and only passes through objects when the traversal returns a result

.has() is still the primary go-to filtering step

- `.identity()` - takes the element entering the step and returns that same element unaltered

#### Porjecting key-value pairs

#### Adding the traversal to our application

## 8.5 Writing the last recommendation engine traversal

## Summary

- Start developing traversals for a use case by identifying the vertices and edges required to answer the business question
- Develop known-walk traversals starts with identifying the relevant portions of the schema, finding the starting and ending points for the traversal, identifying the series of vertices and edges needed to traverse from the starting to the ending points, and finally, composing the traversal by iteravely adding steps while validating the results against test data as we build each step
- A good starting point for a traversal minimizes the number of starting vertices, ideally to a single vertex. To do this, apply all possible filtering at the start of the traversal
- Prioritization of which use case questions to start on be done by either choosing the hardes question if we want to de-risk the use of graph tech, or the simplest question if we want an early win as a building block for future success
- Using a systematic, step-by-step approach to building traversals makes it easier to id the source of a problem if an error is encountered. Troubleshooting any errors can involve multiple steps, including investigating the data, changing the approach to the traversal, and consulting with other staff or online resources
- Paging results in a graph traversal requires an ordered result set and the use of limits and offsets to specify the desired subset of results
- Grouping and ordering traversals create results that are key-value pairs. Further processing key-value pairs uses special overloads of the select() step to work with the key and value portions of the pair
