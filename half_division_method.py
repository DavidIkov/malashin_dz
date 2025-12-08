def solve(a, b, accuracy, f):
    c = (a + b) / 2
    while abs(f(c)) > accuracy:
        if f(a)*f(c) < 0:
            b = c
        elif f(b)*f(c) < 0:
            a = c
        else:
            exit(1)
        c = (a + b) / 2
    return c


