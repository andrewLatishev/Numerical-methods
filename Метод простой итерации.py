import math


def simple_iteration_method(a, x0, eps = 0.1, max_iterations=500):
    x = x0

    for i in range(max_iterations):
        next_x = math.sqrt(a)  # Функция f(x) = sqrt(a)

        # Проверяем условие сходимости
        if abs(next_x - x) < eps:
            return next_x, i + 1  # Возвращаем приближенное решение и количество итераций

        x = next_x

    return None, max_iterations  # Если не удалось достичь сходимости за максимальное количество итераций


# Пример использования
a = 25
x0 = 1.0
solution, iterations = simple_iteration_method(a, x0)
if solution is not None:
    print("Приближенное решение:", solution)
    print("Количество итераций:", iterations)
else:
    print("Метод не сошелся за максимальное количество итераций.")
