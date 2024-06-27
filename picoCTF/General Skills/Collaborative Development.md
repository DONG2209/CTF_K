# Overview 
Category: [General Skills]()

AUTHOR: JEFFERY JOHN

# Description
My team has been working very hard on new features for our flag printing program! I wonder how they'll work together?

# Solution

Download and extract

    ┌──(kali㉿kali)-[~/Downloads/drop-in]
    └─$ ls -la
    total 16
    drwxr-xr-x 3 kali kali 4096 Jun 27 03:22 .
    drwx------ 4 kali kali 4096 Jun 27 03:22 ..
    -rw-r--r-- 1 kali kali   55 Jun 27 03:22 flag.py
    drwxr-xr-x 8 kali kali 4096 Jun 27 03:22 .git

 You see available branches:

    ┌──(kali㉿kali)-[~/Downloads/drop-in]
    └─$ git branch -a                              
    feature/part-1
    feature/part-2
    * feature/part-3
    main



You can either go to each branch and fetch the flags individually, or you can merge all of them into main and resolve merge conflicts. Here's the command to print all feature branches at once:


    ┌──(kali㉿kali)-[~/Downloads/drop-in]
    └─$ git checkout feature/part-1 && cat flag.py && git checkout feature/part-2 && cat flag.py && git checkout feature/part-3 && cat flag.py
    Switched to branch 'feature/part-1'
    print("Printing the flag...")
    print("picoCTF{t3@mw0rk_", end='')Switched to branch 'feature/part-2'
    print("Printing the flag...")

    print("m@k3s_th3_dr3@m_", end='')Switched to branch 'feature/part-3'
    print("Printing the flag...")

    rint("w0rk_798f9981}")

Flag
> **picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_798f9981}**