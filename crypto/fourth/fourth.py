from Crypto.Util.number import *

flag = b'***'

def keygen():
    p = getPrime(1024)
    q = p ** 2 + (1<<256)
    while not(isPrime(q)):
        q += 2
    n = p ** 2 * q
    return p, q, n

def encrypt(flag, n, e):
    return pow(bytes_to_long(flag), e, n)

e = 65537
print("e=", e)
p, q, n = keygen()
print("n=", n)

print("enc=", encrypt(flag, n, e))



