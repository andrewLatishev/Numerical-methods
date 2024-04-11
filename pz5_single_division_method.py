import numpy as np

def solve_system(matrix):
    for i in range(len(matrix)):
        max_index = max(range(i, len(matrix)), key=lambda x: abs(matrix[x][i]))
        matrix[i], matrix[max_index] = matrix[max_index], matrix[i]

        matrix[i] = [elem / matrix[i][i] for elem in matrix[i]]

        for j in range(i + 1, len(matrix)):
            factor = matrix[j][i] / matrix[i][i]
            matrix[j] = [matrix[j][k] - factor * matrix[i][k] for k in range(len(matrix[i]))]

        print(f"\nMatrix after {i}-th step:")
        for row in matrix:
            print(row)

    solutions = np.zeros(len(matrix))
    for i in range(len(matrix) - 1, -1, -1):
        solutions[i] = ((matrix[i][-1] - np.dot(matrix[i][:-1], solutions)) / matrix[i][i])

    return solutions


augmented_matrix = [[5, 0, 1, 11],
                   [2, 6, -2, 8],
                   [-3, 2, 10, 6]]

result = solve_system(augmented_matrix)

print("\nSolutions")

for x_index in range(len(result)):
    print(f"x{x_index+1} = {result[x_index]}")
