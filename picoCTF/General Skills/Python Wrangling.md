# Overview 
10 points
Category: [General Skills]()
AUTHOR: SYREAL

# Description
Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?

# Solution
- Read password 
  > **cat pw.txt**
192ee2db192ee2db192ee2db192ee2db
- Run file python and enter password
  > **python ende.py -d flag.txt.en**
Please enter the password:192ee2db192ee2db192ee2db192ee2db
  => **picoCTF{4p0110_1n_7h3_h0us3_192ee2db}**
