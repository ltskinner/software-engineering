# Service-Oriented Architecture Pattern

## Overview

* Computation is achieved by a set of cooperating components that provide and/or consume services over a network
* Computation is often described using a workflow language

## Elements

### Components

* Service Providers
  * Which provide one or more services through published interfaces
  * Concerns are often tied to the chosen implementation technology
    * Include performance, authorization constraints, availability, and cost
* Service Consumers
  * Invoke services directly or through an intermediary
* Service providers
  * May also be service consumers
* ESB
  * Intermediary element that can route and transform messages between service providers and consumers
* Registry of Services
  * Used by providers to register their services and by consumers to discover services at runtime
* Orchustration Server
  * Which coordinates the interactions between service consumers and providers based on languages for business processes and workflows

### Connectors

* SOAP Connector
  * Which uses SOAP protocol for synchronous comms between WS - typically HTTP
* REST Connector
  * Relies on basic request/reply operations of the HTTP protocol
* Asynchronous Messaging Connector
  * Uses a messaging system to offer point-to-point or publish-subscribe asynch message exchanges
 
## Relations

* Attachment of the different kinds of components available to the respective connectors

## Constraints

* Service consumers are connected to service providers, but intermediary components (ESB, registry, orchustration server) may be used

## Weaknesses

* SOA-based systems are typically complex to build
* You dont control the evolution of independent services
* There is a performance overhead associated with the middleware, and services may be performance bottlenecks, and typically do not provide performance guarantees
