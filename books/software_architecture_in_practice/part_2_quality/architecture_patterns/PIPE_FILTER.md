# Pipe-andFilter Pattern

## Overview

* Data is transformed from a systems external inputs to its external outputs
* This is done through a series of transformations
* Transformations ar performed by its filters, and connected by pipes

## Elements

* Filter
  * A component that transforms data read on its input port to data written on its output port
  * Filters can execute concurrently
  * Filters can also incrementally transform
* Pipe
  * A connector that conveys data from a filters output prots to another filters input ports

## Relations

* The *attachment* relation associates outputs and inputs

## Constraints

* Pipes connect filter output ports to filter input ports
* Connected filters must agree on the type of data being passed along the connecting pipe
* Specializations of the pattern may restrict the association of components to being acyclic
  * --> pipeline
* Other specializations may prescribe certain names ports
  * stdin, stdout, stderr

## Weaknesses

* Not a good choice for interactive systems
* Large number of independent filters can add substantial computational overhead
* May not be appropriate for long running computations
