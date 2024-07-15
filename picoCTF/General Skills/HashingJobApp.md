# Overview 
Category: [General Skills]()

AUTHOR: LT 'SYREAL' JONES

# Description
If you want to hash with the best, beat this test!
nc saturn.picoctf.net 61049

# Solution
- Can use  md5sum command:
>  echo -n 'a used car lot' | md5sum

- nc saturn.picoctf.net 61049 
```
Please md5 hash the text between quotes, excluding the quotes: 'a used car lot'
Answer: 
1a78bc064f8df8b4192ce5f8972c9b80 
1a78bc064f8df8b4192ce5f8972c9b80 
Correct.
Please md5 hash the text between quotes, excluding the quotes: 'a treehouse'
Answer: 
98b0ee4dfd8e04322c60bd32481b512e
98b0ee4dfd8e04322c60bd32481b512e
Correct.
```
**picoCTF{4ppl1c4710n_r3c31v3d_3eb82b73}**


