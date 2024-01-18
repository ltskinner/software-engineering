# Chpter 16. Security Governance and Compliance

## Security Governance

Governance programs: are the sets of procedures and controls put in place to allow an orgnaization to effectively direct its work

### Governance, Risk, and Compliance Programs (GRCs)

- Governance of org
- Risk management
- Compliance

### Information Security Governance

### Types of Governance Structures

- Centralized governance models: use a top down approach where a central authority creates policies and standards, which are then enforced thoughout the organization
- Decentralized governance models: use a bottom-up approach, where individual business units are delegated the authority to achieve cybersecurity objectives and then may do so in the manner they see fit

## Understanding Policy Documents

*Information security policy framework* includes:

- Policies
- Standards
- Procedures
- Guidelines

Things to consider:

- Regulatory and legal requirements that mandate the use of certain protocols
- Industry-specific considerations that may alter your approach to information security
- Jurisdiction-specific considerations based on global, national, and/or local/regional issues in the areas where you operate

### Policies

High level statements of management intent. Compliance with policies is mandatory

- A statement of the importance of cybersecurity to the organization
- Requirements that all staff and contractors take measures to protect the confidentiality, integrity, and availability of information and information systems
- Statement on the ownership of information created and/or possessed by the organization
- Designation of the CISO or other individual as the executive repsponsible for cybersecurity issues
- Delegation of authority granting the aCISO the ability to create standards, procedures, and guidelines that implement the policy

Centers for Medicare and Medicaid Services (CMS) has big fatty doc (95 pages)

Orgs commonly include in their infosec policy library:

- Information security policy: that provides high-level authority and guidance for the security program
- Incident response policy: that describes how the organization will respond to secuirty incidents
- Acceptable use policy (AUP): that provides network and system users with clear direction on permissible uses of information resources
- Business continuity and disaster recovery policies that outline the procedures and strategies to ensure that essential business functions continue to operate during and after a disaster, and that data and assets are recovered and protected
- Software deevelopment life cycle (SDLC) policy: that establishes the processes and standards for developing and maintaining software, ensuring that security is considered and integrated at every stage of development
- Change management and change control policies: that describe how the organization will review, approve, and implement proposed changes to information systems in a manner that manages both cybersecurity and operational risk

### Standards

Provide mandatory requirements describing how an organization will carry out its information security policies (config settings, controls, etc)

Key standards:

- Password standards: set forth requirements for password length, complexity, reuse, and similar issues
- Access control standards: describe the account life cycle from provisioning through active use and decommissioning. This policy should include specific requirements for personnel who are employees of the org as well as contractors. Include requirements for credentials used by devices, service accounts, and admin/root accounts
- Physical security standards
- Encryption standards

### Procedures

Detailed, step-by-step processes that individuals and orgs must follow in specific circumstnaces. Similar to checklists, they ensure consistent processes

Included in frameworks:

- Change managagement procedures
- Onboarding and offboarding procedures (for new and old emplyees)
- Playbooks: describe the actions the orgs incident response team will take when specific types of incidents occur

### Guidelines

Best practices and recommendations related to a given concept, technology, or task

Compliance is not mandatory

#### Exceptions and Compensating Controls

Handle unforseen circumstances

PCI DSS compensating control satisfactory list:

- 1. The control must meet the intent and rigor of the original requirement
- 2. The control must provide a similar level of defense as the original requirement, such that the compensating control sufficiently offsets the risk that the original PCI DSS requirement was designed to defend against
- 3. The control must be "above and beyond" orhter PCI DSS requirements
- 4. The control must address the additional risk imposed by not adhering to the PCI DSS requirement
- 5. The control must address the requirement currently and in in the future

### Monitoring and Revision

Policy monitoring is an ongoing process

Security Information and Event Management (SEIM)

## Change Management

Helps reduce unanticipated outages caused by unauthorized changes

The primary goal of Change Management is to ensure that changes do not cause outages

Unauthorized changes directly affect the A in CIA

### Change Management Processes and Controls

perform *impact analysis*

processes to:

- control
- document
- track
- audit

### SoP for Changes

- 1. Request the change
- 2. Review the change
- 3. Approve/reject the change
- 4. Test the change
- 5. Schedule and implement the change
  - Note: do these in announced maintenance windows
- 6. Document the change

Even if making reactionary changes to isolate malware, need to document the changes

Some issues to consider:

- Whether the change will require any modifications to security controls, such as firewall rules, allow lists, or deny lists
- Whether any other business or technical activities need to be restricted during or after the change
- Whether the change will cause downtime for critical systems
- Whether the change will require restarting any services or applications
- Whether the change involves any legacy applications that lack vendor support
- Whether all possible dependencies have been identified and documented

### Version Control

### Documentation

## Personnel Management

- Least privilege
- Separation of Duties (for sensitive functions)
  - Two person control is similar, but requires two people to perform a single sensitive action
- Job rotation and mandatory vacations
  - motivating force is that many types of fraud require ongoing concealment activities
- Clean desk Space (no paper on desks)
- Onboarding and Offboarding
- NDAs
- Social Media policies

## Third-Party Risk Management

- Vendor Selection
  - Due diligence
  - Conflicts of interest
- Vendor Assessment
  - agreements should include right-to-audit clauses
  - supply chain analysis good too to understand interdependencies
- Vendor agreements
  - Master service agreement (MSAs)
    - Umbrella contract for the work a vendor does
    - When new projects begin, issue new Work Orders, or Statements of Work
  - Service Level Agreements (SLAs)
    - system availability, data durability, response time
  - Memorandum of Understanding (MOU)
    - Document aspects of relationship
    - informal mechanism
  - Memorandum of Agreement (MOA)
    - formal document that outlines terms and details an agreement b/w parties
    - clauses regarding resource allocation, risk management, performance metrics
  - Business Partners Agreements (BPAs)
    - When two orgs agree to do business in a partnership
    - responsibilities, division of profits
- Vendor Monitoring
  - observing and analyzing performance and compliance
  - set KPIs
- Winding Down Vendor Relationships
  - End of Life (EOL)
  - End of Service Life (ESOL)

Use NDAs with vendors too

## Complying with Laws and Regulations

### Common Compliance Requirements

- Health Insurance Portability and Accountability Act (HIPAA)
  - security and privacy rules for healthcare providers and insurer
- Payment Card Industry Data Security Standard (PCI DSS)
  - Storage processing and transmission of credit and debit card info
- Gramm-Leach-Bliley Act (GLBA)
  - US financial institutions
- Sarbanes-Oxley (SOX) Act
  - financial records of US public companies
- General Data Protection Regulation (GDPR)
  - security and privacy requirements for PI of EU
- Family Educational Rights and Privacy Act (FERPA)
  - US educational institutions protect student records
- data breach notification laws

### Compliance Reporting

internal and external

### Consequences of Noncompliance

- financial penalties
- reputaiotnal damage
- loss of business
- fines
- sanctions
- restrictions on business oeprations (revoking licenses)
- termination of contracts

### Compliance Monitoring

- due diligence: process of continually researching and understanding the legal and regulatory requirements that pertain to the org
- due care: complementary concept - refers to ongoing efforts to ensure that the implemented policies and controls are effective and continuously maintained
- acknowledgement: ensure employess and business partners state they are aware of compliance requirements
- attestation: means they are aware and have also confirmed that their practices adhere to the policies

## Adopting Standard Frameworks

### NIST Cybersecurity Framework

Core objectives:

- Describe their current cybersecurity posture
- Describe their target state for cybersecurity
- Identify and prioritize opportunities for improvement within the contect of a continuous and repeatable process
- Assess progress toward the target state
- Communicate among internal and external stakeholders about cybersecurity risk

Five functions:

- identify
- protect
- detect
- respond
- recover

NIST framework includes 3 components:

- The Framework Core
  - the 5 sec functions above
- The Framework Implementation Tiers
  - assess how an organization is positioned to meet cyber objectives
  - like a Maturity Model
- Framework profile
  - descibes how a specific org might approach security functions covered by the framework core

### NIST Risk Management Framework (RMF)

Mandatory standard for federal agencies

### ISO Standards

Best practices for cybersecurity and privacy

- ISO 27001 (14)
  - Information security policies
  - Organization of information security
  - Human resource security
  - Asset management
  - Access control
  - Cryptography
  - Physical and environmental security
  - Operations security
  - Communicatinos security
  - System acquisition, development, and maintenance
  - Supplier relationships
  - Information security incident management
  - Information Security aspects of business continuity management
  - Compliance with internal requirements, such as policies, and with external requirements, such as laws
- ISO 27002
  - Goes beyond control objectives and describes the actual controls that an org may implement to meet objectives
  - supplementary document for orgs that wish to:
    - Select information security controls
    - Implement information security controls
    - Develop information security management guidelines
- ISO 27701
  - managing privacy controls
  - extension of above two
- ISO 31000
  - guidelines for risk management (not cyber specific)

### Benchmarks and Secure Configuration Guidelines

## Security Awareness and Training

### User Training

- Role-based training
- User guidance and training
  - anti-phishing
  - anomalous behavior recognition
- Training frequency
- Development and Execution
- Reporting and monitoring

Other topics:

- Security Policies and Handbooks
- Situational awareness (where to get updates)
- Insider Threats
- Password Management
- Removable Media and Cables
- Social Engineering
- Operational Security
- Hybrid/Remote Work Environments

## Exam Essentials

- Security governance practices ensure that organizations achieve their strategic objectives
- Policy frameworks consist of policies, standards, procedures, and guidelines
- Organizations often adopt a set of security policies covering different areas of their security programs
- Policy documents should include exception processes
- Change management is cruicial to ensuring the availability of systems and applications
- Organizations face a variety of security compliance requirements
- Standards frameworks provide an outline for structuring and evaluating cybersecurity programs
- Security training and awareness ensures that individuals understand their responsiblities

## Review Questions

- 1. C  ~B mf i had it right originally
- 2. A  A
- 3. C  C
- 4. B  B CANCER
- 5. A  ~C idk
- 6. D  D
- 7. A  ~C
- 8. B  B
- 9. C  C
- 10. B B
- 11. C C
- 12. B B
- 13. D D
- 14. B B
- 15. A ~D hooly fuck "detect" instead of "prevent"
- 16. D D
- 17. A A
- 18. B B
- 19. D D
- 20. C D

16/20 = .80
