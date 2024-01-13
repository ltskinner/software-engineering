# Chapter 3. Malicious Code

## Malware

- Malware:
  - wide range of software that is intentionally designed to cause harm to systems and devices, networks, or users
  - can also gather information, provide illicit access, take a broad range of actions that the legitimate owner of a system or network may not want to occur

Exam Note:

When tackling malware-based questions, need to know the distinctive characteristics of each type of malware and how you tell them apart

### Raansomware

- malware that takes over a computer and demands a ransom
- crypto malware (encrypts files and holds hostage)
- driven by phishing campaigns or rdp, w/e

IoCs

- C2 (C&C) traffic to known malicious ip
- Use of legitimate tools in abnormal ways to retain control
- Lateral movement to attack or gain info
- encryption of files
- notice to end users of encryption process
- data exfil

Mitigations

- backup system that stores files in separate location

### Trojans

- malware that is typically disguised as legitimate software
- will typically download more software after initial trojan in

IoCs

- Signatures for the specific malware applications or downloadable files
- C2 hostnames and IP addresses
- Folders or files created on target devices

Remote access Trojans (RATs)

Triada Trojan poses as enhanced version of WhatsApp

Mitigations

- User awreness practices to prevent downloading and running
- Anti-malware, EDR, other tools to id and stop malicious software

### Worms

- unlike trojans (that require user interactions), worms spread themselves
- spread via automated means
- self install, rather than requiring users to click on them

IoCs

- Known malicious files
- Downloads of additional components from remote systems
- Command and control contact to remote systems
- Malicious behaviors using system commands for injection and other activities, including use of cmd.exe, msiexec.exe, and others
- Hands-on-keyboard attacker activity

Mitigations

- effective network-level control focused on preventing infection traffic
- Firewalls, IPS, network segmentation
- Patching and configuring services to limit attack surfaces
- Post infection - antimalware, EFR, similar tools

### Sypoware

- malware designed to obtain information about an individual, org, or system
- various types exist, with different info targetted by each
- combated using antimalware tools

IoCs

- Remote-access and remote-control-related indicators
- Known software file fingerprints
- Malicious processes, often disguised as system processes
- Injection attacks against browsers

Mitigations

- focus on awareness, control of software that is allowed on devices and systems

### Bloatware

- preinstalled software
- generally unwanted applications
- usually isnt intentionally malicious
  - kinda just remove cause it may be bad software wasting resources

### Viruses

- malicious programs that self-copy and self-replicate once activated
- unlike worms, they dont spread temselves via vulnurable services and networks
- viruses require one or more infection mechanisms that they use to spread themselves
- typically have:
  - a *trigger* - sets conditions for when virus will execute
  - a *payload* - is what the virus does, delivers, or actions it performs

Varieties:

- Memory-resident viruses, which remain in memory while the system of the device is running
- Non-memory-resident viruses, which execute, spread, and then shut down
- Boot sector viruses, which reside inside the boot sector of a drive or storage media
- Macro viruses, which use macros or code inside word processing software or other tools to spread
- Email viruses that spread via email either as email attachments or as part of the email itself using flaus inside email clients
- File-less virus - spam emails, browser plugins, etc

IoCs:

- basically threat feeds lol

Mitigations

- keeping everything up to date
- antimalware tools
- network level defenses (IPS)
- reputation-based protection systems

### KeyLoggers

- capture keywtrokes from a keyboard, other inputs to computers

IoCs

- File hashes and signatures
- Exfiltration activity to command and control systems
- Process names
- Known reference URLs

### Logic Bombs

- funtions or code placed within other programs that will activate when set conditions are met
- Because based within code, IoCs are less common (cause have to examine the logic)

### Rootkits

- specifically designed to allow attackers to access a system through a backdoor

IoCs

- File hashes and signatures
- C2 domains, IP addresses, and systems
- Behavior-based identification like the creation of services, executables, configuration changes, file access, and command invocation
- Open ports or creation of reverse proxy tunnels

## Summary

## Exam Essentials

- Understand and explain the different types of malware
- Explain common indicators of malicious activity associated with malware types
- Understand the methods to mitigate malware

## Review Questions

- 1. B  B
- 2. C  C
- 3. A  A
- 4. 6667 A A (6667 botnet C2 port)
- 5. D  D
- 6. A  A
- 7. C  C
- 8. C stupid ass question  ~D
- 9. D  D
- 10. C C
- 11. B B
- 12. C C
- 13. B B
- 14. B worm v virus  B
- 15. B dumb ass question B
- 16. B B
- 17. C C
- 18. D D
- 19. A A
- 20. A A


