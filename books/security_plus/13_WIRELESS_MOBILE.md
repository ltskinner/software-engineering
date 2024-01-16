# Chapter 13. Wireless and Mobile Security

## Building Secure Wireless Networks

### Connection Methods

- Cellular
  - Divides geo areas into cells
  - LTE 4G
  - 5G requires more attention to antenna deployment
  - because ran by external company, treat as external network
- Wi-Fi
  - 2.4 GHz and 5GHz bands with multiple channels
  - one of most important security concern is signal traveling beyond space org owns
  - WPA2 and WPA3 provide security features, like encryption, protection for network frames, and authentication options
  - two modes of deployment:
    - ad hoc: allows devices to talk to each other directly
    - infrastructure: sends traffic through a base station or access point
  - use SSID (service set identifiers) to id network name
- Bluetooth
  - 2.4GHz
  - low power, short range (5-30, max 100m)
  - point-to-point model rather than client-server
  - security modes:
    - 1: no security
    - 2: service-level enforced security
    - 3: Link-level security
    - 4: Standard pairing with Security Simple Pairing (SSP)
- RFID
  - passive tags under 1ft - powered by the reader
  - active 100m - have own power source and send signals to be read
  - attacks: destruction/damage, reprogramming, cloned, modified, spooved
- GPS

### Wireless Network Models

- point to point
- point to multipoint
- mesh
- broadcast

### Attacks Against Wireless Networks and Devices

#### Evil Twins and Rogue Access Points

- evil twin: malicious illigitimate access point setup to appear to be a legitimate, trusted network
- rogue access points: aps added to network intentionally or unintentionally and offer attackers a point of entry to network

most modern wireless controller systems have functionality to detect new access points where they are deployed

#### Bluetooth Attacks

- bluejacking: sends unsolicited messages to bluetooth devices
- bluesnarfing: unauthorized access to a bluetooth device, aimed at gathering information like contact lists

not much you can do. best you can do is turn off when not in use

### RF and Protocol Attacks

help with evil twins

- disassociation: when a device disconnects from an ap. when this happens, will attempt to reconnect
  - uses "deauthentication frame"
  - works against WPA2 but not WPA3, which requires protected management frames
- Jamming: blocks all traffic in the range

### Sideloading and Jailbreaks

- sideloading: process of trasferring files to a mobile device, typically vis USB, MicroSD, or bluetooth, in order to install apps outside of official app store
- Jailbreaking: priviledge escalation attack

## Designing a Network

- careful access point placement
  - do a site survey:
    - walk thry facility to determing what existing networks are in place
    - id possible locations for your aps
  - heatmaps:
    - show where signal is, how strong, and what channels each ap or device is on
- determine which channels that aps will use
  - each channel is 20 MHz wide, with a 5MHz space between
  - 11 channels for 2.4 GHz
  - 1, 6, 11 are used when possible to avoid overlap
  - many aps select best channel when deployed

### Controller and Access Point Security

Enterprise networks rely on Wireless Local Area Network (WLAN) controllers

- intelligence and monitoring
- software defined wireless networks
- blended wifi and 5g roaming

configure:

- change default settings
- disable insecure protocols and services
- set strong passwords
- protect admin interfaces
- ensure regularly patched
- turning on monitoring and logging

### Wi-Fi Security Standards

- WPA2
  - WPA2-personal (WPA2-PSK)
    - uses preshared key, allows users to authenticate without authentication infrastructure
  - WPA2-Enterprise
    - relies on RADIUS authentication as part of 802.1X
    - users have unique creds and must be individually id'd
  - has Counter Mode Cipher Block Chaining Message Authentication Code Protocol (CCMP)
    - uses AES to provide confidentiality
    - stonger than WEP
- WPA3
  - Personal and Enterprise
  - Personal allows Simultaneous Authentication of Equals (SAE)
    - places pre-shared keys in WPA2 and requires both client and network to validate both sides
    - slows down brute force
  - also uses perfect forward secrecy
    - ensures traffic sent between client and network is secure even if clients password is compromised
  - has user authentication AND network authentication
  - opportunistic wireless encryption (OWE) to encrypt on open networks when possible

### Wireless Authentication

- open networks:
  - dont require authentication but use captive portal
  - no encryption
- use preshared keys (PSKs):
  - passphrase shared with anyone who wants to use network
  - encrypted but not uniquely idd
- enterprise authentication:
  - RADIUS with EAP

### Wireless Authentication Protocols

802.1X - for wired and wireless

EAP variants:

- Protected EAP (PEAP):
  - authenticates servers using a certificate and wraps EAP in TLS
  - devices on the network use unique encryption keys
  - Temporal Key Integrity Protocol (TKIP) to replace keys on regular basis
- EAP-FAST:
  - build on LEAP
  - faster reauthentication
  - works around public key exchanges that slow PEAP and EAP-TLS bu using a shared secret (symmetric) key
- EAP-TLS
  - both client and network devices to generate keys
  - infrequent use due to cert management
- EAP-TTLS
  - extends EAP-TLS but does not require client to have cert to create a secure session
  - concern: requires additional software

eduroam is for students, uses RADIUS

## Managing Secure Mobile Devices

### Mobile Device Deployment Models

- BYOD
  - bring your own device
  - you own, you manage
- CYOD
  - choose your own device
  - select option
  - org manages, org owns
- COPE
  - corporate owned, personally enabled
  - you can do some personal shit on it
- Corporate owned

### Hardening Mobile Devices

mobile devices are not well designed for central management

### Mobile Device Management

Difficulties:

- os limitations
- variability in hw manufacturers
- carrier settings
- os versions

orgs turn to tools:

- mobile device management (MDM)
- unified endpoint management (UEM)

Tunable features:

- application management: installing, updating
- content management/storage segmentation: what files are allowed (from work)
- remote-wipe: full wipe or org data wipe, both with confirmation of wipe
- geolocating and geofencing: work or not work in regions, id lost devices
- screen locks, passwords, pins (context aware too)
- biometrics
- containerization to separate work and personal
- full disk encryption
- push messages

## Exam Essentials

- Modern enterprises rely on many types of wireless connectivity
- Secure wireless network designs take existing networks and physical spaces into account
- Cryptographic and authentication protocols provide wireless security
- Understand mobile device vulnurabilities
- Securing underlying wireless infrastructure requires strong network device administration and security practices
- Managing mobile devices relies on both deployment methods and administrative tools

## Review Questions

- 1. B  B
- 2. D  D
- 3. B  B
- 4. D  D
- 5. C  C
- 6. A  A
- 7. B  ~C PEAP idk
- 8. A  A
- 9. C  C
- 10. B B
- 11. C C
- 12. C ~A ok bs
- 13. B B
- 14. C C
- 15. B B
- 16. D D
- 17. C C i def said heatmap
- 18. D D
- 19. B B
- 20. C C

18/20 = .90
