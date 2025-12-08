# 533
import math

const = 1
const1 = 0.5


def f(x):
    return math.exp(4*x)/5+const*math.exp(3*x)+const1/math.exp(x)


def fdyx(y, x):
    return 4*math.exp(4*x)/5+3*const*math.exp(3*x)-const1/math.exp(x)


def f_first_der(y, x, yd):
    return yd()-fdyx(y, x)

def get_pqf():
    return lambda x: -2, lambda x: -3, lambda x: math.exp(4*x)


s = -math.exp(1)/2
e = 0
iters = 100
