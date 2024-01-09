# Chapter 1. Todays Security Professional

## Cyber Objectives

### CIA Triangle: rebranded as "CIA Triad"

- Confidentiality
  - Unauthorized individuals are not able to gain access to sensitive information
- Integrity
  - Ensures no unauthorized modifications to information or systems
- Availability
  - Information and systems are ready to meet the needs of legitimate users at the time users request them
  - Availability controls include: fault tolerance, clustering, backups, etc

Also useful:

- Nonrepudiation
  - Someone who has performed an action cannot later deny having performed the action
  - Assurence that something cannot be denied by someone

## Data Breach Risks

- Security Incidents
  - When an org experiences an breach of the CIA of information or information systems
  - Can either be malicious or just happen lol

As a security professional, reponsive for understanding risks, and implementing controls designed to manage those risks to an acceptible level

### DAD Triad

- Discloseure
  - Exposure of sensitive information to unauthorized individuals (violation of confidentiality)
- Alteration
  - Unauthorized modification of information (violation of integrity)
- Denial
  - Disruption of an authorized users legitimate access to information (violation of availability)

### Breach Impact

- Financial Risk
  - Risk monetary damage, directly or indirectly
- Reputational Risk
  - Negative publicity around a breach causes loss of goodwill among stakeholders (hard to quantify)
- Strategic Risk
  - Risk an org will become less effective in meeting its major goals and objectives
- Operational Risk
  - Risk to an orgs ability to carry out day-to-day functions (business processes, orders, etc)
- Compliance Risk
  - When a breach causes an org to become non-compliant with legal or regulatory requirements (HIPAA is big)

Note: Risks often cross categories. In most cases, a risk will cross multiple risk categories

## Implementing Security Controls

Requirements are expressed as *control objectives*

*Security controls* are specific measures that fulfill the security objectives of an organization

### Gap Analysis

Cyber professionals review the control objectives, and then examine the controls designed to achieve those objectives. If there are any cases where the controls do not meet the control objectives, that is an example of a gap

### Security Control Categories

- Technical controls
  - Enforce confidentiality, integrity, and availability
  - firewall rules, acls, ips, encryption
- Operational controls
  - processes that we put in place to manage technology in a secure manner
  - access reviews, log monitoring, vulnurability management
- Managerial controls
  - procedural mechanisms that focus on the mechanics of the risk management process
  - periodic risk assessments, security planning
- Pysical controls
  - impact the physical world
  - fences, perimiter lighting, locks, fire suppression, burgler alarms

### Security Control Types - **IMPORTANT**

- Preventative controls
  - Intend to stop a security issue before it occurs
  - Firewalls and encryption
- Deterrent controls
  - Prevent an attacker from attempting to violate security policies
  - Guard dogs, barbed wire fences
- Detective controls
  - identify security events that have already occured
  - IDS
- Corrective controls
  - remediate security issues that have already occured
  - restoring backups
- Compensating controls
  - mitigate the risk associated with exceptions made to a security policy
- Directive controls
  - Inform employees and others what they should do to achieve security objectives
  - policies and procedures

## Data Protection

- Data at rest
  - stored on hard drives, tapes, cloud, etc
  - prone to theft by insiders or external attackers who gain access and can browse content
- Data in transit
  - data that is in motion/transit over a network
- Data in use
  - in memory

### Data Encryption

### Data Loss Prevention (DLP)

Help orgs enforce info handling policies and procedures. They search systems for stores of sensitive info that might not be secured, and monitor netowkr traffic for potential attempts to remove sensitive info from org. They can act quickly to block the transmission before damage is done and alert admins

DLP systems work in two diff environments

- Agent-based DLP
  - Software agents installed on systems that search those systems
- Agentless (network-based) DLP
  - Dedicated devices that sit on the network and monitor outbound network traffic

DLPs have two mechanisms of action:

- Pattern matching
  - Watching for telltale signs of sensitive info (like ssn or cc or ts)
- Watermarking
  - Where systems or admins apply electronic tags to docs, so DLP looks for tags
  - aka Digital Rights Management (DRM)

### Data Minimization

Techniques seek to reduce risk by reducing the amount of sensitive info maintained

Best way to achieve is to simply destroy data when it is no longer necessary

If cant destroy, transform it to format where original sensitive info is deidentified (which removes ability to link data back to an individual)

Also can do *data obfuscation*

- hashing
- tokenization
  - basically replace with some token id that can be used to look up true value later
- masking
  - replace some or all sensitive fields with blank characters or Xs

If someone has list of possible values for a field, can do *rainbow table attack* - attacker computes hashes of candidate values and checks to see if hashes exist in file (counter with salt)

### Access Restrictions

Security measures that limit the ability of individuals to access info or resources

- Geographic restriction
  - based on physical location (country, region, etc)
- Permission restriction
  - limit by role or level of authorization

### Segmentation and Isolation

Places sensitive systems on separate network

*Isolation* completely cuts a system off from access to or from outside networks

## Review Questions

- 1. D  D
- 2. B  B
- 3. C  C
- 4. B  B
- 5. D  D
- 6. ~A  D i picked Watermaking, but answer is network-based DLP
- 7. B  B
- 8. A  A
- 9. D  D
- 10. ~D A not doing business is strategic, not operational
- 11. C C
- 12. A A
- 13. D D
- 14. D D
- 15. D D
- 16. A A
- 17. C C
- 18. B B
- 19. C A, oh, tokenization IS supposed to be reversible
- 20. A A

17/20 = .85
