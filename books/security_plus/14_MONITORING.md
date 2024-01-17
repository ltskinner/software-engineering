# Chapter 14. Monitoring and Incident Response

## Incident Response

orgs need:

- incident reponse plan
- process
- team
- skills
- training

incident = violation of orgs policies and procedures

events = observable occurence

### The Incident Response Process

- Preparation
  - build tools, processes, procedures to respond to incident
  - training, exercises, documenting
- Detection
  - IoCs, log analysis, monitoring
- Analysis
  - id orther related events, id target, assess impact
- Containment
  - prevent further issues or damage
  - quarantine (isolated network zone)
- Eradication
  - remove artifacts associated with incident
  - can involve rebuilding and restoring, not just cleaning
  - can be very difficult
  - complete eradication and verification is cruicial to ensure an incident is over
- Recovery
  - restoration to normal
  - bring shit back online

### Preparing for Incident Response

#### Incident Response Team

- member of management or leadership
  - make decisions
- information security staff
  - bring skills
- system admins, architects, etc
- comms and pr staff
- legal and human resources
- law enforcement

#### Exercises

- Tabletop exercises: talk thru process for given scenario
- Simulations: simulate parts of or whole plan, full scale, part scale

#### Building Incident Response Plans

An out of date plan or one that nobody is familliar with can be as much of a problem as no plan

Subplans include:

- communications plans
- stakeholder management plans (external and internal)
  - many include prioritization of which stakeholders receive comms and supp
- business continuity plans
  - focus on keeping an org functional when incidents occur
  - restorations or offloading services
- disaster recovery
  - focus on natural and human made disasters

#### Policies

Formal statements about organizational intent: explain why an org wishes to operate in a certain way, and define things like the purpose or objective of an activity or program

### Training

CISA

### Threat Hunting

Indicators:

- Account Lockout (often due to brute force logins)
- Concurrent session usage
- Blocked content trying to be accessed
- Impossible travel (two conns on same creds from two far away)
- Compute resource consumption
- Resource inaccessibility/unavailability
- Out of cycle logging (event happens at same time and the time is unusual)
- Missing logs

### Understanding Attacks and Incidents

### MITRE ATT&CK

## Incident Response Data and Tools

### Monitoring Computing Resources

- system monitoring
  - via logs
  - via central management tools
  - looking at health and performance
- application monitoring
- infrastructure monitoring
  - SNMP
  - syslog

### Security Information and Event Management Systems (SIEM)

#### SEIM Dashboard

- sensors
- trending and alerting capabilities (should tune alerts - avoid alert fatigue)
- correlation engines and rules
- sensitivity and thresholds (to filter shit)

#### Log Aggregation, Correlation, and Analysis

#### Rules

#### Log Files

- firewall logs
  - blocked and allowed traffic
- application logs
- endpoint logs
- os-specific security logs
- ids/ips logs
- network logs

#### Logging protocols and tools

- linux:
  - syslog
  - systemd journal
- log proecessing: rsyslog - fast
  - alternative: syslog-ng - enhanced filtering, logging to dbs
  - NXlog
