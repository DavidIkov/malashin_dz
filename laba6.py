# 265
import math

const = 1


def f(x):
    return const/math.exp(x)-x*x


def fdyx(y, x):
    a = 1
    b = 4*x
    c = -y*y-2*x*x*y-x**4+4*x*x
    return (-b-math.sqrt(b*b-4*a*c))/2/a


s = -math.exp(1)/2
e = math.pi/4
iters = 50
