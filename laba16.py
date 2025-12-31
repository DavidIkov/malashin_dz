# 790
import math

const1=1
const2=2

def f_x_by_t(t):
    return math.exp(t)*(const1*math.cos(3*t)+const2*math.sin(3*t))

def f_y_by_t(t):
    return math.exp(t)*(const1*math.sin(3*t)-const2*math.cos(3*t))


def orig_f_x_by_t(t, x, y):
    return x-3*y


def orig_f_y_by_t(t, x, y):
    return 3*x+y

iters=500
start_t=0
t_step=0.01
