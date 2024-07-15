# Overview 
Category: [General Skills]()

AUTHOR: ALEX FULTON/DANIEL TUNITIS

# Description
To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with nc jupiter.challenges.picoctf.org 29221.

# Solution
- Convert from binary chain into words :
```
$ python3 -c "print(''.join(chr(int(b, 2)) for b in ['01100011', '01101111', '01101100', '01101111', '01110010', '01100001', '01100100', '01101111']))"

colorado
```
- Convert from values ​​ascii decimal to words :
```
$ python3 -c "print(''.join(chr(d) for d in [164, 141, 142, 154, 145])"

table
```
- Convert from the HEX string into words:
```
$ python3 -c "print(bytes.fromhex('737472656574').decode('utf-8'))"

street

```
- Results:
```
$ nc jupiter.challenges.picoctf.org 29221
Let us see how data is stored
colorado
Please give the 01100011 01101111 01101100 01101111 01110010 01100001 01100100 01101111 as a word.
...
you have 45 seconds.....

Input:
colorado
Please give me the  164 141 142 154 145 as a word.
Input:
table
Please give me the 737472656574 as a word.
Input:
street
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_00a975ff}
```