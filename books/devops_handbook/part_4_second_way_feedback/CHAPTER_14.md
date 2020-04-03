# Chapter 14: Create Telemetry to Enable Seeing and Solving Problems

* Effectively being able to diagnose problems is indicative of better Ops teams
* As opposed to just "restarting"

## Telemetry

"An automated communications process by which measurements and other data are collected at remote points and are subsequently transmitted to receiving equipment for monitoring"

* Want telemetry in both:
  * Applications
  * Environments
* And:
  * Preproduction
  * Deployment pipelines
  * Production

* Yo, I like this:
  * Etsy maintained TV screens with telemetry monitors in the office
  * **Top 30 most important business metrics**

### Locations

* Application features
* Application health
* Databases
* OS
* Storage
* Networking
* Security
* Etc

## Create our Centralized Telemetry Infrastructure

* **Data collection at the business logic, application, and environments layer**
  * In each of these layers, create telemetry in the form of:
    * Events, logs, metrics
  * Store logs in app specific files on each server
    * /var/log/httpd-error.log
  * **Prefer** logs in central service
    * Easy rotation, deletion
    * `syslog` for linux
    * `Event Log` for Windows
* **An event router is responsible for storing our events and metrics**
  * Allows for visualization, trending, alerting, anomaly detection
* Ensure pulling telemetry is completely self service APIs

![alt text](./TELEMETRY.PNG)

## Create Application Logging Telemetry that Helps Production

"When deciding whether a message should be ERROR or WARN, imagine being woken up at 4am. Low printer toner is not an ERROR"

* DEBUG
  * Often about anything that happens in the program
  * Typically disabled in production
* INFO
  * Typically, user driven or system specific actions
* WARN
  * Conditions could potentially become an error
    * Database call taking too long
* ERROR
  * Something actually for sure broke
* FATAL
  * App must terminate

### Things to Log

* Authentication/authorization (including logoff)
* System and data access
* System and application changes (especially priviledged changes)
* Data changes, such as adding, editing, or deleting data
* Invalid input (possible malicious injections, threats)
* Resources (RAM, disk, CPU, GPU, bandwidth - anything with hard or soft limits)
* Health and availability
* Startups and shutdowns
* FAults and errors
* Circuit breaker trips
* Delays
* Backup success/failure

### Things that Help

* Create hierachical logging categories
  * Non-functional
    * Performance
    * Security
  * Features
    * Search
    * Ranking

## Enable Creation of Production Metrics as Part of Daily Work

* Need libraries and infrastructure to make it dummy easy for people in both Dev and Ops to create telemetry for ANY functionality they build
* Use StatsD

## Find and Fill Any Telemetry Gaps

* Business Level
  * Number of sales transactions
  * Revenue of sales transactions
  * User signups
  * Churn rates
  * A/B testing results
* Application level
  * Transaction times
  * User response times
  * Application faults
* Infrastructure Level (DB, OS, network, storage)
  * Web server traffic
  * CPU load
  * Disk usage
* Client software level (JS on client browser, mobile application)
  * App errors and crashes
  * User measured transaction times
* Deployment pipeline level
  * Build pipeline status (red or green on various automated test suites)
  * Change deployment lead times
  * Deployment frequencies
  * Test environment promotions
  * Environment status
