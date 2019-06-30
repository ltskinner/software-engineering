# Command

### General Notes

These are good for **history** based operations like **undo** and **redo**. These were not implemented in the example but are still good to be aware of

### Intent

Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations

aka. **Action** or **Transaction**

### When to Use

* To parameterize objects by an action to perform. These can be expressed as a **callback** function - a function registered to be called at a later point
* To specify, queue, and execute requests at different times
* To support undo (reversing th effect of the command)
* To support logging changes so they can be reapplied in the case of a system crash
* To structure a system around high level operations built on primitive operations

### Participants

* **Command**
  * Declares an interface for executing an operation
* **ConcreteCommand**
  * Defines a binding between a Reciever object and an action
  * Implements Execute by invoking the corresponding operations on Receiver
* **Client**
  * Creates a ConcreteCommand object and sets its receiver
* **Invoker**
  * Asks the command to carry out the request
* **Receiver**
  * Knows how to perform the operations associated with carrying out a request. Any class may serve as a Receiver

### Collaborations

* The client creates a Concretecommand object and specifies its receiver
* An Invoker object stores the ConcreteCommand object
* The invoker issues a request by calling Execute on the command. When the commands are undoable, ConcreteCommand stores state for undoing the command prior to invoking Execute
* The Concretecommand object invokes operations on its receiver to carry out the request

### Consequences

* Command decouples the object that invokes the operation from the one that knows how to perform it
* Commands are first-class objects. They can be manipulated and extended like any other object
* You can assemble commands into a composite command.
  * In general, composite commands are an instance of the Composite pattern
* Its easy to add new commands because you dont have to change existing classes

### Implementation

* Consider how intelligent a command should be
  * Delegate responsibility or do it all itself?
* Supporting undo and redo
  * Need to store additional states
  * Avoid error accumulation in the undo process

### Related Patterns

* A Memento can keep states that the command requires to undo its effect
