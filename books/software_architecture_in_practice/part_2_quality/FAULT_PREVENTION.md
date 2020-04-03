# Fault Prevention

## Removal from Service

* Temporarily places a system component out of service to mitigate potential system failures

## Transactions

* ACID transactions to prevent race conditions
  * Atomic, consistent, isolated, durable

## Predictive Model

* A predictive model, combined with a monitor, is employed to monitor the state of health of a system
* Things tracked could be
  * session establishment rate (HTTP)
  * Threshold crossing
  * Process statistic rate
    * In service, out of service, under maintenance, idle
  * Message queue length stats
  * Etc

## Exception Prevention

* Basically want to prevent exceptions from occuring at all
* Use exception classes to transperently recover from system exceptions

## Increase Competence Set

* A programs competence set is the set of states in which it is "competent" to operate
* If a condition, like zero value, is encountered, the system throws in the towel haha
