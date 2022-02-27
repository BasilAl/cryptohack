exercise = """
The Chinese Remainder Theorem gives a unique solution to a set of linear congruences if their moduli are coprime.

This means, that given a set of arbitrary integers ai, and pairwise coprime integers ni, such that the following linear congruences hold:

Tip:  Note "pairwise coprime integers" means that if we have a set of integers {n1, n2, ..., ni}, all pairs of integers selected from the set are coprime: gcd(ni, nj) = 1.



x ≡ a1 mod n1
x ≡ a2 mod n2
...
x ≡ an mod nn


There is a unique solution x ≡ a mod N where N = n1 * n2 * ... * nn.

In cryptography, we commonly use the Chinese Remainder Theorem to help us reduce a problem of very large integers into a set of several, easier problems.

Given the following set of linear congruences:

x ≡ 2 mod 5
x ≡ 3 mod 11
x ≡ 5 mod 17


Find the integer a such that x ≡ a mod 935

Tip: Starting with the congruence with the largest modulus, use that for x ≡ a mod p we can write x = a + k*p for arbitrary integer k."""

SOLUTION = '''
Apo to kineziko thewrima ypoloipwn exoume:


x ≡ 2 mod 5
x ≡ 3 mod 11
x ≡ 5 mod 17

p = 5*11*17 = 935

thetw: zi = p/ni
z1 = 935/5 = 187
z2 = 935/11 = 85
z3 = 935/17 = 55

yi = zi^1 mod ai:
y1 = 187^-1 mod 5 = 3 mod 5
y2 = 85^-1 mod 11 = 7 mod 11
y3 = 55^-1 mod 17 = 13 mod 17

To thewrima dinei: wi = yizi mod p
w1 = 3*187 = 561 mod 935
w2 = 7*85 = 595 mod 935
w3 = 13*55 = 715 mod 935

kai etsi: 
x = Σaiwi mod p = 6482 mod 935 = 872 mod 935
'''
