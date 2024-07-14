# Overview 
Category: [General Skills]()

AUTHOR: LT 'SYREAL' JONES

# Description
Can you crack the password to get the flag?
Download the password checker here and you'll need the encrypted flag in the same directory too.

# Solution
- Looking at the code, we already know the password (user_pw)
- Script decode:
```
def str_xor(secret, key):
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c, new_key_c) in zip(secret, new_key)])

flag_enc = open('level2.flag.txt.enc', 'rb').read()

user_pw = chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39)

decryption = str_xor(flag_enc.decode(), user_pw)
print("Decrypted flag:", decryption)
```
- Run script : python3 decode_level2.py 
>Decrypted flag: **picoCTF{tr45h_51ng1ng_9701e681}**
