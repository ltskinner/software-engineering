# Chpater 1. Reliable, Scalable, and Maintainable Applications

- Reliability
  - Tolerating hardware and software faults
  - Human error
- Scalability
  - Measuring load and performance
  - Latency percentiles throughput
- Maintainability
  - Operability, simplicity, and evolvability

These days, bigger problems are the amount of data, the complexity of data, and the speed at which it is changing

Many applications need to:

- Store data so they, or another application, can find it later (databases)
- Remember the result of an expensive operation, to speed up reads (caches)
- Allow users to search data by keyword or filter it in various ways (search indexes)
- Send a message to another process, to be handled asynchronously (stream processing)
- Periodically crunch a large amount of accumulated data (batch processing)

## Thinking About Data Systems

- Reliability
  - The system should continue to work *correctly* (performing the correct function at the desired level of performance) even in the face of *adversity* (hardware or software faults, and even human error)
- Scalability
  - As the system *grows* (in data volume, traffic volume, or complexity), there should be reasonable ways of dealing with that growth
- Maintainability
  - Over time, many different people will work on the system (engineering and operations, both maintaining current behavior and adapting the new system to new use cases), and they should all be able to work on it productively

## Reliability

Typical expectations of software:

- The application performs the function that the user expected
- It can tolerate the user making mistakes or using the software in unexpected ways
- Its performance is good enough for the required use case, under the expected load and data volume
- The system prevents any unauthorized access and abuse

Faults are not the same as failute.

- A fault is usuaslly defined as: "one component of the system deviating from its spec"
- failure: "when the system as a whole stops providing the required service to the user

It is impossible to reduce the probability of a fault ot zero, therefore it is usually best to design fault tolerance mechanisms that **prevent faults from causing failures**

In such fault-tolerant systems, can make sense to increase the rates of faults by triggering them deliberately - like randomly killing individual processes without warning. Think chaos monkey

### Hardware Faults

### Software Errors

- Think carefully about assumptions and interactions in the system
- Test thoroughly
- Isolate processes
- Allow processes to crash and restart
- Measure, monitor, and analyze system behavior in production

### Human Errors

One study found that the leading cause of outages were configuration errors by operators

How do we make our systems reliable, in spite of unreliable humans?

- Design systems in a way that minimizes opportunities for error.
  - Well designed abstractions, apis, admin interfaces that make it easy to "do the right thing"
- Decouple the places where people make the most mistakes from places where they can cause the most failures
  - Provide fully featured non-production sandboxes
- Test thoroughly at all levels, from unit tests, to system wide integration tests, and manual tests
- Allow quick and easy recovery from human errors to minimize the impact in case of a failure
  - make rolling back config changes fast
  - make rolling out new code slow (so only impact some users and you can catch before impacting everyone)
  - provide tools to recompute data (in case it turns out that the old computation was incorrect)
- Set up detailed and clear monitoring, such as performance metrics and error rates
- Implement good management practices and training

## Scalability

Even if a system is working reliably today, that doesnt mean it will necessarily work reliably in the future. Increase of load typically leads to degridation

Scalability is the term we use to describe a systems ability to cope with increased load

### Describing Load

Load can be described with a few numbers which we call *load parameters*

The best choice of parameters depends on the architecture of your system:

- requests per second to a web server
- ratio of reads to writes in a database
- number of simultaneously active users in a chat room
- the hit rate on a cache
- etc

### Describing Performance

Two ways to look at:

- When you increase a load parameter and keep the system resources (cpu, memory, network bandwidth, etc) unchanged, how is the performance of your system affected?
- When you increase a load parameter, how much do you need to increase the resources if you want to keep performance unchanged

Latency and Response time

- response time - what the client sees
- latency - the duration that a request is waiting to be handled

Response times can vary a lot - think of response time not as a single number, but as a distribution of values that you can measure

- Use `percentiles`

### Approaches for Coping with Load

Will likely need to rethink architecture on every order of magnitude load increase

- scaling up: vertical scaling (more powerful machine)
- scaling out: horizontal scaling (distributing)

The architecture for a system designed to handle:

- 100,000 requests per second, each 1kb
- 3 requests per minute, each 2GB

Are dramatically different, despite having the same throughput

## Maintainability

Majority of cost of software is not in initial development, but in:

- ongoing maintenance
- fixing bugs
- keeping systems operational
- adapting it to new platforms
- modifying it for new use cases
- repaying technical debt
- adding new features

Pay particular attention to:

- Operability
  - Make it easy for operations teams to keep system running smoothly
- Simplicity
  - Make it easy for new engineers to understand the system, by removing as much complexity as possible from the system
- Evolvability
  - Make it easy for engineers to make changes to the system in the future, adapting it for unanticipated use cases as requirements change
  - Also known as extensibility, modifiability, or plasticity

### Operability: Making Life Easy for Operations

Good ops teams are typically responsible for the following:

- Monitoring the health of the system and quickly restoring service if it goes into a bad state
- Tracking down the cause of problems, such as system failures or degraded performance
- Keeping software and platforms up to date, including security patches
- Keeping tabs on how different systems affect each other, so that a problematic change can be avoided before it causes damage
- Anticipating future problems and solving them before they occur (e.g. capacity planning)
- Establishing good practices and tools for deployment, configuration management, and more
- Performing complex maintenance tasks, such as moving an application from one platform to another
- Maintaining the security of the system as configuration changes are made
- Defining processes that make operations perdictable and help keep the production environment stable
- Preserving the organizations knowledge about the system, even as individual people come and go

Good operability means making routine tasks easy, allowing the ops team to focus on high-value activities. Data systems can do various things to make routine tasks easy:

- Providing visibility into the runtime behavior and internals of the sytem, with good monitoring
- Providing good support for automation and integration with standard tools
- Avoiding dependency on individual machines (allowing machines to be taken down for maintenance while the system as a whole continues running unintrrupted)
- Providing good documentation and an easy-to-understand operational model ("if I do X, Y will happen")
- Providing good default behavior, but also giving administrators the freedom to override defaults when needed
- Self healing where appropriate, but also giving administrators manual control over the system state when needed
- Exhibiting predictable behavior, minimizing surprises

### Simplicity: Managing Complexity

### Evolvability: Making Change Easy
