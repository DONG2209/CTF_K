# Overview 
Category: [General Skills]()

AUTHOR: DANNY

# Description
I wrote you a [song](https://jupiter.challenges.picoctf.org/static/c594d8d915de0129d92b4c41e25a2313/lyrics.txt). Put it in the picoCTF{} flag format.

# Solution
- Use the [online interpreter](https://web.archive.org/web/20190522020843/https://codewithrockstar.com/online) to run the code.
- After we run the code, we can see the output:
```
114
114
114
111
99
107
110
114
110
48
49
49
51
114
```
- We can see the output is a bunch of numbers. we can python to convert the numbers to ascii:
```
$ python3 -c "print(''.join(chr(i) for i in [114, 114, 114, 111, 99, 107, 110, 114, 110, 48, 49, 49, 51, 114]))"
rrrocknrn0113r
```