
Try not to look at these answers, unless you really have too ..

## A.2
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
## A.3
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

## A.4
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
## A.5
Start and end are:
<pre>
-----BEGIN RSA PRIVATE KEY-----
-----END RSA PRIVATE KEY-----
</pre>
## A.6
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
:�H�n�D.Y��?rѐ��XRfZ'����Rs��5|o��{�W��I�f��^9
                                                ��LP.�z���bunn_�RX�N��%�9���w_��<�x��ɯ��G1�={|"�p��F��94.P[_
                                                  </pre>





