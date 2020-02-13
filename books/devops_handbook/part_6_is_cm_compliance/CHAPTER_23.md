# Chapter 23: Protecting the Deployment Pipeline

## Integrate Security and Compliance into Change Approval Processes

### Categories of Change

* Standard Changes
  * Lower risk
  * Updating cost codes, tax tables, country codes
  * Website styling
  * Can be scheduled
  * Need to be logged
* Normal Changes
  * Higher risk
  * Require someone to look at
  * Incudes risk and alternatives
  * Includes a proposed schedule
* Urgent Changes
  * Emergency
  * Usually need to be put into production immediately

### Recategorize the Majority of our Lower Risk Changes as Standard Changes

### What to do When Changes are Categorized as Normal Changes

* Main goal is to ensure quick deployment even if it cant be automated
* Because these will be evaluated by people, ensure that the `context` of the change is effectively conveyed
  * Still include links to machine readable info like .json files

## Reduce Reliance on Separation of Duty

* Use PP and continuous inspection of checkins and code reviews to keep an eye on things
* NOT dedicated code librarians

## Ensure Documentation and Proof for Auditors and Compliance Officers

"DevOps is all about bridging the gap between Dev and Ops. In some ways, the challenge of bridging the gap between DevOps and auditors and compliance officers is even larger."
