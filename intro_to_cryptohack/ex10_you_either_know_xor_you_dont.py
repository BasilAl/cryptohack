"""
I've encrypted the flag with my secret key, you'll never be able to guess it. 
Tip: Remember the flag format and how it might help you in this challenge!
0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
"""

ah = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
ab = bytes.fromhex(ah)
print(ab)
flag = "crypto"

print(ab[1])
# for i in ab:
#     print(type(i))
# key = b"".join(ab[i] for i in range(len("crypto")))
# print(key)
# fl = bytes.

# for i in range(150):
#     c = bytes(a^i for a in ab)
#     print(c)
#     if i%10==0:
#         input("CONTINUE?")