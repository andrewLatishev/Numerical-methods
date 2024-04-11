def find_root(func, x0, x1, epsilon):
    if func(x0) * func(x1) >= 0:
        return None  # Нет гарантии наличия корня в заданном интервале
    else:
        x2 = (x0 + x1) / 2
        while abs(func(x2)) > epsilon:
            if func(x0) * func(x2) < 0:
                x1 = x2
            elif func(x1) * func(x2) < 0:
                x0 = x2
            x2 = (x0 + x1) / 2
        return x2


# Пример использования:
epsilon = 0.01
x0 = 0
x1 = 1.5


def func(x):
    return (x - 1) * (x - 2) * (x - 3)


root = find_root(func, x0, x1, epsilon)
if root is not None:
    print("Корень =", root)
else:
    print("Невозможно найти корень в заданном интервале.")
