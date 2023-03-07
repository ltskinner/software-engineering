# Chapter 9. Consistency and Concensus

This chapter covers algorithms and protocols for building fault-tolerant distributed systems

Best way of building fault-tolerant systems is to find some general purpose abstractions with useful guarantees, implement them once, and then let applications rely on those guarantees

`Concensus`: getting all of the nodes to agree on something

## Consistency Guarantees

A better name for eventual consistency may be `convergence`, as we expect all replicas to eventually converge to the same value

However, is very weak guarantee - doesnt say anything about `when` the replicas will converge

Stronger consistency guarantees dont come for free: worse performance or less fault-tolerant than systems with weaker guarantees

However, stronger guarantees can be appealing because they are easier to use correctly

## Linearizability

Linearizability aka atomic consistency, strong consistency, immediate consistency, external consistency

What if system was able to produce the illusion that there is only one replica

In a linearizable system, as soon as one client successfully completes a write, all clients reading from the db must be able to see the value just written

### What Makes a System Linearizable

Basic idea: make a system appear as if thre is only a single copy of the data

After any one read has returned the new value, all following reads must also return the new value

New operator:

- cas(x, v_old, v_new) -> r
  - compare-and-set operation
  - if the current value of the reguster x is vold, it should be set to vnew

#### Linearizability vs Serializability

- Linearizability:
  - Is a recency guaranteee on reads and writes of a register (individual object)
  - Does group operations, so does not prevent problems such as write skew
- Serializability:
  - Isolation property of transactions
  - Guarantees that transactions behave the same as if they had executed in some serial order

A db may provide both serializability and linearizability - known as: `strict serializability` or `strong one-copy serializability (strong-SR1)`

### Relying on Linearizability

There are a few areas in which linearizability is an imoprtant requirement for making a system work correctly:

#### Locking and Leader Election

Systems using single-leader replication need to ensure there in only one leader (no split brain)

One way to elect a leader is to use a lock: every node that starts up tries to acquire the lock, and the one that succeeds becomes the leader

No matter how the lock is implemented, it must be linearizable, all nodes must agree which node owns the lock, otherwise it is useless

#### Constraints and Uniqueness Guarantees

Need linearizability to prevent folks from duping usernames, which is somewhat similar to acquiring a lock

Not all real world constraints require this tho

#### Cross-Channel Timing Dependencies

Basically good for preventing race conditions

Multiple communication channels are usually the culprit

### Implementing Linearizable Systems

- Single-leader replication (potentially linearizable)
  - delusional leaders will likely violate linearizability
  - this occurs in asynch replication as well
- Concensus algorithms (linearizable)
- Multi-leader replication (not linearizable)
  - multi-datacenter, remember
- Leaderless replication (probably not linearizable)

#### Linearizability and Quorums

Possible if read repair is performed synchronously before returning results

Safe to assume quorums are not linearizable

### The Cost of Linearizability

#### The CAP Theorum

- If your appliaction requires linearizability, and some replicas are disconnected from other replicas due to a network problem, then some replicas cannot process requests while they are disconnected: they must either wait until the network problem is fixed, or return an error (either way, they become unavailable)
- If your application does NOT require linearizability, then it can be written in a way that each replica can process requests independently (even if it is disconnected from other replicas)
  - In this case, the application can remain available in the face of a network problem, but its behavior is not linearizable

#### The Unhelpful CAP Theorum

CAP sometimes presented as:

- Consistency
- Availability
- Partition tolerance

Pick 2 of 3

But misleading because network partitions are a kind of fault, so they arent something about which you have a choice: they will happen whether you like it or not

When a network fault occurs, you have to choose between either:

- linearizability
- total availability

A better phrasing: either Consistent or Available when Partitioned

#### Linearizability and Network Delays

Although linearizability is a useful guarantee, surprisingly few systems are actually linearizable in practice

- For example: even ram on modern multi-core cpu is not linearizable

The reason for dropping linearizability is performance, not fault tolerance

## Ordering Guarantees

### Ordering and Causality

One of the reasons ordering comes up is it helps preserve causality

If a system obeys the ordering imposed by causality, we say that it is `causally consistent`

#### The Causal Order is not a Total Order

total order vs partially ordered

is something comparable or not

- Linearizability
  - We have a total order of operations: if the system behaves as if there is only one single copy of the data, and every operation is atomic, we can always say which operation happened first
- Causality
  - We say that two operations are concurrent if neither happened before the other
  - This means that causality defines a partial order
    - Some operations are ordered with respect to each other, but some are incomparable

#### Linearizability is Stronger than Causal Consistency

Linearizability implies causality: any system that is linearizable will preserve causality correctly

However, linearizability is not the only way of preserving causality

#### Capturing Causal Dependencies

We need some way to describe the "knowledge" of a node in the system

### Sequence Number Ordering

Although causality is an important theoretical concept, actually keeping track of all causal dependencies can become impractical

However, there is a better way: use `sequence numbers` or `timestamps` to order events

Note that timestamps dont need to come from time-of-day clock, and instead can come from a `logical clock` which is an algorithm to generate a sequence of numbers to identify operations, typically using counters - these provide a total order

Easy to do with single leader

#### Noncausal Sequence Number Generators

If not using a single leader, less clear for how to generate a sequence. Some alternatives:

- Each node can generate its own independent set of sequence numbers
  - prevents two different nodes from generating the same sequence number
- Can attach a timestamp from a time of day clock
  - Such timestamps are note sequentil, but if they have high enough resolution, it might be good enough to totally order operations
- Preallocate blocks of sequence numbers

These all perform better and are more scalable than pushing all operations through a single leader that increments a counter

But all have a problem: seuqnce numbers are not consistent with causality

#### Lamport Timestamps

Lamport timestamp is a pair of (counter, node ID)

Two nodes may sometimes have the same counter value, but by including the node id, each timestamp is made unique

If you have two timestamps, the one with the greater counter value is the greater timestamp; if the counter values are the same, the one with the greater node id is the greater timestamp

The key idea about lamport timestamps, which makes them consistent with causality: every node and every client keeps track of the maximum counter value it has seen so far, and includes that macximum on every request

When a node receives a request or response with a max counter value greater than its own counter value, it mimediately increases its counter to that maximum

#### Timestamp Ordering is not Sufficient

The idea of knowing when your total order is finalized is captured in the topic of `total order broadcast`

### Total Order Broadcast

Single-leader replication determines a total order

The challenge is then how to scale the system if the thruput is greater than a single leader can handle, and also how to handle failover if the leader fails

Problem known as `total order broadcast` or `atomic broadcast`

Total order broadcast is usually described as a protocol for exchanging messages between nodes. Informally it requires that two safety properties always be satisfied:

- Reliable Delivery
  - No messages are lost: if a message is delivered to one node, it is delivered to all nodes
- Totally ordered delivery:
  - Messages are dlivered to every node in the same order

#### Using Total Order Broadcast

state machine replication

Another way of lookin gat total order boradcast is that it is a way of creating a log: delivering a message is like appending to the log

#### Implementing Linearizable Storage Using Total Order Broadcast

Total order broadcast is asynchronous: messages are guaranteed to be delivered reliably in a fixed order, but there is no guarantee when a message will be delivered

If you have total order broadcast, you can build linearized storagte on top of it

You can implement such a linearizable compare and set operation as follows, by using total order broadcast as an append only log:

- Append a message to the log, tentatively indeicating the username you want to claim
- Read the log, and wait for the message you appended to be delivered back to you
- Check for any messages claiming the username that you want. If the first message for your desired username is your own message, then you are successful, else, abort the operation

This procedure guarantees linearizable writes, but not reads

To make reads linearizable:

- Sequence reads through the log by appending a message, reading the log, and performing the actual read when the message is delivered back to you
- If the log allows you to fetch the position of the latest log message in a linearizable way, you can query that position, wait for all entries up to that position to be delivered, then perform the read
- You can make your read from replica that is synchronously updated onm writes, and thus is sure to be up to date

#### Implementing Total Order Broadcast Using Linearizable Storage

Unlike lamport timestamps, the numbers you get from incrementing the linearizable register form a sequence with no gaps - thus, if a node delivers message 5 and receives a message number 6, knows it must wait to get message 5

If you think hard enough about linearizable sequence number generators, you inevitable end up with a consensus algorithm - no coincidence: it can be proved taht a linearizable compare-and-set (or increment-and-get) register and total order broadcast are both `equivalent to consensus`. If you can solve one of these problems, you can transform it into a solutoin for the others

## Distributed Transactions and Consensus

One of the most important and fundamental problems in distributed computing

On surface, simple: get several nodes to agree on something

Situations where important for nodes to aggree:

- Leader election
- Atomic commit
  - If a transaction fails on some nodes, but succeeds on others, we have to get all nodes to agree on the outcome of the transaction

### Atomic Commit and Two-Phase Commit (2PC)

#### From Single-Node to Distributed Atomic Commit

The key deciding moment for whether the transaction commits or aborts is the moment at which the disk finishes writing the commit record:

- before the moment, still possible to abort (due to crash)
- after the moment, transaction is committed (even if the db crashes)

In distributed, easy for some commits to succeed on some nodes and fail on others:

- Some nodes may detect a constraint violation or conflict, making an abort necessary, while other nodes are successfully able to commit
- Some of the commit requests might be lost in the network, eventually aborting due to a timeout, while other commit requests get through
- Some nodes may crash before the commit record is fully written and roll back on recovery, while others successfully commit

#### Introduction to Two-Phase Commit

2PC uses a new component that does not normally appear in single-node transactions: a coordinator (known as transaction manager)

A distributed transaction begins with the application reading and writing data on multile nodes - these nodes are called participants

When application ready to commit, the coordinator begins phase 1: it sends a prepare request to each of the nodes, asking them whether they are able commit. The coordinator thent racks the responses from the participants

- If all participants reply "yes", indicating they are ready to commit, then the coordinator sends out a commit request in pahse 2, and the commit actually takes place
- If any of the particiapnts replies "no" the coordinator sends an abort request to all nodes in phase 2

#### A System of Promises

What makes 2PC different?

- When the application wants to begin a distributed transaction, it requests a transaction ID from the coordinator (globally unique)
- The application begins a single-node transaction on each of the participants, and attaches the globally unique transaction id to the single-node transaction. If anything goes wrong, the coordinator or any of the participants can abort
- When the application is ready to commit, the coordinator sends a prepare request to all particpants, tagged with the global transaction id. if any of these requests fail or timeout, the coordinator sends an abort request for that transaction id to all particpants
- When a participant receives the prepare request, it makes sure that it can definitely commit the transaction under all circumstances. If a node responds yes, they surrender their right to abort the transaction, without actually committing it
- When the coordinator has received responses to all prepare requests, it makes a definitive decision on whether to commit or abort the transaction (committing only if all participants voted "yes"). The coordinator writes the decision to its transaction log on disk so it knows what the decision was in case of crash - this is the `commit point`
- Once the coordinators decision has been written, the commit or abort request is sent to all participants. If this request or times out, the coordinator must retry forever until it succeeds. There is no going back

Thus, two commit points:

- the "yes" vote from each node
- the coordinator recording the transaction decision, the literal commit point haha

#### Coordinator Failure

The only way 2PC can complete is by waiting for the coordinator to recover

#### Three-Phase Commit

Two-phase commit is called a `blocking` atomic commit due to the fact that 2PC can become stuck waiting for the coordinator to recover

In theory, it is possible to make an atomic commit protocol nonblocking so that it does not get stuck if a node fails

Nonblocking atomic commit requires a `perfect failure detector` i.e. a reliable mechanism for telling whether a node has crashed or not

### Distributed Transactions in Practice

Mixed reputation

- on one hand, provide an important safety guarantee that would be hard to achieve otherwise
- other hand, criticized for operational problems, killing performance, and promising more than they deliver

MySQL implementation is reported over 10x slower than single node transactions

Two types of "distributed transactions:

- Database-internal distributed transactions
  - some distributed dbs support internal transactions among the nodes of that db
  - in this case, all the nodes participating in the transaction are running the same db software
- Heterogeneous distributed transactions
  - participants are two or more different technologies
  - jfc pls no

#### Exactly-once Message Processing

Heterogeneous distributed transactions allow diverse systems to be integrated in powerful ways

Ex. a message from a message queu can be acknowledged as processed if and only if the db transaction for processing the message was successfully committed

If either the message delivery or db transaciton fails, both are aborted

Such a distributed transaction is only possible if all systems affected by the transaciton are able to use the same atomic commit protocol

#### XA Transactions

X/OpenXA (short for eXtended Architecture) is a standard for implementing two-phase commit across heterogeneous systems

Its a C api for interfacing with a transaction coordinator

#### Holding Locks While in Doubt

problemmatic lol

#### Recovering from Coordinator Failure

In theory, if the coordinator crashes and is restarted, it should cleanly recover its tate from the log

However, in practice, orphaned in-doubt transactions do occur

Requires administrator intervention

#### Limitations of Distributed Transactions

- if the coordinator is not replicated but runs only on a single machine, it is a single point of failure for the entire system
- many server-side applicatinos are developed in a stateless model, with all persistent state stored in a db
  - when the coordinator is part of the app server, it suddenly changes the nature of deployment
  - suddenly, the coordinators logs become a cruicial part of the durable system state
  - such applications are no longer stateless
- single XA needs to be compatible with a wide range of data systems, it is necessarily a lowest common denominator
  - does not work with ssi

### Fault-Tolerant Consensus

the consensus problem is normally formalized as:

- one or more nodes may `propose` values
- the consensus algorithm `decides` on one of those values

In this formalism, a consensus algorithm must satisfy:

- Uniform agreement - no two nodes decide differently
- Integrity - no node decides twice
- Validity - if a node decides a value v, then v was proposed by some node
- Termination - Every node that does not crash eventually decides some value

#### Consensus Algorithms and Total Order Broadcast

Total order broadcast is equivalent to repeated rounds of consensus:

- Due to the agreement property of consensus, all nodes decide to deliver the same message in the same order
- Due to the integrity property, messages are not duplicated
- Due to the validity property, messages are not corrupted and not fabricated out of thin air
- Due to the termination property, messages are not lost

#### Single-Leader Replication and Consensus

In order to solve consensus, we must first solve consensus lol

#### Epoch Numbering and Quorums

Before a leader is allowed to decide anything, it must first check that there isnt some other leader with a higher epoch number which might take a conflicting decision

A node cannot necessarily trust its own judgement - just because a node thinks that it is the leader, that does not necessarily mean the other nodes accept it as their leader

Here, we have two rounds of voting:

- once to choose a leader
- and a second time to vote on a leaders proposal

#### Limitations of Consensus

Most consensus algorithms assume a fixed set of nodes that participate in voting, which means you cant just add or remove nodes in the cluster

### Membership and Coordination Services

Zookeeper has some other useful features for building distributed systems:

- Linearizable atomic operations
- Total ordering of operations
- Failure detection
- Change notifications

#### Allocating Work to Nodes

#### Service Discovery

#### Membership Services

## Summary

- Linearizable compare-and-set registers
  - The register needs to automatically `decide` whether to set its value, based on whether its current value equals the parameter given in the operation
- Atomic transaction commit
  - A db must `decide` whether to commit or abort a distributed transaction
- Total order broadcast
  - The messaging system must `decide` on the order in which to deliver messages
- Locks and leases
  - When several clients are racing to grab a lock or lease, the lock `decided` which one successfully acquired it
- Membership/coordination service
  - Given a failure detector (e.g. timeouts), the system must `decide` which nodes are alive, and which should be considered dead because their sessions timed out
- Uniqueness constraint
  - When several transactions concurrently try to create conflicting records with the same key, the constraint must `decide` which one to allow and which one should fail with a constraint violation

Above is straightforward if you have a single node, or are willing to assign the decision-making capability to a single node. However, if that single leader fails, or if a network interruption makes the leader unreachable, such a system becomes unable to make any progress. There are three ways of handling that situation:

- Wait for the leader to recover, and accept that the system will be blocked in the meantime
- Manually fail over by getting humans to choose a new leader node and reconfigure the system to use it
- Use an algorithm to automatically choose a new leader
