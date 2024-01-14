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

Public key anyone can have, no weakness in security

Private keys can only be owned by one individual - it is never shared

- RSA
- Elliptic Curve (ECC)

Key Length:

- the length of the crypto key is the most important security param
- length of key depends on alg too, 1024 RSA is same as 160 bit ECC

## Hash Functions

Five (5) requirements for hash fns:

- Accept an input of nay length
- Produce an output of a fixed length, regarless of length of input
- Hash value is relatively easy to compute
- Hash fn is one way (super hard to determine input given an output)
- A secure hash function is collision free (two diff inputs shouldnt come up with same output)

Algs:

- SHA (-1 -2 -3)
- MD5 (message digest algorithm) - 128bit
  - subject to collisions

## Digital Signatures

Two distinct goals:

- Signed messages assure the recipient that the message came from the sender (non-repudiation)
- Ensure msg not altered in transit

### HMAC

Hash-Based Message Authentication Code

- guarantees integrity
- does not provide non-repudiation
- More efficient than PKI, like a halfway point between none and PKI

### Which Key Should I Use

- If you want to encrypt, use the recipients public key
- If you want to decrypt, use your private key
- If you want to digitally sign, use your private key
- If you want to verify the signature, use senders public key

### Public Key Infrastructure

- facilitates comms between parties previously unknown to each other
- combines asym and symm crypto with hashing and digital certs

#### Certificates

Digital certificates provide communicating parties with assurance the people are who they claim to be

- signed by a Certificate Authority

Trust in a Cert is only as good as your trust in the CA that issue them

Registration Authorities assist CAs with burden of verifying users identities prior to issuing certs

#### Certificate Generation and Destruction

Digital vertificate formats:

- Distinguished Encoding Rules (DER)
  - Binary, .der, .crt, .cer
- Privacy Enhanced Mail (PEM)
  - Text, .pem, .crt
- Personal Information Exchange (PFX)
  - Binary, .pfx, .p12
- P7B
  - Text, .p7b

## Asymmetric Key Management

- Keep private key secret
- retire keys
- back up keys

### Hardware Security Modules (HSM)

- provide way to manage keys
- YubiKey

## Cryptographic Attacks

- Brute Force
- Frequency Analysis
  - looking at blocks of encrypted messages for patterns
- Known Plain Text
  - Gives attackers starting point
- Chosen Plain Text
  - attacker obtains the ciphertexts corresponding to set of plain texts of their own choosing
- Related Key Attack
  - Same as chosen but get two different sets of plain text matching ciphertext
- Birthday attack
  - attack on hashes
  - probability of collisions
- Downgrade Attack
  - against TLS
  - get system to shift to less ecure crypto mode
- Hashing, Salting, Key Stretching
  - Key stretching (creates keys from passwords)
    - PBKDF2 - Password-Based Key Derivation Function v2

Exploiting Weak Keys

- Dont use WEP

Exploiting Human Error

## Emerging Issues in Crypto

- Tor and the Dark Web
  - perfect forward secrecy - where layers of encryptoin prevent nodes from reading anything other than specific info needed to forward traffic
- Blockchain
- Lightweight Cryptography
  - Lowe power consumption on edge devices
  - satellites, smart cards
- Homomorphic Encryption
  - allows you to still do operations on the data while preserving privacy
  - like operations on ciphertext results in same outputs as when preformed on plain text
- Quantum Computing
  - prime numbers

## Exam Essentials

- Understand the goals fo cryptography
  - Confidentiality, Integrity, authentication, non-repudiation
- Explain differences between symmetric and asymmetric encryption
- Explain how digital signatures provide non-repudiation
- Understand purpose and use of digital certs
- Demonstrate familiarity with emerging issues in cryptography

## Review Questions

- 1. D  D
- 2. A  A
- 3. D  D
- 4. A  A
- 5. A  A
- 6. C  C
- 7. B  ~D AES is symmetric
- 8. B  ~C idk
- 9. D  ~C symmetric = existing
- 10. A ~B asymmetric is always 2
- 11. A ~D idk
- 12. C C
- 13. A A
- 14. C C idk
- 15. A A
- 16. C C
- 17. C C
- 18. D D
- 19. B B
- 20. A A

15/20 = .75
