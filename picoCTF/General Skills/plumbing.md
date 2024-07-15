# Overview 
Category: [General Skills]()

AUTHOR: SANJAY C/DANNY TUNITIS

# Description
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to jupiter.challenges.picoctf.org 7480.

# Solution
Save the result to the output.txt file with Netcat:
```
nc jupiter.challenges.picoctf.org 7480 | tee output.txt
```
Find the flag in the output.txt :
```
$ grep -i "picoCTF" output.txt
picoCTF{digital_plumb3r_06e9d954}
```