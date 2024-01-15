# Chapter 11. Endpoint Security

## Operating System Vulnurabilities

- vulnurabilities
- defaults
- configs
- misconfigs

## Hardware Vulnurabilities

- firmware
- end-of-life hardware
- legacy hardware
  - issue is lack of support

## Protecting Endpoints

can be wired or wireless

things to worry about:

- preserving boot integrity
  - Unified Extensibel Firmware Interfae (UEFI) replaces BIOS
    - secure boot: boot only using software the orig mfct trusts. checks for sigs
    - measured boot: checks hashes. data stored in Trusted Platform Module (TPM)

TPMs have three major functions:

- Remote attestation, allowing hardware and software configs to be verified
- binding, which encrypts data
- sealing, which encrypts data and sets requirements for the state of the TPM chip before decryption

Physically Unclonable Functions (PUFs)

Hardware Security Modules (HSMs) - trypically external devices you plug in

Exam Note:

- TPMs are used for system security
- HSMs are used to create, store, and manage keys for multiple systems
- KMS is a service used to manage secrets

### Endpoint Security Tools

- Antivirus and Antimalware
  - Signature-based detection, hash or pattern to id files or components of previously observed malware
- Heuristic, or behavior-based detection - looks at actions software takes and matches them to profiles of unwanted activities
- AI/ML
- Sandboxing - isolating malware

### Allow Lists and Deny Lists

Control applications that can and cannot be installed. Not widely used bc large effort to maintain

Allow provides greater security than Deny

Deny less likely to interfere with unknown or new apps or programs

### Endpoint Detection and Response and Extended Detection and Response

Endpoint Detection and Response (EDR)

- combine monitoring with network monitoring and log analysis
- allow search and exploration

XDR

- not only endpoints, the full tech stack (cloud, email, etc)
- ingest logs and churn

### Data Loss Prevention

- ability to classify data
- labeling and tagging
- policy management and enforcement
- monitoring and reporting

dont let data leave the org!

### Network Defenses

- host-based firewalls: built into most modern os
  - simple filtering, no analysis
- host-based intrusion prevention system (HIPS)
  - analyzes traffic before services or applications on the host process it
  - can take action on traffic
  - will sometimes block legit traffic
- host-based intrusion detection system (HIDS)
  - performs similar, but cannot block traffic, only report on it

## Hardening Techniques

### Hardening

- can nab some scripts from CIS and NIST

Key things to do:

- encryption
- installing endpoint protection
- host-based firewalls
- host-based intrusion prevention systems
- disabling ports and protocols
- changing default passwords
- removing unnecessary software

### Service hardening

Common ports and services

| Port and protocol | Windows | Linux |
| - | - | - |
| 22/TCP - Secure Shell (SSH) | Uncommon | Common |
| 53/TCP and UDP - DNS | Common (servers) | Common (servers) |
| 80/TCP - HTTP | Common (servers) | Common (servers) |
| 125-139/TCP and UDP - NetBIOS | Common | Occasional |
| 389/TCP and UDP - LDAP | Common (servers) | Common (servers) |
| 443/TCP - HTTPS | Common (servers) | Common (servers) |
| 3389/TCP and UDP | Remote Desktop Protocol | Common | Uncommon |

- Windows service management: Services.msc
- Linux service management: service [cmd options]

### Network Hardening

- use VLANS

### Default Passwords

### Removing Unnecessary Software

## Operating System Hardening

### Hardening the Windows Registry

- attackers use it to start programs, gather info, and do shit
- should disable remote access
- limiting access to registry tools

### Windows Group Policy and Hardening

GPOs - Group Policy Objects

- can apply localy
- or via Active Directory

MSFT also provides the Security Compliance Toolkit (SCT)

### Hardening Linux: SELinux

Security-Enhanced Linux - kernel-based security module

- Mandatory access control (MAC) enforced at the user, file, system service, and network layer

### Configuration, Standards, and Schemas

To harden in an enterprise environment, need to manage configs. configuration management software is useful

- often start with *baseline configuration* and customize from there

Three phases of a baselines life cycle:

- establishing a baseline (using industry standard)
- deploying the baseline (using mgmt tools)
- maintaining the baseline (using mgmt tools)

### Patching and Patch Management

timely patching decreases how long exploits and flaws can be used against systems

### Encryption

do full-disk encryption (FDE)

if done at hardware level, done with a self-encrypting drive (SED)

## Security Embedded and Specialized Systems

### Embedded Systems

computer systems built into other devices

many use: real-time operating system (RTOS)

os that priority needs to be placed on processing data as it comes in, instead of using interrupts or waiting for task to process

### SCADA and ICS

ICS - industrial control system

SCADA - Supervisory control and data acquisition

run power and water distribution

SCADA is a type of system architecture

Remote TU (RTUs) are used to collect data and pass onto an ICS or SCADA

### Securing the Internet of Things

Common issues:

- poor security practices:
  - weak default settings
  - lack of network security (firewalls)
  - exposed or vulnurable services
  - lack of encryption
  - weak authentication
  - embedded credentials
  - insecure data persistence
- short lifespans
  - IoT devices may never be patched or updated....
- vendor data-handling issues
  - licensing and ownership concerns

### Communication Considerations

Many embedded and specialized systems operate in environments where traditional wired and wireless networks arent available

### Security Constraints of Embedded Systems

- lower compute power
- lack of network conectivity
- authentication likely impossible
- uhh custom made or novel shit has no other options lol

## Asset Management

- provisioning and decomissioning
- enumerating (tracking id of known assets as well as unexpected "assets")

### Decomisisoning

- removing and wiping disks
- or destrooy lol

Certificates are issued when an asset is decomisisoned, or something destroyed

### Retention

- may be required for legal purposes

## Exam Essentials

- Understand operating system and hardware vulnurabilities
- Hardening and protecting systems relies on security tools and technology to keep systems secure
- Hardening endpoints also relies on configuration, settings, policies, and standards to ensure system security
- Specialized systems like SCADA, ICS, and IoT systems exist throughout your org and require unique security solutions
- Explain the importance of asset management for software, data, and hardware
- Drive encryptoin and sanitization help prevent data exposure

## Review Quesions

- 1. B  B
- 2. B  ~C idk
- 3. C  C or B idk how nosian
- 4. C  C
- 5. C  C
- 6. B  B idk
- 7. A  A
- 8. D  D
- 9. D  ~B this is shit question
- 10. A A
- 11. C ~B ok thats shit but fair
- 12. B ~A idk tho footprint = surface thank god theres two words for it
- 13. A A
- 14. D D
- 15. B B
- 16. D ~A asleep implies locked? nosian
- 17. B B
- 18. B B
- 19. C C
- 20. A A

15/20 = .75
