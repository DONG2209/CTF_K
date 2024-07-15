# Overview 
Category: [General Skills]()

AUTHOR: LT 'SYREAL' JONES

# Description
Our flag printing service has started glitching!
$ nc saturn.picoctf.net 64825

# Solution
```
nc saturn.picoctf.net 64825
'picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}'
```
We can see that the flag is being printed, but there are some characters missing. We can fix this by replacing the chr() function with the actual characters. We can use the python3 command to do this:
```
print('picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}')
```
python3 script.py
**picoCTF{gl17ch_m3_n07_a4392d2e}**
