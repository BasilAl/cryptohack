"""
The first step of each AES round is SubBytes. 
This involves taking each byte of the state matrix and substituting it for a different byte in a preset 16x16 lookup table. 
The lookup table is called a "Substitution box" or "S-box" for short, and can be perplexing at first sight. Let's break it down.
"""