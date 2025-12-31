# 783
from scipy.integrate import quad
import numpy as np
import math


def f(x):
    return x*x


s = 0
e = math.pi/4
iters = 200


def fourier_series_self_func(n,x):
    if n == 0:
        return 1
    else:
        return math.cos(n * np.pi * x / e)

def fourier_series_coef(n):
    return ((2 if n else 1)/e) * quad(lambda x: f(x) * fourier_series_self_func(n, x), 0, e)[0]

fourier_series_n=10
