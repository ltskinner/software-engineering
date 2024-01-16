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
