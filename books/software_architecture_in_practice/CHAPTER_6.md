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

## 6.3 [Interoperability Checklist](./INTEROPERABILITY_CHECKLIST.md)
