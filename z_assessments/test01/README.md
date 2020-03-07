![esecurity](https://raw.githubusercontent.com/billbuchanan/esecurity/master/z_associated/esecurity_graphics.jpg)

# Test 1
There will be four main questions in the exam: Symmetric Key (Unit 2), Hashing (Unit 3), Public Key (Unit 4), and Key Exchange (Unit 5). An outline is [here](https://www.youtube.com/watch?v=Oj3T2UO1WDw&feature=emb_title).

A PDF version of the questions is [here](https://github.com/billbuchanan/esecurity/blob/master/z_assessments/test01/2020_fake_exam_questions.pdf).

Test date: 13 Mar 2020 (open book test, taken over Moodle). 

Test time: Lab time for campus-based students (11am) or 6pm onwards for distance students.

## 1. Symmetric Key
Key principles: Salting, AES, ECB, CBC, Key entropy.

1. Computing power increases each year. Outline the challenge this gives when protecting encrypted data. [Ref: Symmetric Key]
2. What are the possible advantages of using stream ciphers over block ciphers? [Ref: Symmetric Key]
3. The AES method is recommended by NIST for symmetric key encryption. What are the main stages involved in the AES process? [Ref: Symmetric Key]
4. Bob encrypts his data using symmetric key encryption and sends it to Alice. Every time he produces the ciphertext it changes, and he is worried that Alice will not be able to decipher the cipher text. He encrypts "Hello" and gets a different cipher stream each time. Why does the cipher text change? [Ref: Symmetric Key]
5. Bob is sending encrypted data to Alice, and Eve is listening. After listening for a while, Eve is able to send a valid encrypted message to Alice. By outlining ECB, discuss how this might be possible. [Ref: Symmetric Key]
6. Bob is using a password to generate a 128-bit encryption key. Explain why the key space is unlikely to be 2<sup>128</sup>, and why key entropy could be used to measure the equivalent key size. [Ref: Symmetric Key]
7. Bob says that the number of bytes used for the cipher text will change directly with the number of bytes used in the plain text. Alice disagrees and says that most encryption methods involve having block sizes. Who is correct? Explain why. [Ref: Symmetric Key]
8. With block encryption, how do we know where the ciphered data actually ends? Does it just use an end-of-file character or a NULL character? [Ref: Symmetric Key]
9. Alice says she is confused that Bob is sending her the same message as a cipher, but every time the cipher text changes. Apart from using the shared encryption key, what does Alice use to decipher the cipher text? [Ref: Symmetric Key]
10. Why would Eve have an aversion to salt? [Ref: Symmetric Key]
11. Bob tells Alice that she won't be able to view the cipher text, but when she looks at the messages, they seem to be full of printable characters. What format is Bob likely to be using for the encoding of the cipher text, and what would you ask Alice to look for, in order to confirm your guess? [Ref: Symmetric Key]
12. Alice has been reading her crypto books, and she reads that there should be an '=' symbol at the end of the encoding. She observes her encoding of cipher messages to Bob and sees that some do not have an '=' sign at the end. Is there a problem with her encoder? If not, how often, on average, should she see an '=' sign at the end of her ciphered messages? [Ref: Symmetric Key]


## 2. Hashing
Key principles: Hashing, Hashing Formats, Time to crack, operation of converting passwords to password with salt.

* Bob uses a six-character password with lower case [a-z]. How many passwords are possible? His password system then tells him he needs to add numeric value [0-9]. If he adds it at the end, how many passwords are possible, and what is the key entropy? [Ref: Symmetric Key]
* Outline the importance of storing the salt value with the hashed value when storing hashed passwords. [Ref: Hashing]
* Eve has captured a hashed password. How might she use the Cloud to be able to crack the hashed password, and what is a likely tool for this? [Ref: Hashing]
* Bob is an administrator for a network, and he tells his management team that user passwords are now salted, and they are thus completely secure against attacks. Is he correct? Explain your viewpoint. [Ref: Hashing]
* Bob looks at the passwd file on his server and wants to know the type of salting that is used. How would he do this? [Ref: Hashing]
* Bob is looking for a new hashing method for storing passwords and thinks that he will pick the fastest one. Is this a good approach? Explain your answer. [Ref: Hashing]
* What are the typical tools that are used to crack hashed passwords, and what are the methods they will use to crack them? [Ref: Hashing]
* If we have a 16-bit key, but only use 200 phrases. What is the key entropy? [Ref: Hashing]
* If it takes 10ns to test an encryption key. How long will it take to crack a 20-bit key? [Ref: Hashing]
* It was stated in the recent Yahoo hack that:
<pre>
"We have confirmed, based on a recent investigation, that a copy of certain user account information 
was stolen from our networks in late 2014 by what we believe is a state-sponsored actor," Lord wrote. 
"The account information may have included names, e-mail addresses, telephone numbers, dates of birth, 
hashed passwords (the  vast majority with Bcrypt), and, in some cases, encrypted or unencrypted security 
questions and answers."
</pre>
* Do you think the vast majority of the hashed passwords will be cracked? Do you think they had good practice in place for hashed passwords? [Ref: Hashing]
* You are working with a security consultant, and he says that you don't need to check the hashing of passwords, as it should work without testing. You disagree with him and decide to test your hashing method. Initially you must find test vectors for MD5, SHA-1 and SHA-256. Can you find three test vectors, and test them against an on-line calculator? [Ref: Hashing]
* At a security presentation a researcher gives a demonstration of Scrypt. In the presentation he shows a demonstration with a password of "password" and fixed salt of "NaCl". For each run he runs the hashing function, the hashed value changes, but, each time, the computation took longer. Which parameter is the researcher likely to be changing, and why does that parameter exist? Can the researcher select any value for the parameter? [Example] [Ref: Hashing]
* There has been a major data breach within your company, and you are to appear on Sky News to report it. Your company has used PBKDF2 to hash its passwords. How do you explain to your customers that their passwords are unlikely to be breached? [Ref: Hashing]


## 3. Public Key
Key topics: RSA, Elliptic Curve, Using public/private key for security/identity, PGP, GCD

* Explain how public key provides both privacy and identity verification. [Ref: Public key]
* Explain how the e and d values are determined within the RSA method. What are the values that are distributed and which are kept secret? [Ref: Public key]
* Bob has just produced a key pair, in a Base-64 format, and now wants to send this to Alice. What advice would you give him on sending the key pair to Alice? [Ref: Public key]
* Bob has two numbers which give a GCD of 1. Trent says that this happens because the numbers are prime. Is Trent correct? Explain your answer. [Ref: Public key]
* Bob sends an encrypted message to Alice, and also sends his digital certificate to Alice to prove hishared key is 868. [Ref: Key Exchange]
* With RSA, Bob selects two prime numbers of: p=3, q=5. What are the encryption and decryption keys? For a message of 4, prove that the decrypted value is the same of the message. [Ref: Public key]
* Bob selects a p value of 7 and a q value of 9, but he cannot get his RSA encryption to work. What is the problem? [Ref: Public key]
* Bob has selected a p value of 11 and a q value of 7. Which of the following are possible encryption keys: (5,77), (3,77), (9,77), (11,77), and (24,77). [Ref: Public key]
* Bob and Alice decide to use RSA encryption to send secure email, where Bob uses Alice's public key to encrypt, and she uses her private key to decrypt. What is the main problem caused with this, as apposed to using symmetric encryption? [Ref: Public key]
* Bob tells Alice that she should send her private key in order that he should encrypt something for her. Outline the main problem caused by this. [Ref: Public key]
* Security professionals say that RSA keys of over 1,024 bits are secure. What is the core protection against the RSA method being cracked for keys of 1,024 bits and more. [Ref: Public key]
* Bob and Alice get into a debate about the size of the d and e values in the RSA encryption key. Bob says that, in real-life keys, the length of the e value in (e,n) is normally about the same size as the d value (d,n). Alice disagrees. Who is correct? [Ref: Public key]
* Bob says that Elliptic Curve Cryptography (ECC) is an easy method to crack. Explain to Bob how ECC operates, and why it can be a secure method. [Ref: Public key]


## 4. Key Exchange
Key topics: Diffie-Hellman, Simple DH calculations, ECDH operation, Passing with public key.

* For Diffie-Hellman: G=2,351; N=5,683; x=7 and y=14. What is the shared key? [Ref: Key Exchange]
* With Diffie-Hellman, G is 1579, and N is 7561. Bob selects 13 and Alice selects 14. Prove that the shared key is 868. [Ref: Key Exchange]
* Eve says that she sees the values passed within ECDH by Bob and Alice, and that she can crack the key. By explaining the ECDH key exchange method, outline how it would likely to be difficult for Eve to determine the shared key.

# Fake example paper
Note this paper was not an open book test.

## Question 1

### Part A

Bob and Co is an ISP, and they have recently been hacked, and their passwords released to the Internet. Their lead Information Officer explains that the passwords use eight character passwords and were salted with a three-character hex value. The regular expression to filter the passwords defines the range of [a-z0-9].

1. What advice would you give to the company on their current policy on hashing their passwords? [4]
2. In the investigation, a hash cracker of 1 Tera hashes per second has been used. Can you estimate how long it would take to crack all the passwords in the data? Give the working-out. [2]
3. On examining the password database, it was found that most passwords had a lower case letter at the start, and always had a number at the end. What effect would this have on the strength of the password and can you estimate the equivalent key entropy [4].

Outline answers:

1. Only lower case and numbers used [1]. The company needs to add a wider range of characters [1]. Small salt value [1] and short password [1].
2. Max time to crack all passwords = 3681×1012=2.82 seconds [2]. Average will be 1.42 seconds. The salt will be included with the hashed value.
3. Discussion around reduction in strength [2]. Calculation becomes 26×366×10= 565,963,407,360. Key entropy = 39.0 bits [2]. We have 26 letters for the first character, then there will 36 possible characters for the next six characters, and then 10 digits at the end.

### Part B

The following is a password entry, outline the information that can be gained from this password entry and the process that is used when the user logs in. If the salt was lost, outline if it would be possible to recover the original password. For the size of salt used, how could you estimate the increase in difficulty in cracking the salted password? [5]

Outline answers:

Identify user name, salt, hash [2]. Process [1]. 8×6=48 bits for salt … for every password 248 new hashes [2].

## Question 2

Calculate, for Diffie-Hellman, the shared key, if the agreed values are G=201, N=31, and Bob selects 15 and Alice selects 3. Give the working-out. [Marks: 3].

1. In RSA, Bob generates two prime numbers: 13 and 11. From this create the encryption and decryption key. Give the working-out. [Marks: 3].

2. Alice tells Bob that, in RSA, you can select any value of e and d, as long as they do not share the same factors. Is she correct? Outline the procedure that is used to select d, e and N, and why the values need to be selected carefully. [Marks: 6]

3. Mallory and Eve have been watched by law enforcement agencies, and they have been using symmetric encryption to pass messages, and public key to prove identifies and share the symmetric key. Eve now says that Trent the Investigator has been able to get access to her key pair (public and private key). What effect might this have on the security of the messages passed between Mallory and Eve? [Marks: 3]

Outline answers:

1. Standard Diffie-Hellman calculation [3].
2. Standard RSA calculation [3].
3. Standard method of selecting for RSA [2]. N too small ... easy to crack [1]. e to small then Me less than N, easy to crack [1]. e too large … large overhead in calculations [1] and p and q constrained by key size (and computation limits) [1]. Session key from Eve to Mallory could have been compromised [1]. Trent could have pretended to be Eve [1].

## Question 3

1. PKI uses key pairs for encryption and digital certificates to prove identity. Explain how PKI can be used to keep messages between Bob and Alice secret, and also how we can prove Bob's identity and the integrity of the message. How might an intruder manage to pretend to be Bob? [Marks: 5]
2. PGP provides a method of securing email. Outline how PGP uses asymmetric and symmetric encryption in order to secure emails, while proving identities. [Marks: 4]
3. Bob is watching Alice's cipher stream and he says that he can determine some information about what her plain text is. If she is using ECB (Electronic Code Book) without salt and a 128-bit block cipher, outline what information Bob could gain from Alice's cipher stream. [Marks: 2]
4. Alice says she is using CBC (Cipher Block Chaining), and continually sends the message "Hello" to Bob. She tells him that the cipher message will always change, and will always be different, so that Eve can't tell that the message is repeating. Is she right? Justify your answer. How could Eve determine that the messages are the same? [Marks: 4]

Outline answers:

1. Outline usage of private key to sign and outline usage of public key to secure messages [2]. Digital certificate contains key pair [0.5]. Export to certificate to check identity [0.5]. Send Alice certificate [1] and signed by root authority [1].
2. Outline process of PGP eg generation of signature [1], session key [1], proving of signature [1], decryption of the message [1].
3. ECB repeated patterns may appear [1]. 128-bit cipher reveals the number of bytes in message [1].
4. Define salt [1]. The cipher is highly likely to change [1]. Eventually the IV vector come round again [1]. Eve matches IV, and knows the messages are the same [1].
