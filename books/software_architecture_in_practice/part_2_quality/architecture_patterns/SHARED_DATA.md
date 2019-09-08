# Shared-Data Pattern

## Overview

* Communication between data accessors is mediated by a shared data store
* Control may be initiated by the data accessors or the data store
* Data is persisted by the data store (??)

## Elements

* Shared-data store
  * Concerns include types of data stored, data performance-oriented properties, data distribution and number of accessors permitted
* Data accessor component
* Data reading and writing connector
  * An important choice here is whether the connector is transactional or not, as well as the read/write language, protocols, and semantics

## Relations

* **Attachment** relation determines which data accessors are connected to which data stores

## Constraints

* Data accessors interact with the data store(s)

## Weaknesses

* The shared-data store may become a performance bottleneck
* The shared-data store may be a single point of failure
* Producers and consumers of data may be tightly coupled
