# 265
import math

const = 1


def f(x):
    return const/math.exp(x)-x*x


def fdyx(y, x):
    return -2*x-(y+x*x)


def original_fd(y, x, fd):
    return fd()**2+4*x*fd()-y*y-2*x*x*y-x**4+4*x*x


s = -math.exp(1)/2
e = 0
iters = 100
