# Composite

### General Notes

Pretty recursive

### Intent

Compose objects into tree structures that represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly

### When to Use

* You want to represent part-whole hierarchies of objects
* You want clients to be able to ignore the difference between compositions of objects and individual objects
  * Clients will treat all objects in the composite uniformly

### Participants

* **Component**
  * Declares the interface for objects in the composition
  * Implements default behavior for the interface common to all classes
  * Declares an interface for accessing and managing its child components
* **Leaf**
  * Represents leaf objects in the composition. A leaf has no children
  * Defines behavior for primitive objects in the composition
* **Composite**
  * Defines behavior for components having children
  * Stores child components
  * Implements child-related operations in the Component interface
* Client
  * Manipulates objects in the composition through the component interface

### Collaborations

* Clients use the Component class interface to interact with objects in the composite structure
  * If the recipient is a Leaf, then the request is handled directly
  * If the recipient is a Composite, then it usually forwards the request to its child components

### Consequences

* Makes clients simple
  * Client dont know and dont care whether theyre dealing with a composite or a componenet
* Makes adding new components easy
* Can make design overly general

### Implementation

* Maintain explicit references from child components to parent components
* Try to maintain one and only one parent
  * Multiple parents makes sharing components difficult
* Define as many common operations as possible
* Need to be conscious of child ordering
  * Iterator pattern can help with this
* Cache to improve performance

### Related Patterns

* Often the component-parent link is used for Chain of Responsibbility
* Decorator is often used with Composite
  * When decorators and composites are used together, they will usually have a commmon parent class
  * So, Decorators will have to support the Component interface with operations like Add, Remove, and GetChild
* Flyweight lets you share components, but they can no longer refer to their parents
* Iterator can be used to traverse composites
* Visitor localizes operations and behavior that would otherwise be distributed across Composite and Leaf classes
