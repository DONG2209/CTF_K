# Overview 
Category: [General Skills]()

AUTHOR: JEFFERY JOHN

# Description
Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses.
Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools!

ssh -p 63814 ctf-player@atlas.picoctf.net
Using the password f3b61b38. Accept the fingerprint with yes, and ls once connected to begin. Remember, in a shell, passwords are hidden!

# Solution
The binary search algorithm is an efficient method for finding an element in a sorted array.

Principles of the Binary Search Algorithm

- **Initialize the search range:**
  Start with the entire range of the array, that is, from the lowest index (usually 1) to the highest index (in this case, 1000).

- **Find the middle element:**
  > mid = (low + high) / 2

- **Compare the value at the middle index with the target value:**
  + If the value at the middle index equals the target value, you have found the element and the algorithm ends.
  + If the value at the middle index is greater than the target value, adjust the search range to the lower half of the array (i.e., from `low` to `mid - 1`).
  + If the value at the middle index is less than the target value, adjust the search range to the upper half of the array (i.e., from `mid + 1` to `high`).
  
Run:

    Enter your guess: 500
    Higher! Try again.
    Enter your guess: 750
    Higher! Try again.
    Enter your guess: 875
    Lower! Try again.
    Enter your guess: 812
    Lower! Try again.
    Enter your guess: 781                                                                               
    Congratulations! You guessed the correct number: 781                                                
    Here's your flag: picoCTF{g00d_gu355_6dcfb67c}                                                      
    Connection to atlas.picoctf.net closed.      