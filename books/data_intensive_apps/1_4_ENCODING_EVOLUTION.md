# Chapter 4. Encoding and Evolution

Idea of evolvability: we should aim to build systems that make it easy to adapt to change

In most cases, a change to an applications features also requires a change to data that it stores

In large applications, code changes often cannot happen instantaneously

- with server-side applications you may want to perform a `rolling upgrade` (also known as a `staged rollout`), deploying the new version to a few nodes at a time, checking whether the new version is running smoothly, and gradually working your way through all the nodes. This allows new versions to be deployed without service downtime, and thus encourages more frequent releases and better evolvability
- with client-side applications, youre at the mercy of the user, who may not install the update for some time

This means that old and new versions of the code, and old and new data formats, may potentially all coexist in the system at the same time. In order for a system to continue running smoothly, we need to maintain compatability in both directions:

- Backward compatability:
  - Newer code can read data that was written by older code
  - Normally not hard to achieve - as the author of newer code, you know the format of old code and can explicitly handle
- Forward compatability:
  - Older code can read data that was written by newer code
  - Trickier because requires older code to ignore additions made by newer versions of the code

## Formats for Encoding Data

Programs usually work with data in (at least) two different representations:

- In memory
  - data is kept in objects, structs, lists, arrays, hash tables, trees, so on
  - data structures are optimized for efficient access an manipulation by the CPU
- On disk and over network
  - Must encode it into some kind of self-contained sequence of bytes (like json)

Thus, we need some kind of translation between the two representation. The translation from in-memory to byte is called `encoding` aka `serialization` or `marshalling`

The reverse is called `decoding` aka `parsing` or `deserialization` or `unmarshalling`

### Language Specific Formats

These are convenient, but have some deep problems:

- encoding is often tied to a particular programming language, so reading data in another language is very difficult
- in order to restore data in the same object types, decoding process needs to be able to instantiate arbitrary classes
  - this is frequently a source of security problems: if an attacker can get your application code to decode an arbitrary byte sequence, they can instantiate arbitrary classes, which in turn often allows them to do bad things
- Versioning data is often an afterthought in these libraries - they often neglect inconvenient probelms of forward and backward compatibility
- Efficiency (cpu time to encode or decode and size of encoded structure) is also an afterthought

For these reasons, generally a bad idea to use built in encoding for anything other than very transient purposes

### JSON, XML, and Binary Variants

Some subtle problems:

- A lot of ambiguity around the encoding of numbers
  - in xml and csv, cannot distinguish between a number and a string that happens to consist of digits
  - in json, it doesnt distinguish integers and floats, nor precision
- json and xml have good support for unicode characters, but dont support binary strings
  - can work around by encoding as base64 but hacky and increases data size by 33%
- there is optional schema support for both xml and json

#### Binary Encoding

MessagePack is good binary encoding for json

### Thrift and Protocol Buffers

#### Field Tags and Schema Evolution

For backwards compatibility, every field you add after the initial deployment of the schema must be optional or have a default value

For forward compatibility, you can only remove fields that are optional (required fields can never be removed)

#### Datatypes and Schema Evolution

Risk that values will lose precision or get truncated

### Avro

#### The Writers Schema and the Readers Schema

writers and readers schema dont have to be the same - just need to be compatible

#### Schema Evolution Rules

#### But What is the Writers Schema

Use cases:

- large files with lots of records
- database with individually written records
  - encode a version number at the beginning of every record so the proper schema can be retrieved
- sending records over a network connection

#### Dynamically Generated Schemas

Avro will generate the schema based on source data structure, and save schema as distinct version

#### Code Generation and Dynamically Typed Languages

### The Merits of Schemas

Binary encodings based on schemas have nice properties:

- They can be much more compact than the various "binary JSON" variants since they can omit fields names from the encoded data
- The schema is a valuable form of documentation, and because the schema is required for decoding, you can be sure that it is up to date (whereas manually maintained documentation may easily diverge from reality)
- Keeping a database of schemas allows you to check forward and backward compatibility of schema changes, before anything is deployed
- For users of statically typed programming languages, the ability to generate code from the schema is useful, since it enables type checking at compile time

## Modes of Dataflow

### Dataflow Through Databases

You can think of storing something in the database as "sending a message to your future self"

#### Different Values Written at Different Times

"data outlives code"

#### Archival Storage

### Dataflow Through Services: REST and RPC

When have processes that need to communicate over a network, there are a few ways of arranging that communication:

- clients and servers
  - api exposed by the server is known as a service

Service Oriented Architecture (SOA) is just a rebranded as Microservices Architecture

#### Web Services

Examples:

- A client applicaiton running on a users device making request to a service over HTTP
- One service making requests to another service owned by the same organization, often located within the same datacenter, as part of a service-oriented/microservices architecture (sometimes this is called `middleware`)
- One service making a erquest to a service owned by a different organization, usually apis

REST and SOAP

SOAP is xml based protocol for making network api requests

#### The Problem with Remote Procedure Calls (RPCs)

Basically, the idea is to treat an api call the same as executing a local function

However, its not, because network issues are involved lmao

- local functions are predictable and either succeed or fail
  - network requests are unpredictable - request or response may be lost, remote machine may be slow or unavailable, problems entirely out of your control so you have to anticipate problems
- a local call either returns a result, throws an exception, or never returns
  - networks may timeout - and you just dont know what happened
- if you try a failed network request again, its still possible the first request worked. must build in mechanism for deduplication (idempotence)
- local calls normally take about the same time to execute, network calls not so much
- when calling local functions, can pass it references to objects in memory
  - have to encode stuff over the wire
- client and service may be implemented in different programming languages

#### Current Directions for RPC

#### Data Encoding and Evolution for RPC

For evolvability, it is important that RPC clients and servers can be changed and deployed independently

Reasonable to assume that all servers will be updated first, and clients second

- only need backward compatibility on requests
- only need forward compatibility on responses

### Message-Passing Dataflow

asynchronous message passing systems

similar to RPC in that a clients request (message) is delivered to another process with low latency

messages go through an intermediary called a `message broker` aka `message queue` or `message-oriented middleware`

Advantages over RPC:

- It can act as a buffer if the recipient is unavailable or overloaded, and thus improve system reliability
- It can automatically redeliver messages to a process that has crashed, and thus prevent messages from being lost
- It avoids the sender needing to know the IP and port of the recipient
- It allows one message to be sent to several recipients
- It logically decouples the sender from the recipient

Communication is one way - a sender normally doesnt expect to receive a reply to its message - asynchronous

#### Message Brokers

- one process sends a message to a `queue` aka `topic`
- broker ensures message delivered to one or more `consumer` aka `subscriber`

#### Distributed Actor Frameworks

The actor model is a programming model for concurrency in a single process

- instead of dealing directly with threads, logic is encapsulated in actors
- each actor typically represents one client or entity, and may have some local state (not shared), and it communicates with other actors by sending and receiving asynch messages
- message delivery is not guaranteed

distributed actor framework spreads this across nodes - essentially integrates a message broker and actor programming model into a single framework
