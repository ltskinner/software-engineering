# Peer-to-Peer Pattern

## Overview

* Computation is achieved by cooperating peers that request service from and provide services to one another across a network

## Elements

* Peer
  * An independent component running on a network node
  * Can provice routing, indexing, and peer search capability
* Request/reply connector
  * Used to
    * Connect to the peer network
    * Search for other peers
    * Inmvoke services from other peers
  * In some cases, there is no need for a reply

## Relations

* The relation associates peers with their connectors.
* Attachments may change at runtime

## Constraints

* Restrictions may be placed on the following:
  * Number of allowable attachments to any given peer
  * Number of hops used for searching for a peer
  * Which peers know about which other peers
* Some P2P networks are organized with star topologies
  * Where peers only connect to supernodes

## Weaknesses

* Managing security, data consistency, data/service availability, backup, and recovery are all more complex
* Small peer-to-peer systems may not be able to consistently achieve quality goals such as performance and availability
