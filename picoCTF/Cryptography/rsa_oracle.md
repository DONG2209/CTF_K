# Overview 
Category: [Cryptography]()

AUTHOR: GEOFFREY NJOGU

# Description
Can you abuse the oracle?
An attacker was able to intercept communications between a bank and a fintech company. They managed to get the message (ciphertext) and the password that was used to encrypt the message.
After some intensive reconassainance they found out that the bank has an oracle that was used to encrypt the password and can be found here nc titan.picoctf.net 65051. Decrypt the password and use it to decrypt the message. The oracle can decrypt anything except the password.

# Solution