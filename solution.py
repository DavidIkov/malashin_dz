
import half_division_method
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import sys
import importlib

module_name=f"laba{sys.argv[1]}"
laba=importlib.import_module(module_name)

step = (laba.e-laba.s)/laba.iters

all_x = [laba.s+step*i for i in range(laba.iters)]

if hasattr(laba, "f"):
    analytic_y = [laba.f(x) for x in all_x]
    plt.plot(all_x, analytic_y, label="analytic")


if hasattr(laba, "fdyx"):
    approximated_y = []
    cur_x = laba.s
    cur_y = laba.f(cur_x)
    for i in range(laba.iters):
        approximated_y += [cur_y]
        cur_y = cur_y+step*laba.fdyx(cur_y, cur_x)
        cur_x += step
    plt.plot(all_x, approximated_y, label="euler")


if hasattr(laba, "fdyx"):
    solution = odeint(laba.fdyx, laba.f(laba.s), all_x)
    plt.plot(all_x, solution.flatten(), label="scipy")

if hasattr(laba, "fdyx"):
    approximated_y = []
    cur_x = laba.s
    cur_y = laba.f(cur_x)
    for i in range(laba.iters):
        approximated_y += [cur_y]
        k1 = laba.fdyx(cur_y, cur_x)
        k2 = laba.fdyx(cur_y+step/2*k1, cur_x+step/2)
        k3 = laba.fdyx(cur_y+step/2*k2, cur_x+step/2)
        k4 = laba.fdyx(cur_y+step*k3, cur_x+step)
        cur_y = cur_y+step/6*(k1+2*k2+2*k3+k4)
        cur_x += step
    plt.plot(all_x, approximated_y, label="runge kutte")


if hasattr(laba, "fdyx"):
    approximated_y = []

    h = step

    cur_x = laba.s
    cur_y = laba.f(cur_x)

    delta = 1

    for i in range(laba.iters):
        approximated_y += [cur_y]

        new_y = half_division_method.solve(
            cur_y-delta, cur_y+delta, 1e-2, lambda y: (y-cur_y)/h-laba.fdyx(cur_y, cur_x))

        diff = new_y-cur_y
        if abs(diff) < 0.01:
            diff = 0.01
        delta = diff/h

        cur_y = new_y
        cur_x += h
    plt.plot(all_x, approximated_y, label="finite difference method")

if hasattr(laba, "get_pqf"):

    import generate_tridiagonal_system as tridiag
    import thomas_algorithm as thomas

    A, B, C, D, x = tridiag.gen(
        laba.iters, laba.s, laba.e, *laba.get_pqf(), laba.f(laba.s), laba.f(laba.e))
    y = thomas.solve(A, B, C, D)

    plt.plot(x, y, label="tridiagonal system")


plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()
