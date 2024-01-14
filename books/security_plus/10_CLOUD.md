# Chapter 10. Cloud and Virtualization Security

## Benefits of the Cloud

- On-demand self-service computing
- Scalability
- Elasticity
- Measured service
- Agility and flexibility (prototyping)

### Cloud Roles

5 key roles:

- cloud service providers
- cloud consumers (users)
- cloud partners (or cloud brokers), training etc
- cloud auditors
- cloud carriers (intermediaries that provide connectivity)

### Cloud Service Models

- Infrastructure as a Service
  - hardware
- Software as a Service
  - Fully managed applications
- Platform as a Service
  - Middle ground
  - Function as a Service is subset
    - AWS Lambda
    - Serverless computing

### Cloud Deployment Models

- public cloud
- private cloud
- community cloud
- hybrid cloud
  - bursting when private is overrun

### Shared Responsibility Model

- edge computing - some processing on remote sensors
- fog computing - iot devices send data to local gateway before forwarding to cloud

## Virtualization

### Hypervisors

- type 1 - bare metal, on top of hardware
- type 2 - app on top of existing os

## Cloud Infrastructure Components

### Cloud Compute Resources

- Virtualization
- Containerization
  - provide application level cirtualization, but must be protected like VMs
  - Enforced isolation between containers to prevent operational and security issues is recommended
- Cloud Storage Resources
  - Block storage - virtual disks
  - Object storage
  - Security considerations:
    - Permissions
    - High availability and durability options
    - Use encryption
- Cloud Networking
- Security groups
- Virtual Private Cloud (VPC)
  - Network segmentation, VLANs
- DevOps and Cloud Automation

## Cloud Security Issues

- Availability
- Data Sovereignty
- Virtualization Security (escape vulnurabilities)
  - vm sprawl
  - resource reuse
- Application Security
  - Secure Web Gateways provide layer
- Governance and Auditing of Third-Party Vendors

## Hardening Cloud Infrastructure

### Cloud Access Security Brokers

Software tools that serve as intermediaries between cloud service users and cloud servie providers

- Inline CASB solutions
  - physically or logically reside in connection path between user and the service
  - allow CASB to block requests that violate policy
- API-based CASB solutions
  - basically just monitor and report

### Resource Policies

### Secrets Management

HSM

## Exam Essentials

- Explain the three major cloud service models
- Describe the four major cloud deployment models
- Understand the shared responsibility model of cloud security
- Implement appropriate security controls in a cloud environment

## Review Questions

- 1. B  ~C wording
- 2. C  C
- 3. C  ~D debate
- 4. B  ~A fair
- 5. A  A
- 6. C  C
- 7. B  B
- 8. C  ~D wording
- 9. A  A
- 10. B ~C rere
- 11. A ~D fair
- 12. D ~C disagree
- 13. A A
- 14. C ~A really?
- 15. D D
- 16. C ~A fair
- 17. A ~C fair
- 18. D D
- 19. A ~D unreal
- 20. A A

9/20 = .45
