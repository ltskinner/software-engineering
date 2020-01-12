# Chapter 9: Create the Foundations of Our Deployment Pipeline

* Use production-like environments at every stage of the value stream
  * Environments that must be made in an automated manner
  * On-demand scripts and configuration stored in version control
  * Entirely self-serve

## Enable On-Demand Creation of Dev, Test and Production Environments

* Automation examples:
  * Copying a virtualized environment (VMWare image, Vagrant script, booting an AMI on EC2)
  * Build an automated environment creation process that starts from "bare metal"
  * Use "infrastructure as code" configurations (Puppet, Chef, Ansible, Salt, CFEngine)
  * Automated operating system config tools (Solaris Jumpstart, Red Hat Kickstart, Debian preseed)
  * Assembling an environment from a set of virtual images or containers (Vagrant, Docker)
  * Spinning up a new environment in a public cloud

## Create Our Single Repository of Truth for the Entire System

### Check in the following items

* All application code and dependencies (libraries, static content)
* Any script used to create database schemas, application reference data, etc
* All the environment creation tools and artifacts described in the environment creation
* Any file used to create containers
* All supporting automated tests and any manual scripts
* Any scripts that supports code packaging, deployment, database migration, and environment provisioning
* All project artifacts (requirements documentation, deployment procedures, release notes)
* All cloud configuration files (AWS Cloudformation templates)
* Any other script or configuration information required to create infrastructure that supports multiple services (enterprise service busses, DBMS, DNS zone files, firewall configs, etc)

#### Whether Ops uses version control is a higher predictor of IT and organizational performance than whether Dev uses is

## Make Infrastructure Easier to Rebuild than to Repair

* Used to treat servers like pets "You name them and when they get sick, you nurse them back to health. Now, servers are treated like cattle. You number them and when they get sick, you shoot them"
* Anytime changes are made, they need to be echoed to all existing deployments
  * The ONLY way to change a production environment is to completely rebuild from scratch
  * This ensures no variation creep can occur

## Modify our Definition of Development "Done" to Include Running in Production-Like Environments

* At the end of each development interval, we have:
  * Integrated
  * Tested
  * Working
  * Potentially shippable code
  * **Demonstrated in a production-like environment**
