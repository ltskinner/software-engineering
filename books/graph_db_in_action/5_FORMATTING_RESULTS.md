# 5. Formatting Results

Generally best to do as much data processing as possible at the database layer

## 5.1 Review of values steps

Most traversal examples return the ID of the elements

We rarely want to return jsut the ID. In most cases we aim to return all or a subset of the properties

- `.values(property_name)`
- `.valueMap()`

```gremlin
g.V().hasLabel('order').out('contains')
```

## 5.2 Constructing our result payload

To return both the order and product vertices, we use an alias on the order vertices

An alias in a graph database is a labeled reference to a specific output of a step, either a vertex or an edge, that can be referenced by later steps. In our order-processing graph, the steps to get a combined order/product result are as follows:

- find all the order vertices in the graph
- give these an alias labeled O
- traverse out the contains edge to the product vertices
- give these an alias labeled P
- return all the properties from the elements labeled O as well as all the properties from the elements labeled P

### 5.2.1 Applying aliases in Gremlin

#### Aliasing elements mid-traversal using `as()`

`g.V().hasLabel('table').as('alias_name')`

```gremlin
out().as('f').
out().as('foff)
```

#### Returning aliased elements

To return aliased elements, lets turn to a new gremlin step:

- `select(string[])` - selects aliased elements from earlier in the traversal. This step always looks back to previous steps in the traversal to find the aliases

Modifiers:

- `by(key)` - specifies the key of the property to return from the corresponding aliased element
- `by(traversal)` - specifies the traversal to perform on the corresponding aliased element

```gremlin
out().as('foff').
select('f', 'foff').
  by('first_name').
  by('first_name')
```

Best practice to pair the `as()` with same number of `by()` statements

### 5.2.2 Projecting results instead of aliasing

Sometimes, instead of looking back in the traversal for earlier results, it is preferable to project results forward from the current elements. Projecting results differs from retrieving the previous results in a simple, but somewhat subtle way. When we retrieve (or select) data, we can only get informatino that we already traversed and aliased. When we project results, *we create new results*, possibly branching to items not yet traversed.

- Selection is the process of working with vertices, properties, or additinoal traversal expressinos to return results from previously labeled steps. Selection always looks back to earlier parts of the traversal
- Projection is the process of working with vertices, properties, or additional traversal expressions to create results from the input to the current step. Projection always moves forward, taking the incoming data as the starting point

Example differences:

- Were no longer aliasing elements as we traverse these
- We dont have to traverse back out to the contains edge a second time

Step:

- `project(string[])`

```gremlin
g.V().hasLabel('person').
  project('name', 'degree').
    by('first_name').
    by(bothE().count())
```

In this traversal, instead of specifying a property name in the second by() statement, we specify additinoal traversal steps. This takes the incoming elements (in this case the product vertex) and then performs additional traversal steps from that point in the graph. This ability to specify additinoal traversal steps within a by() step isnt unique to project(). We can specify these sub-traversals with either a select() or other Gremlin steps. This is quite powerful - the ability to do complex operations within a traversal or steps within steps

- Selection uses the select() step to create a result set based on previously traversed elements of a graph. To use the select() step, we alias each of the elements with the as() step for later use
- Projection uses the project() step to branch from the current location within the graph and creates new objects. In our present example, we had one element remain static, the persons name, but we needed the other elements to be calculated through further traversing of the graph to return the number of friends

## 5.3 Organizing our results

Most common requirements for organizing our result data:

- Ordering the results
- Grouping the results
- Limiting the size of the results

### 5.3.1 Ordering results returned from a graph traversal

- `.order()` - collects all objects up to this point of the traversal into a list, which is ordered according to the accompanying by() modulator

```gremlin
g.V().hasLabel('persson').values('first_name').
  order().
    by(decr) //shuffle works too
```

### 5.3.2 Gouping results returned from a graph traversal

- `.group()` - groups the results based on the specified by() modulator. Data is grouped by using either one or two by() modulators. The first one specifies the keys for the grouping. The second one, if present specifies the values. If not present, the incoming data is collected as a list of the values associated with the grouping key
- `.groupCount()` - groups and counts the results based on the specified by() modulator. it takes on by() modulator to specify the keys. the values are always aggregated by the count() step
- `unfold()` - unrolls an iterable or map into its individual components

```gremlin
g.V().has('person', 'first_name', 'Dave').
  both().
  both().
  groupCount().
    by('first_name').
    by(count()).
  unfold()
```

### 5.3.3 Limiting results

- `.limit(number)` - returns the first number of results
- `.tail(number)` - returns the last number of results
- `.range(startNumber, endNumber)` - returns the results from startNumber (inclusive, zero-based) - to endNumber (not inclusive)

## 5.4 Combining steps into complex traversals

"What three friends of friends of Dave have the most connections?"

```gremlin
g.V().has('person', 'first_name', 'Dave').
  both().
  both().
  groupCount().
    by('first_name').
  unfold().
  order().
    by(values, desc).
    by(keys).
  project('name', 'count').
    by(keys).
    by(values).
  limit(3)
```

## Summary

- By default, properties arent returned from graph elements, so we must explicity ask for those. In Gremlin, we use steps such as values() and valueMap() to retrieve the values in the desired form
- Aliases in the traversal allow for referencing results from earlier steps in later steps, supporting composition of powerful traversals
- Selecting and projecting steps create complex results from multiple vertices or edges, allowing for the composition of intricate result structures
- Selection creates a result set based on previously traversed elements of a graph. To use the select() step, we alias with the as() step elements for use in later steps
- Projection operates from the current location within the graph and creates new objects with either static or calculated properties
- Ordering, grouping, or counting by group are common ways to transform results using the order(), group(), and groupCount() steps
- The limit() step limits the number of results, the tail() step returns the last X records, and the range() step allows for result pagination
- Combining different steps performs complex manipulation and transformation of traversal results in the db prior to returning the results to a client. Used appropriately, this improves performance in the database, across the network, and in the application itself
