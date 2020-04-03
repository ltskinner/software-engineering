# Memento

### Intent

Without violating encapsulation, capture and externalize an objects internal state so that the object can be restored to this state later

### When to Use

* To save a snapshot (some portion) of an objects state
* And when a direct interface to obtaining the state would expose implmenetation details and break the objects encapsulation

### Participatns

* **Memento**
  * Stores an internal state of the Originator object
* **Originator**
  * Creates a memento containing a snapshot of its current internal state
  * Uses the memento to restore internal state
* **Caretaker**
  * Is responsible for the mementos safekeeping
  * Never operates on or examines the contents of a memento

### Collaborations

* A caretaker requests a memento from an originator, holds it for a time, and passes it back to the originator
* Mementos are passive:
  * Only the originator that created the memnto will assign or retrieve its state

### Consequences

* Preserves encapsulation boundaries
  * Memento avoids exposing information that only an originator should manage
* Simplifies the originator
* BUT, mementos may be expensive

### Implementation

* Mementos have two interfaces
  1. A wide one for originators
  2. A narrow one for other objects
* Mementos should be able to change incremental changes

### Related Patterns

* Command: Commands can use mementos to maintain state for undoable operations
* Iterator: Mementos can be used for iteration as desribed earlier
