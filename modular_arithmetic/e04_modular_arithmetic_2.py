ex = """
We'll pick up from the last challenge and imagine we've picked a modulus p, and we will restrict ourselves to the case when p is prime.

The integers modulo p define a field, denoted Fp.

Tip: If the modulus is not prime, the set of integers modulo n define a ring.

A finite field Fp is the set of integers {0,1,...,p-1}, and under both addition and multiplication there is an inverse element b for every element a in the set, such that a + b = 0 and a * b = 1.

Tip:  Note that the identity element for addition and multiplication is different! This is because the identity when acted with the operator should do nothing: a + 0 = a and a * 1 = a.

Lets say we pick p = 17. Calculate 317 mod 17. Now do the same but with 517 mod 17.

What would you expect to get for 716 mod 17? Try calculating that.

This interesting fact is known as Fermat's little theorem. We'll be needing this (and its generalisations) when we look at RSA cryptography.

Now take the prime p = 65537. Calculate 27324678765465536^65536 mod 65537.

Did you need a calculator? 
"""

from e01_greatest_common_divisor import gcd
from sympy import isprime

print(isprime(65537))
print(gcd(27324678765465536,65537))
# An p prwtos kai den diairei to a: a^(p-1) = 1 mod p 
# Isxyoun oi synthikes tou thewrimatos fermat, ara to apotelesma einai 1.
