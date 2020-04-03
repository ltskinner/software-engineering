# Abstract Factory

### Intent

To provide an interface for creating families of related or dependent objects without specifying their concrete classes

### When to use

* A system should be independent of how its products are
  * created
  * composed
  * represented
* A system should be cconfigured with one of multiple families of products
* A family of related product objects is designed to be used together, and you need to enforce this constraint
  * motif scroller with motif text with motif etc
* You want to provide a class library of products, and you want to reveal just their interfaces, not their implementations

### Participants

* **AbstractFactory**
  * Declares an interface for operations that create abstract product objects
* **ConcreteFactory** (bk, micky-ds)
  * Implements the operations to create concrete product objects
* **AbstractProduct** (burger, drink)
  * Declares an interface for a type of product object
* **ConcreteProduct**
  * Defines the product object to be created by the corresponding concrete factory
  * Implements the AbstractProduct interface
* **Client**
  * Uses only the interfaces declared by the AbstractFactory and AbstractProduct classes

### Consequences

#### Good

* It isolates concrete classes
  * Names of product classes dont appear in client code
* It makes exchanging product families easy
* It promotes consistency among products

#### Bad

* Supporting new kinds of products is difficult
  * Extending to accomadate new products is no bueno

### Implementation Techniques

* Use factories as singletons
* Use the Factory Method to actually create the products
  * Abstract Factory only defines the interface

### Related Patterns

* Factory Method
* Can also be done using Prototype

* A concrete factory is often a Singleton
