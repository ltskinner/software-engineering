# Chapter 8: Performance

## 8.1 Performance General Scenario

### Arrival Patterns of Events

* Periodic Events
  * Arrive predictably at regular time intervals
* Stochastic Events
  * Arrive according to some probabilistic distribution
* Sporatic Events
  * Arrive according to a pattern that is neither periodic nor stochastic
  * They may arrive in certain circumstances though

### Response Measurements

* Latency
  * Time between arrival of the stimulis and the systems response to it
* Deadlines in Processing
  * Ex. Fuel should ignite when the cylinder is in a particular position, thus introducing a processing deadline
* Throughput
  * Number of transactions the system can process in a unit of time
* Jitter
  * The allowable variation in latency
* Number of Events Not Processed
  * Typically because the system was too busy to respond

### The General Scenario

* Source
  * Internal or external to the system
* Stimulus
  * Arrival of a periodic, sporatic, or stochastic event
* Artifact
  * System or one or more components in the system
* Environment
  * Operational mode: normal, emergency, peak load, overload
* Response
  * Process events, change level of service
* Response Measure
  * Latency, deadline, throughput, jitter, miss rate

## 8.2 Tactics for Performance

* Processing Time
  * The time that a system is working to respond
* Blocked time
  * The time a system is unable to respond
* Contention for Resources
  * Many resources can only be used by a single client at a time
  * The more contention for a resource, the higher likelihood of latency being introduced
* Availability of Resources
  * Due to a resource being offline or a failure of a component, things might not be available
* Dependency on Other Computation
  * Needs to synch results or get the output of another operation

### Control Resource Demand

Making the demand smaller will require less resource to handle

* Manage Sampling Rate
  * If possible, reduce the frequency at which the stream of environment data is sampled
  * Leads to predictable levels of latency
    * But also comes at the cost of lower fidelity data
* Limit Event Response
  * Deliberately make low bandwidth responses slower so that when the system becomes bogged down the slow responses feel normal
  * This is to the end goal of making response times more predictable
* Prioritize Events
  * If not all events are equally important, can rank them
* Reduce Overhead
  * Intermediaries (used for modifiability) increase resources consumed
  * Come up with system specific solutions that weigh the tradeoffs
* Bound Execution Time
  * Place a limit on how much execution time is used to respond to an event
* Increase Resource Efficiency
  * Improving algorithms used in critical areas will decrease latency

### Manage Resources

Making the resources at hand work more effectively

* Increase Resources
  * Faster processors, additional processors, memory, networks
* Introduce Concurrency
  * If requests can be processed in parallel, the blocked time can be reduced
* Maintain Multiple Copies of Computation
  * Maintaining multiple servers
  * Load balancers distribute work, instead of relying on a single instance
* Maintain Multiple Copies of Data
  * Caching helps
  * Data replication reduces contention from simultaneous access
* Bound Queue Sizes
  * Controls the max number of queued arrivals and consequently the resources used to process arrivals
  * Have to figure out how to handle overflows tho
    * Frequently paired with limit event response tactic
* Schedule Resources
  * Whenever there is contention for a resource, the resource must be scheduled
  * Scheduling policies:
    * First in, first out
    * Fixed priority scheduling
    * Semantic importance (priority the result of a characteristic of the domain that generated the task)
    * Deadline montomic
      * Higher priority to streams with shorter deadlines
    * Rate monotonic
      * Higher priority to periodic streams with the shortest period
    * Dynamic Priority Scheduling
      * Round-Robin
        * Requests are ordered, and get assigned as soon as any resource opens up
      * Earliest Deadline First
      * Least Slack First
        * Slack is the difference between the execution time remaining and the time to the jobs deadline

## 8.3 Performance Checklist

### Allocation of Responsibilities

* [ ] Determine what will have
  * [ ] Heavy loads
  * [ ] Time critical responses
  * [ ] Would impact time critical componennts
* [ ] Find bottlenecks

### Coordination Model

* [ ] Related systems that can benefit from
  * [ ] Concurrency
  * [ ] Event prioritization
  * [ ] Scheduling strategy
* [ ] Can capture event arrivals as needed
  * [ ] Periodic
  * [ ] Stochastic
  * [ ] Sporatic

### Data Model

* [ ] Would multiple copies be benefitial?
* [ ] Will partitioning the data help?

### Choice of Technology

* [ ] Does the technology choice allow
  * [ ] Scheduling a policy
  * [ ] Prioritizing
  * [ ] Policies for reducing demand
