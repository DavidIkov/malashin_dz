# 575
import math

const1 = 1
const2 = -2


def f(x):
    return math.exp(x)*(x*math.log(x)+(const1+const2*x))


def fdyx(y, x):
    return math.exp(x)*(const1+const2+x*const2+x*math.log(x)+1+math.log(x))


def get_pqf():
    return lambda x: -2, lambda x: 1, lambda x: math.exp(x)/x


s = math.pi - math.exp(1)
e = math.pi/2
iters = 100
