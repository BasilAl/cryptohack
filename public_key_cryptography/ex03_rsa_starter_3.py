"""
RSA relies on the difficulty of the factorisation of the modulus N. 
If the primes can be found then we can calculate the Euler totient of N and thus decrypt the ciphertext.
Given N = p*q and two primes:
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
What is the totient of N? 
"""


p = 857504083339712752489993810777
q = 1029224947942998075080348647219
N = p*q

from sympy.ntheory.factor_ import totient as fi

# αν μ,ν πρώτοι μεταξύ τους: φ(μν) = φ(μ)φ(ν)

print(fi(p)*fi(q))