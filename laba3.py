
import math

#121 задача

const = 2

def f(x):
    return x**2*(1-1/(math.log(x)+const))

def fdyx(y, x):
    return 2*x-(2*x*math.log(x)+3*x)/(math.log(x)**2+4*math.log(x)+4)

def f_first_der(y,x,yd):
    return yd()-fdyx(y,x)


s = math.pi/2
e = math.exp(1)*4
iters = 500


