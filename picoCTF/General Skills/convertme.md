# Overview 
Category: [General Skills]()

AUTHOR: LT 'SYREAL' JONES

# Description
Run the Python script and convert the given number from decimal to binary to get the flag.

# Solution
## Method 1
- We need to convert the decimal number 71 to binary. We can do this in another terminal by using the bin() function in python. We can run the following command:
```
$ python3 -c "print(bin(71))" 
0b1000111
```
- We can then enter the answer into the script:
```
$ python3 convertme.py       
If 71 is in decimal base, what is it in binary base?
Answer: 0b1000111
That is correct! Here's your flag: picoCTF{4ll_y0ur_b4535_9c3b7d4d}
```
## Method 2
- We can get the flag through editing the code :
```python
import random

def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])

flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5f) + chr(0x05) + chr(0x08) + chr(0x2a) + chr(0x1c) + chr(0x5e) + chr(0x1e) + chr(0x1b) + chr(0x3b) + chr(0x17) + chr(0x51) + chr(0x5b) + chr(0x58) + chr(0x5c) + chr(0x3b) + chr(0x4c) + chr(0x06) + chr(0x5d) + chr(0x09) + chr(0x5e) + chr(0x00) + chr(0x41) + chr(0x01) + chr(0x13)

flag =str_xor(flag_enc, 'enkidu')
print(flag)
```
We easily get results :
```
$ python3 convertme.py
picoCTF{4ll_y0ur_b4535_9c3b7d4d}
```