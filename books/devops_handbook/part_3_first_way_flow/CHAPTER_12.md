# Chapter 12: Automate and Enable Low-Risk Releases

## Automate out Deployment Process

After the deployment process is documented, the goal is to simplify and automate as many of the manual steps as possible, such as:

* Packaging code in ways suitable for deployment
* Creating pre-configured virtual images or containers
* Automating the deployment and configuration of middleware
* Copying packages or files onto production servers
* Restarting servers, applications, or services
* Generating configuration files from templates
* Running automated smoke tests to make sure the system is working and correctly configured
* Running testing procedures
* Scripting and automating database migrations

Also, will re architect to remove annoying and slow steps

* Reduce number of handoffs and lead times

### Deployment Pipeline Requirements

* Deploying the same way to every environment
  * If the same sequence has been performed on dev and test, high odds it will work for prod
* Smoke test deployments
  * During deployment, try to connect to every service app depends on, and if any of those fail, kill the deployment
* Ensure we maintain consistent environments
* Pull the Andon cord and swarm when anything hits the fan

## Enable Automated Self Service Deployments

* Build
  * Deployment pipeline must create packages from version control that can be deployed to any environment, including production
* Test
  * Anyone should be able to run any or all of the automated test suite
* Deploy
  * Anyone should be able to deploy these packages to any environment where they have access, executed by running scripts that are also checked into version control

## Integrate Code Deployment into the Deployment Pipeline

* Ensure that packages created during the CI process are suitable for deployment into production
* Show the readiness of production environments at a glance
* Provide a push-button, self-service method for any suitable version of the packaged code to be deployed into production
* Record automatically, for auditing and compliance, which commands were run on which machines when, who authorized it, and what the output was
* Run a smoke test to ensure the system is operating correctly and the configuration settings, including items such as database connection strings, are correct
* Provide fast feedback for the developer so they can quickly determine whether their deployment was successful

## Etsy

* **4,500 unit tests** run in less than **1 minute**
* ALL calls to external systems are **stubbed** out
* Leveraged a "Princess" server - a production server taken out of rotation, used to run all smoke tests

## Decouple Deployments from Releases

* Deployment is the installation of a specific version of software to a given environment
* Release is when a new feature is made available to the customer

Decoupling these two makes for

* Developers repsonsible for code working
* POs responsible for making clients happy

### Broad categories of releases:

* Environment Based release patterns
  * Have two or more environments that get deployed too
  * Only one env gets live customer traffic
  * New code is deployed in non-live environment
    * Then traffic is diverted over
  * aka **blue-green deployments**, **canary releases**, **cluster immune systems**
* Application-based release patterns:
  * Modify application so that selected features and functionality can be released by `small config changes`

### Environment-Based Release Patterns

* Easy to retrofit on existing systems
* Benefits
  * Enables team to work normal business hours
  * Can easily conduct simply changeovers

#### Dealing with Database Changes

* Create blue and green database
  * Put blue on read only
  * perform backup of it
  * restore on green DB
  switch reaffic to green
* OOOR
  * only make **additive** changes to the DB
  * never **mutate** an existing database object
  * no assumptions about which database version will be used in prod
  * duplicates the crap out of data, but works super well

### Canary and Cluster Immune System Pattern

* A1 group
  * Production servers that only serve internal employees
* A2 group
  * Production servers that only serve a small percentage of customers
  * Are deployed to when acceptance critera is met (manual or automated)
* A3 group
  * Rest of production servers
  * Deployed to after A2 group meets criteria

### Application-Based Patterns to Enable Safer Releases

#### Implement Feature toggles

* Easily select which features are live
  * Typically controlled code-wise by if statements
  * Configured by external configs
* Enable
  * Easy rollback
  * Gracefully degrade performance
  * Increase resilience through **service oriented architecture**
