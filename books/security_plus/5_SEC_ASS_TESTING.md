# Chapter 5. Security Assessment and Testing

## Vulnurabilty Management

- identifying, prioitizing, and remediating vulnurabilities in envs
- vulnurability scanning detects new vulns

### Identifying Scan Targets

Some scan questions:

- What is the data classification of the information stored, processed or transmitted by the system?
- Is the sytem exposed to the Internet or other public or semipublic networks?
- What services are offered by the system?
- Is the system a production, test, or development system?

Can use scanning tools to document all devices on network, creating an *asset inventory*

### Determining Scan Frequency

Some factors that influence how often an org decides to conduct scans:

- The orgs risk appetite and its willingness to tolerate risk within the env
- Regulatory requirements
- Technical constraints
- Business constraints (like resource availability)
- Licensing limitations

### Configuring Vulnurability Scans

#### Scan Sensitivity Levels

- types of checks performed

### Exam Notes

- Credantialed Scanning:
  - Access operating systems, databses, and applications
  - Basically actually get into system lol
- Non-credentialed is just that
- Server-based scanning -->
- Agent-based Scanning
  - Admins install agents on each target server
  - agents conduct scans of the server config, providing an "inside out" scan
  - server based scans take resources so dont overdo it

### Scan Perspective

Perspective = where you are on the network

- from external internet
- from inside network
- on datacenter
- on personal machine

Controls that affect scan results:

- Firewall settings
- Network segmentation
- IDS
- IPSs

### Scanner Maintenance

ensure scanning software and vuln feeds remain up to date

## Security Content Automation Protocol

From NIST, to create a standardized approach for communicating security related information

- Common Configuration Enumeration (CCE) - system config issues
- Common Platofmr Enumeration (CPE) - product names and versions
- Common Vulnurabilities and Exposures (CVE) - security related software flaws
- Common Vulnurability Scoring System (CVSS) - measuring and dsecribing severity of sec-related software flaws
- Extensible Configuration Checklist Description Format (XCCDF) - languge for specifying checklists and reporting results
- Open Vulnurability and Assessment Language (OVAL) - language for specifying low-level testing prodcedures used by ckecklists

### Vulnurability Scanning Tools

#### Infrastructure Vulnurability Scanning

- Tenable Nessus
- Qualsys
- Rapid7 Nexposure
- OpenVAS

#### Application Testing

- Static testing
  - Analyzes code without executing it
- Dynamic testing
  - executes code as part of the test
- Interactive testing
  - combines static and dynamic
  - testers interact with app through exposed interfaces

#### Web Application Scanning

- Nikto web app scanner (difficult cli)
- Arachni

#### Reviewing and Interpreting Scan Reports

#### Understanding CVSS

Common Vulnurability Scoring System

- component of SCAP
- 0-10

Metrics:

- Attack Vector (AV) Metric
  - Physical, Locall, Adjacent, Network
- Attack Complexity (AC) Metric
  - High, Low
- Privileges Required (PR) Metric
  - High, Low, None
- User Interaction (UI) Metric
  - None, Required
- Confidentiality (C) Metric
  - None, Low, High
- Integrity (I) Metric
  - None, Low, High
- Availability (A) Metric
  - None, Low, High
- Scope (S)
  - Unchanged, Changed

### Calculating the Impact Sub Score (ISS)

basically: 1- product([1-each_metric])

## Vulnurability Classification

### Patch Management

### Legacy Systems

Good vulnurability response and remediation include:

- patching
- insurance
- segmentation
- compensating controls
- exceptions
- exemptions

## Hopefully the last section

### Threat Hunting

Similar to pen testing, but is actively looking for indicators the system was compromised

### Penetration Test Types

- Physical penetration testing
  - focuses on physical security controls
- Offensive PT
  - act as attackers
- Defensive PT
  - eval orgs ability to defend
- Integrated PT
  - combines aspects of both offensive and defensive

Assessment types:

- Known environment
  - full knowledge of underlying technology, configs, etc
- Unknown environment
  - replicate what attacker would encounter
- Partially known environment
  - Truly Remarkable: somewhere in between fully known environment and unknown

### Rules of Engagement

- timeline
- locations, systems, apps, potential targets
- data handling requirements
- behaviors to expect from target
- resources committed to test
- legal concerns
- comms with targets (like how to notify if successfully get in)

### Permission

be sure to get it?

### Reconnaissance

- Passive recon
  - gather info without directly engaging the target
- Active recon
  - directly engage target to see how respond
  - port scanning
  - war driging, war flying (uavs) - want to get on wireless network

### Running the Test

- Initial access
- Privilege escalation
- Pivoting, lateral movement
- Persistence

### Cleaning up

## Audits and Assessments

- Security Tests
  - verify a control is working properly
- Security Assessments
  - comprehensive review of security of a system
- Security Audits
  - lol same shit just done by external group
  - internal audit
  - external audit
    - third-party audits are type of external, but requested by a regulator, customer, etc

Auditing standards: Control Objectives for Information and Related Technologies (COBIT)

### Vulnurability Life Cycle

- identificatino
- analysis
- response and remediation
- validation of remediation
- reporting

## Exam Essentials

- Many vulnurabilities exist in modern computing environments
- Threat hunting discovers existing compromises
- Vulnurability scans probe systems, applications, and devices for known security issues
- Penetration testing places security professionals in the role of attackers
- Bug bounty programs incentivize vulnurability reporting
- Recognize the prupose and types of security audits
- Understand the stages of the vulnurability life cycle

## Review Questions

- 1. C  C
- 2. D  D
- 3. C  C
- 4. C  C
- 5. A A
- 6. B B Integrity
- 7. C C
- 8. A  A
- 9. B  B
- 10. A A doesnt mention escalation
- 11. C ~A no indicator of external group
- 12. C C
- 13. A ~D
- 14. C C
- 15. C ~B idk lmao
- 16. C C
- 17. C C
- 18. B B
- 19. A ~B
- 20. C C

16/20 = .80
