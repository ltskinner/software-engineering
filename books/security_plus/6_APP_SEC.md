# Chapter 6. Application Security

## Software Assurance Best Practices

- planning
- requirements
- design
- coding (HAHA)
- testing
- training/transition (??)
- operations and maintenance
- decomissioning

## DevSecOps and DevOps

- CI
  - integrate code to scm
  - build and test
- CD
  - roll out automatically

## Designing and Coding for Security

### Securre Coding Practices

OWASP top proactive controls:

- Define security requirements
  - Implement security throughout the development process
- Leverage security frameworks and libraries
  - Preexisting security caapabilities can make securing applications easier
- Secure database access
  - Prebuild SQL queries to prevent injection and configure databases for secure access
- Encode and escape data
  - Remove special characters
- Validate all inputs
  - Treat user input as untrusted and filter appropriately
- Implement digital identity
  - Use multifactor authentication, secure password storage and recovery, and session handling
- Enforce access controls
  - Require all requests to go through access control checks, deny by default, and apply the principle of least privilege
- Protect data everywhere
  - Use encryption in transit and at rest
- Implement security logging and monitoring
  - Helps detect problems and allows investigations after the fact
- Handle all errors and exceptions
  - Errors should not provide sensitive data, and applications should be tested to ensure that they handle problems gracefully

### API Security

## Software Security Testing

- static
- dynamic
- integrated
- fuzz testing/fuzzing
  - Sending invalid or random data to an application to test its ability to handle

### Injection Vuln

Primary mechanisms that attackers use to break through a web application to gain access to the systems supporting that app

- SQL injection
- Blind content-based SQL injection
  - basically to check whether app is sinterpreting code

### Code Injecion Attacks

- SQL injections are specific instance of more general code injection
- generally, these attacks seek to insert attacker-written code into legit code

Other types:

- LDAP injection
- XML injection
- DLL injection
- Cross-Site Scripting (XSS) is form of html attack

### Command Injection Attacks

### Exploiting Authentication Vulnurabilities

### Session Attacks

- steal an existing authenticated session

#### Cookie Stealing and Manipulation

ways to obtain:

- eavesdropping on unecrypted
- installing malware on browser to retrieve cookies
- on-path attack, attacker fools user into thinking fake site is the real site

#### Unvalidated Requests

- basically url-params
- attackers can add url redirects as parameters. so url is legit but bounces the user out

## Exploiting Auth Vuln

### Insecure Direct Object References

- like url params with objectId
- if system does not check that caller is authed to view that content, attacker can send ids they dont have access to

### Directory Traversal

- when web servers allow the inclusion of operators that navigate dir paths
- basically, you not getting a 4XX or 5XX when you try to go to a random dir lol

### File Inclusion

- take dir traversal to next level
- instead of just retrieving a file and displaying it, a file is actually executed.
  - allows attacker to fool the web server into exe random code
  - two variants:
    - local file inclusion attacks
    - remote file inclusion - exe code stored on a remote server (accesssed via url)

### Privilege Escalation

- increase level of access

## Exploiting Web App Vuln

- Cross-Site Scripting (XSS)
  - when app allows an attacker to perform HTML injection - inserting their own HTML code into a web page
  - Reflected XSS - basically, reflects your inputted stuff back to the user
  - Stored/Persistent XSS - like shit that lives in message boards?
- Request Forgery
  - Cross-Site Request Forgery (CSRF/XSRF)
    - operates on principle that if user is logged into one site, also probalby logged into another. So if you embed a command in one site, it will send a command to a second?
  - Server-Side Request Forgery (SSRF)
    - SSRF attacks are possible when a webapp accepts urls from a user as input, and then retrieves info from that URL

## App Security Controls

- Input Validation
  - Parameter pollution can get around Input Val - sends more than one value for the same input variale
- Web Application Firewalls (WAFs)
  - work like network firewalls, but at application layer (sitting in front of a web server)
- Parameterized Queries
  - stored procedures are example
- Sandboxing
  - Practice of running an app in a controlled or isolated env to prevent it from interacting negatively with other system resources or apps

### Code Security

safeguard the creation, storage, and delivery of code

- Code signing - prevents malicious updates, like when attacker attempts to deploy a fake patch
- Code Reuse - common for flaws to arise in shared code
- Software Diversity - avoid single points of failure
- Code Repositories

### Application Resilience

- scalability - designed so that computing resources they require may be incrementally added to support increasing demand
- elasticity - app should be able to provision and deprovision resources automatically

## Secure Coding Practices

- Source code comments - explain things to attackers
- Error handling
- Hard-coded credentials
- Package monitoring (dependency mgmt)
- Memory management
- Resource exhaustion
- Pointer dereferencing
- Buffer overflow - put more data into area of memory than is allocated
- Race conditions - when security of code segment depends on sequence of events
  - Time of Check (TOC) time when system verifies access permissions
  - Time of Use (TOU) time when system accesses the resource or uses the permission that was granted
  - Target of Evaluation (TOE) refers to particular component or system being evaluated or tested
  - TOC/TOU when program checks access permissions too far ahead of resource req

## Automation and Orchestration

Security Orchestration, Automation, and Response (SOAR)

### Use Cases of Automation and Scripting

- User provisioning
- Resource provisioning
- Guard rails (enforcing policy controls)
- Security groups
- Ticket creation
- Escalation
- Enabling/disabling services and access
- CI and testing
- Integrations and APIs

### Benefits of Automation and Scripting

- Achieving efficiency and time savings
- Enforcing baselines
- Standardizing infrastructure configs
- Scaling in a secure manner
- Retaining employees
- Reducing reaaction time
- Serving as a workforce multiplier

### Other Considerations

- Complexity
- Cost
- Single point of failure
- Technical debt
- Ongoing supportability

## Exam Essentials

- Understand secure software development concepts
- Know how to analyze the indicators associated with application attacks
- Know how to implement application security controls
- Explain the common benefits and drawbacks of automation and scripting related to secure operations
- Explain common use cases of automation and scripting for cybersecurity

## Review Questions

- 1. B  B
- 2. C  C
- 3. A  A
- 4. A  A but could also be B if sus af (which they are)
- 5. B  B
- 6. B  B - this is crap question its both CI and CD
- 7. B  B
- 8. B  B
- 9. B  B
- 10. D ~B
- 11. A A
- 12. D D but this is like two things
- 13. B ~A - this was shit question
- 14. A A
- 15. A A
- 16. C C
- 17. A A
- 18. C C
- 19. B B
- 20. A A not cool question

18/20 = .90
