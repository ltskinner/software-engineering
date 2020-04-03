# Interoperability

Interoperability is the degree to which two or more systems can usefull exchange meaningful information via interfaces in a particular context

* Discovery: The consimer of a service must discover the location, identity, and the interface of the service
* Handling of the Response
  * Service reports back to the requester with the response
  * Service sends its response on to another system
  * Service broadcasts its response to any interested parties

## 6.1 Interoperability General Scenario

### SOAP vs REST

SOAP offers completeness, REST offers simplicity

### SOAP

* XML based information
* Works with WS* (Web Service)

### REST

* Maintains CRUD operations
  * Create, read, update, delete
* Easy URI interface

## 6.2 Tactics for Interoperability

### Locate

* Discover services
  * Locate a service by searching its known directory service

### Manage Interfaces

* Orchustrate
  * For coordinating, managing and sequencing the invocation of particular services
  * Basically, "scripts" interactions
* Tailor Interface
  * Adds or removes capabilities to an interface
  * Like translation, buffering, smoothing data

## 6.3 Interoperability Checklist

### Allocation of Responsibilities

* [ ] Determinw which parts of the system will need to interoperate
* [ ] Ensure system is able to detect requests to interoperate
  * [ ] From unknown external systems
* [ ] Ensure have handling for
  * [ ] Accepting the request
  * [ ] Exchanging information
  * [ ] Rejecting the request
  * [ ] Notification of people or systems
  * [ ] Logging the request

### Coordination Model

* [ ] Consider volume of traffic on systems in your control and out of your control
* [ ] Consider timliness of messages sent by system
* [ ] Consider currency of messages sent by system
* [ ] Jitter of the messages arrival times
* [ ] Ensure systems under your control make assumptions about protocols and networks that are consistent with systems not under your control

### Data Model

* [ ] Determine syntax and semantics of major data abstractions
* [ ] Ensure abstractions are consistent with interoperating systems

### Mapping among Architectural Elements

* [ ] Ensure communication lines are protected and in good shape

### Resource Management

* [ ] Ensure engaging in an external request never exhausts critical resources

### Binding Time

* [ ] Ensure a policy for dealing with binding to both known and unknown external systems
* [ ] Ensure mecahnisms to reject unacceptable bindings and to log those requests
* [ ] Ensure mechanisms will support discovery of relavent new services or protocols, or the sending of info via a chosen protocol

### Choice of Technlology

* [ ] Are chosen technologies "visible" at the boundary interface?
  * [ ] Ensure effects of choices are acceptable
* [ ] Consider technologies deliberately design to support interoperability
  * [ ] WS*
