from elliptic import *
from finitefield.finitefield import FiniteField

import os


def generateSecretKey(numBits):
   return int(os.urandom(numBits // 8).encode('hex'), 16)


def sendDH(privateKey, generator, sendFunction):
   return sendFunction(privateKey * generator)


def receiveDH(privateKey, receiveFunction):
   return privateKey * receiveFunction()


def slowOrder(point):
   Q = point
   i = 1
   while True:
      if type(Q) is Ideal:
         return i
      else:
         Q = Q + point
         i += 1

def to_bytes(n, length):
    return bytes( (n >> i*8) & 0xff for i in reversed(range(length)))

if __name__ == "__main__":
   F = FiniteField(3851, 1)

   # Totally insecure curve: y^2 = x^3 + 324x + 1287
   curve = EllipticCurve(a=F(324), b=F(1287))

   # order is 1964
   basePoint = Point(curve, F(920), F(303))

   aliceSecretKey = generateSecretKey(8)
   bobSecretKey = generateSecretKey(8)

   print "Alice\'s secret key:\t", aliceSecretKey
   print "Bob\'s secret key:\t", bobSecretKey

   print "=========================="

   alicePublicKey = sendDH(aliceSecretKey, basePoint, lambda x:x)
   bobPublicKey = sendDH(bobSecretKey, basePoint, lambda x:x)

   print "Alice's public key:\t",alicePublicKey
   print "Bob's public key:\t",bobPublicKey

   sharedSecret1 = receiveDH(bobSecretKey, lambda: alicePublicKey)
   sharedSecret2 = receiveDH(aliceSecretKey, lambda: bobPublicKey)

   print "=========================="
   print "Alice\'s shared key:\t",sharedSecret1
   print "Bob\'s shared key:\t",sharedSecret2


   print "=========================="
   print "The shared value is the x-value:\t", (sharedSecret1.x.n)