# Broker Pattern

## Overview

* The broker pattern defines a runtime component, called a broker, that mediates the communication between a number of clients and servers

## Elements

* Clients - requester of services
* Server - provider of services
* Broker - the intermediary that fulfills the clients request, forwards request to the server, and returns the result to the client
* Client-side proxy - an intermediary that manages the actual communication with the broker
* Server-side proxy - ""

## Relations

* The *attachment* relation associates clients and servers with brokers

## Constraints

* The client can only attach to a broker
* The server can only attach to broker

## Weaknesses

* Brokers add a layer of indirection, and hence latency
* Broker adds up front complexity
* Broker may be a target for security attacks
* Broker may be difficult to test
