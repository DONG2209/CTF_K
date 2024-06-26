# Overview 
10 points

Category: [General Skills]()

AUTHOR: SYREAL

# Description
Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...
# Solution
- Download file :
  > **wget https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm**

- Run file 
  > **./warm**
    => zsh: permission denied: ./warm
- Grant the right to execute the file
  >**chmod +x warm** 
- Run
  
  >\.**/warm**       
   Hello user! Pass me a -h to learn what I can do!
  **./warm -h**
  Oh, help? I actually don't do much, but I do have this flag
  here: **picoCTF{b1scu1ts_4nd_gr4vy_616f7182}**


