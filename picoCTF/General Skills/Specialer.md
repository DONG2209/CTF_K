# Overview 
Category: [General Skills]()

AUTHOR: LT 'SYREAL' JONES, ET AL.

# Description
Reception of Special has been cool to say the least. That's why we made an exclusive version of Special, called Secure Comprehensive Interface for Affecting Linux Empirically Rad, or just 'Specialer'. With Specialer, we really tried to remove the distractions from using a shell. Yes, we took out spell checker because of everybody's complaining. But we think you will be excited about our new, reduced feature set for keeping you focused on what needs it the most. Please start an instance to test your very own copy of Specialer.

# Solution
- The command to replace cat is: echo "$(<filename)"
```
Specialer$ ls
-bash: ls: command not found
Specialer$ echo *
abra ala sim
Specialer$ cd abra/
Specialer$ echo *
cadabra.txt cadaniel.txt
Specialer$ cat cadabra.txt 
-bash: cat: command not found
Specialer$ echo "$(<cadabra.txt)"
Nothing up my sleeve!
Specialer$ echo "$(<cadaniel.txt)"
Yes, I did it! I really did it! I'm a true wizard!
Specialer$ cd ..
Specialer$ echo *
abra ala sim
Specialer$ cd ala/
Specialer$ echo *
kazam.txt mode.txt
Specialer$ echo "$(<kazam.txt)"
return 0 picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_c42168d9}
```