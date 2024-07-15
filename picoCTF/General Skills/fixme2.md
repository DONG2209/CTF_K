# Overview 
Category: [General Skills]()

AUTHOR: LT 'SYREAL' JONES

# Description
Fix the syntax error in the Python script to print the flag.

# Solution
- We can easily see the missing "=" sign in the if comparison
```
if flag = "":
  print('String XOR encountered a problem, quitting.')
else:
  print('That is correct! Here\'s your flag: ' + flag)
```
- Correct: 
```
if flag == "":
  print('String XOR encountered a problem, quitting.')
else:
  print('That is correct! Here\'s your flag: ' + flag)
```  
python3 fixme2.py
>That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_f6a5aefc}