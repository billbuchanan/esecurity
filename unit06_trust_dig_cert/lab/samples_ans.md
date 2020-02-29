![esecurity](https://raw.githubusercontent.com/billbuchanan/esecurity/master/z_associated/esecurity_graphics.jpg)

# Lab 6: Trust and Digital Certificates


## A	Introduction

### A.1	

What is CN used for: Common Name

What is OU used for: Organisational Unit

What is O used for: Organisational

What is L used for: Location



### A.3	
<pre>
$ openssl s_client -connect www.live.com:443
CONNECTED(00000005)
depth=2 C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Global Root CA
verify return:1
depth=1 C = US, O = DigiCert Inc, CN = DigiCert Cloud Services CA-1
verify return:1
depth=0 C = US, ST = Washington, L = Redmond, O = Microsoft Corporation, CN = outlook.com
verify return:1
---
Certificate chain
 0 s:C = US, ST = Washington, L = Redmond, O = Microsoft Corporation, CN = outlook.com
   i:C = US, O = DigiCert Inc, CN = DigiCert Cloud Services CA-1
 1 s:C = US, O = DigiCert Inc, CN = DigiCert Cloud Services CA-1
   i:C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Global Root CA
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIHzjCCBragAwIBAgIQCoH8ucQ1FhbxdOc4Y7FvoTANBgkqhkiG9w0BAQsFADBL
MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMSUwIwYDVQQDExxE
aWdpQ2VydCBDbG91ZCBTZXJ2aWNlcyBDQS0xMB4XDTE5MTIyNDAwMDAwMFoXDTIx
MTIyNDEyMDAwMFowajELMAkGA1UEBhMCVVMxEzARBgNVBAgTCldhc2hpbmd0b24x
EDAOBgNVBAcTB1JlZG1vbmQxHjAcBgNVBAoTFU1pY3Jvc29mdCBDb3Jwb3JhdGlv
bjEUMBIGA1UEAxMLb3V0bG9vay5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw
ggEKAoIBAQDLFi2juwqukpMR/dNzYseJ2nU9LPCnrpyYbnFxRxf8m3L8Z+n3XREd
LmTZ0lIK2V2sgJnR+16PvnTeuLlT0XVnaDWsE2/6bR6T3zCI9HlmB5mYgBAKrLq6
yB1yZlf+DqaGFZUVRu1rgAt4DTZvc4liwve3n04Cm7/XZAluv223SGMc6sdRi8cq
IHaPTZsJW2GQeFkvIjb7/Cz6IzwVS7bj62cWRYQeq08Nl3hEOgOPwbWDLmLj7hDe
UbPzdZuh2Mo2PhF1CbZXz2IGRMcsgou6+Tu2s/MhexemAwKwqQntoE5rEdPc2GcC
...
kdLxzsCguY8dsdvU+iKBqqTGrF0+aq++Yu+wSgj8wLUa3jUPJ1/Cd4k/kAKQCCL5
LvT0BheI4kzyqQW/QykMpTRbpctzLgA0IZctBRXj4xsI1aUYj1ZoaKy/XFMO0lGK
Ta7iKyY7UwpRxq2+i4DBGcgnN4mFXif6qMC6LVS2H43fPQ==
-----END CERTIFICATE-----
subject=C = US, ST = Washington, L = Redmond, O = Microsoft Corporation, CN = outlook.com

issuer=C = US, O = DigiCert Inc, CN = DigiCert Cloud Services CA-1

---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA
Server Temp Key: ECDH, P-384, 384 bits
---
SSL handshake has read 3978 bytes and written 472 bytes
Verification: OK
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 2048 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: 752A8406875DA02E17A539E7676182F6EBDC880FE5DA95BE0531B733E6EB054B
    Session-ID-ctx: 
    Master-Key: 4E1B4A0FB630888BA14231377A314568F7B9BABBF5298E79E09561B904DC739DF52F2B1288A78F5DCAEFABFF73D23A3D
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 36000 (seconds)
    TLS session ticket:
    0000 - 00 00 00 00 9f 3a 0d cc-5c 36 33 40 99 33 db 87   .....:..\63@.3..
    0010 - a4 9f 2b 34 57 bb 51 2b-ca f6 9e 71 c2 b1 54 ca   ..+4W.Q+...q..T.
    0020 - a2 49 b8 14 d5 61 02 5f-d4 b2 a3 a4 a0 41 85 f5   .I...a._.....A..
    0030 - 0a a1 92 07 f6 d9 52 23-5a 87 ba 2e d5 78 70 08   ......R#Z....xp.
    0040 - 8d 23 cc ff de 2c d8 1d-20 ba f0 af f2 66 62 20   .#...,.. ....fb 
    0050 - 5f a3 ed 29 8f 8e 5d a5-65 a3 05 4a 71 9b b6 8e   _..)..].e..Jq...
    0060 - 6b 66 9a 4c ec 38 93 63-3b 47 ad 15 ab 72 3a 54   kf.L.8.c;G...r:T
    0070 - a5 25 07 94 38 67 49 89-ee f2 47 09 f7 d5 4b 0b   .%..8gI...G...K.
    0080 - a2 60 9b 07 47 6e 61 fc-b7 3b e1 55 e7 e7 d7 6e   .`..Gna..;.U...n
    0090 - 96 05 08 e4 60 a7 e6 80-40 66 dc 85 34 a7 fa 5a   ....`...@f..4..Z
    00a0 - 2d 6d 11 31 d6 63 d0 86-bc ff f9 bd fa 0a f6 e6   -m.1.c..........
    00b0 - 17 7d dc bd 40 23 9a 46-58 bc de c5 6e 83 b0 2c   .}..@#.FX...n..,
    00c0 - cc 43 7d e5 bb 04 aa 21-51 e8 1b c3 eb fe d6 56   .C}....!Q......V
    00d0 - 8b 20 b0 9d 58 eb c7 6d-2f 51 5c ad 60 f3 36 40   . ..X..m/Q\.`.6@
    00e0 - 7a a6 ce 9b 9a 2f 2b e4-ce 4c 95 61 44 6d 58 b7   z..../+..L.aDmX.
    00f0 - 8b b2 a4 ff 17 6a 3e 05-d2 7f 2d 39 e2 cd 9d 54   .....j>...-9...T
    0100 - f2 45 18 e0                                       .E..

    Start Time: 1582994186
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: yes
    </pre>


