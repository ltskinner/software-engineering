# Strategy

### Intent

Define a family of algorithms, encapsulate each one, and make them interchangable

### When to Use

* Many realted classes differ only in their behavior. Strategies provide a way to configure a class with one o fmany behaviors
* You need different variants of an algorithm
  * For example, same algorithm reflecting different space and time restraints
  * (like the SI Clustering)
* An algorithm uses data that the clients shouldnt know about
  * Dont wanna expose data, or the algorithm itself
* A class defines many behaviors, and these appear as multiple conditional statements in its operations.
  * Instead of many conditionals, move related conditional branches into their own Strategy class

### Participants

* **Strategy**
  * Declares an interface common to all supported algorithms
  * Context uses this interface to call the algorithms defined by a ConcreteStrategy
* **ConcreteStrategy**
  * Implements the algorithm using the Strategy interface
* **Context**
  * Is configured with a ConcreteStrategy object
  * Maintains a reference to a Strategy object
  * May define an interface that lets Strategy access its data

### Collaborations

* Strategy and Context interact to implement the chosen algorithm. A context may pass all data required by the algorithm to the strategy when the algorithm is called
  * Or, the context can pass itself as an argument to Strategy operations. This lets the strategy call back on the context as required
* A context forwards requests from its clients to its strategy
  * Clients usually create and pass a ConcreteStrategy object to the context
    * After that, the client interacts with the context almost exclusively
  * There is often a family of ConcreteStrategy objects the client can choose from

### Consequences

* Can use subclassing to factor out common functionality
* Strategies eliminate conditional statements
* Need to make sure clients are aware of different Strategies for them to choose from
* Strategy interface is shared by all ConcreteStrategy classes whether they use all the parameters or not
* Strategy increases the number of objects in an application

### Implementation

* First, need to define the Strategy and context interfaces
  * A couple different ways to do this with trade offs
  * Have the Context pass data in parameters to Strategy operations
    * Keeps them decoupled?
    * Context may pass data that the Strat doesnt need
  * Have the Context pass *itself* as an argument
    * Now, Context must define a more elaborate interface to its data which makes Strategy and Context more coupled
  * Basically, see what the needs of the algorithm are
* Make Strategy objects optional
  * Have Context carry out default behavior

### Related Patterns

* Flyweight: Strategy objects often make good flyweights
