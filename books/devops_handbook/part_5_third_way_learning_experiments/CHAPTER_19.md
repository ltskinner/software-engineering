# Chapter 19: Enable and Inject Learning into Daily Work

"Responding to crises is not idiosyncratic work. It is something that is done all the time. It is this responsiveness that is their source of reliability"

* Netflix Chaos Monkey is an extreme example of getting used to failure recovery

## Establish a Just, Learning Culture

"When responses to incidents and accidents are seen as unjust, it can impede safety investigations, promoting fear rather than mindfulness in people who do safety-critical work, making organizations more bureucratic rather than more careful, and cultivating professional secrecy, evasion, and self-protection"

* Main thing is want local lessons to become global information

## Schedule Blameless Post-Mortem Meetings After Accidents Occur

Explicitly disallow the phrases 'would have' or 'could have'

* Examine mistakes in a way that focuses on the
  * situational aspects of a failures mechanism
  * decision making process of individuals
  * leverage these to proximate the failure

### Steps in the Meeting

* Construct a timeline and gather details from multiple perspectives on failures, ensuring we dont punish people for making mistakes
* Empower all engineers to improve safety by allowing them to give detailed accounts of their contributions fo failures
* Enable and encourage people who do make mistakes to be the experts who educate the rest of the organization on how not to make them in the future
* Accept that there is always a discretionary space where humans can decide to take action or not, and that the judgement of those decisions lies in hindsight
* Propose countermeasures to prevent a similar accident from happening in the future and ensure these countermeasures are recorded with a target date and an owner for the follow-up

### Attendees

* The peopele involved in decisions that may have contributed to the problem
* The people who identified the problem
* The people who respond to the problem
* The people who diagnosed the problem
* The people who were affected by the problem
* Any anyone else who is interested in attending the meeting

### Good questions

* 'Why did it make sense to me when I took that action?'
  * NOT 'i have no idea what I was doing'
  * Cannot let imposter syndrome take ahold of good engineers

## Publish Our Post-Mortems as Widely as Possible

* Make sure these are visible and searchable
* Weekly newsletter or something like that?

## Decrease Incident Tolerances to Find Ever-Weaker Failure Signals

## Redefine Failure and Encourage Calculated Risk-Taking

* At Netflix, the same engineer took down the site 3 times in 18 months haha
* This b OK tho, get used to things failing

## Inject Production Failures to Enable Resilience and Learning

* Design crumble zones like in cars

## Institute Gamedays to Rehearse Failures

"A system is not really tested until we break it in production"
