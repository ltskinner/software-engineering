# Chapter 6. Using Trees in Development

- Hierarchical data: Hierarchical data represents concepts that naturally organized into a nested structure of dependencies

## Seeing Hierarchies and Nested Data: Three Examples

### Hierarchical Data in a Bill of Materials

### Hierarchical Data in Version Control Systems

Legit Git lmao

### Hierarchical Data in Self-Organizing Networks

- family trees
- corporate hierarchies

### Why Graph Technology for Hierarchical Data

Graph tech enables a more natural way to represent the nested relationships within data

Example convo: some team "translated 150 lines of a query on top of HBase into 20 lines of Gremlin"

## Finding Your Way Through a Forest of Terminology

### Trees, Roots, Leaves

- Tree - connected graph with no cycles (standard top down)

Two special types of vertices:

- Parent vertex: A parent vertex is one step higher in the hierarchy
- Child vertex: A child vertex is one step below a parent in the hierarchy

How roots and leaves fit in:

- Root: A root is the topmost parent vertex; a root is the beginning of the dependency chain within a hierarchy
- Leaf: A leaf is the last child vertex in a dependency chain within a hierarchy; a leaf vertex has a degree of one

### Depth in Walks, Paths, and Cycles

Data within a hierarchy is usually referenced in one of three ways in an application: by its neighborhoods, by its depth, or by its path

- first, app references hierarchical data according to its parents or its children. can walk up or down a level
- second, app ref hierarchical data according to its distance from either a root or leaf. called depth
- third, hierarchical data requires understanding the full dependency chain between two pieces of data

Definition:

- Depth: In a hierarchy, depth is the distance of any vertex in the graph to its root; the max depth in a tree is found from its root

Terming Dependencies:

- Walk: A walk through a graph is a sequence of visited vertices and edges. Vertices and edges can be repeated
- Path: A path through a graph is a sequence of visited vertices and edges. Vertixes and edges cannot be repeated
- Cycle: A cycle is a path where the starting and ending vertixes are the same
- Loop: An edge that starts and ends at the same vertex

## Understanding Hierarchies with Our Sensor Data

Approaching problems:

- 1. Understand the data
- 2. Build a conceptual model using the GSL notation
- 3. Create the database schema

### Seeing hierarchies in data: From the bottom up

### Seeing hierarchies in data: From the top down

### Understanding edges in the sensor hierarchies

In this case, the following rules apply:

- 1. Edges start from any sensor and go to a neighboring sensor or tower
- 2. There can be no loops; a sensor cannot add an edge to itself

## Querying from Leaves to Roots in Development

Question: Waht path did a sensors data follow to pass its information to a tower?

- 1. Where has a specific sensor sent information to?
- 2. What was this sensors path to any tower?

```groovy
sensor = dev.V().has("Sensor", "sensor_name", "1002688"). // look up sensor
  next() // return the sensor vertex

dev.V(sensor).
  out("send").  // walk through all send edges (in first neighborhood)
  // out("send").  // walk 2nd neighborhood, if you want
  // out("send").  // walk 3rd, prolly gonna go to repeat(3)
  project("Label", "Name").  // for each vertex, create a map with two keys
  by(label).  // the value for the first key "Label"
  by(
    coalesce(values(
      "tower_name",  // for the 2nd key "Name": if a tower
      "sensor_name"  // else, return the sensor_name
    ))
  )
```

using until().repeat() now:

```groovy
sensor = dev.V().has("Sensor", "sensor_name", "1002688").next()

dev.V(sensor).
  until(hasLabel("Tower")).
  repeat(
    out("send").
    simplePath()
  )
```

use simplePath() to remove cycles:

- simplePath(): When it is important that a traverser not repeat its path through the graph

### Using the path() step and manipulating its data structure

- path(): the path() step (map) examines and returns the full history of a traverser

```groovy
sensor = dev.V().has("Sensor", "sensor_name", "1002688").next()

dev.V(sensor).
  until(hasLabel("Tower")).
  repeat(
    out("send").
    simplePath()
  ).path().
  by(coalesce(values("tower_name", "sensor_name")))
```

**Warning:** In the path data structure, `labels` is not the same as a vertex label or an edge label

Assigning labels with `as()`

```groovy
sensor = dev.V().has("Sensor", "sensor_name", "1002688").next()

dev.V(sensor).
    as("start").
  until(hasLabel("Tower")).
  repeat(
    out("send").
      as("visited").
    simplePath()
  ).
    as("tower").
  path().
  by(coalesce(values("tower_name", "sensor_name")))
```

### How to shape path() results with by()

When formatting the elements of path(), the by() modulators in Gremlin are applied in a round-robin fashion, meaning they are applied to the traversal objects in a cyclical order. In a case in which there are two by() steps:

- 1. The first by() step operates on the first traversal object
- 2. The second by() step operateson the second traversal object
- 3. Back to the first by() step for the third traversal object
- 4. Back to the second by() step for the 4th traversal object
- 5. And so on...

## Querying from Roots to Leaves in Development

Answer the following questions:

- 1. First, we need to find an interesting tower to explore in our data
- 2. Which sensors have directly connected to that tower?
- 3. From that tower, find all sensors that have connected to it

### Setup Query: Which tower has the most sensor connections so taht we could explore it for our example

Want primary key of the tower with the highest degree

**Warning:** this query is super expensive - dev only

```groovy
dev.V().hasLabel("Tower").  // for all towers
  group("degreeDistribution"). // create a map object
  by(values("tower_name")).  // the key for the map: tower_name
  by(inE("send")count()).  // the value for each entry: its degree
  cap("degreeDistribution").  // barrier step in gremlin to fill the map
  order(Scope.local).  // order the entries within the map object
  by(values, Order.desc)  // sort by values, decreasing
```

- Barrier steps: Barrier steps force the traversal pipeline to complete up until that point before continuing
  - cap() iterates the traversal up until that step, and passes the object with the name degreeDistribution into the next step in the pipeline

### Which Sensors Have Connected Directly to Georgetown

```groovy

sensor = dev.V().has("Sensor", "sensor_name", "1002688").next()

dev.V(sensor).
  out("send").
  project("Label", "Name").
    by(label).
    by(coalesce(
      values("tower_name"),
      "sensor_name"
    ))
```

Becomes:

```groovy
tower = dev.V().has("Tower", "tower_name", "Georgetown").next()

dev.V(tower).
  in("send").
  project("Label", "Name").
    by(label).
    by(values("sensor_name"))
```

### Find All Sensors That Connected to Georgetown

```groovy
tower = dev.V().has("Tower", "tower_name", "Georgetown").next()

dev.V(tower).
  until(hasLabel("Sensor")).  // until you reach a sensor
  repeat(
    __.in("send").  // __ is an anonymous traversal
    simplePath()
  )
```

**Tip:** The Anonymous traversal __. is used to resolve many variants of Gremlin that have clashes with reserved language-specific keywords such as `in`, `as` or `values`

Updated query recursively walk any depth until we find all sensors

```groovy
tower = dev.V().has("Tower", "tower_name", "Georgetown").next()

dev.V(tower).
  //until(hasLabel("Sensor")).  // until you reach a sensor
  repeat(
    __.in("send").  // __ is an anonymous traversal
    simplePath()).  // remove cycles
    times(3).  // only do 3 times - not doing this will timeout bc no end can be reached
    peth()
```
