# Facade

### General Notes

This is about reducing complexity and minimizing communications

These are pretty general too

Can think of these as an adapter to multiple objects

### Intent

Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystems easier to use

### When to Use

* You want to provide a simple interface to a complex subsystem
* There are many dependencies between clients and the implementation classes of an abstraction
* You want to layer your subsystem

### Participants

* **Facade**
  * Knows which subsystem classes are responsible for a request
  * Delegates client requests to appropriate subsystem objects
* **Subsystem Classes**
  * Implement subsystem functionality
  * Handle work assigned by the Facade object
  * Have no knowledge of the facade

### Collaborations

* Clients communicate with the subsystem by sending requests to Facade, which are then forwarded to the appropriate subsystem
* Clients that use the Facade dont have to access its subsystem objects directly

### Consequences

* It shields clients from subsystem components
  * Makes things easier to use
* Promotes weak coupling between the subsystem and its clients
* Doesnt prevent applications from using subsystem classes if they need to

### Implementation

* Reduces client-subsystem coupling
* They are like classes in that they both have interfaces and encapsulate something

### Relateed Patterns

* Abstract Factory can be used with Facade to provide an interface for creating subsystem objects in a subsystem independent way
  * Abstract Factory can also be used as an alternative to Facade to hide platform-specific classes
* Mediator is similar to facade in that it abstracts functionality of existing classes
  * Mediator does centralize functionality that doesnt belong to any one of them
  * Facade just makes things easier to use lmao
* Facades are often singletons
