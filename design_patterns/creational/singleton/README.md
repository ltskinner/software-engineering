# Singleton

### General Notes

* This is less about the client *knowing* there is only one class, and more about programatically preventing the class from being made more than once
* Also, all interface with the class is done through the **Instance** access point

### Intent

Ensure that a class has only one instance, and provide a global point of access to it

### When to Use

* There must be exactly one instance of a class, and it must be accessible to clients from a **well-known access point**
* When the sole instance should be extensible by subclassing, and clients should be able to use an extended instance without modifying their code

### Participants

* **Singleton**
  * Defines an Instance operation that lets clients access its unique instance
  * Instance is a class operation

### Collaborations

* Clients access a Singleton solely through the Singletons Instance operation

### Consequences

#### Good

* Controlled access to sole instance
* Reduced name space
* Permits refinement of operations and representations

### Implementation

* Ensure it is a unique instance
  * Make sure the class is written so that only one class can ever be created
  * Can do this by hiding init behind a class function
    * static or class method
  * Can also maintian registry of singletons

### Related Patterns

* Many patterns can be implemented using the Singleton pattern
  * Abstract Factory
  * Builder
  * Prototype
