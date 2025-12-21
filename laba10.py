# 547
import math

const = 2
const1 = 1


def f(x):
    return math.exp(-2*x)*(const+const1*x)+math.exp(2*x)*(x/16-1/32)


def fdyx(y, x):
   return math.exp(-2*x)*(-2*const+const1-2*const1*x)+math.exp(2*x)*x/8


def get_pqf():
    return lambda x: 4, lambda x: 4, lambda x: x*math.exp(2*x)


s = 0
e = math.exp(1)/2
iters = 100
