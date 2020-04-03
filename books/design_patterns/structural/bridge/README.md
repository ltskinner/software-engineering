# Bridge

### General Notes

The lack of implementation examples has me doubt how widespread this is used

### Intent

Decouple an abstraction from its implementation so that the two can very independently

aka. **Handle**

### When to Use

* You want to avoid a permanent binding between an abstraction and its imlpementation
  * This is good when the implementation must be selected or switched at run-time
* Both the abstractions and their implementations should be extensible by subclassing
  * In this case, the Bridge lets you combine multiple subclasses and implementations and extend them independently
* Changes in the implementation of an abstraction should have no impacts on clients
  * aka no need to recompile

### Participants

* **Abstraction** (ClientInterface/Bridge)
  * Defines the abstractions interface
  * Maintains a reference to an object of type Implementor
* **ExtendedAbstraction** (InterfaceVariant)
  * Extends the interface defined by the abstraction
* **Implementor** (ImplementationInterface)
  * Defines the interface for implementation classes
  * These interfaces can be quire different than the abstraction interface
* **ConcreteImplementor** (WindowsInterface)
  * Implements the Implementor interface and defines its concrete implementation

### Collaborations

* Abstraction forwards client requests to its Implementor object

### Consequences

* Decouples interface and implementation
  * An implementation is not bound permanently to an interface
  * The implementation of an abstraction can be configured at run time
  * Removes compile-time dependencies
* Improves extensibility
  * Can extend the Abstraction and the Implementor hierarchies independently
* Hides implementation details from clients

### Implkementation

* Ensure theres only one Implementor
* Create the right Implementor object

### Related Patterns

* An Abstract Factory can create and configure a particular Bridge
* An Adapter pattern is geared towards making unrelated classes work together. Bridge is used up-front in a design to let abstractions and implementations vary independently
