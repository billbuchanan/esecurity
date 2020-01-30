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

Hashmode: 0 - MD5

Speed.#1.........:   189.9 MH/s (10.87ms) @ Accel:1024 Loops:1024 Thr:1 Vec:8

Started: Thu Jan 30 15:56:05 2020
Stopped: Thu Jan 30 15:56:12 2020
</pre>
This gives 189 MH/s. For SHA-1:
<pre>
$ hashcat -b -m 100
hashcat (v5.1.0-42-g471a8cc) starting in benchmark mode...

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
<pre>
napier
password
Ankle123
inkwell
</pre>

## B.3 
<pre>
orange
apple
banana
pear
peach
</pre>

## B.6
<pre>
celtic
dundee
aberdeen
motherwell
</pre>

## B.7
<pre>
hair
face
eye
</pre>

## B.8
<pre>
passwordW
passowrd5
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
