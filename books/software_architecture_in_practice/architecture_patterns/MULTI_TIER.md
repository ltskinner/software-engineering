# Multi-tier Pattern

## Overview

* The execution structures of many systems are organized as a set of logical groupings of components
* Each grouping is termed a *tier*
* Can be grouped by
  * Type of component
  * Sharing the same execution environment
  * Having the same runtime purpose

## Elements

* Tier
  * Logical grouping of software components

## Relations

* *Is part of,* to group components into tiers
* *Communicates with,* to show how tiers and the components they contain interact with each other
* *Allocated to,* in the case that tiers map to computing platforms

## Constraints

* A software component belongs to exactly one tier

## Weaknesses

* Substantial up-front cost and complexity
