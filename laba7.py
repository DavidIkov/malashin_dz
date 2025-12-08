# 301
import math

const = 1


def f(x):
    return x*const/math.exp(x)-x


def fdyx(y, x):
    return (-x*x-x*y+y)/x


def f_first_der(y, x, yd):
    return yd()-fdyx(y, x)


s = -math.exp(1)/2
e = math.pi/4
iters = 100
