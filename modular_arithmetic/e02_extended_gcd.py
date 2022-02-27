exercise = """
Let a and b be positive integers.

The extended Euclidean algorithm is an efficient way to find integers u,v such that

a * u + b * v = gcd(a,b)

Tip:  Later, when we learn to decrypt RSA, we will need this algorithm to calculate the modular inverse of the public exponent.

Using the two primes p = 26513, q = 32321, find the integers u,v such that

p * u + q * v = gcd(p,q)

Enter whichever of u and v is the lower number as the flag.

Tip: Knowing that p,q are prime, what would you expect gcd(p,q) to be? For more details on the extended Euclidean algorithm, check out this page.
"""
from pprint import pprint


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
            

    
pprint(extended_euclid(26513,32321))