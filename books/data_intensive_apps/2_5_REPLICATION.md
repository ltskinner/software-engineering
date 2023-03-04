# Chapter 5. Replication

"The major difference between a thing that might go wrong, and a thing that cannot possibly go wrong is that when a thing that cannot possibly go wrong goes wrong, it usually turns out to be impossible to get at or repair"

Replicatio means keeping a copy of the same data on multiple machines that are connected via a network. Some reasons to do this:

- To keep data geographically close to your users (and thus reduce latency)
- To allow the system to continue working even if some of its parts have failed (and thus increase availability)
- To scale out the number of machines that can serve read queries (and thus increase read thruput)

If the data youre replicating does not change over time, then replication is easy: you just need to copy the data to every node at once, and youre done

All of the difficulty in replication lise in handling changes

Three popular algorithms for replicating changes between nodes:

- single-leader
- multi-leader
- leaderless

## Leaders and Followers

Each node that stores a copy of the database is called a `replica

Every write to the db needs to be processed by every replica, otherwise, the replicas would no longer contain the same data

Most common solution is called `leader-based replication` or `active/passive` or `master-slave replication`

- One of the replicas is designated as the leader. when clients want to write to the database, they must send their requests to the leader, which first writes the new data to its local storage
- The other replicas are known as followers. Whenever the leader writes new data to its local storage, it also sends the data change to all of its follwoers as part of a replication log or change stream. each follower takes the log from the leader and updates its local copy of the db accordinly
- When a client wants to read from the db, it can either query the leader or any of the followers

### Synchronous vs Asynchronous Replication

In synch, the leader waits until it has received an ok from the follower before reporting to the user it was successful

Can require at least 1 follower is synchronous, while the others are asynch to guarantee that good data makes it onto at least two nodes (leader and the synch follower)

Many systems are asynch, which means if leader fails writes arent guaranteed

Chain replication is another option

### Setting Up New Followers

Conceptually:

- Take a consistent snapshot of the leaders db at some point in time (ideally without taking a lock on the db)
- Copy the snapshot to the new follwoer node
- The follower connects to the leader and requests all the data changes that have happened since the snapshot was taken
  - This requires that the snapshot is associated with an exact position in the leaders replication log

#### Leader Failure: Failover

Handling the failure of the leader is tricky: one of the followers needs to be promoted to the new leader, clients need to be reconfigured to send their writes to the new leader, and other followers need to start consuming data changes from the new leader - this is the `failover`

These can happen manually or automatically

Automatic failover usually consists of:

- Determining that the leader has failed
  - many possible reasons, so typically use a timeout
- Choosing a new leader
  - can be done via election process, or appointed by previously elected controller node
  - best candidate is replica with most up to date data changes
- Reconfiguring the system to use the new leader
  - critical - what happens if the old leader comes back online and some nodes still think its the leader?

Things that can go wrong:

- if asynch replication, the new leader may not have received all writes from old leader
- discarding writes is super dangerous
- two nodes can think theyre the leader - `split brain` - if both leaders accept writes, no process for resolving conflicts
- what is the right timeout before a leader is declared dead

### Implementation of Replication Logs

#### Statement-based Replication

Like, regular sql written to a log

Problems:

- any statment that calls a nondeterministic function like NOW or RAND is likely to generate a different value on each replica
- if statements use an autoincrementing column or if they depend on the existing data in the database (e.g. UPDATE WHERE) - these must be executed in exactly the same order on each replica, or they may have a different effect
- Statements taht have side effects (e.g. triggers, stored procedures, user defined functions)

There are workarounds to these tho

#### Write-ahead Log (WAL) Shipping

Primary disadvantage is that the log describes the data on a very low level (details which bytes were changed in which disk blocks)

- This makes replication closely coupled to the storage engine
- If the database changes its storage format from one version to another, it is typically not possible to run different versions of the database doftware and the leader and the followers

#### Logical (Row-Based) Log Replication

An alternative is to use different log formats for replication and for the storage engine, which allows the replication log to be decoupled from the storage engine internals. this is called `logical log` to distinguish it from the storage engines `physical` data representation

A logical log for a relational db is usually a sequence of records describing writes to database tables at the granularity of a row:

- For an inserted row, the log contains the new values of all columns
- For a deleted row, the log contains enough information to uniquely identify the row that would be deleted (typically the primary key, but if none, old values of all cols need to be logged)
- For an updated row, the log contains enough information to uniquely identify the updated row, and the new values of all columns

Better backwards compatibility

Easier for external applications to parse - `change data capture`

#### Trigger-Based Replication

A trigger lets you register custom applicatio code that is automatically executed when data changes

Typically has greater overhead than other replication methods, more prone to bugs, and subject to limitations of the db

Can be useful due to flexibility

## Problems with Replication Lag

In read-scaling architecture, can increase capacity for serving read-only requests simply by adding more followers

Only realistically works with asynch replication - if you tried to synch replicate to all follwers, a single node failure or network outage would make the entire system unavailable for writing. more nodes = higher likelihood of one being down

asynch might not be up to date tho - but will have eventual consistency

### Reading Your Own Writes

With asynch, user might not see data they just wrote

Need `read-after-write consistency` aka `read-your-writes consistency`

Possible techniques:

- when reading something that the user may have modified, read it from the leader, otherwise read it from a follower
  - if most things in the application are potentially editable by the user, above approach wont be effective (constantly reading from leader defeats whole point of read scaling)
- client can remember the timestamp of its most recent write, then the system can ensure that the replica serving any reads for that user reflects updates at least until taht timestamp. timestamp could also be a logical timestamp. also, clock synchronization becomes critical

Some additional issues:

- approaches that require remembering the timestamp of the users last update become more difficult - this metadata will need to be centralized
- if your replicas are distributed across different datacenters, there is no guarantee that connections from different devices will be routed to the same datacenter

### Monotonic Reads

Possible for a user to see things `moving backward in time`

This can happen if a user makes several reads from different replicas - can be due to random routing of requests from new connections, and getting unlucky on which replicas receive the request

Monotonic reads is a guarantee that this kind of anomaly does not happen - its a lesser guarantee than strong consistency, but a stronger guarantee than eventual consistency. you may still see old data, but will not read data older than you have previously read

### Consistent Prefix Reads

concerns violation of causality

basically two items have a dependency on each other, and if those get read out of order it looks weird

Preventing this requires another guarantee: `consistent prefix reads`

This guarantee says that if a sequence of writes happens in a certain order, then anyone reading those writes will see them appear in the same order

This is a particular problem for sharded databases

### Solutions for Replication Lag

When working with an eventual consistency system, it is worth thinking about how the application behaves if the replication lag increases to several minutes or even hours. If the answer is "no problem", lit

However, if a problem for users, gotta design the system to provide a stronger guarantee - such as read-after write

Pretending that replication is synchronous when it is in fact asynch is a recipie for problems

## Multi-Leader Replication

In this setup, each leader simultaneously acts as a follower to other leaders

### Use Cases for Multi-Leader Replication

#### Multi-datacenter operation

- can have a leader in each datacetner

Comparing to single leader:

- Performance
  - every write processed by local datacenter and replicated asynch to other datacenters - so inter-datacenter network delay is hidden from users, which means percieved performance may be better
- Tolerance of Datacenter Outages
  - in event of failover, each datacenter can continue operating independently of the others and replication catches up when the failed datacenter comes back online
- Tolerance of Network Problems
  - open internet is less reliable than local network in datacenter

Big downside: the same data may be concurrently modified in two different datacenters, and those write conflicts must be resolved

#### Clients with Offline Operation

If you have an application that needs to continue to work while it is disconnected from the internet

#### Collaborative Editing

### Handling Write Conflicts

Biggest problem with multi-leader replication is that write conflicts can occur

#### Synchronous vs Asynch Conflict Detection

- in single leader, the second writer will either block and wait for first to complete, or abort the write and force the user to retry

#### Conflict avoidance

- the simplest strategy for dealing with conflicts is to avoid them: if the application can ensure that all writes for a particular record go through the same leader, than conflicts cannot occur

#### Converging Toward a Consistent State

Database must resolve conflicts in a `convergent way` - all replicas must arrive at the same final value when all changes have been replicated

Some ways of achieving convergent conflict solution:

- Give each write a unique id, and pick the write with the highest id as the winner
  - or use timestamp - last write wins (LWW) lmao (which is popular but prone to dataloss)
- Give each replica a unique id and let writes that originated at higher numbered replicas take prescedent (implies data loss)
- Somehow merge values together - e.g. order them alphabetically and then concatenate them
- Record the conflict in an explicit data structure that preserves all information, and write application code that resolves the conflict at some later time (perhaps by prompting the user)

#### Custom Conflict Resolution

The most appropriate way of resolving a conflict may depend on the application, most multi-leader replication tools let you write conflict resolution logic using application code

- executed on write - as soon as the db detects a conflict, calls the conflict handler
- executed on read - when conflict detected, all writes are stored. the next time the data is read, the multiple versions are returned to the application, and the user is prompted to resolve (or can be done automatically) and the result is written back

Note resolution usually applies at the level of an individual row or document - not an entire transaction

### Automatic Conflict Resolution

- Conflict-free replicated datatypes (SRDTs)
- Mergeable persistent data structures - similar to git
- Operational transformation

### Multi-Leader Replication Topologies

A `replication topology` describes the communication paths along which writes are propogated from one node to another

- Circular
- Star - can be generalized to a tree
- All-to-all - the most general

In circular and star, a write may need to pass through several nodes before reaching all replicas

In circular and star, if one node fails, can interrupt flow of replication messages between other nodes

Some links between some nodes may be faster than others, so some replication messages may "overtake" others

## Leadership Replications

In some leaderless implmenetations, the client directly sends its writes to several replicas, while in others, a coordinator node does this on behalf of the client

However, unlike a leader database, that coordinator does not enforce a particular ordering of writes (which has profound consequences for the way the db is used)

### Writing to the DB When a Node is Down

reading from the once-downed node has stale data

when a client reads from the db, it doesnt just send its request to one replica: read requests are also sent to several nodes in parallel. the client may get different responses from different nodes - version numbers are used to determine which value is newer

#### Read Repair and Anti Entropy

Two mechanisms:

- Read Repair
  - When a client makes a read from several nodes in parallel, can detect stale responses
- Anti-Entropy Process
  - Some datastores have a background process taht constantly looks for differences in the data
  - may be significant delay for new data to be copied over

#### Quorums for Reading and Writing

- min number of votes required for a read or write to be valid
- n, w, r
- `w` = `r` = `(n+1)/2`
- n is typically odd number, `n = 3 or 5`
- as long as `w + r > n` we good

Tolerating unavailable nodes:

- If w < n, we can still process writes if a node is unavailable
- If n < n, we can still process reads if a node is unavailable
- With n=2, w=2, and r=2 we can tolerate one unavailable node
- With n=5, w=3, and r=3 we can tolerate two unavailable nodes
- Normally, reads and writes are always sent to all n replicas in parallel. The parameters w and r determine how many nodes we wait for - i.e. how many of the n nodes need to report success before we consider the read or write to be successful

### Limitations of Quorum Consistency

With a smaller w and r you are more likely to read stale values, but configuration allows lower latency and higher availability

Possible scenarios leading to stale values:

- If a sloppy quorum is used, the w writes may end up on different nodes than the r reads, so there is no longer a guaranteed overlap between the r nodes and w nodes
- If two writes occur concurrently, it is not clear which one happened first. In this case, the only safe solution is to merge the concurrent writes. If a winner is picked based on a timestamp (lwwlwwww) writes can be lost due to clock skew
- If a write happens concurrently with a read, the write may be reflected on only some of the replicas. In this case, its undetermined whether the read returns the old or the new value
- If a write succeeded on some replicas but failed on others - subsequent reads may or may not return the value from that write
- If a node carrying a new value fails, and its data is restored from a replica carrying an old value, the nubmer of replicas storing the new value may fall below w, breaking the quorum condition
- Even if everything is working correctly, there are edge cases in which you can get unlucky with the timing

#### Monitoring Staleness

Should be able to quantify "eventual" of eventual consistency

### Sloppy Quorums and Hinted Handoff

Databases with appropriately configured quorums can tolerate the failure of individual nodes without the need for failover

Leaderless replication appealing for use cases with high availability and low latency, and can tolerate occasional stale reads

But, quorums are not as fault-tolerant as they could be

DB designers must decide:

- Is it better to return errors to all requests for which we cannot reach a quorum of w or r nodes?
- Or, should we accept writes anyway and write them to some nodes taht are reachable but arent among the n nodes on which the value usually lives?

The latter is known as `sloppy quorum`: writes and reads still require w and r successful responses, but those may include nodes that are not among the designated n "home" nodes for a value

If you lock yourself out of your house, ask a neighbor to sleep on their couch

Then you find your keys, and your neighbor asks you to get off their couch and go home - this is the `hinted handoff`

Sloppy quorums are particularly useful for increasing write availability

#### Multi-Datacenter Operation

Leaderless is also suitable for multi-datacenter operation since designed to tolerate conflicting concurrent writes, network interruptions, and latency spikes

### Detecting Concurrent Writes

#### Last Write Wins (discarding concurrent writes)

Concurrent - order is undefined

lww can even write drops that are not current

if losing data is not acceptable, lww is a poor choice for conflict resolution

the only safe way to use lww is to ensure that a key is only writte once and thereafter is treated as immutable, thus avoiding any concurrent updates to the same key

#### The "Happens-Before" Relationship and Concurrency

##### Concurrency, Time, and Relativity

because of clock issues, for defining concurrency, exact time doesnt matter: we simply call two operations concurrent if they are both unaware of each other, **regardless** of the physical time at which they occured

#### Capturing the "Happens-Before" Relationship

Algorithm for determining - based on version numbers, not the value itself:

- The server maintains a version number for every key, increments the version number every time that key is written, and stores the new version number along with the value written
- When a client reads a key, the server returns all values that have not been overwritten, as well as the latest version number. A client must read a key before writing
- When a client writes a key, it must include the version number from the prior read, and it must merge together all values that it received in the prior read
- When the server receives a write with a particular version number, it can overwrite all values with that version number or below but must keep all values with a higher version number

#### Merging Concurrently Written Values

Ensures that no data is silently dropped, but unfortunately requires that the clients do some extra work

#### Version Vectors

Need to use a version number per replica as well as per key (when multiple replicas accept writes concurrently)

The collection of version numbers from all the replicas is called a version vector

## Summary

Replication can serve several purposes:

- High Availability
  - Keep the system running, when one machine (or several machines, or an entire datacenter) goes down
- Disconnected Operation
  - Allowing an application to continue working when there is a network interruption
- Latency
  - Placing data geographically close to users, so that users can interact with it faster
- Scalability
  - Being able to handle a higher volume of reads than a single machine could handle, by performing reads on replicas

Main approaches:

- Single-leader replication
  - client sends all writes to single node (leader), which are sent to other replicas
  - reads performed by any replica
- Multi-Leader replication
  - clients send writes to one of several leaders
  - leaders send changes to each other and to followers
- Leaderless replication
  - Clients send each write to several nodes, and read from several nodes in parallel in order to detect and correct nodes with stale data

Consistency models:

- Read-after-write consistency
  - Users should always see data that they submitted themselves
- Monotonic reads
  - After users have seen the data at one point in time, they shouldnt later see the data from some earlier point in time
- Consistent prefix reads
  - Users should see the data in a state that makes causal sense
