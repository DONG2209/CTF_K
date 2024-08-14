# Overview 
Category: [Cryptography]()

AUTHOR: NGIRIMANA SCHADRACK

# Description
Can you get the real meaning from this file.
Download the file [here](https://artifacts.picoctf.net/c_titan/109/enc_flag)

# Solution
- Open the file I saw "==", I immediately thought of the Base64 encryption. I used [CyberChef](https://cyberchef.org/) to decode it
<img src="https://i.imgur.com/O7kdJk2.png">

- Similarly, I decode again
<img src="https://i.imgur.com/bCXSyR1.png">

- Because the flag has a picoctf {...}, I think the code is only "+" or "-" Number. Can solve the hand, but I used the [tool](https://www.dcode.fr/caesar-cipher) to solve faster :>>
<img src="https://i.imgur.com/RgNXCfe.png">

>Flag : **picoCTF{caesar_d3cr9pt3d_f0212758}**