integer = 9
eps = 10 ** (-10)
x_0 = 5


def calc_next_x(digit: int, x_start: int):
    return 0.5 * (x_start + (digit / x_start))


def lite_iter_method(integer: int, eps: int, x_0: int):
    x = calc_next_x(integer, x_0)

    while abs(x - x_0) > eps:
        x, x_0 = calc_next_x(integer, x), x

    return x


sqr = lite_iter_method(integer, eps, x_0)
print(sqr, sqr == integer ** 0.5)
