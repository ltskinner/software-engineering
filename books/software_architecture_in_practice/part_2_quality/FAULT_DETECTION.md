# Fault Detection

## Ping/Echo

* Asynchronous request/response message pair between nodes
* Used to determine reachability and delay across the associated netowrk path

## Monitor

* Component used to monitor the state of health of various other parts of the system
  * Processors, processes, IO, memory

## Heartbeat

* Periodic message exchange between a system monitor and a process being monitored
* The difference between a heartbeat and a ping/echo is who holds responsibility for initiating the health check - the monitor or the ehartbeat itself

## Timestamp

* Used to detect incorrect sequence of events

## Sanity Check

* Checks the validity or reasonableness of specific operations or outputs of a component
* Typically based on a knowledge of the internal design, state of the system, or nature of the information under scrutiny

## Condition Monitoring

* Checking condition in a process or device
* Or validating assumptions made during the design
* Like a checksum

## Voting

* Commonly, the triple modular redundancy (TMR) employs three components to do the same thing
* Differences in outputs are recorded and reported

## Replication

* Simplest form of voting
* Components are exact clones of each other

## Functional Redundancy

* Form of voting
* Components are expected to have the same results, from the same inputs, but they are implemented differently

## Analytic Redundancy

* Components have different inputs, and different internal processes, but are expected to have the same results
* Example is sensor data and aircraft guidance stuff calculated with different measurements

## Exception Detection

* Detection of a system condition that alters the normal flow of execution

### System exceptions

* Faults like divide by zero, bus and address faults, illegal instructions

## Parameter Typing

* Strong typing trades higher availability against ease of evolution

## Timeout

* Tactic that raises an exception when a component detects that it or another componnent has failed to meet its timing constraints

## Self-Test

* Can be run from inside the component, or initiated externally
