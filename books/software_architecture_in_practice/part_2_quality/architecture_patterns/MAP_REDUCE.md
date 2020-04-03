# Map-Reduce Pattern

## Overview

* The map-reduce pattern provides a framework for analyzing a large distributed set of data
  * Executes in parallel on a set of processors
  * Has lwo latency and high availability
* The map performs the *extract* and *transform* portions of the analysis
* The reduce performs the *loading* of the results

## Elements

* Map
  * Is a function with multiple instances deployed across multiple processors that performs the extract and transformation portions of the analysis
* Reduce
  * Is a function that may deployed as single instance or as multiple instances across processors to perform the load portion of ETL
* Infrastructure
  * The framework responsible for deploying map and reduce instances
  * Shepards data between them
  * Detects and recovers from failure

## Relations

* Deploy *on* relationship between an instance of a map or reduce function and the processor onto which it is installed
* *Instantiate, monitor, and control* is the relation between the infrastructure and the isntances of map and reduce

## Constraints

* The data to be analyzed must exist as a set of files
* The map functions are stateless and do not communicate with each other
* The only communications between the map instances and the reduce instances is the data emitted from the map instances as <key, value> pairs

## Weaknesses

* If you do not have large datasets, the overhead of map-reduce is not justified
* If you cannot divide the dataset into similar sized subsets, the advantages of parallelism are lost
* Operations that require multiple reduces are complex to orchustrate
