<!---
B.4
```python
print (chars//16+1)*32
```
--->
<!---
C.4
```python
print (chars//16+1)*16
```
--->

Commands in Section A:

* openssl list-cipher-commands
* openssl version
* openssl prime –hex 1111
* openssl enc -aes-256-cbc -in myfile.txt -out encrypted.bin
* openssl enc -aes-256-cbc -in myfile.txt -out encrypted.bin –base64
* openssl enc -d -aes-256-cbc -in encrypted.bin -pass pass:napier -base64

## A.7
We can use the -bf-cbc option for Blowfish:

<pre>
openssl enc -bf-cbc -in myfile.txt -out encrypted1.bin 
openssl enc -d -bf-cbc -pass pass:password -in encrypted1.bin 
</pre>

A sample run is:
<pre>
$ openssl enc -bf-cbc -in myfile.txt -out encrypted1.bin 
enter bf-cbc encryption password: password
Verifying - enter bf-cbc encryption password: password
$ openssl enc -d -bf-cbc -pass pass:password -in encrypted1.bin 
Hello
</pre>

##  B.2
You may need to install "Crypto" with:
<pre>
pip install pycrypto
</pre>
And Padding with:
<pre>
pip install padding
</pre>

```python
from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

val='hello'
password='hello'

plaintext=val

def encrypt(plaintext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password).digest()


plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='CMS')
print "After padding (CMS): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode='CMS')
print "  decrypt: "+plaintext


plaintext=val


plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='ZeroLen')
print "\nAfter padding (Bit): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,blocksize=Padding.AES_blocksize,mode='ZeroLen')
print "  decrypt: "+plaintext


plaintext=val

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='Space')
print "\nAfter padding (Null): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,blocksize=Padding.AES_blocksize,mode='Space')
print "  decrypt: "+plaintext


plaintext=val

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='Random')
print "\nAfter padding (Random): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode='Random')
print "  decrypt: "+plaintext
```

## C.2

```python
from Crypto.Cipher import DES
import hashlib
import sys
import binascii
import Padding

val='hello'
password='hello'

plaintext=val


def encrypt(plaintext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.decrypt(ciphertext))


print "\nDES"
key = hashlib.sha256(password).digest()[:8]

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.DES_blocksize,mode='CMS')
print "After padding (CMS): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,DES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,DES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode='CMS')
print "  decrypt: "+plaintext
```

## D.1
```python
from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

val='hello'
password='hello'

plaintext=val

def encrypt(plaintext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password).digest()


plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='CMS')
print "After padding (CMS): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode='CMS')
print "  decrypt: "+plaintext


plaintext=val
```
## E.1
Possible solution for E.1:

```python
from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

val='fox'
password='hello'
cipher=''

import sys

if (len(sys.argv)>1):
	cipher=(sys.argv[1])
if (len(sys.argv)>2):
	password=(sys.argv[2])

plaintext=val

def encrypt(plaintext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password).digest()


ciphertext=binascii.unhexlify(cipher)

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
print plaintext
plaintext = Padding.removePadding(plaintext,mode='CMS')
print "  decrypt: "+plaintext


plaintext=val
```
## E.2
DES uses a 64-bit key, of which we have use 56 bits for the actual key. We thus need to truncate our SHA-256 generated key, down to a 64-bit key. We can do that in Python with [:8]. A possible solution for E.2:

```python
from Crypto.Cipher import DES
import hashlib
import sys
import binascii
import Padding

val='fox'
password='hello'
cipher=''

import sys

def encrypt(plaintext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password).digest()


ciphertext=binascii.unhexlify("f37ee42f2267458d")

plaintext = decrypt(ciphertext,key[:8],DES.MODE_ECB)
print plaintext

plaintext = Padding.removePadding(plaintext,mode='CMS')
print "  decrypt: "+plaintext


plaintext=val
```


## F.1
A sample code for Section F is:

```python
pw = ["hello","ankle","changeme","123456"]

for password in pw:

	try:
		key = hashlib.sha256(password).digest()
		cipherhex = base64.decodestring(cipher).encode('hex')

		ciphertext = binascii.unhexlify(cipherhex)

		print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

		plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
		plaintext = Padding.removePadding(plaintext,mode='CMS')
		print "  decrypt: "+plaintext
		print "  Key found"+password

	except:	
		print(".")
 ```


## G.1
Answers:
* e47a2bfe646a - orange
* ea783afc66 - apple
* e96924f16d6e - banana

Just convert the hex value to a byte array:

```javascript
var chacha20 = require("chacha20");
var crypto = require('crypto');

var keyname="qwerty";

var key = crypto.createHash('sha256').update(keyname).digest();

var nonce = new Buffer.alloc(8);

nonce.fill(0);

console.log( key);

var ciphertext="e96924f16d6e" 
// var ciphertext="ea783afc66"
// var ciphertext="e47a2bfe646a"

console.log("Ciphertext:\t",ciphertext);

console.log("Decipher\t",chacha20.decrypt(key,nonce, new Buffer(ciphertext,"hex")).toString());
```
## G.2
Answers:
* 8d1cc8bdf6da - orange
* 911adbb2e6dda57cdaad - strawberry
* 8907deba - kiwi

```javascript
// RC4

var crypto = require('crypto');

var keyname="napier";

var key = crypto.createHash('sha256').update(keyname).digest();

var cipher = crypto.createCipheriv('rc4', key,'' );
var ciphertext = '8d1cc8bdf6da'
console.log("Ciphertext:\t",ciphertext);


var decipher = crypto.createDecipheriv('rc4', key,'' );
var text = decipher.update( new Buffer(ciphertext,"hex"), 'hex','utf8');
console.log("Decipher:\t",text);
```

## Sample answers

A possible answer for Section E is:

```python
from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

val='hello'
password='hello'


cipher=raw_input('Enter cipher:')
password=raw_input('Enter password:')

plaintext=val

def encrypt(plaintext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password).digest()


ciphertext = binascii.unhexlify(cipher)

print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode='CMS')
print "  decrypt: "+plaintext
```


