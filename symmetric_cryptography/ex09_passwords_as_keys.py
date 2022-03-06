from Crypto.Cipher import AES
import hashlib
import random


# /usr/share/dict/words from
# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words
# import os
# print(os.getcwd())
with open('symmetric_cryptography/words', "r") as f:
    words = [w.strip() for w in f.readlines()]
keyword = random.choice(words)

KEY = hashlib.md5(keyword.encode()).digest()
# FLAG = ?

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    # key = bytes.fromhex(password_hash)
    key = password_hash
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}
    ret = decrypted.hex()
    
    ret = bytes.fromhex(decrypted.hex())
    return {"plaintext": ret}


def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())

    return {"ciphertext": encrypted.hex()}


ciphertext = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"


for keyword in words:
    KEY = hashlib.md5(keyword.encode()).digest()
    a = decrypt(ciphertext, KEY)['plaintext']
    if a.startswith(b"crypto"):
        print(a)