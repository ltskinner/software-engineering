# Iterator

### Intent

Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation

### When to Use

* To access an aggregate objects contents without exposing its internal representation
* To support multiple traversals of aggregate objects
* To provide a uniform interface for traversing different aggregate structures

### Participants

* **Iterator**
  * Defines an interface for accessing and traversing elements
* **ConcreteIterator**
  * Implements the Iterator interface
  * KEeps track of the current position in the traversal of the aggregate
* **Aggregate**
  * Defines an interface for creating an Iterator object
* **ConcreteAggregate**
  * Implements the Iterator creation interface to return an instance of the proper ConcreteIterator

### Collaborations

* A ConcreteIterator keeps track of the current object in the aggregate and can compute the succeeding objects in the traversal

### Consequences

* It supports variations in the traversal of an aggregate
* Iterators simplify the Aggregate interface
* Iterators keep track of their own traversal state so more than one traversal can happen at the same time

### Implementation

* Who controls the iteration
  * The client
  * The iterator
* Who defines the traversal algorithm
* How robust is the iterator?
  * Might be dangerous to modify the aggregate while its being traversed
  * Robust iterators are unaffected by inserts and removals
* May want operations other than: First, Next, IsDone, CurrentItem
  * Previous
  * SkipTo
  * etc.
* Proxy patterns are useful

### Related Patterns

* Composites: Iterators are often applied to recursive structures like Composites

* Factory Method: Polymorphic iterators rely on factory methods to instantiate the appropriate Iterator subclass

* Memento is oftenused in conjunction with the Iterator pattern. An iterator can use a memento to capture the state of an iteration

