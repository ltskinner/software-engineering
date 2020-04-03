# Chapter 21: Architecture Evaluation

"Fear cannot be banished, but it can be calm and without panic; it can be mitigated by reason and evaluation"

* Analysis lies at the heart of architecture evaluation
* The main goal is to determine if an architecture is fit for the purpose for which it is intended

## 21.1 Evaluation Factors

### Evaluation by the Designer

* Every time the designer makes a key design decision, or completes a milestone, the chosen and competing alternatives should be evaluated
* Consider
  * The imporance of the decision
  * The number of potential alternatives
    * Try to eliminate as many alternatives as possible
  * Good enough as opposed to perfect

### Peer Review

Architecture can be reviewed like any chunk of code can

#### Steps

* Reviewers determine a number of quality attribute scenarios to drive the review
* The architect presents the portion of the architecture to be evaluated
  * Reviewers need to ensure they understand the architecture
  * There is to be no debating of the decisions made
* For each scenario, the designer walks through the architecture and explains how the scenario is satisfied
  * Reviewers then ask questions
  * First, reviewers want to determine if the scenario is actually satisfied
  * Second, they want to determine if any other scenarios might not be satisfied
* Potential problems are captured
  * A list of problems forms the basis of a follow-up of the review
  * Any real problems, like existing currently, should be fixed promptly

### Analysis by Outsiders

* Outsiders are typically picked because of an area of expertise
* Managers are also more likely to listen to problems uncovered by an outside team

### Contextual Factors

* What artifacts are available?
* Who sees the results?
  * Sometimes for stakeholders
  * Sometimes purely for internal improvement
* Who performs the evaluation?
  * Individuals or teams
  * Internal or external
* What stakeholders will participate?
* What are the business goals?

## 21.2 The Architecture Tradeoff Analysis Method (ATAM)

### Three Groups

#### The Evaluation Team

* Group is external to the project
* Must be competent, unbiased with no hidden agendas or axes to grind

| Role | Responsibilities |
| - | - |
| Team Leader | Sets up the eval; coordinates with the client, makes sure clients needs are met |
| Evaluation Leader | Runs evaluation; facilitates elicitation of scenarios |
| Scenario Scribe | Takes notes |
| Questioner | Probes the architect |

#### Project Decision Makers

* The people that speak on behalf of the development and design decisions
* PMs, Archtiect

#### Archtiecture Stakeholders

* Those with a vested interest in the architecture performing as advertised
* The ones whos ability to do their job depends on architectural integrity

### Outputs of the ATAM

* A concise presentation of the architecture
  * Created by PMs
* Articulation of the business goals
  * Created by PMs
* Prioritized quality attribute requirements expressed as quality attribute scenarios
  * Are particularly valuable
* Sets of Risks
  * A set of risks and non risks
  * A set of risk themes
    * Used to prevent future risks in similar veins
* Captured information
  * Mappings of architectural decisions to quality requirements
  * A set of identified sensitivity and tradeoff points
