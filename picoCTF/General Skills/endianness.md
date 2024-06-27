# Overview 
Category: [General Skills]()

AUTHOR: NANA AMA ATOMBO-SACKEY

# Description
Know of little and big endian?

# Solution
First connected to the server: 
> nc titan.picoctf.net 61087

After that, you will receive a word, in this case "Yzewx". By using [Cyberchef](https://cyberchef.org/) , converts from this to HEX form. This will give you how to express the big endian of this word.

Convert BIG ENDIAN ⇔ LITTLE ENDIAN : [here](https://www.save-editor.com/tools/wse_hex.html#littleendian) 

    ┌──(kali㉿kali)-[/]
    └─$ nc titan.picoctf.net 63810 
    Welcome to the Endian CTF!
    You need to find both the little endian and big endian representations of a word.
    If you get both correct, you will receive the flag.
    Word: yzewx
    Enter the Little Endian representation: 7877657A79
    Correct Little Endian representation!
    Enter the Big Endian representation: 797A657778
    Correct Big Endian representation!
    Congratulations! You found both endian representations correctly!
    Your Flag is: picoCTF{3ndi4n_sw4p_su33ess_cfe38ef0}
