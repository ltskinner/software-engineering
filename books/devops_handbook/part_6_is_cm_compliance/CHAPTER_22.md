# Chapter 22: Information Security as Everyones Job, Every Day

## Integrate Security into Development Iteration Demonstrations

## Integrate Security into Defect Tracking and Port-Mortems

* This is different from how Infosec has traditionally worked
* Used to be kep in GRC tools (governance, risk and compliance)

## Integrate Preventative Security Controls Into Shared Source Code Repositories and Shared Services

* Code libraries and their reccomended configurations
  * 2Fa, bcrypt password hashing, logging
* Secret management
  * connection settings
  * encryption keys
  * Vault, sneaker, Keywhiz, credstash, Trousseau, Red October
* OS Packages and Builds
  * NTP for time syncinc
  * Secure versions of OpenSSL
  * OSSEC ot Tripwire for file integrity
  * syslog config for logging to central ELK stack

## Integrate Security Into Our Development Pipeline

## Ensure Security of the Application

* Test with `sad/bad paths` that only serve to test when things break
  * As opposed to `happy paths` where everything works fine

### Things to test

* Static Analysis
  * Non runtime environment, ideally in deployment pipeline
  * Inspect program code for all possible runtime behaviors
  * Seek out coding flaws, back doors, banned code functions ("exec()")
  * -> Brakeman, Code Climate
* Dynamic Analysis
  * Testing done while program is running
  * Monitor memory, functional behavior, response time, performance
  * -> Arachni and OWASP ZAP
  * -> Nmap and Metasploit
* Dependency Scanning
  * Gemnasium, OWASP Dependency-Check
* Source code integrity and signing
  * Each developer should have their own PGP key
  * Sign each commit
  * All CI packages should be signed too

## Ensure Security of Our Software Supply Chain

* Make sure youre not using OSS that has known vulnurabilities (as best as possible lmao)

## Ensure Security of the Environment

## Integrate Information Security Into Production Telemetry

### Creating Telemetry in Our Applications

* Successful and unsuccessful user logins
* User password resets
* User email address resets
* User credit card changes

### Creating Security Telemetry in our Environment

* OS Changes (in prod, build infrastructure)
* Security group changes
* Changes to configurations (OSSED, Puppet, Chef, Tripwire)
* Cloud infrastructure changes (VPC, security groups, users and priviledges)
* XSS attemps
* SQL Inejections
* Web errors (4XX, 5XX)

## Protect Our Deployment Pipeline

* Harden CI build and integration servers to ensure we can reproduce in an automated manner
* Review all changes introduced into version control
* Instrument our repository to detect when test code contains suspicious API calls
  * unit tests accessing the filesystem or network
* Ensuring every CI process runs on its own isloated container of VM
* ensuring the version control creds used by CI are read only
