# Factory Method

### Intent

Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses

### When to Use

* A class cant anticipate the class of objects it must create
* A class wants its subclasses to specify the objecct it creates
* Classes delegates responsibility to one of several helper subclasses, and you want to localize the knowledge of which helper subclass is the delegate

### Participants

* **Product** (Button)
  * Defines the interface of objects the factory method creates
* **ConcreteProduct** (Image, Input, Flash)
  * Implements the product interface
* **Creator** (ButtonFactory)
  * Declares the factory method, which returns an object of type Button
* **ConcreteCreator**
  * Overrides the factory method to return an instance of a Button

### Collaborations

* Creator relies on its subclasses to define the factory method so that it returns an appropriate instance of the appropriate ConcreteProduct

### Consequences

* Factory methods eliminate the need to bind application-specific classes into your code
* These connect parallel class hierarchies (which is good)

### Implementation

* There are two major varieties of Factory Method
  1. The case when the Creator Class is an abstract class and does not provide an implementation for the catory method it declares
  2. The case when the Creator is a concrete class and provides a default implementation for the factory method.
* Parameterized factory methods let it create multiple kinds of products
  * This is what most of the examples are, using the if-else tree

### Related Patterns

* Abstract factory is often implemented with factory methods
* Factory methods are usually called within Template Methods
* Prorotypes done require subclassing Creator
  * These often require an Initialization operation
  * Factory method does not require Initialization
