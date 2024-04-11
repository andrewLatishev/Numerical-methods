import numpy as np

def solve_system(matrix):
    for i in range(len(matrix)):
        matrix[i] = [elem / matrix[i][i] for elem in matrix[i]]
        for j in range(i + 1, len(matrix)):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, len(matrix) + 1):
                matrix[j][k] -= factor * matrix[i][k]

    solutions = np.zeros(len(matrix))
    for i in range(len(matrix) - 1, -1, -1):
        solutions[i] = (matrix[i][-1] - np.dot(matrix[i][:-1], solutions)) / matrix[i][i]

    return solutions

augmented_matrix = [[2, 1, 4, 16],
                    [3, 2, 1, 10],
                    [1, 3, 3, 16]]

solution = solve_system(augmented_matrix)

print("\nSolutions:")
for index, value in enumerate(solution):
    print(f"x{index+1} = {value}")
