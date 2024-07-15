# Overview 
Category: [General Skills]()

AUTHOR: SANJAY C/DANNY TUNITIS

# Description
Can you find the flag in file without running it?

# Solution
- Use "strings" commands and save results to Ouput.txt
>$ strings strings > output.txt

- Find flag in Ouput.txt:
```
$ grep -i "picoCTF" output.txt
picoCTF{5tRIng5_1T_827aee91}
```
