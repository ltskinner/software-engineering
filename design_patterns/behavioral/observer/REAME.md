# Observer

### Intent

Define aone-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically

This can be though of as a **publish-subscribe** relationship

### When to Use

* When an abstraction has tow aspects, one dependent on the other
  * Encapsulating these aspects in separate objects lets you vary and reuse them independently
* When a change to one object requires changein others, and you dont know how many objects need to be changed
* When an object should be able to notify other objects without making assumptions about who these objects are
  * aka nothing tightly coupled

### Participants

* **Subject**
  * Knows its observers. Any number of Observer objects may observe a subject
  * Provides an interface for attaching and detaching Observer objects
* **Observer**
  * Defines an updating interface for objects that should be notified of changes in a subject
* **ConcreteSubject**
  * Stores state of interest to Concrete Observer objects
  * Sends notification to its observers when its state changes
* **ConcreteObserver**
  * Maintains a reference to a ConcreteSubject object
  * Stores state that should stay consistent with the subjects
  * Implements the Observer updating interface to keep its state consistent with the subjects

### Collaborations

* ConcreteSubject notifies its observers whenever a change occurs that could make its observers state inconsistent with its own
* After being informed of a change in the concrete subject, a ConcreteObserver object may query the subject for information. ConcreteObserver uses this information to reconcile its state with that of the subject

### Consequences

* Can reuse subjectw without resuing observers, and vice versa
* Abstracts the coupling between Subject and Observer
* Support for broadcast communication
* Unexpected updates can arise as the Observers have no knowledge of each other

### Implementation

* Mapping subjects to their observers is a little hairy
  * Book complains about overhead
* Observers may observe more than one subject
  * Need to be consious how the observed items interact
* Who triggers the update?
  * The Subject calls Notify
    * Clients dont have to remember to call notify
    * But may cause several consecutive updates
  * Make clients responsible for calling Notify
    * Avoids useless intermediate updates
    * More errors are likely as clients might forget to call notify
* Need to beware of dangling references to deleted subjects
* Make sure the state of the Subject is consistent before broadcasting
* Notify which subject operations trigger notifications
* Only notify on modifications of interest
* Encapsulate complex update semantics
* Consider combining the Subject and Observer
  * Can make this a Singleton

### Related Patterns

* Mediator: By encapsulating complex update semantics, the ChangeManager acts as a mediator between subjects and observers
* Singleton: The ChangeManager may use the Singleton to make it unique and globally accessible
