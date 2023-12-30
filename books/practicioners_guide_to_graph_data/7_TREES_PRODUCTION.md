# Chapter 7. Using Trees in Production

Especially with unbounded and hierarchical data, the mental distance between the data on disk and using it is *much shorter* when using graphs. However, simple questions with expressive languages and natural models can open the door to unexpected behavior

## Understanding Time in the Sensor Data

The sensors collect and send data throughout the network at specific time intervals. This means that the number of vertices in our graph will be fixed, and it is the relationships in the graph that grow over time

We model the dynamic communcation over time intervals with a timestep property on the edges

Uhh so each message becomes an edge, and the message has a property timestamp

Topics needed to understand using time series properties:

- 1. Understanding time from the bottom up
- 2. Valid paths from the bottom up
- 3. Understanding time from the top down
- 4. Valid paths from the top down

### Understanding time in hierarchies of data: From the bottom up

Every walk from a sensor to a tower is no longer a valid walk bc have to consider the timing of the communication along the way.

That is, a message passed from a sensor at ts 3 will be passed along from its recipient at ts 4

- start, ts, end node
- S - 1 -> A
- A - 2 -> B
- B - 3 -> C
- C - 4 -> D
- D - 5 -> FirstHill

### Valid and invalid paths from the bottom up

In the data, a valid path increments time by one as you walk through the edges

An invalid path is when you try to pass information to another sensor out of order. Sensors cannot give or receive data early or late. Must be in exact sequence on time

### Understanding time in hierarchies of data: From the top down

Lets start with sensor M, at want the valid path from the sensor up to WestLake:

- M - 2 -> I
- I - 3 -> F
- F - 4 -> WestLake

The goal is to be able to see this in reverse from WestLake back to sensor M. So trace that same path, but in the opposite direction

- WestLake - 4 -> F
- F - 3 -> I
- I - 2 -> M

In this case, it is easier to walk backwards from towers to sensors in the hierarchical structure

There are many ways to represent, but as long as you can see how to decrease time as we walk from a tower back down to sensors, then we have achieved the goal

### Valid and invalid paths from the top down

Again, no early, and no late - must be exactly on time

### Final Thoughts on Time Series Data in Graphs

Understanding time in this dataset is easy for modeling: we added it to our edges. The detail and difficulty com ein when we want to use time in our queries

Rule of Thumb 11: Time goes up onthe way up, and time goes down on the way down. When this rule of thumb isnt true, the path is invalid and should be filtered out of the results

## Understanding Branching Factor in Our Example

The example at the end of ch6 - we were unable to walk from a tower down to all sensors that connected to it because of the datas branching factor

### What is Branching Factor

- Branching factor: A graphs branching factor (BF) is the expected, or average, number of edges for any vertex

Computational overhead for a traversal, according to depth, is `BF^depth`

### How do we get around branching factor

When working with Cassandra, can already get around BF. A primary way to mitigate a queries bf goes back to how you store data on disk

Best tip: use properties on edges to give yourself a way to navigate your datas bf during queries

Rule of Thumb 12: Cluster your edges on disk so that you can sort through them in your queries and mitigate the effect of your datas branching factor

## Production Schema for Our Sensor Data

Basically, make materialized views of the inverse of directed edges

```groovy
schema.edgeLabel("send").
  from("Sensor").
  to("Tower").
materializedView("sensor_tower_inv").
  ifNotExists().
  inverse().
  create()
```

Bonus Rule of Thumb: To reinforce traversal driven modeling, you want your production edge labels to be in the direction that you will most commonly traverse, and the materialized views to be the less common direction

## Querying from Leaves to Roots in Production

We want to ask the same questions as before, but now we want to use time on the edges to consider only valid paths

### Where has this sensor sent information to, and at what time

```groovy
sensor = g.V().has("Sensor", "sensor_name", "104115939").next()

g.V(sensor)
  outE("send").
    project("Label", "Name", "Time").
    by(
      __.inV().
      label()
    ).
    by(
      __.inV().
      coalesce(
        values("tower_name"),
        values("sensor_name")
      )
    ).
    by(values("timestamp"))
```

### From this sensor, find all trees up to a tower by time

```groovy
sensor = g.V().has("Sensor", "sensor_name", "104115939").next()

g.V(sensor).
    as("start").
  until(hasLabel("Tower")).
  repeat(outE("send")
      as("send_edge").
    inV().
      as("visited").
    simplePath()
  ).
    as("tower").
  path().
  by(
    coalesce(
      values(
        "tower_name",
        "sensor_name"
      )
    )
  ).
  by(values("timestamp"))
```

### From this sensor, find a valid tree

```groovy
sensor = g.V().has("Sensor", "sensor_name", "104115939").next()

g.V(sensor).
  outE("send").has("timestep").inV().  // traverse edges with timestep == 0
  outE("send").has("timestep").inV()  // traverse edges with
  // ... so on
```

- loops(): the loops() step extracts the number of times the traverser has gone through the current loop

```groovy
sensor = g.V().has("Sensor", "sensor_name", "104115939").next()

g.V(sensor).as("start").
  until(hasLabel("Tower")).
  repeat(
    outE("send").as("send_edge").
      where(eq("send_edge")).
      by(loops()).
      by("timestep").
    inV().as("visited")
  ).as("tower").
  path().
  by(
    coalesce(values("tower_name", "sensor_name"))
  ).
  by(
    values("timestep")
  )
```

### Advanced Gremlin: Understanding the where().by() pattern

#### Understanding a common Gremlin mistake: Overloading has()

basically, the "dumb" solution doesnt work:

```groovy
sensor = g.V().has("Sensor", "sensor_name", "104115939").next()

g.V(sensor).
  outE("send").has(
    "timestep",
    loops()
  ).inV().  // traverse edges with timestep == 0
  //outE("send").has("timestep").inV()  // traverse edges with
  // ... so on
```

however, when doing:

```groovy
g.V(sensor).
  outE("send").
  where(
    eq("send_edge").
    by(loops()).
    by("timestep")
  ).inV().  // traverse edges with timestep == 0
  //outE("send").has("timestep").inV()  // traverse edges with
  // ... so on
```

basic form of where is:

- where(a, pred(b))
- sameas:
- where(pred(b)) - this uses incoming traverser as A

## Querying from Roots to Leaves in Production

### Which Sensors Have Connected to Georgetown Directly, by Time?

```groovy
tower = dev.V().hs("Tower", "tower_name", "Georgetown").next()

g.V(tower).
  inE("send").
  project("Label", "Name", "Time").
  by(outV().label()). // values for first key "Label"
  by(outV().  // values for second key "Name"
    coalesce(
      values("tower_name")
      values("sensor_name")  
    )
  ).
  by(values("timestep"))  //values for third key "Time"
```

### What valid paths can we find from georgetown down to all sensors?

Pseudocode:

- Init a counter variable
- For a total of coutner + 1 times (to account for the 0th edge),
  - Do the following:
  - Walk to incoming send edges
  - Create a filter to compare an edges timestep with the coutner
  - Decrease the counter by 1
- Show and shape the path from the tower to the ending sensor

To write this type of query, we need to dive into a new Gremlin concept: the sack() operator

loops() increments by one, but here we need to decrease by one

We can customize a variable in a gremlin traversal with the sack() step. Think of this as giving each traverser a backpack at the beginning of its journey in your graph data. You can initialize the sack with whatever you would like. As the traverser moves through graph data, it can mutate the contents of its sack according to what it is processing from the graph data

- Sack(): A traverser can contain a local data structure called a sack. The sack() step is used to read and write to a traversers sack
- WithSack(): the withSack() step is sued to initialize the sack data structure

Using repeat() with times() and the sack()

```groovy
start = 3
tower = dev.V().has("Tower", "tower_name", "Georgetown").next()

g.withSack(start).  // every traverser starts with a sack with a value of 3
  V(tower).as("start").
  repeat(
    inE("send").as("send_edge").
    where(eq("send_edge")).
      by(sack()).  // test if the sack() value
      by("timestep").  // equals the edges timestep
    sack(minus).  // decrease the sacks value
      by(constant(1)).  // by 1
    outV().as("visited").
    simplePath()).  // traverse to adjacent vertex
  times(start+1)
    .as("tower").  // do above 4 times
  path().
    by(coalesce(values("tower_name", "sensor_name"))).
    by(values("timestep"))
```

## Applying Your Queries to Tower Failure Scenarios

Consider what would happen if the Georgetown tower were to go down. Which sensors, if any, will we lose connection to? Will they be the only sensors that surround the tower?

We have ironed out two tools to use to answer this question:

- 1. We can report, for any tower, all of the sensors that communicated with it
- 2. For any sensor, we can tell which towers connected with

To resolve network failure problem, we can apply the following procedure:

- 1. Get a list of sensors that connected with Georgetown in any time window
- 2. For each sensor, query the network to see if they used a different tower in that time window

### Get a list of sensors that connected with Georgetown in any time window

Process:

- Wrap our query form a tower to sensors in a method: getSensorsFromTower()
- for each step in time:
  - find all sensors that connected with georgetown
- create a unique list of the sensors

[script](./energy_7_queries.groovy)

### For each at-risk sensor, find all towers it communicated with

Process:

- Wrap our query from a sensor to towers in a method
- for each sensor in atRiskSensors:
  - for each step in time
    - find the towers the sensors connected with
  - add to a map of the unique towers a sensor connected to
  - find sensors that connected only to Georgetown

### Applying the final results of our complex problem

## Seeing the Forest for the Trees
