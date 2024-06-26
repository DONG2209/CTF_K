# Overview 
20 points

Category: [General Skills]()

AUTHOR: SYREAL

# Description
Can you look at the data in this binary: static? This BASH script might help!

# Solution
- Download file
  > **wget https://mercury.picoctf.net/static/66932732825076cad4ba43e463dae82f/static**
- Grant the right to execute the file
  > **chmod +x static** 
- Run file and find flag :
  > **strings static | grep pico**

  >=> picoCTF{d15a5m_t34s3r_f5aeda17}
