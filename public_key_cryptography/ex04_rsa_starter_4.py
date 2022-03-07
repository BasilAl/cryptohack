"""
The private key d is used to decrypt ciphertexts created with the corresponding public key (it's also used to "sign" a message but we'll get to that later).
The private key is the secret piece of information or "trapdoor" which allows us to quickly invert the encryption function. 
If RSA is implemented well, if you do not have the private key the fastest way to decrypt the ciphertext is to first factorise the modulus.
In RSA the private key is the modular multiplicative inverse of the exponent e modulo the totient of N.
Given the two primes:
p = 857504083339712752489993810777

q = 1029224947942998075080348647219

and the exponent:

e = 65537

What is the private key d? 
"""

from sympy.ntheory.factor_ import totient as fi

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
N = p*q
fiN = fi(p)*fi(q)
print(pow(e,fiN-2,fiN))

def extended_euclid(a,b):
    """q*a + p*b = gcd(a,b)"""
    s = 0 
    old_s = 1
    r = b 
    old_r = a
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q*r
        old_s, s = s, old_s - q*s
    if b != 0:
        bezout_t = (old_r - old_s *a) // b
    else:
        bezout_t = 0
        
    print(f"({old_s})*({a}) + ({bezout_t})*({b}) = {old_r}")
    return ({'q*a + p*b = gcd(a,b)' : f"({old_s})*({a}) + ({bezout_t})*({b}) = {old_r}", 'q' : old_s, 'p': bezout_t, f"gcd({a},{b})" : old_r})

extended_euclid(e, fiN)