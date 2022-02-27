exercise = """
As we've seen, we can work within a finite field Fp, adding and multiplying elements, and always obtain another element of the field.

For all elements g in the field, there exists a unique integer d such that g * d ≡ 1 mod p.

This is the multiplicative inverse of g.

Example: 7 * 8 = 56 ≡ 1 mod 11

What is the inverse element: 3 * d ≡ 1 mod 13?
Tip:  Think about the little theorem we just worked with. How does this help you find the inverse of an element?
"""



Solution = """
13 prime, 13 -| 3 ==> (fermat's little theorem) 3^(13-1) = 1 mod 13 =>  solution = 3^11mod13 = 9"""

