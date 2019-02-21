from Crypto.Cipher import AES

import hashlib
import sys
import binascii
import Padding

val='Hello'
password='qwerty'
salt='241fa86763b85341'

print key
plaintext=val

def get_key_and_iv(password, salt, klen=32, ilen=16, msgdgst='md5'):
    '''
    Derive the key and the IV from the given password and salt.
    This is a niftier implementation than my direct transliteration of
    the C++ code although I modified to support different digests.
    CITATION: http://stackoverflow.com/questions/13907841/implement-openssl-aes-encryption-in-python
    @param password  The password to use as the seed.
    @param salt      The salt.
    @param klen      The key length.
    @param ilen      The initialization vector length.
    @param msgdgst   The message digest algorithm to use.
    '''
    # equivalent to:
    #   from hashlib import <mdi> as mdf
    #   from hashlib import md5 as mdf
    #   from hashlib import sha512 as mdf
    mdf = getattr(__import__('hashlib', fromlist=[msgdgst]), msgdgst)
    password = password.encode('ascii', 'ignore')  # convert to ASCII

    try:
        maxlen = klen + ilen
        keyiv = mdf(password + salt).digest()
        tmp = [keyiv]
        while len(tmp) < maxlen:
            tmp.append( mdf(tmp[-1] + password + salt).digest() )
            keyiv += tmp[-1]  # append the last byte
        key = keyiv[:klen]
        iv = keyiv[klen:klen+ilen]
        return key, iv
    except UnicodeDecodeError:
         return None, None

def encrypt(plaintext,key, mode,salt):
	key,iv=get_key_and_iv(key,salt.decode('hex'))
	
	encobj = AES.new(key,mode,iv)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode,salt):
        key,iv=get_key_and_iv(key,salt.decode('hex'))
	encobj = AES.new(key,mode,iv)
	return(encobj.decrypt(ciphertext))

padding_len = 16 - (len(plaintext) % 16)
plaintext = plaintext + (chr(padding_len) * padding_len)

ciphertext = encrypt(plaintext,key,AES.MODE_CBC,salt)

ctext = b'Salted__' + salt.decode('hex') + ciphertext

print "Cipher (ECB): "+base64.b64encode(ctext)

plaintext = decrypt(ciphertext,key,AES.MODE_CBC,salt)
plaintext = Padding.removePadding(plaintext,mode='CMS')
print "  decrypt: "+plaintext
