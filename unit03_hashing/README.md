![esecurity](https://raw.githubusercontent.com/billbuchanan/esecurity/master/z_associated/esecurity_graphics.jpg)

# Unit 3: Hashing and MAC

The key concepts involved are defining key entropy; key generators (such as using hashing methods to generate keys based on passphrases); symmetric key methods (AES, Twofish, 3DES, RC4 and ChaCha20); stream or block encryption; symmetric key modes (ECB/CBC/OFB); and salting/IV.

## What you should know at the end of unit?

* How the lengths of the hashes vary with the number of bits in the hash.
* How we can calculate the strengths on passwords.
* Understand how salt is applied to the hashing process.
* Define how collisions can occur within hashing.
* Implement hash cracking methods (John the Ripper and Hashcat).
* Defines the usage of signed hashes (eg HMAC).
* Outlines the usage of OTP and Timed Passwords.

## What you should know at the end of unit?

* How the lengths of the hashes vary with the number of bits in the hash.
* How we can calculate the strengths on passwords.
* Understand how salt is applied to the hashing process.
* Define how collisions can occur within hashing.
* Implement hash cracking methods (John the Ripper and Hashcat).
* Defines the usage of signed hashes (eg HMAC).
* Outlines the usage of One-time Passwords (OTP) and Timed Passwords.

## Presentations

* Week 3 Presentation (PDF) - Hashing: here
* Week 3 Presentation (video) - Hashing: here
* Week 3 Presentation (live lecture) - Hashing: here

## Lab

* Unit 3 Lab (PDF): here
* Unit 3 Lab (video): here
* Unit 3 Lab Part 2 (video): here

## Tests

* Test (Hash Encryption): here

## Important points

* BCrypt, PBKDF2 and Scrypt are slow hashing methods, which also have salt, and are highly recommended for password storage.
    The strength of the encryption implementation is measured by key entropy. Anything less than 72 bits is likely to be weak.

## Sample Exam Questions

The following are some sample questions for hashing:

* Outline the importance of storing the salt value with the hashed value when storing hashed passwords.
* Bob is using a password to generate a 128-bit encryption key. Explain why the key space is unlikely to be 2128, and why key entropy could be used to measure the equivalent key size.
  * Where would I find this info? This is related to key enthropy here, and try and understand how key enthopy relates to the strengh of the encryption.
* Bob has just produced a key pair, in a Base-64 format, and now wants to send this to Alice. What advice would you give him on sending the key pair to Alice?
  * Where would I find this info? Have a think about the certificate which is distributed. You can observe it here.
* Bob sends an encrypted message to Alice, and also sends his digital certificate to Alice to prove his identity. How does Alice prove that it is Bob who sent the message?
* Eve has captured a hashed password. How might she use the Cloud to be able to crack the hashed password, and what is a likely too for this?
  * Where would I find this info? This article outlines a number of methods which might be used, included within Cloud cracking.
* Bob is an administrator for a network, and he tells his management team that user passwords are now salted, and they are thus completely secure against attacks. Is he correct? Explain your viewpoint.
  * Where would I find this info? Have a read of the following article.
* Bob looks at the passwd file on his server, and wants to know the type of salting that is used. How would he do this?
  * Where would I find this info? Have a quick look at the additional lab on Software Hashes. If you can get the Python script to run in Section G, you'll see them all.
* Bob is looking for a new hashing method for storing passwords, and thinks that he will pick the fastest one. Is this a good approach? Explain your answer.
  * Where would I find this info? Think about whether being fast for hashing is a good idea. Have a look at this article. But make up your own mind on the subject.
* What are the typical tools that are used to crack hashed password, and what are the methods they will use to crack them?
  * Where would I find this info? Unit 3 and Lab 2
* Why would Eve have an aversion to salt?
* A password is defined as [a-z]. For a four character password, show that there are 456,976 different passwords.
  * Where would I find this info? Have a look here.
* A password is defined as [a-zA-Z]. For a four character password, show that there are 7,311,616 different passwords.
  * Where would I find this info? Have a look here.
* A password is defined as [a-zA-Z0-9]. For a four character password, show that there are 14,776,336 different passwords.
  * Where would I find this info? Have a look here.
* It was stated in the recent Yahoo hack that:

    "We have confirmed, based on a recent investigation, that a copy of certain user account information was stolen from our networks in late 2014 by what we believe is a state-sponsored actor," Lord wrote. "The account information may have included names, e-mail addresses, telephone numbers, dates of birth, hashed passwords (the vast majority with bcrypt), and, in some cases, encrypted or unencrypted security questions and answers."

Do you think the vast majority of the hashed passwords will be cracked? Do you think they had good practice in place for hashed passwords?

* You are working with a security consultant, and he says that you don't need to check the hashing of passwords, as it should work without testing. You disagree with him, and decide to test your hashing method. Initially you must find test vectors for MD5, SHA-1 and SHA-256. Can you find three test vectors, and test them against an on-line calculator?

* At a security presentation a researcher gives a demonstration of Scrypt. In the presentation he shows a demonstration with a password of "password" and fixed salt of "NaCl". For each run he runs the hashing function, the hashed value changes, but, each time, the computation took longer. Which parameter is the researcher likely to be changing, and why does that parameter exist? Can the researcher select any value for the parameter? [Example]
* There has been a major data breach within your company, and you are to appear on Sky News to report it. Your company has used PBKDF2 to hash its passwords. How do you explain to your customers that their passwords are unlikely to be breached?

## Addendum

In the lecture, the slide at the end of Unit 2 (Symmetric Key) should be (for an eight character password and with [a-z]):

## Important points

    BCrypt, PBKDF2 and Scrypt are slow hashing methods, which also have salt, and are highly recommended for password storage.
    The strength of the encryption implementation is measured by key entropy. Anything less than 72 bits is likely to be weak.

## Interested in knowing more?

Hashcat with 8xGPUs in Cloud: here

