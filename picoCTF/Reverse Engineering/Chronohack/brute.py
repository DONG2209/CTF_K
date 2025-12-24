#!/usr/bin/env python3

from pwn import *
import random
import time

alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
TOKEN_LEN = 20

def gen_token(seed):
    random.seed(seed)
    return "".join(random.choice(alphabet) for _ in range(TOKEN_LEN))

found_flag = False

for t in range(-50, 1000,20):
    print('=====time==='+str(t)+'=====')
    now = int(time.time() * 1000)

    for i in range(0, 50):
        print('Tweak: ' + str(i + t))
        token = gen_token(now + i + t).encode("utf-8")