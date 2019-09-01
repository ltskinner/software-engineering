# Builder

### General Notes

* Builder focuses on constructing a complex object **step-by-step**
  * Abstract Factory emphasizes a family of objects (either simple or complex)
* Builder often builds a composite
* Designs often start out suing Factory method (less complicated, more customizable, subclasses proliferate)
  * Evolve towards:
    * Abstract Factory
    * Prototype
    * Builder
* Builder can use one of the other patterns to implement which components get built

### Intent

Separate the construction of a complex object from its representation so that the same construction process can create different representations

### When to Use

* The algorithm for creating a complex object should be independent of the parts that make uo the object and how theyre assembled
* The construction process must allow different representations for the object thats constructed

### Participants

* **Builder**
  * specifies an abstract interface for creating parts of a Vehicle object
* **ConcreteBuilder** (JeepBuilder)
  * Constructs and assembles parts of the product by implementing the Builder interface
  * Defines and keeps track of the representation it creates
  * Provides an interface for retrieving the product
* **Director**
  * Constructs an object using the Builder interface
* **Product**
  * Represents the complex object under construction
  * ConcreteBuilder builds the preoducts internal representation and defines the process by which its assembled
  * Includes classes that define the constituent parts, including interfaces for assembling the parts into the final result

### Collaborations

* The client creates the Director object and configures it with the desired Builder object
* Director notifies the builder whenever a part of the product should be built
* Builder handles requests from the director and adds parts to the product
* Client retrieves the product from the builder

### Consequences

### Good

* It lets you vary a products internal representation
* It isolates code for construction and representation
* Different directors can use the same Builder to build Product variants
* It gives you finer control over the construction process

### Implementation

* The Builder class interface must be general enough to allow the construction of products for all kinds of ConcreteBuilders

### Related Patterns

* Abstract factory is similar to builder in that it may construct complex objects
  * The primary difference is that the Builder focuses on constructing a complex object step by step
  * Abstract focuses on families of objects
* A Composite is what the builder often builds
