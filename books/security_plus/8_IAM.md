# Identity and Access Management

## Identity

- Identities
  - Sets of claims made about a subject
  - subjects are people, applications, devices, systems, organizations

Ways to claim an identity:

- Usernames
- certificates
- tokens
- ssh keys
- smartcards

Lost key pairs is big issue

## Authentication and Authorization

Wehn subject wants to claim an identity, need to prove the id is theirs - this is *authentication*

*authorization* verifies what you have access to

### Authentication and Authorization Technologies

AAA - Authentication, Authroization, Accounting system

### Signel Sign-On

- Allows users to log in with single identityf and use it with multiple systems or services without reauthenticating

SSO-related tech:

- LDAP (Lightweight Directory Access Protocil)
  - used to make available an org directory for email or other contact
- OAuth
  - authorization standard used by many websites
- SAML (Security Assertion Markup Language)
  - XML-based open standard for exchanging authentication and authorization info
- OpenID
  - standard for decentralized authentication
- 802.1x
  - IEEE standard for Network Access Control (NAC)
  - for devices that want to connect to a network
  - rely on RADIUS
- RADIUS (Remote Authentication Dial-In User Service)
  - AAA
  - Operate via TCP or UDP on client-server model
  - sends passwords obfuscated by shared secret and md5 hash
- TACAS
  - Another AAA from Cisco
- Kerberos
  - between trusted hosts on untrusted network
  - users composed of 3 elements:
    - the primary (a username)
    - the instance
    - the realm (groups of users)
      - realms separated by Kerberos key distribution centers
- EAP (Extensible Authentication Protocol)
  - wireless technology
- CHAP (Challenge Handshake Authentication Protocol)
  - provide more security than PAP
  - 3-way handshake

SSO coupled with LDAP and Kerberos

#### Federation

## Authentication Methods

- passwords are most common

Best practices:

- reducing password complexity - favor longer passwords
- not requiring special characters
- allwoing ascii and unicode chars in passwords
- allowing pasting into pw fields and allows pw managers to work properly
- monitoring new passwords to ensure not easily compromised
- eliminating password hints

Settings:

- length
- complexity
- reuse limitations
- expiration dates
- age settings

### Password Managers

- 1Password
- Bitwarden

### Passwordless

- increasingly common

Lean on:

- security tokens
- otps
- certs
- biometrics

### Multifactor Authentication (MFA)

- something you know
  - password, pin, security question
- something you have
  - smartcard, usb/bluetooth, object, key
- something you are
  - biometrics, typing speed and pattern
- somewhere you are
  - gps

### One-Time Passwords

- time based one time password (TOTP)
  - alg generates code based on current time
- hmac based (hash-based message auth code) - HOTP
  - typically based on a counter

### Biometrics

- fingerprints
- retina
- iris
- facial rec
- voice rec
- vein (blood) rec
- gait analysis

four major markers:

- type 1 errors - fals rejection rate (FRR)
- type 2 errors - false acceptane rate (FAR)
- ROC - recever operating characteristic, compares the two

## Accounts

Claiming an id requires an account. Accounts contain info about user, rights, permissions

### Account Types

- User accounts
- Privileged or admin accounts
- Shared and generic accounts
- Guest accounts
- Service accounts

### Provisioning and Deprovisioning Accounts

permission creep: when users take on new roles and permissions not associated with current or past role

### Privileged Access Management

PAM tools can be used to handle admin and privileged accounts. focus on least priviledged

Features:

- Just-in-Time (JIT) permissions
  - granted and revoked as needed
- Password vaulting
  - for emergencies
- Ephemeral accounts
  - temp accounts with limited lifespans

## Access Control Schemes

determine which users, services, programs can access variou files or objects they host

- Mandatory Access Control (MAC) systems
  - rely on operating system to enforce control
  - came from government and military
  - SELinux, Windows as Mandatory Integrity Control (MIC)
  - reltively rare
- Discretinoary Access Control (DAC)
  - used on personal PCs
- Role-based Access Control (RBAC)
  - popular in enterprise
  - role assignment - onlu use permisisons to match role assigned
  - role authorization - prevent taking on roles shouldnt
  - permission authorization - only use permissions active role is allowed
- Rule-based AC (RuBAC)
  - rules and ACLs
  - firewalls
- Attribute-based AC (ABAC)
  - based on attributes of users (typically context driven)

Two additional concepts:

- Time-of-day restrictions
- Least privilege

### Filesystemm Permissions

- linux chmod, read, write, execute

## Exam Essentials

- Identities are the foundation of authentication and authorization
- SSO and federation are core elements of many id infrastructures
- Passwords, passwordless authentication, and MFA all have roles to play in authentication systems
- Account types and account policies determine what users can do and provoleged accounts must be managed and controlled
- Access control schemes determine what rights accounts have

## Review Questions

- 1. C  ~D
- 2. A  A
- 3. D  ~B idk
- 4. D  D
- 5. D  ~B idk
- 6. A  A
- 7. A  ~B idk
- 8. A  A
- 9. C  C
- 10. D D
- 11. B B
- 12. A A
- 13. C C
- 14. D D
- 15. B B
- 16. C C
- 17. A A
- 18. C C
- 19. C C
- 20. C C

16/20 = .80
