
import math

# 52 задача

def f(x):
    return 1/(1+math.log(abs(x*x-1)))


def fdyx(y, x):
    return -(2*x)/((x**2-1)*math.log(x**2-1)**2+2*(x**2-1)*math.log(x**2-1)+x**2-1)

def f_first_der(y,x,yd):
    return yd()-fdyx(y,x)

s = math.pi/2
e = math.exp(1)
iters = 500
