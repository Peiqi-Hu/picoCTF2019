# RSA Algo Encrypt and Decrypt
import gmpy2

def find_n(p, q):
    n = p*q
    print("n = ", n)
    #return n

def find_ph(p, q):
    ph = (p-1)*(q-1)
    print("ph(n) = ", ph)
    #return ph

def encrypt(msg, e, n):
    cipher = (msg**e)%n
    print("Ciphertext is: ", cipher)

def decrypt(ciphertext, d, n):
    plain = (ciphertext**d)%n
    print("Plaintext is: ", plain)

def find_d(e, ph):
    # de = 1 (mod(ph)) which is d = (1 + x*ph)/e
    # but we will get "int division result too large for a float error" if ph is huge

    # use d = (1+x*ph)//e however, "//" may leads to non-accurate result

    #use gmpy2
    d = gmpy2.invert(ph, e)
    print("d = ", d)

'''
Based on online codes - solving gcd using extended Euclidean algo
https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
'''
def egcd(a, b):
    if a == 0:   # if remainder is 0, then print out value and exit the function egcd
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)   #ax = 1 (mod m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
