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
