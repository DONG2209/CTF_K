# Overview 
Category: [General Skills]()

AUTHOR: DANNY

# Description
There's a flag shop selling stuff, can you buy a flag? Source. Connect with nc jupiter.challenges.picoctf.org 4906.

# Solution
- We can see that the cost is negative, even though it was entered as 9999999999999 multiplied by 900, which is 2147483647—the maximum value of an `int` in C. Therefore, the multiplication causes an integer overflow and the cost becomes negative. Since we subtract a negative cost, we end up with a positive number. That's why we can purchase the flag now.
```
Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
1
These knockoff Flags cost 900 each, enter desired quantity
99999999999999

The final cost is: -305595268

Your current balance after transaction: 305596368

Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
1



 Balance: 305596368 


Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
2
1337 flags cost 100000 dollars, and we only have 1 in stock
Enter 1 to buy one
1
YOUR FLAG IS: picoCTF{m0n3y_bag5_9c5fac9b}
``` 