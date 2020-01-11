# Chapter 6: Understanding the Work in Our Value Stream, Making it Visible, and Expanding it Across the Organization

* First step is understanding how value is delivered to the customer:
  * What work is performed and by whom, and what steps we can take to improve flow

## Identifying the Teams Supporting our Value Stream

Include, but not limited to:

* Product Owner
  * Internal voice of the business that defines the next set of functionality in the service
* Development
  * The team responsible for developing application functionality in the service
* QA
  * The team responsible for ensuring that feedback loops exist to ensure the service functions as desired
* Operations
  * The team often responsible for maintaining the production encironment and ensure that required service levels are met
* Infosec
  * The team responsible for securing systems and data
* Release managers
  * The people responsible for managing and coordinating the production deployment and release processes
* Technology executives or value stream manager
  * Someone responsible for "ensuring that the value stream meets or exceeds the customer [and organizational] requirements for the overall value stream, from start to finish

## Create a Value Stream Map to See the Work

* Dont be afraid to tackle this ove the course of multiple days
* Goal is NOT to document every step and minutiae
  * Rather, goal is to sufficiently understand areas in our value stream that are jeopardizing other goals like:
    * Fast flow
    * Short lead times
    * Reliable customer outcomes
  * Also, want to make sure we know who the powerful people are that can change their portion of the value stream

### Focus on:

* Places where work must wait weeks or even months
  * Production-like environments
  * Change approval processes
  * Security review processes
* Places where significant rework is generated or received

### Diagrams

* Use process blocks with:
  * Lead time
  * Processing time
  * %C/A as measured by the downstream consumers of the output
* Then, compound all these blocks stats to report:
  * Total lead time
  * Value added time
  * Percent complete and accurate
* Then, start identifying which metrics we want to improve
  * Perform more observations and measurements
  * Create a future value stream map and a date to achieve by

## Creating a Dedicated Transformation Team

* Team that operates outside of the rest of the organization
* Focus on improving daily operations
* Hold this team accountable for achieving clearly defined, and measurable goals
  * Like reducing deployment lead time of code in version control by 50%

### How is this done?

* Assign members of the dedicated team to be solely allocated to the DevOps transformation efforts
  * As opposed to "maintain all your current responsibilities, but spend 20% of your time on DevOps"
* Select team members who are generalizts, who have skills across a wide variety of domains
* Select team members who have longstanding and mutually respectful relationships with the rest of the org
* Create separate physical space for the dedicated team if possible
  * Do everything to maximize communication as well

## Agree on a Shared Goal

* Need to define a measurable goal with a clearly defined deadline, between 6 mo and two years in the future
* Goal should create obvious value for the organization as a whole and to the customers

### Example goals

* Reduce percentage of the budget spent on product support and unplanned work by 50%
* Ensure lead time from code check-in to production release is one week or less for 95% of changes
* Ensure releases can always be performed during normal business hours with zero downtime
* Integrate all the required information security controls into the deployment pipeline to pass all required compliance requirements

## Keep our Improvement Planning Horizons Short

* Want to make sure there is actionable data within weeks (not months)

### Short intervals achieve

* Flexibility and ability to reprioritize and replan quickly
* Decrease the delay between work expended and improvement realized
  * Strengthens the feedback loop
  * Makes it more likely to reinforce desired behaviors
  * When improvement initiatives are successful, it encourages more investment
* Faster learning generated from the first iteration
  * Meaning faster integrations of our learnings into the next iteration
* Reduction in activation energy to get improvements
* Quicker realization of improvements that make meaningful differences in our daily work
* Less risk that our project is killed before we can generate any demonstratable outcomes

## Reserve 20% of our Cycles fo Non-Functional Requirements and Reducing Technical Debt

## Increase the Visibility of Work

### Use Tools to Reinforce Desired Behavior

* Tools for sharing information quickly - chats, new techniques
  * Thankfully, the book notes how distracting these things can be haha
  * Decide what is appropriate for what channels
* Tools for making work visible
  * Joint task boards between Dev and Ops
  * SAME tool (no Jira + VTB - either, or)
