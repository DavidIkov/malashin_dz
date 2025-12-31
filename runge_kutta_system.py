def solve(t_start, x0, y0, step, n_iters, f_x, f_y):
        approximated_x = []
        approximated_y = []
        times = []

        cur_t = t_start
        cur_x = x0
        cur_y = y0

        for i in range(n_iters):
            approximated_x.append(cur_x)
            approximated_y.append(cur_y)
            times.append(cur_t)

            k1x = f_x(cur_t, cur_x, cur_y)
            k1y = f_y(cur_t, cur_x, cur_y)

            k2x = f_x(
                cur_t + step/2, cur_x + step/2 * k1x, cur_y + step/2 * k1y)
            k2y = f_y(
                cur_t + step/2, cur_x + step/2 * k1x, cur_y + step/2 * k1y)

            k3x = f_x(
                cur_t + step/2, cur_x + step/2 * k2x, cur_y + step/2 * k2y)
            k3y = f_y(
                cur_t + step/2, cur_x + step/2 * k2x, cur_y + step/2 * k2y)

            k4x = f_x(
                cur_t + step, cur_x + step * k3x, cur_y + step * k3y)
            k4y = f_y(
                cur_t + step, cur_x + step * k3x, cur_y + step * k3y)

            cur_x = cur_x + step/6 * (k1x + 2*k2x + 2*k3x + k4x)
            cur_y = cur_y + step/6 * (k1y + 2*k2y + 2*k3y + k4y)

            cur_t += step

        return times, approximated_x, approximated_y


