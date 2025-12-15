# 187
import math

const = 1


def f(x):
    return math.sqrt((3*x*x*x+math.sqrt(9*x**6-4*(x*x-const)))/2)


def fdyx(y, x):
    return -x*(2-9*x*y*y)/y/(4*y*y-6*x*x*x)


s = -math.exp(1)/4
e = math.pi/2
iters = 50
