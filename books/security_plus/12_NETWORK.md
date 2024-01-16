# Chapter 12. Network Security

## Designing Secure Networks

*Selection of effective controls* is key component in securing networks

Keep "defense in depth" in mind

### Networking Cocnepts: the OSI Model

7 layers - host layers (4-7), and media layers (1-3)

- 7. Application layer -> human/computer interaction
- 6. Presentation layer -> format data, handles data encryption, compression
- 5. Session layer -> authentication, sessions, permissions
- 4. Transport layer -> transmission of data, error control (TCP, UDP)
- 3. Network layer -> physical path decisions, addressing, routing (IP, ICMP, IPSec)
- 2. Data Link layer -> data format for the network error detection, flow control (Frames, Ethernet)
- 1. Physical Layer -> sends electrical impulses, light, and radio waves (Cables, NICs)

### Infrastructure Considerations

Key concerns:

- attack surface - points where unauthorized user could gain access
- device placement - place in specific zones or network segment
- security zones - related do device placement, physical or virtual
- connectivity considerations - how connect to outside internet
- failure modes - how should something fail? fail-closed and fail-open
- network taps (which monitor and acecss traffic) - can be active or passive

## Network Design Concepts

- Physical Isolation - idea of separating devices so no connection (air-gapped)
- Logical Segmentation - VLANs
- High Availability (HA)
  - ability of service, network, to be consistently available without downtime
  - can patch, handle failures, change load, without interruption of services
- Implementation of secure protocols - literall use TLS or SSH
- Reputation Services - track IP addresses, domains, of hosts that are malicious
- Software-Defined Networking
- SD-WAN - software-defined wide area network - 4G, 5G, broadband
- Secure Access Service Edge (SASE)
  - dump vpn, sdwan cloud, firewall, casb, zero-trust into one thing to enable secure access for devices regardless of location
- Network Segmentation - divide network into logical or physical groupings, based on trust, function, etc. use VLANs
  - broadcast domain: segment of network where all devices can reach one another
  - screened subnets (aka DMZs) - network zones that contain systems that are exposed to less trusted areas
  - Intranets - internal networks, protected from external access
  - Extranet - for external access

### Zero Trust

Presumes there is no trust boundary and no network edge. each action is validated when requested as part of continuous authentication process

By the NIST model:

- *Subjects* are users, services, or systems that request access or attempt to use rights
- *Policy Engines* make policy decisions based on both rules and external systems (threat intelligent, iam, etc). Once a decision is made, is logged, and policy admin takes action
- *Policy Administrators* components that establish or remove comms path between subject and resource
- *Policy Enforcement Points* communicate w Policy Admins to fwd requests from subjects and receive instruction

Shit for test:

- Control Plane:
  - Adaptive identity: leverages context-based auth, such as where user logged in from, device used, etc
  - Threat scope reduction: limits scope of what subject can do and associated access
  - Policy-driven access control: use policies?
  - The Policy Administrator: ?
- Data Plane:
  - Implicit trust zones: which allow use and movement once a subject is authenticated by a Zero Trust Policy Engine
  - Subjects and systems (subjects/system) which are the devices and users that are seeking access
  - Policy Enforcement Plints

### Network Access Control (NAC)

Determine whether a system or device should be allowed to connect to a network

#### NAC and 802.1X

- 802.1X is std for authenticating devices connected to networks, using EAP

### Port Security and Port-Level Protections

- Port security is a capability that allows you to limit the number of MAC addresses that can be used on a single port
- Spoofing MAC addresses is relatively easy, so dont rely on port security

Protocol level protections:

- Loop prevention forcuses on detecting loops and then disabling ports to prevent the loops form causing issues. Spanning Tree Protocil
- Broadcase storm prevention, prevents broadcast packets from being amplified as they traverse a network
- Bridge Protocol Data Unit (BPDU) Guard - prevents ports that shouldnt send from sending BPDUs?
- Dynamic Host Configuration Protocol (DHCP) snooping - preents rogue DHCP servers from handing out IP addresses to clients on managed network

### Virtual Private Networks and Remote Access

Way to create a virtual network link across a public network. Allows the endpoints to act as thought they are on the same networking - easy to think about a VPN as an encrypted tunnel, though encryption is not formally required

Two VPN technologies:

- IPSec VPNs
  - operate at layer 3
  - operate in tunnel or transport mode
  - in tunnel, entire packets are protected
  - in transport, IP header not protected, but IP payload is
  - used for site-to-site, and for transporting more than just web and application traffic
- SSL VPNs
  - lol actually use TLS now
  - portal based, like access thru HTML page, then access services thru the connection
  - or tunnel mode
  - popular can be used without a client installed, or endpoint config
  - also enable segment application access

Decision boundaries:

- whether used for remote access, or for site-to-site
  - remote access vpns common for remote workers
    - remote access are used as-needed
  - site-to-site always on and will try to reconnect
- tunneling
  - split-tunnel
    - only sends traffic intended for systems on the remote network
    - less bandwidth
  - full-tunnel
    - sends all traffick through tunnel

### Network Appliances and Security Tools

#### Jump Servers

Secured and monitored system to provide access to secure areas of a network with different security levels

#### Load Balancing

Distribute traffic to multiple systems, providing redundancy, and allowing ease of upgrades and patching

Modes of operation:

- Active/active: designs distribute the load among multiple systems that are online and in use at the same time
- Active/passive: designs bring backup or sencondary systems online when an active system is removed or fails. part of disaster recovery

Load balancing algorithms:

- Round-robin: sends each request to servers by working through a list, with each server receiving traffic in turn
- Least connection: sends traffic to the server with the fewest number of active connections
- Agent-based adaptive: monitors the load and other factors that impact a servers ability to respond and updates the load balancers traffic based on reports
- Source IP hashing: uses a hash of the source IP to assign traffic to servers. Essentially random

Weighted algs:

- Weighted least connection: uses least connection alg combined with a predetermined weight for each server
- Fixed weighted: relies on preassigned weight for each server, often based on capability or capacity
- Weighted response time: combines servers current response time with weight value to assign it traffic

Also need to establish persistent sessions

#### Layer 4 vs Layer 7

for firewalls, this is a big deal

#### Proxy Servers

Accept and forward requests, centralizing requests and allowing actions to be taken on requests and responses. Can filter or modify traffic, and cache data

- Forward proxies: placed in between clients and servers
- Reverse proxies: placed between servers and clients, used to load balance and cache content. Clients can query single system but have traffic load spread to multiple systems or sites

#### Web Filters

Content filters

Centralized proxy devices or agent-based tools that allow or block traffic based on content rules. Can be as simple as conducting Uniform Resource Locator (URL) scanning

#### Data Protection

part of Data Loss Prevention (DLP)

#### IDS and IPS

- signature-based detections: rely on known hash or signature matching to detect a threat
- anomaly-based detection: establishes a baseline and flags out of ordinary behavior

both can be placed in active or passive modes. passive just listens without taking action

##### Configuration Decisions: Inline vs Tap, Active vs. Passive

#### Firewalls

- stateless firewalls: (packet filters) filter every packet based on data such as source ip, port, protocol
- stateful firewall: (dynamic packet filters) pay attention to the state of traffic between systems. can make a decision about a conversation and allow it to continue once approved, rather than reviewing every packet. more context to make security decisions

Unified Threat Management (UTM)s include:

- firewall
- ids/ips
- antimalware
- url and email filtering
- dlp
- vpn
- security monitoring and analytics

UTMs are quick and out of the box. NGFW require more config and expertize

UTM deployed at network boundaries

Web Applicaiton Firewalls (WAFs)

- designed to intercept, analyze, and apply rules to web traffic
- include db queries, apis, web app tools
- like a firewall combined with ids

Example rule:

`ALLOW TCP port ANY from 10.0.10.0/24 to 10.1.1.68/32 to TCP port 80`

Firewalls can also be used to create screened subnets

#### Access Control Lists (ACLs)

Rules that either permit or deny actions

| Rule number | Protocol | Ports | Destination | Allow/deny | Notes |
| - | - | - | - | - | - |
| 10 | TCP | 22 | 10.0.10.0/24 | ALLOW | Allow SSH |
| 20 | TCP | 443 | 10.0.10.45/32 | ALLOW | Inbound HTTPS to web server |
| 30 | ICMP | ALL | 0.0.0.0/0 | DENY | Block ICMP |

### Deception and Distruption Technology

- honeypots
  - systems intentionally configured to appear vulnurable
- honeynets
  - networks setup to collect info about network attacks
  - group of honeypots
- honeyfiles
  - used for intrusion detection
  - contrain identifiers that get flagged leaving network
- honeytoken
  - data intended to be attractive, but allow tracking
  - entries in dbs, files, dirs

### Network Security, Services, and Management

#### Out-of-Band Management

Access to the management inferface for a network appliance or device needs to be protected so that attackers cant sieze control, and to ensure admins can reliably gain access when they need to.

Whenever possible, network designs must include a way to do secure out-of-band management

Achieved thru VLANs primarily, or entirely separate physical network

#### Domain Name System (DNS)

native DNS is not encrypted and there are no authentication abilities

DNSSSEC provides authentication of DNS data

Properly configuring DNS is key component.

- Prevent zone transfers
- ensure DNS logging is turned on
- ensure requests to malicious domains blocked

DNS Filtering - used by many orgs to block malicious domains. uses list of prohibited domains, subdomains, and hosts

#### Email Security

- DomainKeys Identified Mail (DKIM)
  - adds content to messages to id them as being from their domain
  - signs body and header
- Sender Policy Framework (SPF)
  - allows orgs to publish list of authorized email servers
- Domain-based Message Authentication Reporting and Conformance (DMARC)
  - protocol that uses DKIM and SPF to determine if email is authentic

#### Secure Sockets Layer/Transport Layer Security

TLS uses ephemeral (short lasting) keys - for perfect forward security. even if single key exchange is compromised, entire comm thread will not be

#### What about IPv6

IPv6 has many more addresses, but relies on ICMP

#### SNMP

Simple Network Management Protocol - used to manage network devices

network devices like:

- network switches
- routers
- other devices

listed in a management information base (MIB) and queried for SNMP information

SNMP trap: message sent when error occurs

#### Monitoring Services and Systems

- level 1: that a service port is open and responding
- level 2: that valid responses are received in timely manner
- level 3: looking for indicators of failure

#### File Integrity Monitors

detecting changes in files

Tripwire is faithful tool

#### Hardening Network Devices

everything we do for endpoints

be sure to protect the management console

## Secure Protocols

Not every connection is encrypted end-to-end

### Using Secure Protocols

- Voice and video:
  - video conference: https
  - Session Initiation Protocol (SIP) and Real-time Transport Protocol (RTP) exist
- Network Time Protocol (NTP) aka NTs
  - relies on TLS
  - does not protect time data
  - focuses on authentication to ensure info not changed in transit
- Email and web traffic:
  - HTTPS, IMAPS, POPs, Domain-based Message Authentication Reporting and Conformance (DMARC), DomainKeys Identified Mail (DKIM), Sender Policy Framework (SPF)
- File Transfer Protocol (FTP)
  - largely replaced by combination of HTTPS and SFTP or FTPS
- Directory services like LDAP can be moved to LDAPS
- Remote access technologies (like shell access) - was one Telnet, and now SSH
  - msft RDP is encrypted by default
  - others may use HTTPS to ensure traffic is not exposed
- Domain name resolutoin
  - DNSSEC
  - DNS reputation lists
- Routing and switching
  - Border Gateway Protocol (BGP)
  - unreliable. design around shortcomings
- Network address allocation
  - DHCP - not secure
  - security relies on detection and reponse, not secure protocol

| Unsecure protocol | Original port | Secure protocol option(s) | Secure port | Notes |
| - | - | - | - | - |
| DNS | UDP/TCP 53 | DNNSEC | UDP/TCP 53 | |
| FTP | TCP 21 (and 20) | FTPS | TCP 21 in explicit mode, and 990 in implicit mode (FTPS) | Using TLS |
| FTP | TCP 21 (and 20) | SFTP | TCP 22 (SSH) | Using SSH |
| HTTP | TCP 80 | HTTPS | TCP 443 | Using TLS |
| IMAP | TCP 143 | IMAPS | TCP 993 | Using TLS |
| LDAP | UDP and TCP 389 | LDAPS | TCP 636 | Using TLS |
| POP3 | TCP 110 | POP3 | TCP 995 - Secure POP3 | Using TLS |
| RTP | UDP 16384-32767 | SRTP | UDP 5004 | |
| SNMP | UDP 161 and 162 | SNMPv3 | UDP 161 and 162 | |
| Telnet | TCP 23 | SSH | TCP 22 | |

To memorize:

- DNNSEC focuses on ensuring DNS information is not modified or malicious, but doesnt provide confidentiality. digital signatures
- SNMPv3 adds authentication of message sources, message integrity, and confidentiality
- SSH - use passwords
- HTTPS - often called SSL
- SRTP (Secure Real-Time Protocol) for audio and video calls. uses encryption and authentication
- LDAPS - TLS protected version, offers confidentiality and integrity

#### Email-Related Protocols

- POP - Post Office Protocol
- Internet Message Access Protocol (IMAP)
- Secure/Multipurpose Internet Mail Extensions (S/MIME)
  - Provides ability to encrypt and sign MIME data (email attachments)
  - confidentiality, integrity, authentication, and nonrepudiation

#### File Transfer Protocols

- FTPS
  - FTP with TLS
  - can require additional ports
- SFTP
  - SSH
  - easier to get thru firewalls

#### IPSec

Internet Protocol Security

- Authentication Header (AH)
  - Uses hashing and shared secret key to ensure integrity of data
  - ensure IP payload and headers are protected
- Encapsulating Security Payload (ESP)
  - operates in either transport mode or tunnel mode
  - in tunnel, provides integrity and auth for entire packet
  - in transport, only protects payload

## Network Attacks

### On-Path Attacks (Man in the Middle)

Attacker intercepts traffic and forwards to original destination

Used to conduct ssl striping:

- user sends http request for web page
- server responds with redirect to https version
- users sends https to page they were redirected to

How to stop:

- expect good certs

#### Man in the Browser

- trojan inserted into browser
- trojan can access and modify info sent and received by browser

On-path attack indicators are typically changed network gateways or routes, or compromised switches or routers that redirect traffic

### Domain Name System Attacks

- Domain hijacking
  - changes registration of a domain
  - allows traffic to be intercepted, to send and receive email
  - basically act as true domain holder
- DNS poisoning
  - one form: on-path attack where attacker provides a DNS reponse while pretending to be an authoritative DNS server
  - another: vulns in DNS protocols or implementations can permit, but rate
  - another: posiioning DNS cache on systems. once a malicious dns entry is in a systems cache, it will continue to use that info until cahce is purged or updated
- URL redirection
  - insert alternate IP addresses into systems host-file

Use domain reputation services

### Credential Replay Attacks

- attacker captures valid network data
- resends or delys sending as to insert attackers data
- most common is to re-send authentication hashes
- common indicator are on path attack indicators like modified gateways or routes

### Malicious Code

### Distributed Denial-of-Service (DDoS)

distributed means multiple locations, networks, or systems

#### Network DDos

botnets

- volume-based
  - UDP floods
    - UDP doesnt use 3 way handshake
  - ICMP floods
    - ping floods
  - handle both with network rules
- protocol-based
  - SYN floods. gets ack back but doesnt sned final sun
  - ping of death - ping packet too large for many to handle
  - smurf attacks - icmp broadcase with spoofed sender, causing systems in boradcast domain to send traffic to fake sender thus overwhelming it
  - xmas tree attacks (tcp flags turned on) aka fragmented packets

#### Amplified Denial-of-Service Attacks

Take advantage of protocols that allow a small query to return large results, like a dNS query

#### Reflected Denial-of-Service Attacks

spoofed ip address causes a legitimate service to conduct the attack

can combine amplified and reflected

## Exam Essentials

- The foundation of network security is a secure design
- Network appliances are used to provide security services to networks and systems
- Network security services and management techniques help make sure that a network stays secure
- Secure protocols provide ways to send and receive information securely
- Network attacks drive network security decisions and designs

## Review Questions

- 1. C  C
- 2. C  C
- 3. B  B
- 4. D  D
- 5. B  B
- 6. A  A
- 7. A  A idk bro cesspool of acronyms
- 8. B  ~C - SD-WAN replace MPLS
- 9. D  D
- 10. D D
- 11. A ~B - policy enforcers
- 12. D ~C pos gotcha
- 13. A A
- 14. B B
- 15. C ~A guessed
- 16. D D
- 17. A ~B shit question
- 18. C C
- 19. A A
- 20. C C

15/20 = .75
