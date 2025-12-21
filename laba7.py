# 301
import math

const = 1


def f(x):
    return x*const/math.exp(x)-x


def fdyx(y, x):
    return (-x*x-x*y+y)/x


def original_fd(y, x, fd):
    return x*fd()+x*x+x*y-y


s = -math.exp(1)/2
e = math.pi/4
iters = 200
