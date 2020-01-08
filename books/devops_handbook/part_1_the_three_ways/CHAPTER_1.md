# Chapter 1: Agile, Continuous Delivery, and the Three Ways

## The Manufacturing Value Stream

* `value stream`
  * The sequence of activities an organization undertakes to deliver upon a customer request
  * Easy to see in the context of pure manufacturing
* Goals:
  * Smooth and even workflows
  * Small batch sizes
  * Reducing work in progress (WIP)
  * Preventing the need for rework
  * Dont pass defects downstream

## The Technology Value Stream

* Technology is only valuable when its deployed
* Smoothly going from concepts to live things is the main goal
* Want to ensure that all deployments are easy and minimize chaos and distruption

## Focus on Deployment Lead Time

* Value stream:
  * Starts: when a change is checked into version control
  * Ends: when change is successfully running in production
    * And is:
      * Providing value to the customer
      * Generating useful feedback
      * Generating telemetry

### Defining Lad Time vs Processing time

* Lead time
  * Starts: when the ticket is created
  * Ends: when work is completed
* Process time
  * Starts: when work starts (after the ticket is created)
  * Ends: when work is commpleted
* Typically, the focus is on **improving lead time** because that is what the customer experiences
  * Seek to keep minimze idle time that work is waiting in queues

### DevOps Ideal: Deployment Lead Times of Minutes

* Continually checking small code changes in
* Performing tons of automated testing
* Deploying rapidly
* Goal is to detect errors very quickly

#### How is this done?

* Modular architecture
* Things are well encapsulated
* Loosely coupled

##### Testing stages

1. Automated tests run on commit
2. Exploratory tests run by developers (tests with no plan)
3. Deploy

## Observing "%C/A" as a Measure of Rework

* Percent complete and accurate
* Ask customers what percentage of the time they recieve work that is 'usable as is'
  * Can do their work without having to correct the information that was provided
  * Not missing information that should have been supplied
  * Info given could have been clearer

## The Three Ways: The Principles Underpinning DevOps

* The First Way
  * Enables fast Dev -> Ops (Bus -> Cust) workflows
* The Second Way
  * Enables fast and constant feedback left and right across all stages of the value stream
* The Third Way
  * Short, tight feedback loops, in a high trust environment that encourages scientific approach and risk taking to the end of learning
