import numpy as np

def gauss_elimination(matrix):
    for i in range(len(matrix)):
        max_index = max(range(i, len(matrix)), key=lambda x: abs(matrix[x][i]))
        matrix[i], matrix[max_index] = matrix[max_index], matrix[i]
        matrix[i] = [elem / matrix[i][i] for elem in matrix[i]]

        for j in range(i + 1, len(matrix)):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, len(matrix) + 1):
                matrix[j][k] -= factor * matrix[i][k]

        print(f"\nMatrix after {i + 1}-th step:")
        for row in matrix:
            print(row)

    solutions = np.zeros(len(matrix))
    for i in range(len(matrix) - 1, -1, -1):
        solutions[i] = ((matrix[i][-1] - np.dot(matrix[i][:-1], solutions)) / matrix[i][i])

    return solutions


augmented_matrix = [[-3, 2.099, 6, 3.901],
                   [10, -7, 1, 7],
                   [5, -1, 5, 6]]

result = gauss_elimination(augmented_matrix)

print("\nSolutions")

for x_index in range(len(result)):
    print(f"x{x_index+1} = {result[x_index]}")
