# 691
import math

const1 = -1
const2 = 1


def f(x):
    return const1*math.exp(2*x)+const2*math.exp(-x)*(3*x+1)


def fdyx(y, x):
   return 2*const1*math.exp(2*x)+const2*math.exp(-x)*(-3*x+2)


def get_pqf():
    return lambda x: -(x+1)/x, lambda x: -2*(x-1)/x, lambda x: 0


s = -math.exp(1)/8
e = math.pi/8
iters = 200
