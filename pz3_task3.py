import numpy as np


def calculate_theorem4(func: list):
    function = np.array(func)

    if min(function) >= 0 or max(function) <= 0:
        return 'Нельзя применить теорему'

    if function[0] < 0:
        function *= -1

    a_index = 0

    for index, a in enumerate(function, start=1):
        if a < 0:
            a_index = index
            break

    return 1 + float(function[function < 0].min() / -function[0]) ** (1 / (len(function) - 1 - a_index))


def calculate_theorem5(func: list):
    function = np.array(func)
    rn = []
    pn = (function, function[::-1], -function, -function[::-1])

    for p in pn:
        rn.append(calculate_theorem4(p))

    return (-rn[2], -1 / rn[3]), (1 / rn[1], rn[0])


result = calculate_theorem5([1, 2, -5, 8, -7, -3])

print(result)
