# Overview 
Category: [General Skills]()

AUTHOR: LT 'SYREAL' JONES

# Description
Can you crack the password to get the flag?
Download the password checker [here](https://artifacts.picoctf.net/c/33/level5.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/33/level5.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/33/level5.hash.bin) in the same directory too. Here's a [dictionary](https://artifacts.picoctf.net/c/33/dictionary.txt) with all possible passwords based on the password conventions we've seen so far.

# Solution
- We perform Brute-Force Password based on files Dictionary.txt.
This is the script:
```python
import hashlib

def str_xor(secret, key):
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

flag_enc = open('level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level5.hash.bin', 'rb').read()

def try_passwords_from_dictionary():
    with open('dictionary.txt', 'r') as f:
        passwords = f.read().splitlines()

    for password in passwords:
        if hash_pw(password) == correct_pw_hash:
            print("Password found:", password)
            decryption = str_xor(flag_enc.decode(), password)
            print("Flag:", decryption)
            return

    print("Password not found in dictionary.")

try_passwords_from_dictionary()
```
- Results:
```
$ python3 decode_level5.py
Password found: eee0
Flag: picoCTF{h45h_sl1ng1ng_fffcda23}
```