"""
For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.
I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.
73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d
"""


ah = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
ab = bytes.fromhex(ah)


for i in range(150):
    c = bytes(a^i for a in ab)
    try:
        if c.decode("utf-8").startswith("crypto"):
            print(c, i)
    except UnicodeDecodeError as e:
        # print(e)
        pass

### Afou to ekana me ton parapanw brute tropo eida tin parakatw lisi sto link pou anevazoume to gist me tis lyseis mas kai 
### den mporw me tipota na katalavw ti sto diaolo ekane o typos pou to elyse etsi. Einai i lysi me tis perissoteres psifous
### Kai gia afto me nevriazei pou den katalava apo pou to vrike afto to ab[0]^ord('c')?

key = ab[0]^ord('c')
print(f"Key = {key}")
print(''.join(chr(c ^ key) for c in ab))