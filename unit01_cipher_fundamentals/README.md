# Unit 1: Cipher Fundamentals

The key concepts are: Ciphers. Encoding methods (ASCII, UTF-16, Base64, Hex). Prime Numbers. GCD Large numbers. Random Number Generator . Data Integrity (CRC-32). Frequency Analysis. Key-based encryption. Key sizes. We will crack some ciphers, in order to get you into the way of solving puzzles.

##What you should know at the end of unit?

* Understand the conversion of characters between hex, decimal and octal. Sample question: Convert "hello" into a hex stream. Related material: [here]. Why are we studying this? Encrypted content is converted into a range of different formats, so we need to understand the process of taking plain text and then converting it into other encoding formats. Encryption keys, ciphertext and digital certificates are examples of binary content which must be represented in a text format.
* Compute the GCD for values. Sample question: What is the GCD for 42 and 56? Related material: [here]. Why are we studying this? GCD is a fundamental building block used in public key encryption, where we must find two numbers who do not share a common divisor. When we look at public key encryption we will see how GCD is used.
* Compute the MOD for values. Sample question: What is the result of 13 MOD 7? Why are we studying this? Within many of the public key methods we use the MOD operator with a prime number, and where it is difficult to find the value of x for Y=g^x(modp), even though we know Y, g and p.
* Understand how to manually convert from ASCII to Base-64, and vice-versa. Sample question: What is the Base-64 conversion of “hello”? [here]. Base-64 is used extensively in encryption, and many of the keys and cipher text are transported and stored in a Base-64 format.
Calculate the time taken to crack a code given a time to try each key, and for the number of processing elements. Sample question: If it takes 100 years to crack a cipher code, and computing power doubles each year. How long will it take to crack a code after five years? Why are we studying this? We always need to understand the strengths of your encrypted data, especially in the face of GPU based crackers, so we need to understand how quickly it will take to crack our cipher.

## Main content
This is Unit 1 and the content is here:

https://asecuritysite.com/esecurity/unit01

The lecture is here:

https://www.youtube.com/watch?v=zqmjUpJNcJA



