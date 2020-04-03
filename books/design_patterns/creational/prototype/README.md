# Prototype

### Intent

Specify the kinds of obbjects to create using a prototypical instance, and create new objects by copying this prototype

### When to Use

* When a system should be independent of how its products are created, composed, and represented
* When the classes to instantiate are specified at runtime
* To avoid building a class hierarchy of factories that parallels the class hierarchy of products
* When instances of a class can have one of only a few different combinations of state

### Structure

* **Prototype**
  * Declares an interface for cloning itself
* **ConcretePrototype**
  * Implements an operations for cloning itself
* **Client**
  * Creates a new object by asking a prototype to clone itself

### Collaborations

* A client asks a prototype to clone itself

### Consequences

* Hides the concrete product class from the client, reducing the number of names clients now about
* Can add and remove products at runtime
* Can create new objects by varying structure, as opposed to defining new classes
* Reduces the need for subclassing
  * Lets you clone a prototype instead of asking a factory method to create a new object

### Implementation

* Consider using a prototype manager
  * When number of prototypes isnt fixed, keep a registry of available tpyes
  * (clients wont manage it themseleves)
* Be heads up about the clone operation
* When initializing clones, some will want unique internal states

### Related Patterns

* Prototype and Abstract Factory are competing patterns in some ways
  * They can also be used together tho
  * An abstract factory may store a set of prototypes from which to clone
* Designs that make heavy use of the Composite and Decorator can often benefit from Prototype as well
