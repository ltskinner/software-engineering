# Chapter 18: Create Review and Coordination Processes to Increase Quality of Our Current Work

* Primary goal is to reduce risk of production changes before they are made

## Pull Request Workflow

* To work on something new, the engineer creates a descriptively named branch off master ("new-oath2-scopes")
* Engineer commits to that branch locally, regularly pushing their work to the same named branch on the server
* When they need feedback or help, or when they thing branch is ready for merging, they open up a pull request
* When they get their desired reviews and get any necessary approvals of the feature, the engineer can then merge it into master
* Once the code changes are merged and pushed to master, the engineer deploys them into production

## The Dangers of Change Approval Processes

"The people closest to a problem typically know the most about it"

## Enable Peer Review of Changes

"Ask a programmer to review ten lines of code, he'll find ten issues. Ask him to do 500 lines, and he'll say it looks good" HAHA

* Everyone must have someone to review their changes before committing to trunk
* Everyone should monitor the commit stream of their fellow team members so that potential conflicts can be identified and reviewed
* Define which changes qualify as high risk and may require a review from a SME
  * DB changes, Security sensitive modules like auth
* If someone submits a change that is too large to reason about easily, it needs to be split into multiple, smaller changes that can be easily understood

## Watch Out!

* For:
  * Manual testing
  * Change freezes

## Critique Effectiveness of Pull Request Process

* Want good descriptive text in the pull request
* Explain the problem
* Explain why a change is being bade
* Explain the fix
* Identify risks
* @people that are relavent to approving the request
