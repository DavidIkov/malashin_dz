# 540
import math

const = 1
const1 = 0.5


def f(x):
    return -(3*x/10+17/50)*math.sin(x)+(x/10-3/25)*math.cos(x)+const*math.exp(2*x)+const1*math.exp(x)


def fdyx(y, x):
    return -(3/10)*math.sin(x)-(3*x/10+17/50)*math.cos(x)+(1/10)*math.cos(x)-(x/10-3/25)*math.sin(x)+2*const*math.exp(2*x)+const1*math.exp(x)


def f_first_der(y, x, yd):
    return yd()-fdyx(y, x)


def get_pqf():
    return lambda x: -3, lambda x: 2, lambda x: x*math.cos(x)


s = -math.exp(1)*2
e = -math.pi/4
iters = 200
