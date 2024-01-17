# Chapter 15. Digital Forensics

## Digital Forensics Concepts

### Legal Holds and e-Discovery

forensics starts when litigation is pending or anticipated

legal hold: (litigation hold) is a notice that informs an org they must preserve data and records that might be destroyed or midified in the course of normal operations

- backups, paper docs, electronic files

e-discovery: electronic descovery

Electronic Discovery Reference Model (EDRM):

- 1. information governance before the fact to assess what data exists and to allow scoping and control of what data needs to be provided
- 2. Identification of electronically stored information so that you know what you have and where it is
- 3. Preservation of the information to ensure that it isnt changed or destroyed
- 4. Collection of the information so that it can be processed and managed as part of the collection process
- 5. Processing of the data to remove unneeded or irrelevant information, as well as preparing it for review and analysis by formatting or collating it
- 6. Review of the data to ensure that it only contains what it is supposed to, and that information that should not be shared is not included
- 7. Analysis of the information to identify key elements like topics, terms, and individuals or organizations
- 8. Production of the data to provide the information to third parties or those involved in legal proceedings
- 9. Presentation of the data, both for testimony in court and for further analysis with experts or involved parties

## Conducting Digital Forensics

## Acquiring Forensic Data

Order of volatility:

- 1. CPU cache and registers
- 2. Routing table, ARP cache, process table, kernel statistics
  - Ephemeral data
- 3. System memory - RAM
- 4. Temp files and swap swpace
- 5. Data on hard disk
- 6. Remote logs
- 7. Backups

Chain of custody docs should be filled out whenever an artifact is accessed, transferred, or handled

### Cloud Forensics

Things to consider:

- right-to-audit clauses, part of contract between cloud service and org
  - either direct ability to audit provider or agreement to use third-party audit agency
- regulatory and jurisdiction concerns
- data breach notification laws

venue: where case is heard

nexus: where a company has a physical location

### Acquisition Tools

copy bit for bit

- dd
- FTK Imager
  - can copy memory
- WinHex
  - memory, RAID

### Acquiring Netework Forensic Data

### Forensic Coplies vs Logical Copies

- logical copy is standard
- forensic needs bit by bit

mention write blockers (these are truly read only)

## Reporting

typical reports include:

- summary of forensic investigation and findings
- outline of forensic process, including tools used and any assumptions made about the tools or process
- series of sections detailing the findings for each device or drive. accuracy is critical when findings are shared, and conclusions must be backed up with evidence and appropriate detail
- recommendations or conclusions in more detail than the summary included

## Examm Essentials

- legal holds and e-discovery drive some forensic activities
- acquisition techniques and procedures ensure usable and admissible forensic data
- there are many options for acquisition tools, and selecting the right tool combines technical needs and skillsets
- validation and preservation of forensic data is a key part of the forensic process
- forensic reports must be well organized and to the point (unlike this book)

## Review Questions

- 1. C  C
- 2. D  ~C or C but idgaf you can use D to get C
- 3. A  A
- 4. B  B
- 5. C  C
- 6. B  B
- 7. C  ~D
- 8. D  D
- 9. C  ~B or B
- 10. C C
- 11. A A idk
- 12. A ~C assuming system log includes events
- 13. B B
- 14. B B
- 15. C ~B what?? right to forensic over jurisdiction???
- 16. D D
- 17. A ~C bro u need to think like a retard in this section
- 18. C C
- 19. C C
- 20. A A

14/20 = .70
