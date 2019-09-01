# Mediator

### Intent

Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently

### When to Use

* A set of objects communicate in well-defined but coomplex ways.
  * The resulting interdependencies are unstructured and difficult to understand
* Reusing an object is difficult because it refers to and communicates with many other objects
* A behavior thats distributed between several classes should be customizable without a lot of subclassing

### Participants

* **Mediator**
  * Defines an interface for communicating with Colleague objects
* **ConcreteMediator**
  * Implements cooperative behavior by coordinating Colleague objects
  * Knows and maintains its colleagues
* **Colleage Classes**
  * Each Colleague class knwos its Mediator object.
  * Each colleague communicates with its mediator whenever it would have communicated with another colleague

### Collaborations

* Colleagues send and receive requests from a Mediator object. The mediator implements the cooperative behavior by routing requests between the approriate colleagues

### Consequences

* Limits subclassing
* Decouples collegaues
* Simplifies object protocols
  * Replaces many to many with one to many
* It abstracts how objects cooperate
* Centralizes control
  * Which can make the Mediator a monolith thats difficult to maintain

### Implementation

* No need to define an abstract mediator class
* Colleagues shoudl only communicate with their mediator when an event of interest occurs

### Related Patterns

* Facade differs from Mediator in that it abstracts a subsystem of objects to provide a more conveniant interface
  * Essentially, Facade is unidirectional in that it makes requests fo the subsystem, but the subsystem does not make requests of it

* Colleagues can communicate with the mdeiator using the Observer pattern
