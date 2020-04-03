# Decorator

### General Notes

This is to add functionality to a specific object, not an entire class.

"Change the skin - not the guts"

### Intent

Attach additional responsibilities to an object dynamically. Decorators provice a flexible alternative to subclassing for extending functionality

### When to Use

* To add responsibilities to individual ojects dynamically and transperently (without affecting other objects)
* For responsibilities that can be withdrawn
* When extension by subclassing is impractical

### Participants

* **Components**
  * Defines the interface for objects that can have responsibilities added to them dynamically
* **ConcreteComponent**
  * Defines an object to which additional responsibilities can be attached
* **Decorator**
  * Maintains a reference to a Component object and defines an interface that conforms to Components interface
* **ConcreteDecorator** (BorderDecorator, ScrollDecorator)
  * Adds responsibilities to the component

### Collaborations

* Decorator forwards requests to its Component object. It may perform additional operations before and after forwarding the request

### Consequences

* More flexibility than static inheritance
  * Added and removed at runtime
* Offer a pay as you go approach
  * No need for feature-laden classes high in the hierarchy
* Typcially, decorator dense systems have lots of little and similar objects

### Implementation

* A decorator objects interface must conform to the interface of the component it decorates
  * (inherit from common classes)
* Dont ened to use an abstract Decorator - just roll it out raw
* Need everything to inherit from a common Component class
  * Helps to keep this Component as simple as possible
  * (dont put lots of functionality in it)

### Related Patterns

* Adapter: A decorator is different in that it changes the objects responsibilites, not the interface

* Composite: A decorator can be viewed as a degenerate composite with only one component

* Strategy: A decorator lets you change the skin, a strategy lets you change the guts

