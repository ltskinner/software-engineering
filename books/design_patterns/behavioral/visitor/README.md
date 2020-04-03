# Visitor

### General Notes

Due to the amount of infighting on stackoverflow posts, combined with the lack of any reasonable explanation or implementation, **this pattern causes more problems than it solves.**

There will be no code implementation of this.

### Intent

Represent an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates

### When to Use

* An object structure contrains many classes of objects with differing interfaces, and you want to perform operations on these objects that depend on their concrete classes
* Many distinct and unrelated operations need to be performed on objects in an object structure, and you want to avoid "polluting" their classes with these operations
* The classes defining the object structure rately change, but you want to define new operations over the structure
  * changing the object structure classes requires redefining the interface to all visitors, which can be costly

### Participants

* **Visitor**
  * Declares a Visit operation for each class of ConcreteElement in the object structure
    * The operations name and signature identifies the class that sends the Visit request to the visitor
* **ConcreteVisitor**
  * Implements each operation declared by Visitor
* **Element**
  * Defines an Accept operation that takes a visitor as an argument
* **ConcreteElement**
  * Implements an Accept operation that takes a visitor as an argument
* **ObjectStructure**
  * Can enumerate its elements
  * May provide a high level interface to allow the visitor to visit its elements
  * May either be a composite or a collection like list or set

### Collaborations

* A client that uses the Visitor pattern must create a ConcreteVisitor object and then traverse the object structure, visiting each element with the visitor
* When an element is visited, it calls the Visitor operation that corresponds to its class.
  * The element supplies itself as an argument to this operations to let the visitor access its state, if necessary

### Consequences

* Visitor makes adding new operations easy
* Visitor gathers related operations and separates unrelated ones
* Adding new ConcreteElement classes is hard

## Related Patterns

* Composite: visitors can be used to apply any operation over an object structure defined by the Composite pattern
* Interpreter: Visitors may be applied to do the interpretation

### Unsurprisingly, both of the related patterns are my least favorite and the least intuitive.
