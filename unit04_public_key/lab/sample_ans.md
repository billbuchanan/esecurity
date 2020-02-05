
Try not to look at these answers, unless you really have too ..

# OpenSSL RSA
## B.1
What is the type of public key method used? RSA

How long is the default key: 1024

A sample key:

<pre>
-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQC3qXK4kCxn3BNk87vJUMwIznU8pTjr10Kma9+Jkj4zEy/fiZtY
xvdmn1rKNq/8fEUDCcRVC8hQBpevqxFiJ3dbA7ZM6VjUAmztOfRfxSezgvkjswVS
F1/cgBM32AB4nx1dkCV/Wgedn3KFIFU+b8LH1ZLoyRMyLnwWmAkT/mBC/QIDAQAB
AoGAE8Yao+Rh44y+SdA0F6irTwdrd+wSBNJYSrKyjo1ARR97uAWIxDYnzNS7Yaoh
qH14sKsMiFuMZZFQI4m3hWnaX7OFjhJvxKjP6+BdXKsnwWxpwec7RS6n9ptA7qlE
aIFfVARyiWjG+q+8Bg8CTaHjGgtYPnfLzJM0Vef6gKg5vgECQQDZSKGxtdbpXwXw
VAC78SyfOOYmWKL1HiZs0nyTOnZmhMSkE4+S38zhDTjITh0cuKTksTFeUku/sRij
4T4Y9iz5AkEA2GMpeeRT3IQntmzQgTc7Rgez73Y/UWFynuErg++9gzI758TO3AoV
lFs4NOUAqhZ5fdwizs6sa0bjYm+BC1mbJQJBAMQVts4QItVSSqK6vDrfh/xctd4v
KUh5oAWe4otfPBCCio7jlDLgwxzp+K9TRxRvUWeMvNe4/uEMKgdiss6GAskCQQCf
MpVZMDriifgNppDgABqDszcWfhCnduI1McQqFT+APn0ETy9Bg8nMlDAN+k061b4c
ctDJBhSj+EtiKFbwWsRhAkAnEPn+6m3djTwJMw82DxK1q2fcIjTR0ng8pyrF2iIR
P7oBP8I4hGix/FOrV8M8virK6iCsslEcZBo39FkEqc0N
-----END RSA PRIVATE KEY-----
</pre>
## B.2
Start and end are:
<pre>
-----BEGIN RSA PRIVATE KEY-----
-----END RSA PRIVATE KEY-----
</pre>
## B.3
We get **modulus** (N), **publicExponent** (e), **privateExponent** (d), **prime1** (p), **prime2** (q). The other parameters are stored to speed up the RSA process, such as **exponent1** (d mod p-1), **exponent2** (d mod q-1) and **coefficient** (inv q mod p).
<pre>
Private-Key: (1024 bit)
modulus:
    00:b7:a9:72:b8:90:2c:67:dc:13:64:f3:bb:c9:50:
    cc:08:ce:75:3c:a5:38:eb:d7:42:a6:6b:df:89:92:
    3e:33:13:2f:df:89:9b:58:c6:f7:66:9f:5a:ca:36:
    af:fc:7c:45:03:09:c4:55:0b:c8:50:06:97:af:ab:
    11:62:27:77:5b:03:b6:4c:e9:58:d4:02:6c:ed:39:
    f4:5f:c5:27:b3:82:f9:23:b3:05:52:17:5f:dc:80:
    13:37:d8:00:78:9f:1d:5d:90:25:7f:5a:07:9d:9f:
    72:85:20:55:3e:6f:c2:c7:d5:92:e8:c9:13:32:2e:
    7c:16:98:09:13:fe:60:42:fd
publicExponent: 65537 (0x10001)
privateExponent:
    13:c6:1a:a3:e4:61:e3:8c:be:49:d0:34:17:a8:ab:
    4f:07:6b:77:ec:12:04:d2:58:4a:b2:b2:8e:8d:40:
    45:1f:7b:b8:05:88:c4:36:27:cc:d4:bb:61:aa:21:
    a8:7d:78:b0:ab:0c:88:5b:8c:65:91:50:23:89:b7:
    85:69:da:5f:b3:85:8e:12:6f:c4:a8:cf:eb:e0:5d:
    5c:ab:27:c1:6c:69:c1:e7:3b:45:2e:a7:f6:9b:40:
    ee:a9:44:68:81:5f:54:04:72:89:68:c6:fa:af:bc:
    06:0f:02:4d:a1:e3:1a:0b:58:3e:77:cb:cc:93:34:
    55:e7:fa:80:a8:39:be:01
prime1:
    00:d9:48:a1:b1:b5:d6:e9:5f:05:f0:54:00:bb:f1:
    2c:9f:38:e6:26:58:a2:f5:1e:26:6c:d2:7c:93:3a:
    76:66:84:c4:a4:13:8f:92:df:cc:e1:0d:38:c8:4e:
    1d:1c:b8:a4:e4:b1:31:5e:52:4b:bf:b1:18:a3:e1:
    3e:18:f6:2c:f9
prime2:
    00:d8:63:29:79:e4:53:dc:84:27:b6:6c:d0:81:37:
    3b:46:07:b3:ef:76:3f:51:61:72:9e:e1:2b:83:ef:
    bd:83:32:3b:e7:c4:ce:dc:0a:15:94:5b:38:34:e5:
    00:aa:16:79:7d:dc:22:ce:ce:ac:6b:46:e3:62:6f:
    81:0b:59:9b:25
exponent1:
    00:c4:15:b6:ce:10:22:d5:52:4a:a2:ba:bc:3a:df:
    87:fc:5c:b5:de:2f:29:48:79:a0:05:9e:e2:8b:5f:
    3c:10:82:8a:8e:e3:94:32:e0:c3:1c:e9:f8:af:53:
    47:14:6f:51:67:8c:bc:d7:b8:fe:e1:0c:2a:07:62:
    b2:ce:86:02:c9
exponent2:
    00:9f:32:95:59:30:3a:e2:89:f8:0d:a6:90:e0:00:
    1a:83:b3:37:16:7e:10:a7:76:e2:35:31:c4:2a:15:
    3f:80:3e:7d:04:4f:2f:41:83:c9:cc:94:30:0d:fa:
    4d:3a:d5:be:1c:72:d0:c9:06:14:a3:f8:4b:62:28:
    56:f0:5a:c4:61
coefficient:
    27:10:f9:fe:ea:6d:dd:8d:3c:09:33:0f:36:0f:12:
    b5:ab:67:dc:22:34:d1:d2:78:3c:a7:2a:c5:da:22:
    11:3f:ba:01:3f:c2:38:84:68:b1:fc:53:ab:57:c3:
    3c:be:2a:ca:ea:20:ac:b2:51:1c:64:1a:37:f4:59:
    04:a9:cd:0d
writing RSA key
-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQC3qXK4kCxn3BNk87vJUMwIznU8pTjr10Kma9+Jkj4zEy/fiZtY
xvdmn1rKNq/8fEUDCcRVC8hQBpevqxFiJ3dbA7ZM6VjUAmztOfRfxSezgvkjswVS
F1/cgBM32AB4nx1dkCV/Wgedn3KFIFU+b8LH1ZLoyRMyLnwWmAkT/mBC/QIDAQAB
AoGAE8Yao+Rh44y+SdA0F6irTwdrd+wSBNJYSrKyjo1ARR97uAWIxDYnzNS7Yaoh
qH14sKsMiFuMZZFQI4m3hWnaX7OFjhJvxKjP6+BdXKsnwWxpwec7RS6n9ptA7qlE
aIFfVARyiWjG+q+8Bg8CTaHjGgtYPnfLzJM0Vef6gKg5vgECQQDZSKGxtdbpXwXw
VAC78SyfOOYmWKL1HiZs0nyTOnZmhMSkE4+S38zhDTjITh0cuKTksTFeUku/sRij
4T4Y9iz5AkEA2GMpeeRT3IQntmzQgTc7Rgez73Y/UWFynuErg++9gzI758TO3AoV
lFs4NOUAqhZ5fdwizs6sa0bjYm+BC1mbJQJBAMQVts4QItVSSqK6vDrfh/xctd4v
KUh5oAWe4otfPBCCio7jlDLgwxzp+K9TRxRvUWeMvNe4/uEMKgdiss6GAskCQQCf
MpVZMDriifgNppDgABqDszcWfhCnduI1McQqFT+APn0ETy9Bg8nMlDAN+k061b4c
ctDJBhSj+EtiKFbwWsRhAkAnEPn+6m3djTwJMw82DxK1q2fcIjTR0ng8pyrF2iIR
P7oBP8I4hGix/FOrV8M8virK6iCsslEcZBo39FkEqc0N
-----END RSA PRIVATE KEY-----
</pre>
## B.4
If someone gets your private key they could decrypt things sent to you with your public key, or sign things on your behalf.
## B.5
We see a PUBLIC KEY string:
<pre>
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC3qXK4kCxn3BNk87vJUMwIznU8
pTjr10Kma9+Jkj4zEy/fiZtYxvdmn1rKNq/8fEUDCcRVC8hQBpevqxFiJ3dbA7ZM
6VjUAmztOfRfxSezgvkjswVSF1/cgBM32AB4nx1dkCV/Wgedn3KFIFU+b8LH1ZLo
yRMyLnwWmAkT/mBC/QIDAQAB
-----END PUBLIC KEY-----
</pre>
## B.7
<pre>
napieraccount@ubuntu:~/test$ openssl rsautl -decrypt -inkey private.pem -in file.bin -out decrypted.txt
napieraccount@ubuntu:~/test$ cat decrypted.txt 
Hello
</pre>

## B.8
We have a hex format for the -hexdump output:
<pre>
napieraccount@ubuntu:~/test$ openssl rsautl -encrypt -inkey public.pem -pubin -in myfile.txt -out file.bin -hexdump
napieraccount@ubuntu:~/test$ cat file.bin
0000 - 88 a7 53 b6 da 09 6d 9f-c6 80 95 3b 23 2a bd 20   ..S...m....;#*. 
0010 - 46 fb 4b f0 51 ee 64 66-79 96 3a b4 5c 32 c4 2b   F.K.Q.dfy.:.\2.+
0020 - 62 b6 5b 1c da 99 1d 5f-1f 81 06 2e 2e 53 eb 7e   b.[...._.....S.~
0030 - c9 c4 4e 6c d4 60 86 e0-9f 52 8c aa d2 8f 65 c2   ..Nl.`...R....e.
0040 - 7c 08 83 13 d3 c0 3e ce-fc b6 be 01 75 ad ee bb   |.....>.....u...
0050 - 9a b6 56 b4 e5 22 7b ea-a5 85 2d 16 fa 7f 50 6f   ..V.."{...-...Po
0060 - d7 67 ff bd 97 c2 26 04-1f 8d 4d c7 52 ea 40 6e   .g....&...M.R.@n
0070 - 9a d9 03 10 67 52 a3 05-8f 0c fd 83 7b 1b 89 1b   ....gR......{...
napieraccount@ubuntu:~/test$ openssl rsautl -encrypt -inkey public.pem -pub
</pre>
We get a binary format with:
<pre>
napieraccount@ubuntu:~/test$ openssl rsautl -encrypt -inkey public.pem -pubin -in myfile.txt -out file.bin 
napieraccount@ubuntu:~/test$ cat file.bin
:�H�n�D.Y��?rѐ��XRfZ'����Rs��5|o��{�W��I�f��^9��LP.�z���bunn_�RX�N��%�9���w_��<�x��ɯ��G1�={|"�p��F��94.P[_
 </pre>

# ECC
## C.1
<pre>
napieraccount@ubuntu:~/test$ openssl ecparam -name secp256k1 -genkey -out priv.pem
napieraccount@ubuntu:~/test$ cat priv.pem 
-----BEGIN EC PARAMETERS-----
BgUrgQQACg==
-----END EC PARAMETERS-----
-----BEGIN EC PRIVATE KEY-----
MHQCAQEEIIjZk1BI+xwWQZ6XetT17JrQgGLdQzvDnTB6iqLEFsGCoAcGBSuBBAAK
oUQDQgAE4VZg4yjli491gWC+f7mNAtI8pdRyHYXhUVjVTFlVXKvflEd3BxRiMUWC
KJPzklyIgOZFAOMYzSv5YvMA/YovWQ==
-----END EC PRIVATE KEY-----
</pre>
## C.2
Values are A, B, Generator (G) and Prime (p), and where G is the generator point. The curve is:

y<sup>2</sup>=x<sup>3</sup>+a x + b (mod p)

<pre>
napieraccount@ubuntu:~/test$ openssl ecparam -in priv.pem -text -param_enc explicit -noout
Field Type: prime-field
Prime:
    00:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:
    ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:fe:ff:
    ff:fc:2f
A:    0
B:    7 (0x7)
Generator (uncompressed):
    04:79:be:66:7e:f9:dc:bb:ac:55:a0:62:95:ce:87:
    0b:07:02:9b:fc:db:2d:ce:28:d9:59:f2:81:5b:16:
    f8:17:98:48:3a:da:77:26:a3:c4:65:5d:a4:fb:fc:
    0e:11:08:a8:fd:17:b4:48:a6:85:54:19:9c:47:d0:
    8f:fb:10:d4:b8
Order: 
    00:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:
    ff:fe:ba:ae:dc:e6:af:48:a0:3b:bf:d2:5e:8c:d0:
    36:41:41
Cofactor:  1 (0x1)
</pre>
## D.3
We generate the public key from the private key. If we have a private key (priv) and a generator point (G). The public key is priv G. In this case we are using a curve of secp256k1.
<pre>
napieraccount@ubuntu:~/test$ openssl ec -in priv.pem -text -noout
read EC key
Private-Key: (256 bit)
priv:
    00:88:d9:93:50:48:fb:1c:16:41:9e:97:7a:d4:f5:
    ec:9a:d0:80:62:dd:43:3b:c3:9d:30:7a:8a:a2:c4:
    16:c1:82
pub: 
    04:e1:56:60:e3:28:e5:8b:8f:75:81:60:be:7f:b9:
    8d:02:d2:3c:a5:d4:72:1d:85:e1:51:58:d5:4c:59:
    55:5c:ab:df:94:47:77:07:14:62:31:45:82:28:93:
    f3:92:5c:88:80:e6:45:00:e3:18:cd:2b:f9:62:f3:
    00:fd:8a:2f:59
ASN1 OID: secp256k1
</pre>

# RSA
## E.1
```python
import rsa
(bob_pub, bob_priv) = rsa.newkeys(512)
print bob_pub
print bob_priv
ciphertext = rsa.encrypt('Here is my message', bob_pub)
message = rsa.decrypt(ciphertext, bob_priv)
print(message.decode('utf8'))
```

A sample run gives:

<pre>
PublicKey(7044152640361902500168576401792350494310726185372977704588682647070501920385795486653093710793158373161949147824992313215786223524754692116109993477603703, 
65537)
PrivateKey(7044152640361902500168576401792350494310726185372977704588682647070501920385795486653093710793158373161949147824992313215786223524754692116109993477603703, 
65537, 1031520101462581111343482730793310461173078401529280666355457029829494893917496934907266419334856470211959662572029962392609614789178286814805200163248601, 
7009636621105341733056641551350073875772161289792261672243040042003271353299512989, 1004924081107519375914073833480034561474534624800691686376057520755477027)
Here is my message
</pre>
The keys are (e,N) for the public key, and (d,N) for the private key. In this case the value of N is:
<pre>
7044152640361902500168576401792350494310726185372977704588682647070501920385795486653093710793158373161949147824992313215786223524754692116109993477603703
</pre>
And e is:
<pre>
65537
</pre>
For the decryption key, N is the same value as the encryption key, and d is:
<pre>
1031520101462581111343482730793310461173078401529280666355457029829494893917496934907266419334856470211959662572029962392609614789178286814805200163248601
</pre>
The two prime numbers used (p and q) are then:
<pre>
7009636621105341733056641551350073875772161289792261672243040042003271353299512989 1004924081107519375914073833480034561474534624800691686376057520755477027
</pre>
Sample:
<pre>
>>> 7009636621105341733056641551350073875772161289792261672243040042003271353299512989*1004924081107519375914073833480034561474534624800691686376057520755477027 
7044152640361902500168576401792350494310726185372977704588682647070501920385795486653093710793158373161949147824992313215786223524754692116109993477603703L
</pre>

## E.2
The code used is:
```python
from Crypto.PublicKey import RSA
from Crypto.Util import asn1
from base64 import b64decode

msg="Pob7AQZZSml618nMwTpx3V74N45x/rTimUQeTl0yHq8F0dsekZgOT385Jls1HUzWCx6ZRFPFMJ1RNYR2Yh7AkQtFLVx9lYDfb/Q+SkinBIBX59ER3/fDhrVKxIN4S6h2QmMSRblh4KdVhyY6cOxu+g48Jh7TkQ2Ig93/nCpAnYQ="
privatekey = 'MIICXAIBAAKBgQCwgjkeoyCXm9v6VBnUi5ihQ2knkdxGDL3GXLIUU43/froeqk7q9mtxT4AnPAaDX3f2r4STZYYiqXGsHCUBZcI90dvZf6YiEM5OY2jgsmqBjf2Xkp/8HgN/XDw/wD2+zebYGLLYtd2u3GXx9edqJ8kQcU9LaMH+ficFQyfq9UwTjQIDAQABAoGAD7L1a6Ess+9b6G70gTANWkKJpshVZDGb63mxKRepaJEX8sRJEqLqOYDNsC+pkKO8IsfHreh4vrp9bsZuECrB1OHSjwDB0S/fm3KEWbsaaXDUAu0dQg/JBMXAKzeATreoIYJItYgwzrJ++fuquKabAZumvOnWJyBIs2z103kDz2ECQQDnn3JpHirmgVdf81yBbAJaXBXNIPzOcCth1zwFAs4EvrE35n2HvUQuRhy3ahUKXsKX/bGvWzmC2O6kbLTFEygVAkEAwxXZnPkaAY2vuoUCN5NbLZgegrAtmU+U2woa5A0fx6uXmShqxo1iDxEC71FbNIgHBg5srsUyDj3OsloLmDVjmQJAIy7qLyOA+sCc6BtMavBgLx+bxCwFmsoZHOSX3l79smTRAJ/HY64RREIsLIQ1q/yW7IWBzxQ5WTHgliNZFjKBvQJBAL3t/vCJwRz0Ebs5FaB/8UwhhsrbtXlGdnkOjIGsmV0vHSf6poHqUiay/DV88pvhN11ZG8zHpeUhnaQccJ9ekzkCQDHHG9LYCOqTgsyYms//cW4sv2nuOE1UezTjUFeqOlsgO+WN96b/M5gnv45/Z3xZxzJ4HOCJ/NRwxNOtEUkw+zY='

keyDER = b64decode(privatekey)
keys = RSA.importKey(keyDER)

dmsg = keys.decrypt(b64decode(msg))
print dmsg
```
The output is:
<pre>
Congrats! The flag is nothing_is_impossible
</pre>


# GitHub integration
## H.1
<pre>
napieraccount@ubuntu:~/.ssh$ cd ~/.ssh
napieraccount@ubuntu:~/.ssh$ ssh-keygen -t rsa -C "w.buchanan@napier.ac.uk"
Generating public/private rsa key pair.
Enter file in which to save the key (/home/napaccount/.ssh/id_rsa): 
/home/napaccount/.ssh/id_rsa already exists.
Overwrite (y/n)? 
napieraccount@ubuntu:~/.ssh$ cat id_rsa
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,231906D9476629A1F38BF98A15E72E03

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
-----END RSA PRIVATE KEY-----
napieraccount@ubuntu:~/.ssh$ ls
id_rsa  id_rsa.pub  known_hosts
napieraccount@ubuntu:~/.ssh$ cat id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCjH32w6ZwaLvaFS2ngOdsc7LVvYiqMKg+z42lwX8Hs58N69gjnPFzrHDPr/BnoIGOEkAGUQxbbUJwLXPiy7X682e6S235+Gh3jSW/xKuGbF9Zq+a/gESZ7t4ReBNweg90Baz24438Zodr6wA7AUdQSO9H1qdb7r4gNN5lvr1zMRhitfZW4UtTF/kXyE5KIDicU2zOFwCJ+AmeuBJGx3NI3YX03JWloZqB2y8zRsBNJ8A8BpeszN95p75Xni1AiHLCXM2HdW87mbdD/lsdrgUTYpMco7srcybeI/1ukbbOsPG6tDbEz3o0KFHgvDWc/XfFG/9I/8mOK1pcQRLj9bYRFHd2O4qdKgSTwtw/PDFAQ+pvCjIzylQp/sTCYI/6KvEEiHxWrY10jF+LDe4CDrmxSFxbgXYIjVMFAwCb0fyxud8V4filZwyFAoeSJWW2lHIFiEJpshQhRvu2zlM1vZHBVmKdVtBBVhq5vJ69SKfMgA2Ms7DRhLoqeqcMmzM+egDBEfvW50w6TeAsB3zoocAkPAdaLmORMGLFS1J/KIeme2LpEryC5FaG8/gziM7RsqjrAcQ/ipeIb+fNYT6POX5z/KVM6x7VcdkV0vr/k+Zkb9qeVcsIlBUAQIAfz24wOQCYZ6UnB9va88JWnjVSgwxeL5KmqgHDelFt50LgXrN/KOw== w.buchanan@napier.ac.uk
</pre>

For the private key, we are using 128-bit AES.


