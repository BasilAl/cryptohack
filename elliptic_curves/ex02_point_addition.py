"""
While working with elliptic curve cryptography, we will need to add points together. In the background challenges, we did this geometrically by finding a line that passed through two points, finding the third intersection and then reflecting along the y-axis.

It turns out that there is an efficient algorithm for calculating the point addition law for an elliptic curve.

Taken from "An Introduction to Mathematical Cryptography", Jeffrey Hoffstein, Jill Pipher, Joseph H. Silverman, the following algorithm will calculate the addition of two points on an elliptic curve

Algorithm for the addition of two points: P + Q

(a) If P = O, then P + Q = Q.
(b) Otherwise, if Q = O, then P + Q = P.
(c) Otherwise, write P = (x1, y1) and Q = (x2, y2).
(d) If x1 = x2 and y1 = −y2, then P + Q = O.
(e) Otherwise:
  (e1) if P ≠ Q: λ = (y2 - y1) / (x2 - x1)
  (e2) if P = Q: λ = (3x12 + a) / 2y1
(f) x3 = λ2 − x1 − x2,     y3 = λ(x1 −x3) − y1
(g) P + Q = (x3, y3)


We are working with a finite field, so the above calculations should be done mod p, and we do not "divide" by an integer, we instead multiply by the modular inverse of a number. e.g. 1 / 5 = 9 mod 11.

We will work with the following elliptic curve, and prime:

E: Y2 = X3 + 497 X + 1768, p: 9739

You can test your algorithm by asserting: X + Y = (1024, 4440) and X + X = (7284, 2107) for X = (5274, 2841) and Y = (8669, 740).

Using the above curve, and the points P = (493, 5564), Q = (1539, 4742), R = (4403,5202), find the point S(x,y) = P + P + Q + R by implementing the above algorithm.

After calculating S, substitute the coordinates into the curve. Assert that the point S is in E(Fp)
"""


# Sto https://stackoverflow.com/questions/31074172/elliptic-curve-point-addition-over-a-finite-field-in-python kapoios egrapse kalo kwdika gia addition kai
# ton pira etoimo. Einai apli diadikasia, opote apla glytwsa ligo xrono ylopoiisis.a


# Create a simple Point class to represent the affine points.
from collections import namedtuple
Point = namedtuple("Point", "x y")

# The point at infinity (origin for the group law).
O = 'Origin'

# Choose a particular curve and prime.  We assume that p > 3.
p = 9739
a = 497
b = 1768

def valid(P):
    """
    Determine whether we have a valid representation of a point
    on our curve.  We assume that the x and y coordinates
    are always reduced modulo p, so that we can compare
    two points for equality with a simple ==.
    """
    if P == O:
        return True
    else:
        return (
            (P.y**2 - (P.x**3 + a*P.x + b)) % p == 0 and
            0 <= P.x < p and 0 <= P.y < p)

def inv_mod_p(x):
    """
    Compute an inverse for x modulo p, assuming that x
    is not divisible by p.
    """
    if x % p == 0:
        raise ZeroDivisionError("Impossible inverse")
    return pow(x, p-2, p)

def ec_inv(P):
    """
    Inverse of the point P on the elliptic curve y^2 = x^3 + ax + b.
    """
    if P == O:
        return P
    return Point(P.x, (-P.y)%p)

def ec_add(P, Q):
    """
    Sum of the points P and Q on the elliptic curve y^2 = x^3 + ax + b.
    """
    if not (valid(P) and valid(Q)):
        raise ValueError("Invalid inputs")

    # Deal with the special cases where either P, Q, or P + Q is
    # the origin.
    if P == O:
        result = Q
    elif Q == O:
        result = P
    elif Q == ec_inv(P):
        result = O
    else:
        # Cases not involving the origin.
        if P == Q:
            dydx = (3 * P.x**2 + a) * inv_mod_p(2 * P.y)
        else:
            dydx = (Q.y - P.y) * inv_mod_p(Q.x - P.x)
        x = (dydx**2 - P.x - Q.x) % p
        y = (dydx * (P.x - x) - P.y) % p
        result = Point(x, y)

    # The above computations *should* have given us another point
    # on the curve.
    assert valid(result)
    return result





# After calculating S, substitute the coordinates into the curve. Assert that the point S is in E(Fp)


# You can test your algorithm by asserting: X + Y = (1024, 4440) and X + X = (7284, 2107) for X = (5274, 2841) and Y = (8669, 740).
X = Point(5274,2841)
Y = Point(8669,740)
assert ec_add(X, Y) == Point(1024,4440)

# Using the above curve, and the points P = (493, 5564), Q = (1539, 4742), R = (4403,5202), find the point S(x,y) = P + P + Q + R by implementing the 
# above algorithm.
P = Point(493, 5564)
Q = Point(1539,4742)
R = Point(4403,5202)
S = ec_add(ec_add(P,P), ec_add(Q, R))
print(S)