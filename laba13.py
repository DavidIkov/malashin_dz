# 752
import math

def f(x):
    return x+math.exp(-x)-1/math.exp(1)


def fdyx(y, x):
   return 1-math.exp(-x)


def get_pqf():
    return lambda x: 1, lambda x: 0, lambda x: 1


s = -math.exp(1)/2
e = math.pi/4
iters = 200
