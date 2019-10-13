import math
import random

def my_sqrt(a):
    x = random.randint(1, 10)    #  chooses random starting value for x
    while True:
        y = (x + a/x) / 2.0
        if y == x:
            break
        x = y
    return y    # return its final value

def test_sqrt():
    for i in range(1, 26):
        my = my_sqrt(i)
        pc = math.sqrt(i)
        # this print uses 'f literal - can read about it here ->   https://cito.github.io/blog/f-strings/
        print(f"a = {i} | my_sqrt(a) = {my} | math.sqrt(a) = {pc} | diff = { abs( my - pc ) }") # absolute value of differences

test_sqrt()