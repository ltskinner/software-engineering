# Flyweight

### Intent

Use sharing to support large number of fine-grained objects efficiently

These represent things that are too high in number to each be an object

### When to Use

* An application uses a large number of objects
* Storage costs are high because of the sheer quantity of objects
* Most object states can be made extrinsic
* Many groups of objects may be replaced by relatively few shared objects one extrinsic state is removed
* The application doesnt depend on object identity

### Participants

* **Flyweight**
  * Declares an interface through which flyweights can receive and act on extrinsic state
* **ConcreteFlyweight**
  * Implements the Flyweight interface and adds storage for intrinsic state (if any)
  * A ConcreteFlyweight object must be sharable
  * Any state it stores must be intrinsic - independent of the ConcreteFlyweights context
* **UnsharedConcreteFlyweight**
  * Not all Flyweight subclasses need to be shared
* **FlyweightFactory**
  * Creates and manages flyweight objects
  * Ensures that flyweights are shared properly
* **Client**
  * Maintains a reference to flyweights
  * Computes or stores the extrinsic state of flyweights

### Collaborations

* States that a flyweight needs to function must be characteriszed as either intrinsic or extrinsic
  * Intrinsic is stored in the ConcreteFlyweight object
  * Extrinsic is stored or computed by Client objects
* Clients pass this state to the flyweight when they invoke its operation
* Clients must only get flyweights from the Factory

### Consequences

* Runtime costs associated with transferring, finding and computing will be high
* These costs are offset by space savings
  * Which increase the more flyweights are shared
* Flyweights are fotwn combined with the Composite pattern

### Implementation

* Remove extrinsic state
  * This patterns applicability is largely determined by how easy it is to identify extrinsic state and remove it
* Because objects are shared, they shouldnt be instantiated directly
  * FlyweightFactory lets clients locate a particular flyweight

### Related Patterns

* Flyweight is often combined with the Composite
* Its often best to implement State and Strategy objects as flyweights
