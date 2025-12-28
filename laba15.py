# 427
import math

const1=-1
const2=1

def f(x):
    return const1*x-math.exp(-x)*const1+const2


def fdyx(y, x):
   return (1+math.exp(-x))*const1

s = -math.exp(1)/2
e = math.pi/4
iters = 100
