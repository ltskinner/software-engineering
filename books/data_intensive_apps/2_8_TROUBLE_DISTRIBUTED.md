# Chapter 8. The Trouble with Distributed Systems

We will now turn our pessimism to the max and assume that anything that can go wrong will go wrong

(Experienced system operators will tell you that is a reasonable assumption)

Our task as engineers is to build systems that do what users expect, in spite of everything going wrong

"This chapter is a thoroughly pessimistic and depressing overview of things that may go wrong in a distributed system"

## Faults and Partial Failures

There is no fundamental reason why software on a single computer should be flaky: when a the hardware is working correctly, the same operation always produces the same result (it is deterministic)

An individual computer with good software is either fully functional, or entirely broken

Partial failures are nondeterministic - if you try and do anything involving multiple nodes and the network, it may sometimes work and sometimes unpredictably fail

Also possible for you to not even know whether something has succeeded or not, as the time it takes for a message to travel across a network is also nondeterministic

### Cloud Computing and Supercomputin'

#### Building a Reliable System From Unreliable Components

## Unreliable networks

Asynch - if you send a request and expect a response, many things could go wrong:

- Your request may have been lost
- Your request may be waitining in a queue and will be delivered later
- The remote node may have failed
- The remote node may have temporarily stopped responding, but will start responding later
- The remote node may have processed your request, but the response has been lost on the network
- The remote node may have processed your request, but the response has been delayed and will be delivered later

### Network Faults in Practice

most network errors are human caused (misconfigured switches)

just because a network link works in one direction doesnt guarantee its working in the opposite direction

### Detecting Faults

### Timeouts and Unbounded Delays

- long timeouts may mean users have to wait a long time just to get an error message
- short timeouts may incorrectly declare anode is dead, even tho it is just suffering a temporary slowdown
  - declaring a node dead has a lot of implications

#### Network Congestion and Queueing

Uhh use statistical analysis on network round-trip times and determine a good timeout

### Synchronous vs Asynchronous Networks

## Unreliable Clocks

Apps depend on clocks in various ways:

- Has this request timed out yet?
- Whats the 99th percentile response time of this service?
- How many queries per second did this service handle on average in the last 5 minutes?
- How long did the user spend on out side?
- When was this article published?
- At what date and time should the reminder email be sent?
- When does this cache entry expire?
- What is the timestamp on this error message in the log file?

### Monotonic vs Time-of-Day Clocks

- time of day - time of the day
- monotinic - suitable for measuring a duration (the absolute value of the clock does not matter)

In distributed systems, monotonic clocks are good

### Clock Synchronization and Accuracy

Monotonic clocks dont nees synchronization

Time of day clocks need to be set according to an NTP server or other external time source

### Relying on Synchronized Clocks

If using software that requires synchronized clocks, it is essential that you also carefully monitor the clock offsets between machines - any node whose clock drifts too far should be declared dead and removed

#### Timestamps for Ordering Events

lwwwwwwww

- database writes can mysteriously disappear
- cannot distinguish between writes that occured sequentually in quick succession, and writes that were truly concurrent
- possible for two nodes to independently generate writes with the same timestamp

#### Clock Readings have a Confidence Interval

#### Synchronized Clocks for Global Snapshots

Tool called `Spanner`

Google deploys a gps receiver or atomic clock in each datacenter - thats sick

### Process Pauses

#### Response Time Guarantees

real-time systems are super expensive, and most commonly used in safety-critical embedded devices (airbags n shit)

basically, guarantee that processes are allocated a portion of cpu time in specified intervals

actually super intricate

#### Limiting the Impact of Garbage Collection

Emerging idea is to treat GC pauses like brief planned outages of a node, and to let other nodes handle requests from clients while one node is collecting its garbage

## Knowledge, Truth, and Lies

A node in the network cannot know anything for sure - it can only make guesses based on the messages it receives (or doesnt receive) via the network

- What do we know to be true or false in our system?
- How sure can we be of that knowledge, if the mechanisms for perception and measurement are unreliable?
- Should software systems obey the laws that we expect of the physical world, such as cause and effect?

### The Truth is Defined by the Majority

use votes to make decisions

- like if a node is dead

#### The Leader and the Lock

Frequently, a system requires there to be only one of some thing:

- only one node is allowed to be the leader
- only one transaction or client is allowed to hold the lock for a particular resource or object
- only one user is allowed to register a particular username

#### Fencing Tokens

need to ensure that a node who falsley believes it to be "the chosen one" cannot disrupt the rest of the system

a `fencing token` is a number that increases every time a lock is granted (incremented by the lock service)

### Byzantine Faults

lmao - if a node deliberatley wanted to subvert the systems guarantees, it could easily do so by sending messages with a fake fencing token

if there is a risk that nodes may lie, thats a prolem haha

particularly relevant in:

- aerospace environments, the data in a computers memory or cpu register could become corrupted by radiation, leading it to respond to other nodes in arbitrarily unpredictable ways
- in systems with multiple participating organizations, some participants may attempt to cheat or defraud others (p2p networks, bitcoin)

However, most of the time ok to assume there are no byzantine faults

most byzantine fault-tolerant algorithms require a supermajority of more than two thirds of the nodes to be functioning correctly

#### Weak Forms of Lying

### System Model and Reality

System model - an abstraction that describes what things an algorithm may assume

- Synchronous model
  - assumes bounded network delay, bounded process pauses, bounded clock error
- Partially synchronous model
  - system behaved like a synchronous model most of the time, but some assumption bounds are exceeded
  - realistic of most real world systems
- Asynchronous model
  - algorithm not allowed to make any timing assumptions
  - not even have a clock

Also have to consider node failures. Most common models for these:

- Crash-stop faults
  - alg may assume that a node can only fail on one way, namely crashing
  - after the node is gone forever
- Crash-recovery faults
  - Nodes may fail at any moment, but may start responding again after some unknown time
- Byzantine (arbitrary) faults
  - Nodes may do absolutely anything, including trying to trick and decieve other nodes

#### Correctness of an Algorithm

Some properties

- Uniqueness
  - no two requests for a fencing token return the same value
- Monotonic sequence
- Availability

#### Safety and Liveness

- Safety - nothing bad happens
- Liveness - something good eventually happens

For distributed algorithms, common to require that safety properties `always` hold, in all possible situations of a system model

With liveness properties, we are allowed to make caveats

#### Mapping System Models to the Real World

## Summary

Some problems:

- Packets may be lost or delayed, so you have no idea if the message got thru
- A nodes clock may be significantly out of synch
- A process may pause for a substantial amount of time

Build tolerance of partial failures, so that the system as a whole may continue to function

- First, must be able to detect faults (but can be hard)
- Then, have to handle - but not easy considering no shared memory or common knowledge, and all info must be exchanged over the unreliable network. Use quorums
