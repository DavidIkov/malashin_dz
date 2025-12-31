
import half_division_method
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import sys
import importlib

module_name = f"laba{sys.argv[1]}"
laba = importlib.import_module(module_name)

if hasattr(laba, "f"):
    step = (laba.e-laba.s)/laba.iters
    all_x = [laba.s+step*i for i in range(laba.iters)]

    analytic_y = [laba.f(x) for x in all_x]
    plt.plot(all_x, analytic_y, label="analytic")


if hasattr(laba, "fdyx"):
    step = (laba.e-laba.s)/laba.iters
    all_x = [laba.s+step*i for i in range(laba.iters)]

    approximated_y = []
    cur_x = laba.s
    cur_y = laba.f(cur_x)
    for i in range(laba.iters):
        approximated_y += [cur_y]
        cur_y = cur_y+step*laba.fdyx(cur_y, cur_x)
        cur_x += step
    plt.plot(all_x, approximated_y, label="euler")


if hasattr(laba, "fdyx"):
    step = (laba.e-laba.s)/laba.iters
    all_x = [laba.s+step*i for i in range(laba.iters)]

    solution = odeint(laba.fdyx, laba.f(laba.s), all_x)
    plt.plot(all_x, solution.flatten(), label="scipy")

if hasattr(laba, "fdyx"):
    step = (laba.e-laba.s)/laba.iters
    all_x = [laba.s+step*i for i in range(laba.iters)]

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


if hasattr(laba, "original_fd"):
    step = (laba.e-laba.s)/laba.iters
    all_x = [laba.s+step*i for i in range(laba.iters)]

    approximated_y = []

    h = step

    cur_x = laba.s
    cur_y = laba.f(cur_x)

    delta = 0.1

    for i in range(laba.iters):
        approximated_y += [cur_y]

        new_y = half_division_method.solve(
            cur_y-delta, cur_y+delta, 1e-2, lambda y: laba.original_fd(cur_y, cur_x, lambda: (y-cur_y)/h))

        cur_y = new_y
        cur_x += h
    plt.plot(all_x, approximated_y, label="finite difference method")
elif hasattr(laba, "original_fd_fdd"):
    step = (laba.e-laba.s)/laba.iters
    all_x = [laba.s+step*i for i in range(laba.iters)]

    approximated_y = []

    h = step

    prev_x = laba.s
    prev_y = laba.f(prev_x)
    cur_x = prev_x+h
    cur_y = laba.f(cur_x)

    delta = 0.1

    for i in range(laba.iters):
        approximated_y += [cur_y]

        new_y = half_division_method.solve(
            cur_y-delta, cur_y+delta, 1e-2, lambda y: laba.original_fd_fdd(cur_y, cur_x, lambda: (y-prev_y)/2/h, lambda: (y-2*cur_y+prev_y)/h/h))

        prev_x = cur_x
        prev_y = cur_y
        cur_y = new_y
        cur_x += h
    plt.plot(all_x, approximated_y, label="finite difference method")

if hasattr(laba, "get_pqf"):

    step = (laba.e-laba.s)/laba.iters
    all_x = [laba.s+step*i for i in range(laba.iters)]

    import generate_tridiagonal_system as tridiag
    import thomas_algorithm as thomas

    tridiagonal_sys = tridiag.gen(
        laba.iters, laba.s, laba.e, *laba.get_pqf(), laba.f(laba.s), laba.f(laba.e))
    y = thomas.solve(*tridiagonal_sys)

    plt.plot(all_x, y, label="tridiagonal system")

if hasattr(laba, "fourier_series_self_func") and hasattr(laba, "fourier_series_coef") and hasattr(laba, "fourier_series_n"):

    step = (laba.e-laba.s)/laba.iters
    all_x = [laba.s+step*i for i in range(laba.iters)]

    approximated_y = []

    for x in all_x:
        res_y = 0
        for cur_n in range(laba.fourier_series_n):
            coef = laba.fourier_series_coef(cur_n)
            func = laba.fourier_series_self_func(cur_n, x)
            res_y += coef*func
        approximated_y += [res_y]

    plt.plot(all_x, approximated_y, label="fourier series")

if hasattr(laba, "f_x_by_t") and hasattr(laba, "f_y_by_t"):

    all_t = [laba.start_t+laba.t_step*i for i in range(laba.iters)]

    x = [laba.f_x_by_t(t) for t in all_t]
    y = [laba.f_y_by_t(t) for t in all_t]
    plt.plot(x, y, label="analytic by t")


if hasattr(laba, "orig_f_x_by_t") and hasattr(laba, "orig_f_y_by_t") and hasattr(laba, "f_x_by_t") and hasattr(laba, "f_y_by_t"):
    import runge_kutta_system

    x0 = laba.f_x_by_t(laba.start_t)
    y0 = laba.f_y_by_t(laba.start_t)

    times, x_vals, y_vals = runge_kutta_system.solve(
        laba.start_t, x0, y0, laba.t_step, laba.iters, laba.orig_f_x_by_t, laba.orig_f_y_by_t)

    plt.plot(x_vals, y_vals, label="runke kutte by t")


plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()
