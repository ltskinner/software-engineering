# Publish-Subscribe Pattern

## Overview

* Components publish and subscribe to events
* When an event is announced by a component, the connector infrastructure dispatches the event to all registered subscribers

## Elements

* Any C&C Component
  * Has at least one publish or subscribe port
  * Concerns include which events are published and subscribed to, and the granularity of events
* Publish-Subscribe Connector
  * Must announce and listen for components wishing to act

## Relations

* The *attachment* relation associates components with the publish-subscribe connector
* Done by prescribing which components announce events, and which components are registered to receive events

## Constraints

* All components are connected to an event distributor that may be viewed as either a bus - connector - or a components
* Constraints may restrict which components can listen to which events, whether a component can listen to its own events, and how many publish-subscribe connectors can exist within a system
* A component may be both a publisher and a subscriber, by having ports of both types

## Weaknesses

* Typically increases in latency and has a negative effect on scalability and predictability of message delivery time
* Less control over ordering of messages, and delivery of messages is not guaranteed
