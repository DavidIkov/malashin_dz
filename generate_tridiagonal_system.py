import numpy as np


def gen(n, a, b, p, q, f, alpha, beta):
    """
    y'' + p(x)y' + q(x)y = f(x)
    y(a)=alpha, y(b)=beta
    """
    h = (b - a) / (n - 1)
    x = np.linspace(a, b, n)

    A = np.zeros(n)
    B = np.zeros(n)
    C = np.zeros(n)
    D = np.zeros(n)

    B[0] = 1
    C[0] = 0
    D[0] = alpha

    A[n-1] = 0
    B[n-1] = 1
    D[n-1] = beta

    for i in range(1, n-1):
        A[i] = 1/h**2 - p(x[i])/(2*h)
        B[i] = -2/h**2 + q(x[i])
        C[i] = 1/h**2 + p(x[i])/(2*h)
        D[i] = f(x[i])

    return A, B, C, D, x
