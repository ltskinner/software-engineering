# Chapter 9: Security

## CIA Triangle

* Confidentiality
  * Data/services are protected from unauthorized access
* Integrity
  * Data/services are not subject to unauthorized manipulation
* Availability
  * System will be available for legitimate use

### Other Characteristics

* Authentification
  * Verifies the identities of the parties to a transaction
* Nonrepudiation
  * The sended of the message cannot deny having sent it
* Authorization
  * Grants privileges to perform a task

## 9.1 General Security Scenario

## 9.2 Tactics for Security

### Detect Attacks

* Detect Intrusion
  * Compare network traffic or service request patterns
* Detect Service Denial
  * Compare network traffic to patterns and signatures
* Verify Message Integrity
  * Use checksums to verify messages, resource files, deployment files, configuration files
* Detect Message Delay
  * Indicative of man in the middle

### Resist Attacks

* Identify Actors
  * Really just finding the source of any external input to the system
  * Either malicious or legitimate, need to know whos doing what
* Authenticate Actors
  * Ensure actors are who they say they are
* Authorize Actors
  * Access control policies
* Limit Access
* Limit Exposire
  * Concealing information about the system
  * Dividing and distributing critical resources (not all eggs in one basket)
* Encrypt Data
* Separate Entities
  * Never hurts to break things into compartments
* Change default settings
  * Most OTS things have default values, change those

### React to Attacks

* Revoke Access
  * Even to legit users
* Lock Computer
  * Like after too many login attempts
* Inform Actors
  * Make sure operators, other personnel and cooperating systems are aware

### Recover from Attacks

* Mostly need to restore services
* Maintain audit trail to help identify attackers

## 9.3 Security Checklist

### Allocation of Responsibilities

* [ ] Identify the actor
* [ ] Authenticate the actor
* [ ] Authorize the actor
* [ ] Grant or deny access
* [ ] Record attempts to access or modify
* [ ] Encrypt data
* [ ] Recognize reduced availability and inform those affected
* [ ] How to recover from an attack
* [ ] Verify checksums and hash values

### Coordination Model

* [ ] Confirm who is allowed to talk to who
* [ ] Authenticate and authorize communication channels

### Data Model

* [ ] Determine sensitivity of different data fields
* [ ] Split data accordingly
* [ ] Log access to sensitive data
* [ ] Ensure data can be restored if inappropriately modified

### Mapping

* [ ] Determine alternate mappings of elements and how those would effect access to data or services

### Resource Management

* [ ] Monitor, record and notify activity
* [ ] Ensure contaminated elements can be quarantined
