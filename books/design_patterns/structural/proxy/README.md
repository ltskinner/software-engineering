# Proxy

### Intent

To provide a surrogate or placeholder for another object to control access to it

This is good for deferring the full cost of creation and initialization until it actually needs to be used

### When to Use

* A **Remote Proxy** provides a local representative for an object in a different address space
* A **Virtual Proxy** creates expansive objects on demand
  * Like images and whatnot - maybe big data or cuda handle
* A **Protection Proxy** is used to protect access rights
* A **Smart Reference** is a replacement for a bare pointer that performs additional actions when an object is accessed

### Participants

* **Proxy**
  * Maintains a reference that let the proxy access the real subject
  * Provides an interface identical to the Subjects so taht a proxy can be substituted for the real object
  * Controls access to the real subject and may be responsible for creating and deleting it
  * *Remote Proxies* are responsible for encoding a request and its arguments,a nd for sending the encoded request to the real subject in a different address space
  * *Virtual Proxies* may cache additional information about the real subjects so they can postpone accessing it
  * *Protection Proxies* check that the caller has access permisions required to perform a request
* **Subject**
  * Defines the common interface for RealSubject and Proxy so the Proxy can be used anywhere a RealSubject is expected
* **RealSubject**
  * Defines the real object that the proxy represents

### Collaborations

* Proxy forwards requests to RealSubject when appropriate, depending on the type of proxy

### Consequences

* Creates indirection which is useful
  * A proxy can hide the fact that an object resides in a different address space
  * A virtual proxy can perform optimizations such as creating an object on demand
  * Both protection proxies and smart references allow additional housekeeping tasks when an object is accessed

### Implementation

* Proxies dont *always* need to know info about the concrete class
  * Sometimes they do but like not really

### Related Patterns

* Adapters provide a different interface tot he object it adapts Proxies provide the same interface, and is used for protection
* Decorators add one or more responsibilities to an object, while proxies may or may not add responsibilities.
