# 1.1 - Requirements

## Functional Requirements

* [ ] Are system boundary conditions specified?
  * [ ] Inputs?
  * [ ] Outputs?
  * [ ] Results formats?
* [ ] Are software needs specified?
  * [ ] Is there any reason any OS MUST or CANNOT be used?
  * [ ] Rough idea of what open source software will be used?
  * [ ] COTS software has been profiled and is within budget?
* [ ] Are compute needs are properly specified?
  * [ ] Using cloud? On-prem? Personal Compute?
  * [ ] Need GPUs? Special RAM loads?
* [ ] Do you have a detailed enough description to build the system?

## Quality Attribute Requirements

* [ ] Do you have enough information to design the simplest system possible?
* [ ] Have you ensured there are no requirements that add unneccesary complexity?
* [ ] Have you eliminated erroneous requirements that only serve to appease egos or unrealistic expectations?
* [ ] Do you have definitions of:
  * [ ] Success?
  * [ ] Failure?
* [ ] Are tradeoffs between attributes documented?

### Quality Attributes: Tier One

* [ ] Are **availability** requirements specified?
  * [ ] Uptime needs?
  * [ ] What types of events will lead to the system being down?
  * [ ] Are **error** handling requirements specified?
    * [ ] Consequences of software failure are noted?
    * [ ] Vital system information is documented?
    * [ ] Vital system components are documented?
    * [ ] Error detection strategy is documented?
    * [ ] Error recovery strategy is documented?
* [ ] Are **interoperability** requirements specified?
  * [ ] Are all interfaces to external systems specified?
  * [ ] Are all protocols to communicate with external system specified?
  * [ ] Are all auth considerations for external communication specified?
* [ ] Are **modifiability** requirments specified?
  * [ ] Have things that are NOT likely to change been noted?
  * [ ] Have things that are likely to be changed noted?
  * [ ] Have the likelihoods and conditions of change been noted?
  * [ ] If a change needs to be made, who will need to make it?
  * [ ] What kind of cost will a change incur?
* [ ] Are **performance** requirements specified?
  * [ ] Have all classes of events been catalogued with their expected responses?
    * [ ] Periodic events - predictable and on regular interval?
    * [ ] Stochastic events - can arrive on some probabilistic distribution?
    * [ ] Sporatic events - circumstantial or otherwise non-pattern events?
  * [ ] Are **timing** requiremnts specified?
    * [ ] Response times? (latency)
    * [ ] Jitter - variations in latency?
    * [ ] Processing time?
    * [ ] System trhoughput?
    * [ ] Data transfer rates?
    * [ ] Number of events not processed (due to system being bogged down)?
* [ ] Are **Security** requirements specified?
  * CIA Triangle (Confidentiality, Integrity, Availability)
    * [ ] Do data/services need to be protected from unauthorized access?
    * [ ] Do we need to ensure that data/services are not manipulated improperly?
    * [ ] Have system availability needs been characterized?
  * Others:
    * [ ] Will users need to authenicate?
    * [ ] Will actions need to be tracked for nonrepuditation?
    * [ ] Will there be different levels of authorization?
* [ ] **Testability**
  * [ ] Have budgeted 30-50% of the project timeline to be used for testing?
  * What do you know and what can you expect at the requirements level?
* [ ] **Usability**
  * [ ] Things that will make the system easy to use have been noted?
  * [ ] What things could change to make the system easier to use?
  * [ ] Things that could make the user more efficient with the system?
  * [ ] Have things that will instill confidence in the user been noted?
* [ ] Does the system need to be **monitored** while live?
  * [ ] Transaction time?
  * [ ] Health of components
  * [ ] Queue lengths
  * [ ] What will be monitoring it?
  * [ ] How will data be viewed by the monitor?

### Quality Attributes: Tier Two

* [ ] Will it be neccessary to make slight **variations** to the final product?
  * [ ] Have the areas that vary been explicitly designated for change?
* [ ] Will this product need to be **portable** to different platforms?
* [ ] Will this product need to be **developed** by remote teams?
  * [ ] Have proper collaboration tools been prepared?
* [ ] **Scalability** has been considered?
  * [ ] Will the system scale horizontally with more logical units/clusters?
  * [ ] Will the system scale vertically with more resources to one unit?
* [ ] Have the **deployment** needs been reviewed?
  * [ ] Porting code to site?
  * [ ] Integrating with existing systems?
* [ ] Is **mobility** a requirement?
  * [ ] Will the size, display, input, bandwidth need to be adjusted for different deployment environments?

## Constraints

* [ ] Is there any compute hardware we are bound to?
* [ ] Is there any cloud or on-prem compute we are bound to?
* [ ] Is there any OS we are bound to?
* [ ] Is there any implementation language we are bound to?
* [ ] Is there a source control we are bound to?
* [ ] Is there any software we are forbidden from using?

## Recap

* [ ] If every requirement is satisfied, will the product be complete?
* [ ] Aggreed upon reqs are reasonable:
  * [ ] Nothing is impossible to implement
  * [ ] **No reqs that only serve to appease a customer or boss**
* [ ] Each requirement is testable:
  * [ ] Can see how developing tests will be easy?
  * [ ] Requirements are able to be tested by a third party?
* [ ] Have you made the requirements easy to navigate in the future?
  * [ ] Properly indexed?
  * [ ] Stored with proper visibility?
  * [ ] Easy to revisit and mobilize for ass coverage?
