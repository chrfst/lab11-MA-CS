# https://github.com/chrfst/lab11-MA-CS.git
# Partner 1: Matas Ambrukaitis
# Partner 2: Christopher St. John
import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

# First example

import math
def add(a, b): 
    return a + b
def sub(a, b):
    return a-b
def mul(a,b):
    return a * b
def div(a,b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a
def log(a, b):
    if b < 0 or b == 0:
        raise ValueError
    if a < 0 or a == 1:
        raise ValueError
    else:
        math.log(b, a)
def exp(a, b):
    return math.pow(a, b)