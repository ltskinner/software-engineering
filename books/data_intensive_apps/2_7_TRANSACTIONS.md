# Chapter 7. Transactions

Harsh realities of data systems:

- The database software or hardware may fail at any time (including in the middle of a write operation)
- The application may crash at any time (including halfway through a series of operations)
- Interruptions in the network can unexpectedly cut off the application from the database, or one database node from another
- Several clients may write to the database at the same time, overwriting each others changes
- A client may read data that doesnt make sense because it has only been partially updated
- Race conditions between clients can cause surprising bugs

For decades, `transactions` have been the mechanism of choice for simplifying these issues

- A transaction is a way for an application to group several reads and writes into a logical unit
- Conceptually, all the reads and writes in a transaction are executed as one operation: either the entire transaction succeeds (commit) or it fails (abort, rollback)
- Transactions were created with a purpose: namely to `simplify the programming model` for applications accessing a database
- Not every application needs transactions, and sometimes there ae advantages to weakening transactional guarantees or abandonning them entirely (for example, to achieve higher performance or higher availability)

## The Slippery Concept of a Transaction

### The Meaning of ACID

The safety guarantees provided by transactions are often described by ACID

- Atomicity
- Consistency
- Isolation
- Durability

These days, ACID is mostly a marketing term

#### Atomicity

Atomic refers to something that cannot be broken down into smaller parts

Atomicity describes what happens if a client wants to make several writes, but a fault occurs after some of the writes have been processed

Atomicity simplifies the problem of not knowing which specific operation failed: if a transaction was aborted, the application can be sure that it didnt change anything, so it can be safely retried

"Perhaps `abortability` would have been a better term

#### Consistency

The term consistency is terribly overloaded

In the context of ACID, consistency refers to an application-specific notion of the database being in a "good state"

The idea of ACID consistency is that you have certain statements about your data (`invariants`) that must always be true

- if a transaction starts with a database that is valid according to these invariants, and any writes during the transaction preserve the validity, then you can be sure that the invariants are always satisfied
- however, this idea of consistency depends on the applications notion of invariants
  - its the applications responsibility to define its transactions correctly so they preserve consistency
  - this is not something the database can guarantee: if you werite bad data that violates your invariants, the db cant stop you

Thus, the letter C doesnt reeeally belong in acid

#### Isolation

If you have multiple clients reading and writing to the same db records, you can run into concurrency problems (race conditions)

Isolation in the sense of ACID means that concurrently executing transactions are isolated from each other: they cannot step on each others toes

The db ensures that when the transactions have been committed, the result is the same as if they had run serially

#### Durability

The purpose of a database system is to provide a safe place where data can be stored without fear of losing it

Durability is the promise that once a transaction has committed successfully, any data it has written will not be forgotten, even if there is a hardware fault or the db crashes

### Single-Object and Multi-Object Operations

#### Single-Object Writes

Imagine writing a 20kb json to a db

- If the network connection is interrupted after the first 10kb, does the db store that unparsable 10kb fragment of jason?
- If the power fails while the db is in the middle of overwriting the previous value on disk, do you end up with the old and new values spliced together?
- If another client reads that document while the write is in progress, will it see a partially updated values?

#### The Need for Multi-Object Transactions

Many distributed datastores have abandoned multi-object transactions because they are difficult to implement across partitions, and they can get in the way in some scenarios where very high availability or performance is required

In many other cases writes to several different objects need to be coordinated:

- In a relational model, a row in one table often has a foreign key reference to a row in another table.
  - Multi-object transactinos allow you to ensure that these references remain valid
  - when inserting several records that refer to one another, the foreign keys have to be correct and up to date, or the data becomes nonsensical
- In a document data model, the fields that need to be updated are often within the same document
  - What if you are denormalizing data and need to update several doucments?
- In dbs with secondary indexes, the indexes also need to be updated every time you change a value
  - without transaction isolation, its possible for a record to appear in one index, but not another, because the update to the second index hasnt happened yet

#### Handling Errors and Aborts

A key feature of a transaction is that it can be aborted and safely retried if an error occured

Not all systems follow this philosopy: in particular, datastores with leaderless replication work more on a "best effort basis" aka "the database will do as much as it can, and if it runs into an error, it wont undo something it has already done"

Although retrying an aborted transaction is a simple and effective error handling mechanism, it isnt perfect:

- If the transaction actually succeeded, but the network failed while the server tried to acknowledge, the client thinks it failed. retrying causes the transaction to be performed twice, unless you have application level deduplication implemented
- If the error is due to overload, retrying the transaction will make the problem worse, not better. To avoid such feedback cycles, you can limit the number of retries, use exponential backoff, and handle overload-related errors differently from other errors (if possible)
- It is only worth retrying after transient errors (example due to deadlock, isolation violation, temporary network interruptions, and failover) after a permanent error (e.g. constraint violation) a retry would be pointless
- If the transaction also has side effects outside of the database, those side effects may happen even if the transaction is aborted. ex. if you are sending an email, you wouldnt want to send the email again every try you retry the transaction. `two-phase commit` can help
- If the client process fails while retrying, any data it was trying to write to the db is lost

## Weak Isolation Levels

If two transactions dont touch the same data, they can safely be run in parallel, because neither depends on the other

Concurrency bugs are hard to find by testing, because such bugs are only triggered when you get unlucky with timing

DBs have long tried to hide concurrency issues from app developers by providing transaction isolation. In theory isolation should make your life easier by letting you pretend that no concurrency is happening: serializable isolation means that the db guarantees that transactions have the same effect as if they ran serially

In practice, isolation is not that simple. Serializable isolation has a performance cost, and many dbs dont wanna pay that price. Therefore, its common for systems to use weaker levels of isolation, which protect against some concurrency issues, but not all

### Read Committed

The most basic level of transaction isolation is read committed, which makes two guarantees:

- When reading from the database, you will only see data that has been committed (no `dirty reads`)
- When writing to the db, you will only overwrite data that has been committed (no `dirty writes`)

#### No Dirty Reads

Can another transaction see that uncommitted data?

Why good to prevent dirty reads:

- If a transactin needs to update several objects, a dirty read means that another transaction may see some of the updates but not others
- If a transaction aborts, any writes it has made needs to be rolled back. If the database allows dirty reads, tha tmeans a transaction may see data that is later rolled back

#### No Dirty Writes

Whathappens if two transactions concurrently try to update the same object in a database?

Usually prevented by delaying the second write until the first writes transaction has been committed or aborteds

#### Implementing Read Committed

Most commonly, dbs prevent dirty writes by using row-level locks: when a transaction wants to modify a particular object (row or document) it must first acquire a lock on that target, and hold that lock until the transaction is committed or aborted

The approach of requiring read locks does not work well in practice, because one long-running write transaction can force many other transactions to wait until the long running transaction has completed, even if the other transactions only read and do not write anything to the db

For that reason, most dbs prevent dirty reads by: for every object that is written, the db remembers both the old committed value and the new value set by the transaction that currently holds the write lock. While the transaction is ongoing, any other transaction that reads th eobject are simply given the old value. Only when the new value is committed do transactions switch over to reading the new value

### Snapshot Isolation and Repeatable Read

Read skew anomaly, and is an example of a nonrepeatable read

basically a timing anomaly cause some transactions have not finished when the read was requested - not a lasting problem but looks like a problem

Some situations cannot tolerate temporary inconsistency

- Backups
  - Taking a backup requires making a copy of the entire database, which may take hours
  - During that time, writes will continue to be made to the db, so could end up with some parts of the backup containing an older version of the data
  - If you restore from this backup, indonsistencies will become permanent
- Analytics queries and integrity checks
  - These queries are likely to return nonsensical results if they observe parts of the db at different points in time

Snapshot isolation is the most common solution to this problem

The idea is that each transaction reads from a consistent snapshot of the database - that is the transaction sees all the data that was committed in the database at the start of the transaction

#### Implementing Snapshot Isolation

Like read committed isolation, implementations of snapshot isolation typically use write locks to prevent dirty writes

Key principle of snapshot isolation:

- readers never block writers
- writers never block readers

Db may keep several different committed versions of an object, because various in-progress transactions may need to see the data of the db at different points in time. this is known as `multi-version concurrency control (MVCC)`

#### Visibility Rules for Observing a Consistent Snapshot

By carefully defining visibility rules, the db can present a consistent snapshot of the db to the application:

- At the start of each transaction ,the db makes a list of all the other transactions that are in progress (not yet committed or aborted) at that time. Any writes that those transactions have made are ignored, even if the transactions subsequently commit
- Any writes made by aborted transactions are ignored
- Any writes made by transactions with later transaction id (which started after the current transaction began) are ignored, regardless of whether those transactions have committed
- All other writes are visible to the applications queries

#### Indexes and Snapshot Isolation

How do indexes work in a multi-version database?

One option is to have the index simply point to all versions of an object and require an index query to filter out any object versions that are not visible to the current transaction

#### Repeatable Read and Naming Confusion

different interpretations

### Preventing Lost Updates

`lost update` problem: can occur if an application reads some value from the db, modifies it, and writes back the modified value (read-modify-write cycle)

If two transactions do this concurrently, one of the modifications can be lost because the second write does not include thr first modification (we sometimes say that the later write `clobbers` the earlier write). This pattern occurs in various scenarios:

- incrementing a counter or updating an account balance (requires reading the current value, calculating the new value, and writing back the updated value)
- making a local change to a complex value, e.g. adding an element to a list within a json document (requires parsing the document, making the change, and writing back the modified document)
- Two users editing a wiki page at the same time, where each user saves their changes by sending the entire page contents to the server, overwriting whatever is currently in the db

Super common, so variety of solutions

#### Atomic Write Operations

many dbs have an atomig `UPDATE` operator, which removes the need to implement read-modify-write cycles in app code

Atomic operations are usually implemented by taking an exclusive lock on the object when it is read so that no other transaction can read it until the update has been applied - known as `cursor stability`

#### Explicit Locking

If any other transaction tries to concurrently read the same object, it is forced to wait

#### Automatically Detecting Lost Updates

An alternative is to allow them to execute in parallel, and if the transaction manager detects a lost update, abort the transaction and force it to retry its read-modify-write cycle again

#### Compare-and-Set

In dbs that dont provide transactions, sometimes you find an atomic compare-and-set operation

The purpose of this operation is to avoid lost updates by allowing an update to happen only if the value has not changed since you last read it

If the current value does not match what you previously read, the update has no effect, and the read-modify-write cycle must be retried

#### Conflict Resolution and Replication

In replicated databases, preventing lost updates takes on another dimension: since they have copies of the data on multiple nodes, and the data can potentially be modified concurrently on different nodes, some additional steps need to be taken to prevent lost updates

### Write Skew and Phantoms

A generalization of the lost update problem. Write skew can occur if two transactions read the same objects, then update some of those objects

Ex.

- Claiming a username
- Booking a room
- Double spending

#### Materializing Conflicts

## Serializability

- Isolation levels are hard to understand, and inconsistently implemented in different databases (e.g. meaning of "repeatable read" varies significantly)
- If you look at your application code, its difficult to tell whether it is safe to run at a particular isolation level - especially in a large application, where you might not be aware of all the things that may be happening concurrently
- There are no good tools to help us detect race conditions

The answer from researchers has been simple: use `serializable` isolation

Usually regarded as the strongest isolation level. Guaranteees that even though transactions may execute in parallel, the end result is the same as if they had executed one at a time - serially - without any concurrency

If this serializable isolation is so much better than the mess of weak isolation levels, then why isnt everyone using it?

### Actual Serial Execution

The simplest way of avoiding concurrency problems is to remove the concurrency entirely: to execute only one transaction at a time, in serial order, on a single thread

What makes this possible now:

- RAM became cheap enough that for many use cases, it is now feasible to keep the entire dataset in memory
  - When all data that a transaciton needs to access is in memory, transactions can execute much faster than if they have to wait for data to be loaded from disk
- Database designers realized that OLTP transactions are usually short and only make a small number of reads and writes
  - By contrast, long-running analytic queries are typically read-only, so they can be run on a consistent snapshot (using snapshot isolation) outside of the serial execution loop

#### Encapsulating Transactions in Stored Procedures

#### Pros and Cons of Stored Procedures

Bad reputation for various reasons:

- Each db vendor has own language for stored procedures
  - many are old and clunky
- Code running on a db is difficult to manage: compared to an application server, its harder to debug, more awkward to keep in version control and deploy, trickier to test, and difficult to integrate with a metrics collection system for monitoring
- A database is often more performance-sensitive than an application server, because a single database instance is often shared by many application servers
  - A badly written stored procedure in a db can cause much more trouble than equivalently badly written code in an application server

#### Partitioning

Executing transactions serially makes concurrency control much simpler, but limits the transaction thruput of the db to the speed of a single cpu core on a single machine

For apps with high write thruput, the single threaded transaction processor can become a serious bottleneck

Cross-partition transactions have additional coordination overhead, and are vastly slower than single-partition transactions

#### Summary of Serial Execution

- Every transaction must be small and fast, because it only takes one slow transaction to stall all transaction processing
- It is limited to use cases where the active dataset can fit in memory. Rarely accessed data could potentially be moved to disk, but if it needed to be accessed in a single-threaded transaction, the system would get very slow
- Write thruput must be lower enough to be handled on a single cpu core, or else transactions need to be partitioned without requiring cross-partition coordination
- Cross partition transactions are possible, but there is a hard limit to the extent to which they can be used

### Two-Phase Locking (2PL)

Several transactions are allowed to concurrently read the same object as long as nobody is writing to it. But as soon as anyone wants to write (modify or delete) an object, exclusive access is required

In 2PL, writers dont just block other writers, they also block readers and vice versa

Protects against all race conditions, including lost updates and write skew

#### Implementation of Two-Phase Locking

- If a transaction wants to read, must first acquire the lock in shared mode
  - Several transaction are allowed to hold a lock in shared mode
  - But if any transaction has an exclusive lock, transactions must wait
- If a transaction wants to write an object, it must first acquire the lock in exclusive mode
  - No other transaction may hold the lock at the same time
- If a transaction first reads, and then writes to an object, it may upgrade its shared lock to an exclusive lock
- After a transaction has aquired the lock, it must continue to hold the lock until the end of the transaction
  - This is where the name "two-phase" comes from: the first phase is when the lock is acquired, and the second is when all locks are released

Since so many locks are in use, it can happen easily that transaction A is stuck waiting for transaction B to release its lock, and vice versa - this is called `deadlock`

The db automatically detects deadlocks between transactions and aborts one of them so that others can make progress. The aborted transaction needs to be retried by the application

#### Performance of Two-Phase Locking

The big reason why it hasnt been used by everyone is performance: transaction thrupur and response times of queries are significantly worse under 2PL than under weak isolation

Can have quite unstable latencies

#### Predicate Locks

predicate lock - rather than belonging to a particular object (e.g. one row in a table), it belongs to all objects taht match some search conditions

predicate locks do not perform well: if there are many locks by active transactions, checking for matching locks becomes time-consuming

#### Index-Range Locks

many dbs with 2PL implement `index-range locking` aka `next-key locking` which is a simplified approximation of predicate locking

Index locks are not as precise as perdicate locks (they may lock a bigger range of objects than is strictly necessary to maintain serializability), but since they hav emuch lower overheads, they are a good compromise

### Serializable Snapshot Isolation (SSI)

Provides full serializability, but has only a small performance penalty compared to snapshot isolation

#### Pessimistic vs Optimistic Concurrency Control

optimistic - when a transaction wants to commit, the db checks whether anything bad has happened. if so, abort and retry

#### Decisions Based on an Outdated Premise

How does the db know if a query result might have changed:

- Detecting reads of stale mvcc object version (uncommitted write occured before the read)
- Detecting writes that affect prior reads (the write occurs after the read)

#### Detecting Stale MVCC Reads

By avoiding unnecessary aborts, SSI preserves snapshot isolations support for long-running reads from a consistent snapshot

#### Detecting Writes that Affect Prior Reads

#### Performance of Serializable Snapshot Isolation

Big advantage is taht one transaction doesnt need to block waiting for locks held by another transaction

Not limited to thruput of single cpu core
