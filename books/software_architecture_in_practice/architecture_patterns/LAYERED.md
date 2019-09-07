# Layered Pattern

## Overview

* The layered pattern defines layers (groups of modules) that have unidirectional *allowed-to-use* relation among the layers

## Elements

* Layer, a kind of module
* The description of a layer should define what modules the layer contain, and a characterization of the set of services the layer provides

## Relations

* Allowed to use
* Defines what the layer usage rules are
  * And allowable exceptions

## Constraints

* Every piece of software is allocated to exactly one layer
* There are at least two layers (but typically three or more)
* The *allowed-to-use* relation should not be circular

## Weaknesses

* The addition of layers adds up-front cost and complexity
* Layers contribute a performance penalty
