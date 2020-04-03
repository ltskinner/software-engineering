# State

### Intent

Allow an object to alter its behavior when its internal state changes. The object will appear to change its class

### When to Use

* An objects behavior depends on it state, and it must change its behavior at run-time depending on that state
* Operations have large, multipart conditional statements that depend on an object state

### Participants

* **Context** (TCPConnection)
  * Defines the interface of interest to clients
  * Maintains an instance of a Concrete State subclass that defines the current state
* **State** (TCPState)
  * Defines an interface for encapsulating the behavior associated with a aprticular state of the Context
* **ConcreteState subclasses** (TCPEstablished, TCPListen, TCPClosed)
  * Each subclass implements a behavior associated with a state of the Context

### Collaborations

* Context delegates state-specific requests to the current ConcreteState object
* A context may pass itself as an argument to the State object hadling the request. This lets the State object access the context if necessary
* Context is the primary interface for clients
* Clients can configure a context with State objects. Once a context is configured, its clients dont have to deal with the State objects directly
* Either Context or the ConcreteState subclasses can decide which state succeeds another and under what circumstances

### Consequences

* It localizes state-specific behavior and partitions behavior for different states
  * New states and transitions can be added easily by defining new subclasses
* It makes state transitions very explicit
* State objects can be shared
  * Like Flyweights

### Implementation

* Who defines state transitions
  * Generally, let the State subclasses themselves specify their sucessor state and then make the transition
  * Downside is this requires adding an interface to the Context that lets State objects set the Contexts current state explicitly
* Can use tables too, which are nice because of their regularity
* Creating and destroying state objects is important as well
  * Can either create as needed and destroy after
  * Or create them ahead of time and never destroy them

### Related PAtterns

* The flyweight epxplains when and how State objects can be shared
* State objects are often Singletons
