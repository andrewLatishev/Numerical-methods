def calculate_max_limit(an: float, a: float) -> float:
    return 1 + a / abs(an)


def calculate_min_limit(a0: float, b: float) -> float:
    return 1 / (1 + b / abs(a0))


def theorem3(numbers: list) -> tuple[float, float]:
    absolute_numbers = []

    for number in numbers:
        absolute_numbers.append(abs(number))

    return (calculate_min_limit(absolute_numbers[-1], max(absolute_numbers[0:-1])),
            calculate_max_limit(absolute_numbers[0], max(absolute_numbers[1:-1])))


root_limits = theorem3([1, 2, -5, 8, -7, -3])

print(f"{root_limits[0]} < |root| <= {root_limits[1]}")
