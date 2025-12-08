
import math

#101 задача

const = 2

def f(x):
    return (x/const-1)*x


def fdyx(y, x):
    return (x+2*y)/x

def f_first_der(y,x,yd):
    return yd()-fdyx(y,x)


s = math.pi/2
e = math.exp(1)*4
iters = 500


