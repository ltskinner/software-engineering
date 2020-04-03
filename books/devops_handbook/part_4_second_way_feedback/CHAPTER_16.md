# Chapter 16: Enable Feedback So Development and Operations Can Safely Deploy Code

## Use Telemetry to Make Deployments Safer

* Main goal is to ensure new features are operating as expected once deployed
* Also want to ensure that another service has not been broken

## Dev Shares Pager Rotation Duties with Ops

* Make sure everyone in the value stream shares downstream responsibilities of something breaking

## Have Developers Follow Work Downstream

* One of the most powerful technqiues in interaction and UX is `contextual inquiry`.
  * This is where the product team watches a customer use the application in their natural environment

## Have Developers Initially Self-Manage Their Production Service

* This is done before deployed thing is passed onto Ops for maintenance
* Launch guidance and requirements include:
  * Defect counts and severity
    * Does the app actually perform as designed?
  * Type/frequency of pager alerts:
    * Is the application generating an unsupportable number of alerts in production?
  * Monitoring coverage
    * Is the coverage of monitoring sufficient to restore service when things go wrong?
  * System architecture
    * Is the service loosely-coupled enough to support a high rate of changes and deployments in production?
  * Deployment process
    * Is there a predictable, deterministic, and sufficiently automated process to deploy the code into production?
  * Production hygiene
    * Is there evidence of good enough production habits that would allow production support to be managed by anyone else?
