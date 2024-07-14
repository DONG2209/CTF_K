# Overview 
Category: [General Skills]()

AUTHOR: LT 'SYREAL' JONES

# Description
Can you crack the password to get the flag?
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too.
There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

# Solution
- As we can see, the password is hashed and then compared with the hash file. We also have a list of possible passwords (pos_pw_list). We can try to crack the password using a list of possible passwords. We can use hashlib library to hash passwords and compare them with hash file.
- Script decode:

    import hashlib

    def str_xor(secret, key):
        new_key = key
        i = 0
        while len(new_key) < len(secret):
            new_key += key[i]
            i = (i + 1) % len(key)
        return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c, new_key_c) in zip(secret, new_key)])

    flag_enc = open('level3.flag.txt.enc', 'rb').read()
    correct_pw_hash = open('level3.hash.bin', 'rb').read()

    def hash_pw(pw_str):
        pw_bytes = bytearray()
        pw_bytes.extend(pw_str.encode())
        m = hashlib.md5()
        m.update(pw_bytes)
        return m.digest()

    pos_pw_list = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]

    def find_correct_password():
        for password in pos_pw_list:
            if hash_pw(password) == correct_pw_hash:
                print(f"Correct password found: {password}")
                decryption = str_xor(flag_enc.decode(), password)
                print(f"Decrypted flag: {decryption}")
                return

    find_correct_password()

- Run script : python3 decode_level3.py 
>Correct password found: 2295
Decrypted flag: **picoCTF{m45h_fl1ng1ng_6f98a49f}**
