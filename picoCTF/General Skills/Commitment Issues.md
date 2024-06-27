# Overview 
Category: [General Skills]()

AUTHOR: JEFFERY JOHN

# Description
I accidentally wrote the flag down. Good thing I deleted it!

# Solution

Download and extract

Then,go to the logs directory, you will see:
<img src="https://i.imgur.com/v7tLqY5.png">

You see a note that says "create flag" with the id of "b562f0b425907789d11d2fe2793e67592dc6be93"

Run:

    git show b562f0b425907789d11d2fe2793e67592dc6be93
    commit b562f0b425907789d11d2fe2793e67592dc6be93
    Author: picoCTF <ops@picoctf.com>
    Date:   Tue Mar 12 00:06:23 2024 +0000

        create flag

    diff --git a/message.txt b/message.txt
    new file mode 100644
    index 0000000..0e0fefc
    --- /dev/null
    +++ b/message.txt

> git show b562f0b425907789d11d2fe2793e67592dc6be93:message.txt
        **picoCTF{s@n1t1z3_c785c319}**