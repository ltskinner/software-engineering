# Chapter 20: Convert Local Discoveries into Global Improvements

## Use Chat Rooms and Chat Bots to Automate and Capture Organizational Knowledge

* Everyone can see everything happening
* Engineers on their first day could see what daily work looked like and how it was performed
* People were more apt to ask for help when they saw others helping each other
* Rapid organizational learning was enabled and accumulated

### Using chat rooms is opposed to searching across email threads

### Automation is cool too

* Use chat room to Trigger:
  * Builds
  * Test suite
  * Etc
* Use chat rooms to Report:
  * Commits
  * Pull requests
  * Test results
  * Build status
  * Deployment status

## Automate Standardized Processes in Software for Re-Use

* Things in Word docs get lost
* Have to convert these information stores into executable and reusable form
* "The actual compliance of an organization is in direct proportion to the degree to which its policies are expressed as code"

## Create a Single, Shared Source Code Repository for Our Entire Organization

* Include Config standards for:
  * Libraries
  * Infrastructure
  * Environments
* Deployment tools
* Testing standards and tools, including security
* Deployment pipeline tools
* Monitoring and analysis tools
* Tutorials and standards

## Spread Knowledge by Using Automated Tests as Documentation and Communities of Practice

## Design for Operations Through Codified Non-Functional Requirements

* Sufficient production telemetry on our apps and environments
* The ability to accurately track dependencies
* Services that are resilient and degrade gracefully
* Forward and backward compatability between versions
* The ability to archive data to manage the size of the production dataset
* The ability to easily search and understand log messages across services
* The ability to trace requests from users through multiple services
* Simple, centralized runtime confis using **feature flags** and so forth

## Build Reusable Operations User Stories into Development

* Automate as much as possible
* Make anything manual incredibly hard to mess up
* Explicitly define handoff procedures

## Ensure Technology Choices Help Achieve Organizational Goals

* Identify technologies that
  * Impede or slow down the flow of work
  * Disproportionately create high levels of unplanned work
  * Disproportionately create large numbers of unsupported requests
  * Are most inconsistent with our desired architectural outcomes
    * throughput, stability, security, reliability, business continuity
