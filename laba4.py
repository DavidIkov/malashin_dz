import math


# 146 задача

const = -2


def f(x):
    return math.log(math.sqrt(x*x/4-const)+x/2)


def fdyx(y, x):
    return 1/(2*math.exp(y)-x)

def f_first_der(y,x,yd):
    return yd()-fdyx(y,x)


s = -math.pi*2
e = math.exp(1)*2
iters = 50
