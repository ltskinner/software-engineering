# Chapter 9. Resilience and Physical Security

## Resilience and Recovery in Security Architectures

A sometimes neglected element of availability is resilience and the ability to recover

Common elements in designs for redundancy:

- geographic dispersion of systems
- separation of servers and other devices in a datacenter
- use of multiple network paths (multipath)
- redundant network devices
  - load balancing
  - clustering - groups of computers connected together to perform the same task
- protection of power - uninteruptible power supply (UPS)
- system and storage redundancy
- platform diversity - of technologies and vendors

### Architectural Considerations and Security

concerns:

- availability
- resilience (level of disruption can handle without an availability issue)
- cost
- responsiveness
- scalability
- ease of deployment
- risk transferrence (insurence)
- ease of recovery
- patch availability and vendor support
- inability to patch
- power consumption
- compute requirements

### Storage Resiliency

| RAID description | Description | Advantage | Disadvantage |
| - | - | - | - |
| RAID 0 - Striping | Data is spread across all drives in the array | Better IO performance (speed); all capacity used | Not fault tolerant - all data is lost if a drive is lost |
| RAID 1 - Mirroring | All data is duplicated to another drive or drives | High read speeds from multiple drives; data is available if a drive fails | Uses twice the storage for the same amount of data |
| RAID 5 - Striping with parity | Data is striped across drives with one drive used for parity (checksum) of disk. parity is spread across drives as well as data | Data reads are fast; data writes are slightly slower. Drive failures can be rebuild as long as only a single drive fails | Can tolerate only a single drive failure at a time. Rebuilding arrays after a drive loss can be slow and impact performance |
| RAID 10 - mirroring and striping | Requires at least four dries, with drives added in pairs. Data is mirrored, then striped across drives | Combines the advantages and disadvantages of both RIAD 0 and RAID 1 | Combines the advantages and disadvantages of both RAID 0 and RAID 1. Sometimes written as RAID 1+0 |

- replication
  - focuses on either synchronous or asynchonous methods to copy live data to another location or device
  - happens as soon as changes made
- journaling
  - creates a log of changes that can be reapplied if an issue occurs
- recovery
  - recovery point objectives (RPOs)
  - recovery time objectives (RTOs)
- snapshot
  - full state of system
  - common in vms
- images
  - similar to snapshot
  - but down to bit level of drive

Backup media:

- tape
  - low cost
  - large scale
- disk
  - magnetic or ssd
  - faster than tape
- optical media
  - blue ray, dvd
  - not common for large scale backups
- flash media
  - microSD
  - usb

backup types:

- online is high avilability
- offline are slow but verify not having complete data loss
- nearline - offline but can become offline w/o human intervention (robot+tapes)

third party backup considerations:

- bandwidth requirements
- time to retrieve files and cost to retrieve
- reliability
- new security models required for backups

## Response and Recovery Controls

Types of sites:

- hot sites
  - all infrastructure and data needed to operate org
- warm sites
  - some or all infrastructure
  - no live data
- cold sites
  - space, power, network
  - not prepared with systems or data

Restoration order:

- network
- firewall
- storage, dbs
- operational servers
- logging and monitoring
- other services

### Capacity Planning for Resilience and Recovery

Areas:

- People (staffing)
- Technology (software)
- Infrastructure (hardware)

### Testing Resilience and Recovery Controls and Designs

4 methods:

- tabletop exercises
  - discussions
  - least disruptive
- Simulation exercises - dont actually make the change
  - drills
  - may cause disruption
- Parallel processing exercises - both sites same time
  - move processing to hot site or alternate/backup system
  - potential to disrupt
- Failover - actual failover
  - test a full fail and failing over to alternate system or site
  - greatest potential for disruption

## Physical Security Controls

### Site Security

Security thru obscurity

- fences
- bollards - prevent vehicle access
- lighting
- drones
- access badges

### Guards

### Video Surveillance, Cameras, Sensors

- motion detection
- object detection

### Sensors

- infrared sensors
- pressure sensors
- microwave sensors (more expensive)
- ultrasonice sensors (uncommon)

### Detecting Physical Attacks

- Brute force (breaking down doors, cutting locks)
- Radio frequency id (RFID) cloning
- Environmental attacks (going after heating or cooling)

## Exam Essentials

- Redundancy builds resilience
- Backups help ensure organizations can recover from events and issues
- Response and recovery are critical when failures occur
- Physical security controls are a first line of defense

## Review Questions

- 1. A  A
- 2. C  ~D - differential is since last full backup, incrementel is since las non full
- 3. B  B
- 4. A  ~C
- 5. B  B
- 6. A  A
- 7. D  D
- 8. D  D
- 9. D  ~C bro what "any point in time" means journaling
- 10. A A
- 11. A A
- 12. C C
- 13. A A
- 14. C C
- 15. D D
- 16. D D
- 17. C ~A
- 18. A ~B bro what
- 19. B B
- 20. C C

15/20 = .75
