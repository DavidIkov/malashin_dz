# 511
import math

const = 1
const1 = 0


def f(x):
    return const*math.exp(x)+const1/math.exp(2*x)


def fdyx(y, x):
    return const*math.exp(x)+(-2)*const1/math.exp(2*x)


def f_first_der(y, x, yd):
    return yd()-fdyx(y, x)

def get_pqf():
    return lambda x: 1, lambda x: -2, lambda x: 0


s = -math.exp(1)/2
e = math.pi/4
iters = 50
