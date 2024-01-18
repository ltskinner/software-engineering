# Chapter 17. Risk Management and Privacy

## Analyzing Risk

Enterprise Risk Management (ERM) program

Takes a formal approach to risk analysis:

- id risks
- determine severity
- adopt risk management stategies for each

Definitions:

- threats: any possible event that might have an adverse impact on the confidentiality, integrity, and/or availability of our information systems
- vulnurabilities: are weaknesses in our systems or controls that could be exploited by a threat
- risks: occur at the intersection of a vulnurability and a threat that might exploit that vulnurability. A threat without a corresponding vulnurability does not pose a risk, nor does a vulnurability without a corresponding threat

### Risk Identification

- external risks:
  - cyber adversaries
  - malicious code
  - natural disasters
- internal risks:
  - malicious insiders
  - mistakes made by authorized users
  - equipment failures
- mutiparty risks: imact more than one organization
  - power outages taking down a whole block
  - compromise of SaaS db
- legacy systems:
  - outdated tech may not receive patches
- Intellectual Property (IP) theft risks
  - trade secrets
  - proprietary info
- software compliance/licensing risks:
  - accidentially breaking rules leading to financial and legal risk

### Risk Assessment

Assess by two factors:

- likelhood of occurence (probability)
- magnitude/impact of risk

risk severity = likelihood * impact

Risk assessments may be performed several ways:

- one-time risk assessments:
  - point in time view of current risk state
  - in response to incedent, at request of mgmt, etc
- ad hoc risk assessment:
  - conducted in response to specific events or situations
  - new projects, new technology, change in business env
- recurring risk assessments:
  - quarterly, annualy
  - meant to track evolution of risks over time, monitor change, ensure adapting to
- continuous risk assessments:
  - ongoing monitoring and analysis
  - automated scans, regular reviews and updates to risk mgmt strategy

### Risk Analysis

Formalized approach to risk prioritization

- Quantitative risk analysis:
  - numeric data
- Qualitative risk analysis:
  - subjective judgements and categories

#### Quantitative Risk Analysis

- 1. Determine the asset value (AV) of the asset affected by the risk
  - expressed as dollars
- 2. Determine likelihood that the risk will occur
  - Annualized rate of occurence (ARO)
- 3. Determine the amount of damage that will occur to the asset if the risk materializes
  - Exposure Factor (EF)
  - complete destruction is 100
- 4. Calculate  the single loss expectancy
  - SLE amount of financial damage each time risk materializes
  - AV * EF
- 5. Calculate the annualized loss expectancy
  - Annualized loss expectancy (ALE)
  - SLE * ARO

#### Qualitative Risk Analysis

- reputational damage
- public health and safety
- employee morale
- supply chains

Use matrix of

- low
- medium
- high

### Managing Risk

Process of systematically addressing the risks facing an organization. Serves two important roles

- The risk analysis provides guidance in prioritizing risks so that the risk swith the highest probability and magnitude are addressed first
- Quantitative risk analyses help to determine whether the potential impact of a risk justifies the cost incurred by adopting a risk management approach

Four strategies:

- risk mitigation:
  - applying security controls to reduce probability and/or magnitude
  - many controls involve engineering tradeoffs between functionality, performance, and security
- risk avoidance
  - change business practices to eliminate the potential that a risk will materialize
  - typically have a detrimental impact on the business
- risk transference
  - shifts some impact of a risk from the org to another entity
  - most common is insurance
- risk acceptance
  - lol just deal wit it march on
  - exceptions: org achnowledges the risk and decided to accept (e.g. mitigation cost too high)
  - excemptions: more formal, require higher level of approval

### Risk Tracking

- inherent risk: original level of risk that exists before implementing any controls
- residual risk: risk remains after an org implements controls
- risk appetite: level of risk org is willing to accept as a cost of doing business (overall risk)
- risk threshold: the specific level at which a risk becomes unacceptable. usually more quantitative
- risk tolerance: ability to withstand risk and continue operations without any significant impact
- Key Risk Indicators (KRIs)
  - metrics used to measure and provide early warning signals for increasing levels of risk
- risk owner: individual or entity responsible for managing and monitoring risks, including implementing necessary controls and actions to mitigate them

#### Risk Appetites

- expansionary risk appetites:
  - willing to take on higher levels of risk in the pursuit of potential higher rewwards
  - for orgs looking to grow, capture markets
- neutral risk appetites:
  - balanced approach
  - steady growth and returns
  - secure investments
- conservative risk appetites
  - avoid high risks
  - focus on maintaining stability and protecting existing assets

### Risk Register

track risks facing the org. risk matrix or heatmap good for communiating

communicate:

- risk owner
- risk threshold information
- Key Risk Indicators (KRIs)

### Risk Reporting

communicating the status and evolution of risks to stakeholders within the org

forms of risk reporting:

- regular updates
- dashboard reporting
- ad hoc reports
- risk trend analysis
- risk event reports

## Disaster Recovery Planning (DRP)

### Disaster Types

A disaster is any event that has the potential to disrupt an orgs business

### Business Impact Analysis (BIA)

Formal process designed to identify the mission-essential functions within an org, and facilitate the id of critical systems that support those functions

4 metrics:

- Mean Time Between Failures (MTBF)
- Mean Time to Repair (MTTR)
- Recovery Time Objective (RTO)
  - amount of time that the org can tolerate a system being down
- Recovery Point Objective (RPO)
  - amount of data that the org can tolerate losing in an outage

## Privacy

### Data Inventory

- Personally Identifiable Information (PII)
- Protected health information (PHI)
- Financial information
- Intellectual property
- Legal information
- Regulated information
  - HIPAA, GLBA, PCI DSS

### Information Classification

- Top Secret
  - reasonably expected to cause *exceptionally grave* damage to national security
- Secret
  - reasonably expected to cause *serious* damage to national security
- Confidential
  - reasonably expected to cause *identifiable* damage to national security
- Unclassified

Businesses use:

- Public
- Private
- Sensitive
- Confidential
- Critical
- Restricted

### Data Roles and Responsiblities

Cancer governance shit:

- data subjects: people whose personal data is being processed
- data controllers: entities who determine the reasons for processing, and methods of processing
- data stewards: who carry out the intent of the data controller
- data custodians: responsible for safekeeping, but not processing
- data processors: service providers that process on behalf of controller

### Right to Be Forgotten

Can request erasure if

- data no longer needed for its original purpose
- individual withdraws consent
- individual complains and there is no overriding legitimate interest to continue processing
- data has been unlawfully processed
- there is a legal obligation to erase the data

Reducing the amount of data that you retain is a good risk minimization

### Privacy Enhancing Technologies

- deidentification
- data obfuscation:
  - hashing
  - tokenization
  - data masking

### Privacy and Data Breach Notifications

## Exam Essentials

- Risk identification and assessment helps organizations prioritize cybersecurity efforts
- Vendors are a source of external risk
- Organizations may choose from a variety of risk management strategies
- Disaster recovery planning builds resiliency
- Privacy controls protext personal information

## Review Questions

- 1. C  C
- 2. C  C
- 3. B  ~C
- 4. A  ~D
- 5. C  C
- 6. A  A
- 7. B  B
- 8. C  C
- 9. B  B
- 10. D D
- 11. A A
- 12. A A
- 13. A A
- 14. C ~A
- 15. B B
- 16. C C
- 17. C C
- 18. D D
- 19. B B
- 20. D D

17/20 = .85
