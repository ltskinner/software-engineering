# Fault Recovery

## Active Redundancy (hot spare)

* A configuration where all nodes (active or redundant) in a protection group receive and process identical inputs in parallel
  * This allows the redundant spares to maintain synchronous state with active nodes

## Passive Redundancy (warm spare)

* Only active members process input traffic
* Actives provide spares with periodic state updates

## Spare (cold spare)

* Spares remain out of service until a falure occurs
* Not grat for high availability requirement systems

## Exception Handling

* Like, handle stuff instead of just dying

## Rollback

* Reverts a system back to a previously known good state
* Store these checkpoints somewhere and update them regularly

## Software Upgrade

* Patches and whatnot
* Goal is to achieve in-service upgrades to executable code in a non-service-affecting manner

## Retry

* Assumes the fault that caused a failure is transient and retrying the operation may lead to success
* Common in networks and server farms
* Be sure to limit the number of retries attempted before declaring permanent failure

## Ignore Faulty Behavior

* Calls for ignoring messages sent from a particular source when it is determined that the messages ar spurious
* Like DoS attacks

## Degradation

* Maintains most critical system functions
* Drops less critical ones

## Reconfiguration

* Attempts to recover from component failures by assigning responsibilities to the (potentially restricted) resources left functioning
* While maintaining as much functionality as possible

## Reintroduction

Reintroduces a failed component after it has been corrected

### Shadow

* Operate a previously failed component in "shadow mode" for a predefined duration before reverting it back to an active role
* During this time, a component can be monitored for correctness, and let its state repopulate

### State Resynchronization

* Has different steps to get back in synch (hot vs warm spares)

### Escalating Restart

* Dont restart everything at once, just like incremental

### Non-stop forwarding

* Functionality is split into two parts:
  * Supervisory/Control Plane
  * Data Plane (where work is actually done)
