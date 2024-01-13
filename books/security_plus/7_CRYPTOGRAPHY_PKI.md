# Chapter 7. Cryptography and PKI

Goals of crptography

- confidentiality
- integrity (ensures not altered)
- authentication - validate identity of individuals
- nonrepudiation

## Types of Ciphers

- Subsititution Ciphers
  - shifts
  - ROT13
- Polyalphabetic substitution
  - swapping by two different rules basically
- Trnsposition Ciphers
  - scrambling letters in certain way
  - cut into blocks, and scramble accordingly
- The Enigma machine
- Steganography
  - embed messages within another file
  - works for images, text, audio, video
  - form of watermarking

## Goals of Cryptography

### Confidentiality

- Ensures data remains private in 3 different situations:
  - at rest
  - in transit
  - when in use

Two main types of cryptosystems enforce confidentiality:

- Symmetric cryptosystems - use a shared secret key available to all users of the system
- Asymmetric cryptosystems - use individual combinations of public and private keys for each user of the system

Most common way to protect data in transit is TLS (Transport Layer Security)

#### Protecting Data at Rest with Different Levels of Encryption

- Encrypting Data on Disk
  - Full-disk encryption (FDE) - all data automatically encrypted
  - Partition encryption - targets specific partition of a hard drive
  - File-level encryption
  - Volume encryption - several folders and files
- Encrypting Database Data
  - Database encryption
    - Transparent Data Encryption (TDE) - entire db
    - Column-level Encryption (CLE)
  - Record-level encryption

#### Integrity

Digital signatures

#### Authentication

#### Non-repudiation

## Cryptographic Concepts

### Cryptographic Keys

Kerckhoffs Principle: crypto should be secure even if everything about the system (except the key) is public knowledge

### Ciphers

Algs used to perform encryption and decryptoin

- block ciphers - operate on chunks - most modern algs
- stream ciphers - one character (or bit) at a time

## Modern Cryptography

### Cryptographic Secrecy

### Symmetric Key Algorithms

aka:

- secret key cryptography
- private key cryptography

Weaknesses:

- key exchange is a major problem
- Symmetric key crypto does not implement non-repudiation
- The algorithm is not scalable
- Keys must be regenerated often

Better for hardware implementations

### Asymmetric Key Algorithms

aka:

- public key algorithms

provide solution to weaknesses of symmetric key encryptoin. each user has two keys:

- public key - shared with all users
- private key - kept secret to owner of key pair

but opposite and related keys must be used in tandem to encrypt and decrypt

Major strengths of asymmetric keys:

- addition of new users requires the generation of only one public-private key pait
- Users can be removed far more easily from asymmetric systems
- Key regeneration is required only when a users private key is compromised
- Asymmetric key encryption can provide integrity, authentication, and non-repudiation
- Key exchange is a simple process
- No preexisting communication link needs to exist

### Comparing Symmetric and Asymmetric

| Symmetric | Asymmetric |
| - | - |
| Single shared key | Key pair sets |
| Out-of-band exchange | In-band exchange |
| Not scalable | Scalable |
| Fast | Slow |
| Bulk encryption | Small blocks of data, digital signatures, digital certificates |
| Confidentiality, integrity | Confidentiality, integrity, authentication, non-repudiation |

## Symmetric Cryptography

- DES (3DES) - depreciated dec 2023
- AES - superseded DES
  - 128, 192, 256
  - used in TLS, file/disk encryption

### Symmetric Key Management

- creation and distribution (big issue)
  - offline distribution
  - public key encryption - start with public key to exhcnage, then go to symmetric
  - diffie-hellman key exchange
- storage and destruction of symmetric keys
  - never store an ancryption key on same system where encrypted data resides
  - for sensitive keys, consider providing two different individuals with half of the key, then they must colalb to re-create entire key ("split knowledge")
- Key Escrow and Recovery
  - key escrow - third party stores a copy of the key for use in emergency

## Asymmetric Cryptography
