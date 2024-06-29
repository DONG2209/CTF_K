# Overview 
Category: [General Skills]()

AUTHOR: LOIC SHEMA

# Description
There's an interesting script in the user's home directory

# Solution

>ssh picoplayer@saturn.picoctf.net -p61245

Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 6.5.0-1016-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

>picoplayer@challenge:~$ ls

>useless

>picoplayer@challenge:~$ cat useless

    #!/bin/bash
    \# Basic mathematical operations via command-line arguments

    if [ $# != 3 ]
    then
        echo "Read the code first"
    else
        if [[ "$1" == "add" ]]
        then
          sum=$(( $2 + $3 ))
          echo "The Sum is: $sum"

        elif [[ "$1" == "sub" ]]
        then
          sub=$(( $2 - $3 ))
          echo "The Substract is: $sub"

        elif [[ "$1" == "div" ]]
        then
          div=$(( $2 / $3 ))
          echo "The quotient is: $div"

        elif [[ "$1" == "mul" ]]
        then
          mul=$(( $2 * $3 ))
          echo "The product is: $mul"

        else
          echo "Read the manual"

        fi
    fi

I notice a very interesting else statement at the end of the if loop.It says Read the Manual ..  In Linux, the man command is used to display the manual pages (documentation) for various commands, programs, and system functions. It provides detailed information about the usage, options, and examples of how to use a particular command or function.

>picoplayer@challenge:~$ man useless

useless
     useless, -- This is a simple calculator script

SYNOPSIS
     useless, [add sub mul div] number1 number2

DESCRIPTION
     Use the useless, macro to make simple calulations like addition,subtraction, multiplication and division.

Examples
    ./useless add 1 2
       This will add 1 and 2 and return 3
    ./useless mul 2 3
       This will return 6 as a product of 2 and 3
    ./useless div 6 3
       This will return 2 as a quotient of 6 and 3
    ./useless sub 6 5
       This will return 1 as a remainder of substraction of 5 from 6

Authors
    This script was designed and developed by Cylab Africa

     picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_6194}

picoplayer@challenge:~$ Connection to saturn.picoctf.net closed by remote host.
Connection to saturn.picoctf.net closed.