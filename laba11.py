# 575
import math

const1 = 1
const2 = -2


def f(x):
    return x*math.exp(x)*math.log(x)+(const1*x+const2)*math.exp(x)


def fdyx(y, x):
    return (x+1)*math.exp(x)*math.log(x)+(const1*x+const1+const2+1)*math.exp(x)


def get_pqf():
    return lambda x: -2, lambda x: 1, lambda x: math.exp(x)/x


s = math.pi - math.exp(1)
e = math.pi/2
iters = 200
