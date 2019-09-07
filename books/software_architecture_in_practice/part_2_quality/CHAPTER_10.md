# Chapter 10: Testability

"Testing leads to failure, and failure leads to understanding" - the leading to failure is why its so hard to rally to test, and why its so critical

* 30-50% of well engineered systems is taken up by testing
* For a system to be testable, it must be possible to
  * Control each of the components inputs
  * Possibly modify internal state
  * Observe outputs
  * Possibly observe internal state

## 10.1 Testability General Scenario

## 10.2 Tactics for Testability

The goal of tactics is to make for easier testing when an increment of software completed

### Control and Observe System State

* Specialized Interfaces
  * A special testing interface lets you control and capture values through a test harness or normal execution
    * Set and get methods are needed
    * Report methods to see states
    * Resets to clear intetrnal state
    * Method for selecting verbose output, logging levels, resource monitoring
* Record/Playback
  * The state causing a fault can ofted be difficult to re-create
* Localize State Storage
  * Make internal stating state easy to access
  * If buried, makes things annoying
* Abstract Data Sources
  * Making the control of input data easy makes it easy to test
* Sandboxing
  * Isolate an instance of the system from the real world to enable experimentation
* Executable assertions

### Limit Complexity

* Limit Structural Complexity
  * Avoid and resolve cyclic dependencies
  * Reduce dependencies in general
  * Limit inheritance hierarchies
  * Build systems with "eventual consistency" data models, so that eventually all data will reach a constant state
* Limit nondeterminism
  * Limit parallelism?
  * Limit complex control structures (conditionals, loops)

### Other Tips

#### Test Data

* Need to take the time to create a good varied testing dataset
  * The best ones are made by hand

#### Test Automation

* Have to automate as much as possible
* This area is typically underestimated

## 10.3 Testability Checklist

### Allocation of Responsibilities

* [ ] Determine what will run the testing suite
* [ ] Where results are captured

### Coordination Model

* [ ] Can capture faults in between systems
* [ ] Can inject state into communication channels

### Data Model

* [ ] Ensure can capture values of data abstractions
* [ ] Ensure can set data abstraction values

### Resource Management

* [ ] Test resource limits
* [ ] Capture detailed resource logs
* [ ] Inject new resource limits to test with
* [ ] Provide virtualized resources for testing

### Choice of Technology

* [ ] Find best tools to aid in testing
