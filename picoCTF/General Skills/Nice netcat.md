# Overview 
15 points

Category: [General Skills]()

AUTHOR: SYREAL

# Description
There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 7449, but it doesn't speak English...

# Solution
-  Invokes the Netcat utility (nc)
  > **nc mercury.picoctf.net 7449**
112 
105 
99 
...
...
97 
125 
10 
- Convert ascii to text 
  [Link convert](https://www.duplichecker.com/ascii-to-text.php)
=> **picoCTF{g00d_k1tty!_n1c3_k1tty!_f2d7cafa}**