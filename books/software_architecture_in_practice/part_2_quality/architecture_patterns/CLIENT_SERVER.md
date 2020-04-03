# Client-Server Pattern

## Overview

* Clients initate interactions with servers
  * Invoke services as needed
  * Wait for the results of those requests

## Elements

* Client
  * Component that invokes services of a server component
  * Clients have ports that describe the services they require
* Server
  * Component that provides services to clients
  * Servers also have ports that describe the services they provide
    * Nature of the prots, how many clients can connect
    * Performance characteristics, max rates of service invocation
* Request/reply connectos
  * A data connector employing a request/reply protocol
  * Dictate if calls are local or remote, and whether data is encrypted

## Relations Constraints

* The *attachment* relation associates clients with servers
* Clients are connected to servers through request/reply connectors
* Server components can be clients ot other servers
* Specializations may impose restrictions on:
  * Number of attachments to a given port
  * Allowed relations among servers
* Components may be arranged in tiers, which are logical groupings of related functionality
  * Or functionality that will share a host computing environment

## Weaknesses

* Server can be a performance bottleneck
* Server can be a single point of failure
* Discussions about where to locate functionality (in the client or server) are often complex and costly to change after a system has been built
