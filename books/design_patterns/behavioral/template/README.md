# Template

### Intent

Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Themplate Method lets subclasses redefine certain steps of an algorithm withouth changing the algorithms structure

### When to Use

* To implement the invariant parts of an algorithm once and leave it up to subclasses to implement the behavior that can vary
* When common behavior among subclasses should be factored and localized in a common class to avoid code duplication
* To control subclasses extensions

### Participants

* **AbstractClass**
  * Defines abstract **primitive operations** that concrete subclasses define to implement steps of an algorithm
  * Implements a template method defining the skeleton of an algorithm
    * The template method calls primitive operations as well as operations defined in AbstractClass or those of other objects
* **ConcreteClass**
  * Implements the primitive operations to carry out subclass-specific steps of the algorithm

### Collaborations

* ConcreteClass relies on Abstract Class to implement the invariant steps of the algorithm

### Consequences

* Template methods are a fundamental technique for code reuse
* Template leads to an inverted control structure referred to as "The Hollywood Principle" - "Dont call us, well call you"
  * Refers to how a parent class call the operations of a subclass, and not the other way around
* Templates call the following kinds of operations
  * Concrete operations
  * Concrete AbstractClass operations
  * Primitive operations
  * Factory methods
  * Hook operations

### Implementation

* Minimize primitive operations that a subclass must override
  * The more operations that need overridding, the more tedious things get for clients
* Keep a consistent naming convention

### Related Patterns

* Factory Methods are often called by template methods
* Strategy: Template methods use inheritance to vary part of an algorithm. Strategies use delegation to vary the entire algorithm
