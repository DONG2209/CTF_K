# Overview 
Category: [General Skills]()

AUTHOR: SYREAL

# Description
Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `ee388b88`

# Solution
- Connect :
>ssh ctf-player@venus.picoctf.net -p 56307

- List the files available in the present
```
ctf-player@pico-chall$ ls
1of3.flag.txt  instructions-to-2of3.txt
```
- The flag is divided into 3 parts, reading "instructions.txt" to find the next part of the flag
```
ctf-player@pico-chall$ cat 1of3.flag.txt 
picoCTF{xxsh_
ctf-player@pico-chall$ cat instructions-to-2of3.txt 
Next, go to the root of all things, more succinctly `/`
ctf-player@pico-chall$ cd /
ctf-player@pico-chall$ ls -a
.   .dockerenv     bin   dev  home                      lib    media  opt   root  sbin  sys  usr
..  2of3.flag.txt  boot  etc  instructions-to-3of3.txt  lib64  mnt    proc  run   srv   tmp  var
ctf-player@pico-chall$ cat 2of3.flag.txt 
0ut_0f_\/\/4t3r_
ctf-player@pico-chall$ cat instructions-to-3of3.txt 
Lastly, ctf-player, go home... more succinctly `~`
ctf-player@pico-chall$ cd ~
ctf-player@pico-chall$ ls
3of3.flag.txt  drop-in
ctf-player@pico-chall$ cat 3of3.flag.txt 
3ca613a1}
```

>Flag : **picoCTF{xxsh_0ut_0f_\/\/4t3r_3ca613a1}**