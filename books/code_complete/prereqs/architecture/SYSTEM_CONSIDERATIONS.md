# System Considerations

## Performance

* If performance is a concern, goals need to be specified in the reqs
* Provide estimates and explain why goals are achievable
* Areas at risk of not making goals should be noted and elaborated on

## Resource Management

* Architecture should describe a plan for managing scarce resources such as:
  * Database connections
  * Memory
  * Threads
  * Handles
* **Need to make estimates of all these with justification**

## Scalability

* How will the system address growth in:
  * Number of users
  * Number of servers
  * Number of network notes
  * Number of database records
  * Size of database records
  * Transaction volume
  * Etc.
* If system is not expected to grow and scalability isn’t an issue, that assumption needs to be made explicit
