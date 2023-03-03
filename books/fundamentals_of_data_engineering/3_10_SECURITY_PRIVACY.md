# Chapter 10. Security and Privacy

One security breach or data leak can leave your business dead in the water; your career and reputation are ruined if its your fault

## People

The weakest link in security and privacy is you

- security is often compromised at the human level
- condust yourself as if your always a target
- a bot, or human actor is trying to infultrate your sensitive credentials and information at any given time

Exercise the power of negative thinking and always be paranoid

### The Power of Negative Thinking

Positive thinking can blind us to reality and deter preparation

The best way to protect private and sensitive data is to avoid ingesting this data in the first place

### Always be Paranoid

Trust nobody at face value when asked for credentials, sensitive data, or condifential information - including from your coworkers

## Processes

Make security a habit

### Security Theater vs Security Habit

Security needs to be simple and effective enough to become habitual throughout an organization

### Active Security

requires thinking about and researching security threats an a dynamica and changing world

e.g. instead of deploying a scheduled simulated phishing attack, research successful phishing attacks and think through how those would have been handled by your rings

### The Principle of Least Privilege

Treat humans and machines the same way: give them only the privileges and data they need to do their jobs, and only for the timespan when needed

Use broken glass processes

### Shared Responsibility in the Cloud

Most cloud security breaches continue to be caused by end users, not the cloud. Breaches occur because of unintended misconfigurations, mistakes, oversights, and slopiness

### Always Back Up Your Data

- test your restoration process on a regular basis as well

### [Example Security Policy](./_SECURITY_POLICY.md)

## Technology

### Patch and Update Systems

- software gets stale, and security vilnurabilities are constantly discovered
- set alerts or automate builds on releases and vulnurabilities so you can be prompted to perform updates manually

### Encryption

- encryption at reat
- encryption over the wire

### Logging, Monitoring, and Alerting

Monitor:

- Access
  - Whos accessing what, when and from where
  - Are there strange patterns of current users
- Resources:
  - again, any weird patterns?
- Billing
  - Is the bill higher than usual?
- Excess permissions
  - Use tools to see what permissions ARENT being used

### Network Access

dont do stupid shit like leaving ssh enpoint open to all ips

### Security for Low-Level Data Engineering

- Internal security research
- make every employee a security practicioner
