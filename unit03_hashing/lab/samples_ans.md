Try not to look at these answers, unless you really have too ..

## A.1
<pre>
Edinburgh - 03CF54D8CE19777B12732B8C50B3B66F
Glasgow - D586293D554981ED611AB7B01316D2D5
Falkirk - 48E935332AADEC763F2C82CDB4601A25
Stirling - EE19033300A54DF2FA41DB9881B4B723
</pre>

## A.3
<pre>
MD5: 32 hex characters (128 bits)
SHA-1: 40 hex characters (160 bits)
SHA-256: 64 hex characters (256 bits)
SHA-384: 96 hex characters (384 bits)
SHA-256: 128 hex characters (384 bits)
</pre>

## A.4
<pre>
napier - bill:$apr1$waZS/8Tm$jDZmiZBct/c2hysERcZ3m1 Use: openssl passwd -apr1 -salt waZS/8Tm napier
Ankle123 - mike:$apr1$mKfrJquI$Kx0CL9krmqhCu0SHKqp5Q0 Use: openssl passwd -apr1 -salt mKfrJquI Ankle123
inkwell - fred:$apr1$Jbe/hCIb$/k3A4kjpJyC06BUUaPRKs0 Use: openssl passwd -apr1 -salt Jbe/hCIb inkwell
password - ian:$apr1$0GyPhsLi$jTTzW0HNS4Cl5ZEoyFLjB. Use: openssl passwd -apr1 -salt 0GyPhsLi password
napier - jane: $1$rqOIRBBN$R2pOQH9egTTVN1Nlst2U7. Use: openssl passwd -1 -salt rqOIRBBN napier
</pre>



## A.5
The hash values are:
<pre>
$ cat 1.txt | openssl md5
(stdin)= 5d41402abc4b2a76b9719d911017c592
$ cat 2.txt | openssl md5
(stdin)= e3fc91b12a36c2334ebb5b66caa2d75b
$ cat 3.txt | openssl md5
(stdin)= fea0f1f6fede90bd0a925b4194deac11
$ cat 4.txt | openssl md5
(stdin)= d89b56f81cd7b82856231e662429bcf2
</pre>

We can see that **2.txt** has been modified.

## A.6
The files have the same MD5 signature, but are different in their content:
<pre>
$ cat letter_of_rec.ps | openssl md5
(stdin)= a25f7f0b29ee0b3968c860738533a4b9
$ cat order.ps | openssl md5
(stdin)= a25f7f0b29ee0b3968c860738533a4b9
</pre>

## B.1
<pre>
$ hashcat --help
       # | Name                                             | Category
  ======+==================================================+======================================
    900 | MD4                                              | Raw Hash
      0 | MD5                                              | Raw Hash
   5100 | Half MD5                                         | Raw Hash
    100 | SHA1                                             | Raw Hash
   1300 | SHA2-224                                         | Raw Hash
   1400 | SHA2-256                                         | Raw Hash
  10800 | SHA2-384                                         | Raw Hash
   1700 | >HA2-512                                         | Raw Hash
  17300 | SHA3-224                                         | Raw Hash
  17400 | SHA3-256                                         | Raw Hash
  17500 | SHA3-384                                         | Raw Hash
  17600 | SHA3-512                                         | Raw Hash
  17700 | Keccak-224                                       | Raw Hash
  17800 | Keccak-256                                       | Raw Hash
  17900 | Keccak-384                                       | Raw Hash
  18000 | Keccak-512                                       | Raw Hash
    600 | BLAKE2b-512                                      | Raw Hash
  10100 | SipHash                                          | Raw Hash
   6000 | RIPEMD-160                                       | Raw Hash
   6100 | Whirlpool                                        | Raw Hash
   6900 | GOST R 34.11-94                                  | Raw Hash
</pre>
<p>Sample benchmark for MD5:</p>
<pre>
$ hashcat -b -m 0
hashcat (v5.1.0-42-g471a8cc) starting in benchmark mode...

Hashmode: 0 - MD5

Speed.#1.........:   189.9 MH/s (10.87ms) @ Accel:1024 Loops:1024 Thr:1 Vec:8

Started: Thu Jan 30 15:56:05 2020
Stopped: Thu Jan 30 15:56:12 2020
</pre>
This gives 189 MH/s. For SHA-1:
<pre>
$ hashcat -b -m 100
hashcat (v5.1.0-42-g471a8cc) starting in benchmark mode ...

OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Benchmark relevant options:
===========================
* --optimized-kernel-enable

Hashmode: 100 - SHA1

Speed.#1.........:   139.2 MH/s (14.44ms) @ Accel:1024 Loops:1024 Thr:1 Vec:8

Started: Thu Jan 30 15:57:41 2020
Stopped: Thu Jan 30 15:57:47 2020
</pre>
We can 139.2 MH/s for SHA-1. For SHA-256:
<pre>
$ hashcat -b -m 1400
hashcat (v5.1.0-42-g471a8cc) starting in benchmark mode...


OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Benchmark relevant options:
===========================
* --optimized-kernel-enable

Hashmode: 1400 - SHA2-256

Speed.#1.........: 60286.7 kH/s (34.61ms) @ Accel:1024 Loops:1024 Thr:1 Vec:8

Started: Thu Jan 30 15:59:16 2020
Stopped: Thu Jan 30 15:59:23 2020
</pre>
This gives 60.2 MH/s. And for APR-1:
<pre>
$ hashcat -b -m 1600
hashcat (v5.1.0-42-g471a8cc) starting in benchmark mode...

Benchmarking uses hand-optimized kernel code by default.
You can use it in your cracking session by setting the -O option.
Note: Using optimized kernel code limits the maximum supported password length.
To disable the optimized kernel code in benchmark mode, use the -w option.

OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Benchmark relevant options:
===========================
* --optimized-kernel-enable

Hashmode: 1600 - Apache $apr1$ MD5, md5apr1, MD5 (APR) (Iterations: 1000)

Speed.#1.........:    14387 H/s (70.39ms) @ Accel:1024 Loops:500 Thr:1 Vec:8

Started: Thu Jan 30 16:01:15 2020
Stopped: Thu Jan 30 16:01:18 2020
</pre>
This is only 14.4 kH/s, and which is much slower than the other methods.

## B.2
Answers:
<pre>
napier
password
Ankle123
inkwell
</pre>
Here is a sample run:
<pre>
$ nano words
$ nano hash1
$ cat words
napier
password
Ankle123
inkwell
$ cat hash1
232DD5D7274E0D662F36C575A3BD634C
5F4DCC3B5AA765D61D8327DEB882CF99
6D5875265D1979BDAD1C8A8F383C5FF5
04013F78ACCFEC9B673005FC6F20698D
$ hashcat -m 0 hash1 words
hashcat (v5.1.0-42-g471a8cc) starting...

OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Hashes: 4 digests; 4 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Salt
* Raw-Hash

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

ATTENTION! Pure (unoptimized) OpenCL kernels selected.
This enables cracking passwords and salts > length 32 but for the price of drastically reduced performance.
If you want to switch to optimized OpenCL kernels, append -O to your commandline.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Dictionary cache built:
* Filename..: words
* Passwords.: 4
* Bytes.....: 33
* Keyspace..: 4
* Runtime...: 0 secs

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.  

232dd5d7274e0d662f36c575a3bd634c:napier          
5f4dcc3b5aa765d61d8327deb882cf99:password        
6d5875265d1979bdad1c8a8f383c5ff5:Ankle123        
04013f78accfec9b673005fc6f20698d:inkwell         
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Type........: MD5
Hash.Target......: hash1
Time.Started.....: Thu Jan 30 16:06:47 2020 (0 secs)
Time.Estimated...: Thu Jan 30 16:06:47 2020 (0 secs)
Guess.Base.......: File (words)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:     9512 H/s (0.01ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 4/4 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 4/4 (100.00%)
Rejected.........: 0/4 (0.00%)
Restore.Point....: 0/4 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: napier -> inkwell

Started: Thu Jan 30 16:06:46 2020
Stopped: Thu Jan 30 16:06:48 2020
</pre>

## B.3 
The answers are:
<pre>
orange
apple
banana
pear
peach
</pre>
Here is a sample run:
<pre>
$ nano hash2
$ nano fruits
$ cat hash2
FE01D67A002DFA0F3AC084298142ECCD
1F3870BE274F6C49B3E31A0C6728957F
72B302BF297A228A75730123EFEF7C41
8893DC16B1B2534BAB7B03727145A2BB
889560D93572D538078CE1578567B91A
$ cat fruits 
apple
orange
kiwi
lemon
grape
banana
pear
peach
$ hashcat -m 0 hash2 fruits 
hashcat (v5.1.0-42-g471a8cc) starting...

OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Hashes: 5 digests; 5 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Salt
* Raw-Hash

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

ATTENTION! Pure (unoptimized) OpenCL kernels selected.
This enables cracking passwords and salts > length 32 but for the price of drastically reduced performance.
If you want to switch to optimized OpenCL kernels, append -O to your commandline.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Dictionary cache built:
* Filename..: fruits
* Passwords.: 8
* Bytes.....: 48
* Keyspace..: 8
* Runtime...: 0 secs

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.  

1f3870be274f6c49b3e31a0c6728957f:apple           
fe01d67a002dfa0f3ac084298142eccd:orange          
72b302bf297a228a75730123efef7c41:banana          
8893dc16b1b2534bab7b03727145a2bb:pear            
889560d93572d538078ce1578567b91a:peach           
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Type........: MD5
Hash.Target......: hash2
Time.Started.....: Thu Jan 30 16:11:51 2020 (0 secs)
Time.Estimated...: Thu Jan 30 16:11:51 2020 (0 secs)
Guess.Base.......: File (fruits)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    16388 H/s (0.01ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 5/5 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 8/8 (100.00%)
Rejected.........: 0/8 (0.00%)
Restore.Point....: 0/8 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: apple -> peach

Started: Thu Jan 30 16:11:51 2020
Stopped: Thu Jan 30 16:11:53 2020
</pre>

## B.4
The word is "help". Here is a sample run:
<pre>
$ nano mywords.txt
$ nano file.txt
$ cat mywords.txt 
hello
goodbye
help
nowhere
$ cat file.txt 
106a5842fc5fce6f663176285ed1516dbb1e3d15c05abab12fdca46d60b539b7
$ hashcat -m 1400 file.txt mywords.txt 
hashcat (v5.1.0-42-g471a8cc) starting...

OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

ATTENTION! Pure (unoptimized) OpenCL kernels selected.
This enables cracking passwords and salts > length 32 but for the price of drastically reduced performance.
If you want to switch to optimized OpenCL kernels, append -O to your commandline.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Dictionary cache built:
* Filename..: mywords.txt
* Passwords.: 4
* Bytes.....: 27
* Keyspace..: 4
* Runtime...: 0 secs

Approaching final keyspace - workload adjusted.  

106a5842fc5fce6f663176285ed1516dbb1e3d15c05abab12fdca46d60b539b7:help
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Type........: SHA2-256
Hash.Target......: 106a5842fc5fce6f663176285ed1516dbb1e3d15c05abab12fd...b539b7
Time.Started.....: Thu Jan 30 16:16:54 2020 (0 secs)
Time.Estimated...: Thu Jan 30 16:16:54 2020 (0 secs)
Guess.Base.......: File (mywords.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    10317 H/s (0.00ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 4/4 (100.00%)
Rejected.........: 0/4 (0.00%)
Restore.Point....: 0/4 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: hello -> nowhere

Started: Thu Jan 30 16:16:53 2020
Stopped: Thu Jan 30 16:16:55 2020
</pre>
## B.5
A sample run is:
<pre>
$ nano nthash
$ cat nthash
0333c27eb4b9401d91fef02a9f74840e
$ hashcat -m 1000 nthash mywords.txt 
hashcat (v5.1.0-42-g471a8cc) starting...

OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

ATTENTION! Pure (unoptimized) OpenCL kernels selected.
This enables cracking passwords and salts > length 32 but for the price of drastically reduced performance.
If you want to switch to optimized OpenCL kernels, append -O to your commandline.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Dictionary cache hit:
* Filename..: mywords.txt
* Passwords.: 4
* Bytes.....: 27
* Keyspace..: 4

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.  

0333c27eb4b9401d91fef02a9f74840e:help            
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Type........: NTLM
Hash.Target......: 0333c27eb4b9401d91fef02a9f74840e
Time.Started.....: Thu Jan 30 16:22:39 2020 (0 secs)
Time.Estimated...: Thu Jan 30 16:22:39 2020 (0 secs)
Guess.Base.......: File (mywords.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    10770 H/s (0.00ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 4/4 (100.00%)
Rejected.........: 0/4 (0.00%)
Restore.Point....: 0/4 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: hello -> nowhere

Started: Thu Jan 30 16:22:38 2020
Stopped: Thu Jan 30 16:22:40 2020
</pre>
## B.6
<pre>
celtic
??
aberdeen
livingston
</pre>
A sample run:
<pre>
$ nano football
$ cat football 
celtic
rangers
hearts
inverness
dundee
aberdeen
motherwell
hamilton
hibernian
kilmarnock
livingston
motherwell
$ cat hash3
635450503029fc2484f1d7eb80da8e25bdc1770e1dd14710c592c8929ba37ee9
b3cb6d04f9ccbf6dfe08f40c11648360ca421f0c531e69f326a72dc7e80a0912
bc5fb9abe8d5e72eb49cf00b3dbd173cbf914835281fadd674d5a2b680e47d50
6ac16a68ac94ca8298c9c2329593a4a4130b6fed2472a98424b7b4019ef1d968
$ rm ~/.hashcat/hashcat.potfile
$ hashcat -m 1400 hash3 football
hashcat (v5.1.0-42-g471a8cc) starting...

OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Hashes: 4 digests; 4 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Salt
* Raw-Hash

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

ATTENTION! Pure (unoptimized) OpenCL kernels selected.
This enables cracking passwords and salts > length 32 but for the price of drastically reduced performance.
If you want to switch to optimized OpenCL kernels, append -O to your commandline.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Dictionary cache hit:
* Filename..: football
* Passwords.: 12
* Bytes.....: 111
* Keyspace..: 12

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.  

635450503029fc2484f1d7eb80da8e25bdc1770e1dd14710c592c8929ba37ee9:celtic
bc5fb9abe8d5e72eb49cf00b3dbd173cbf914835281fadd674d5a2b680e47d50:aberdeen
6ac16a68ac94ca8298c9c2329593a4a4130b6fed2472a98424b7b4019ef1d968:livingston
                                                 
Session..........: hashcat
Status...........: Exhausted
Hash.Type........: SHA2-256
Hash.Target......: hash3
Time.Started.....: Thu Jan 30 16:42:24 2020 (0 secs)
Time.Estimated...: Thu Jan 30 16:42:24 2020 (0 secs)
Guess.Base.......: File (football)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    26495 H/s (0.01ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 3/4 (75.00%) Digests, 0/1 (0.00%) Salts
Progress.........: 12/12 (100.00%)
Rejected.........: 0/12 (0.00%)
Restore.Point....: 12/12 (100.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: celtic -> motherwell

Started: Thu Jan 30 16:42:24 2020
Stopped: Thu Jan 30 16:42:26 2020

</pre>

## B.7
<pre>
hair
face
eye
</pre>
a->z: 26
aa->zz: 676
aaa->zzz:  17576
aaaa->zzzz:456976

A sample run is:
<pre>
$ nano face
$ cat face
4dc2159bba05da394c3b94c6f54354db1f1f43b321ac4bbdfc2f658237858c70
0282d9b79f42c74c1550b20ff2dd16aafc3fe5d8ae9a00b2f66996d0ae882775
47c215b5f70eb9c9b4bcb2c027007d6cf38a899f40d1d1da6922e49308b15b69
$ hashcat -a 3 -m 1400 face ?l?l?l?l?l?l?l?l --increment
hashcat (v5.1.0-42-g471a8cc) starting...

OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Hashes: 3 digests; 3 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates

Applicable optimizers:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Salt
* Brute-Force
* Raw-Hash

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

ATTENTION! Pure (unoptimized) OpenCL kernels selected.
This enables cracking passwords and salts > length 32 but for the price of drastically reduced performance.
If you want to switch to optimized OpenCL kernels, append -O to your commandline.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.  

Session..........: hashcat                       
Status...........: Exhausted
Hash.Type........: SHA2-256
Hash.Target......: face
Time.Started.....: Thu Jan 30 16:48:55 2020 (0 secs)
Time.Estimated...: Thu Jan 30 16:48:55 2020 (0 secs)
Guess.Mask.......: ?l [1]
Guess.Queue......: 1/8 (12.50%)
Speed.#1.........:    68915 H/s (0.00ms) @ Accel:1024 Loops:26 Thr:1 Vec:8
Recovered........: 0/3 (0.00%) Digests, 0/1 (0.00%) Salts
Progress.........: 26/26 (100.00%)
Rejected.........: 0/26 (0.00%)
Restore.Point....: 1/1 (100.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-26 Iteration:0-26
Candidates.#1....: s -> x

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.  

Session..........: hashcat                       
Status...........: Exhausted
Hash.Type........: SHA2-256
Hash.Target......: face
Time.Started.....: Thu Jan 30 16:48:56 2020 (0 secs)
Time.Estimated...: Thu Jan 30 16:48:56 2020 (0 secs)
Guess.Mask.......: ?l?l [2]
Guess.Queue......: 2/8 (25.00%)
Speed.#1.........:  1527.7 kH/s (0.06ms) @ Accel:1024 Loops:26 Thr:1 Vec:8
Recovered........: 0/3 (0.00%) Digests, 0/1 (0.00%) Salts
Progress.........: 676/676 (100.00%)
Rejected.........: 0/676 (0.00%)
Restore.Point....: 26/26 (100.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-26 Iteration:0-26
Candidates.#1....: sa -> xq

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.  

47c215b5f70eb9c9b4bcb2c027007d6cf38a899f40d1d1da6922e49308b15b69:eye
                                                 
Session..........: hashcat
Status...........: Exhausted
Hash.Type........: SHA2-256
Hash.Target......: face
Time.Started.....: Thu Jan 30 16:48:56 2020 (0 secs)
Time.Estimated...: Thu Jan 30 16:48:56 2020 (0 secs)
Guess.Mask.......: ?l?l?l [3]
Guess.Queue......: 3/8 (37.50%)
Speed.#1.........: 10092.9 kH/s (1.36ms) @ Accel:1024 Loops:26 Thr:1 Vec:8
Recovered........: 1/3 (33.33%) Digests, 0/1 (0.00%) Salts
Progress.........: 17576/17576 (100.00%)
Rejected.........: 0/17576 (0.00%)
Restore.Point....: 676/676 (100.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-26 Iteration:0-26
Candidates.#1....: sar -> xqx

0282d9b79f42c74c1550b20ff2dd16aafc3fe5d8ae9a00b2f66996d0ae882775:face
4dc2159bba05da394c3b94c6f54354db1f1f43b321ac4bbdfc2f658237858c70:hair
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Type........: SHA2-256
Hash.Target......: face
Time.Started.....: Thu Jan 30 16:48:56 2020 (0 secs)
Time.Estimated...: Thu Jan 30 16:48:56 2020 (0 secs)
Guess.Mask.......: ?l?l?l?l [4]
Guess.Queue......: 4/8 (50.00%)
Speed.#1.........: 22926.1 kH/s (2.09ms) @ Accel:1024 Loops:26 Thr:1 Vec:8
Recovered........: 3/3 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 212992/456976 (46.61%)
Rejected.........: 0/212992 (0.00%)
Restore.Point....: 6144/17576 (34.96%)
Restore.Sub.#1...: Salt:0 Amplifier:0-26 Iteration:0-26
Candidates.#1....: snts -> xolc

Started: Thu Jan 30 16:48:54 2020
Stopped: Thu Jan 30 16:48:57 2020
</pre>

## B.8
<pre>
passwordW
passowrd5
</pre>
A sample run is:
<pre>
napier@napier-virtual-machine:~/steg/python/lsb$ hashcat -a 3 -m 0 file.txt password?d
hashcat (v5.1.0-42-g471a8cc) starting...

OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Hashes: 2 digests; 2 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates

Applicable optimizers:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Salt
* Brute-Force
* Raw-Hash

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

ATTENTION! Pure (unoptimized) OpenCL kernels selected.
This enables cracking passwords and salts > length 32 but for the price of drastically reduced performance.
If you want to switch to optimized OpenCL kernels, append -O to your commandline.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.  

db0edd04aaac4506f7edab03ac855d56:password5       
                                                 
Session..........: hashcat
Status...........: Exhausted
Hash.Type........: MD5
Hash.Target......: file.txt
Time.Started.....: Thu Jan 30 17:00:38 2020 (0 secs)
Time.Estimated...: Thu Jan 30 17:00:38 2020 (0 secs)
Guess.Mask.......: password?d [9]
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    23640 H/s (0.01ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/2 (50.00%) Digests, 0/1 (0.00%) Salts
Progress.........: 10/10 (100.00%)
Rejected.........: 0/10 (0.00%)
Restore.Point....: 10/10 (100.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: password1 -> password6

Started: Thu Jan 30 17:00:36 2020
Stopped: Thu Jan 30 17:00:39 2020
</pre>

## C.1
<pre>
APPLE
ORANGE
</pre>

## C.2
<pre>
DUNDEE
ABERDEEN
PERTH
</pre>

## C.3
<pre>
TIGER
SNAKE
ELEPHANT
</pre>

