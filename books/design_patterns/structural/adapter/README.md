# Adapter

### Intent

Convert the interface of a class into an interface that clients expect. Adapters let classes work together that couldnt otherwise because of incompatibel interfaces

aka **Wrapper**

### When to Use

* You want to using an existing class and its interface does not match the one you need
* You want to create a reusable class that cooperates with unrelated or unforseen classes that dont have compatible interfaces
* (*Object adapter only*) you need to use several existing subclasses, but its impractical to adapt their interface by subclassing each one. An object adapter can adapt the interface of its parent class

### Participants

* **Target** (USASocketInterface)
  * Defines the domain specific interface that the client uses
* **Client** (ElectricDevice)
  * Collaborates with objects conforming to the Target interface
* **Adaptee** (Socket)
  * Defines an existing interface that needs adapting
* **Adapter**
  * Adapts the interface of adaptee to the Target interface

### Collaborations

* Clients call operations on an Adapter instance. In turn, the adapter calls Adaptee operations that carry out the request

### Consequences

#### Class Adapter

* Adapts Adaptee to Target by committing to a concrete Adaptee class
  * As a consequence, a class adapter wont work when we want to adapt a class and all its subclasses
* Lets Adapter override some of Adaptees behavior, since Adapter is a subclass of Adaptee
* Introduces only one object, and no additional pointer indirection is needed to get to the adaptee

#### Object Adapter

* Lets a single Adapter work with many Adaptees - that is the Adaptee and all of its subclasses
* Makes it harder to override Adaptee behavior

#### Other Considerations

* How much adapting does the Adapter do
* Pluggable adapters
  * A class is more reusable when you minimize the addumptions other classes must make to use it
* Two way adapters are good for providing transperancy
* Parameterized adapters make things easier?

### Related Patterns

* Bridge has a similar structure to an object adapter, but it has a different intent
  * It is meant to separate an interface from its implementation so that they can be varied easily and independantly
  * An adapter is meant to change the interface of an *existing* object
* Decorator enhances another object without changing its interface
* Proxy defines a representative or surrogate for another object and does not change its interface
