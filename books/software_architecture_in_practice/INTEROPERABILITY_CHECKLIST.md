# Interoperability Checklist

## Allocation of Responsibilities

* [ ] Determinw which parts of the system will need to interoperate
* [ ] Ensure system is able to detect requests to interoperate
  * [ ] From unknown external systems
* [ ] Ensure have handling for
  * [ ] Accepting the request
  * [ ] Exchanging information
  * [ ] Rejecting the request
  * [ ] Notification of people or systems
  * [ ] Logging the request

## Coordination Model

* [ ] Consider volume of traffic on systems in your control and out of your control
* [ ] Consider timliness of messages sent by system
* [ ] Consider currency of messages sent by system
* [ ] Jitter of the messages arrival times
* [ ] Ensure systems under your control make assumptions about protocols and networks that are consistent with systems not under your control

## Data Model

* [ ] Determine syntax and semantics of major data abstractions
* [ ] Ensure abstractions are consistent with interoperating systems

## Mapping among Architectural Elements

* [ ] Ensure communication lines are protected and in good shape

## Resource Management

* [ ] Ensure engaging in an external request never exhausts critical resources

## Binding Time

* [ ] Ensure a policy for dealing with binding to both known and unknown external systems
* [ ] Ensure mecahnisms to reject unacceptable bindings and to log those requests
* [ ] Ensure mechanisms will support discovery of relavent new services or protocols, or the sending of info via a chosen protocol

## Choice of Technlology

* [ ] Are chosen technologies "visible" at the boundary interface?
  * [ ] Ensure effects of choices are acceptable
* [ ] Consider technologies deliberately design to support interoperability
  * [ ] WS*
