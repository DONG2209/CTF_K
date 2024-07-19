# Overview 
Category: [General Skills]()

AUTHOR: ALEX BUSHKIN

# Description
I wrote you another [song](https://jupiter.challenges.picoctf.org/static/b99c57e4274172bf3c93534b6d59632d/lyrics.txt). Put the flag in the picoCTF{} flag format

# Solution
- Install rockstar-py :
```bash
$ pip install rockstar-py
```
- After installing the compiler, we can run the following command to compile the code:
```bash
$ rockstar-py -i lyrics.txt -o lyric.py
```
- Results:
```python
Rocknroll = True
Silence = False
a_guitar = 10
Tommy = 44
Music = 170
the_music = input()
if the_music == a_guitar:
    print("Keep on rocking!")
    the_rhythm = input()
    if the_rhythm - Music == False:
        Tommy = 66
        print(Tommy!)
        Music = 79
        Jamming = 78
        print(Music!)
        print(Jamming!)
        Tommy = 74
        print(Tommy!)
        They are dazzled audiences
        print(it!)
        Rock = 86
        print(it!)
        Tommy = 73
        print(it!)
        break
        print("Bring on the rock!")
        Else print("That ain't it, Chief")
        break
```
- We Can See the code is not valid python code. and we cannot run it, if we try to under stand it we will find that it is a simple code that will print some numbers but if we noticed the code we will find a comment that says "They are dazzled audiences" If we know try to run the following code, in the online interpreter:
```
They are dazzled audiences
shout it!
```
- we will get this output:
```
79
```
- So we can see that the code is trying to print the ASCII value of the string They are dazzled audiences.
- So we got all the numbers that the code is trying to print. So we can use the following python code to get the flag:
```
$ python3 -c "print(''.join(chr(int(i)) for i in [66, 79, 78, 74, 79, 86, 73]))"
BONJOVI
```
> Flag: **picoCTF{BONJOVI}**