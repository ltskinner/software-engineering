# Chain of Responsibility

### Intent

Avoid coupling the sender of the request to its receiver by giving more than one object a change to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it

### When to Use

* More than one object may handle a request, and the handler isnt known at the time the request was initiated
  * The handler should be ascertained automatically
* You want to issue a request to one of several objects without specifying the receiver explicitly
* The set of objects that can handle a request should be specified dynamically

### Participants

* **Handler**
  * Defines an interface for handling requests
  * (Optional) implements the successor link
* **ConcreteHandler**
  * Handles request it is responsible for
  * Can access its successor
  * If the Concrete Handler can handle the request, it does so
  * Otherwise, it forwards the request to its successor
* **Client**
  * Initiates the request to a ConcreteHandler object on the chain

### Consequences

* Reduced coupling
  * Both the sender and receiver have no knowledge of each other
  * Just trust that the request will be handled appropriately
* Simplified object interconnections
  * Just a single reference to successor is maintained
* Can add and remove objects to the chain at runtime
* !! Reciept isnt guaranteed - if not configured properly some requests may go unprocessed

### Implementation

* Two possible ways to implement the successor chain
  1. Define new links
  2. Use existing links
* Connect all successors
* Create implementation for representing requests

### Related Patterns

* CoR is often used with a Composite. There, a components parent can act as its successor

