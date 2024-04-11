def simple_stop_criteria(absolute_value: float, epsilon: float) -> bool:
    return absolute_value < epsilon


def calc_y(func: list, x: float) -> float:
    return sum(value * (x ** index) for index, value in enumerate(func))


def calc_x(func: list, x: float, xn: float) -> float:
    y_x = calc_y(func, x)
    return xn - (calc_y(func, xn) * (xn - x) / (calc_y(func, xn) - y_x))


def seq_method(func: list, initial_approx: float, xn: float, stop_criteria: callable, epsilon: float) -> float:
    x = calc_x(func, initial_approx, xn)

    while not stop_criteria(abs(x - initial_approx), epsilon):
        x, initial_approx = calc_x(func, x, initial_approx), x

    return x


initial = 0
x_n = 0.5
eps = 0.01
function = [-6, 11, -6, 1]

answer = seq_method(function, initial, x_n, simple_stop_criteria, eps)
print(f"Корень, найденный методом секущих: {answer}. Что ≈ {round(answer)}")
