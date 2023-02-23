from __init__ import *
np.set_printoptions(precision = 7, suppress = True, linewidth = 100)

def neville(x, y, x_test):
    size = len(x)
    neville_matrix = np.zeros((size, size), dtype = float)
    for index in range(size):
        neville_matrix[index][0] = y[index]
    for i in range(1, size):
        for j in range(1, size):
            first_mult = (x_test - x[i - j]) * neville_matrix[i][j - 1]
            second_mult = (x_test - x[i]) * neville_matrix[i - 1][j - 1]
            denominator = x[i] - x[i - 1]
            coeff = (first_mult - second_mult) / denominator
            neville_matrix[i][j] = coeff
    return neville_matrix[1][1]

def newton_forward(x, y):
    size = len(x)
    newton_matrix = np.zeros((size, size), dtype = float)
    for index in range(size):
        newton_matrix[index][0] = y[index]
    for i in range(1, size):
        for j in range(1, size):
            numerator = newton_matrix[i][j - 1] - newton_matrix[i - 1][j - 1]
            denominator = x[i] - x[i - j]
            fraction = numerator / denominator
            newton_matrix[i][j] = fraction
    global div_diff_1, div_diff_2, div_diff_3
    div_diff_1 = newton_matrix[1][1]
    div_diff_2 = newton_matrix[2][2]
    div_diff_3 = newton_matrix[3][3]
    print("[", end = "")
    print(newton_matrix[1][1], end = ", ")
    print(newton_matrix[2][2], end = ", ")
    print(newton_matrix[3][3], end = "]\n")

def question_3(x, y, x_test):
    result = y[0] + div_diff_1 * (x_test - x[0]) + div_diff_2 * (x_test - x[1]) * (x_test - x[0]) + div_diff_3 * (x_test - x[2]) * (x_test - x[1]) * (x_test - x[0])
    print(result)

def divided_difference(matrix: np.array):
    for i in range(2, len(matrix)):
        for j in range(2, i + 2):
            if (j >= len(matrix[i])) or (matrix[i][j] != 0):
                continue
            numerator = matrix[i][j - 1] - matrix[i - 1][j - 1]
            denominator = matrix[i][0] - matrix[i - j + 1][0]
            fraction = numerator / denominator
            matrix[i][j] = fraction
    return matrix

def hermite(x, y, dy):
    size = len(x)
    hermite_matrix = np.zeros((size * 2, size * 2))
    index = 0
    for i in range(0, size * 2, 2):
        hermite_matrix[i][0] = x[index]
        hermite_matrix[i + 1][0] = x[index]
        index += 1
    index = 0
    for i in range(0, size * 2, 2):
        hermite_matrix[i][1] = y[index]
        hermite_matrix[i + 1][1] = y[index]
        index += 1
    index = 0
    for i in range(1, size * 2, 2):
        hermite_matrix[i][2] = dy[index]
        index += 1
    hermite_matrix = divided_difference(hermite_matrix)
    print(hermite_matrix)


def cubic_spline_interpolation(x, y):
    size = len(x)
    A = np.zeros((size, size), dtype = float)
    A[0][0] = 1
    A[size - 1][size - 1] = 1
    for i in range(1, size - 1):
        A[i][i - 1] = x[i] - x[i - 1]
        A[i][i] = 2 * (x[i + 1] - x[i - 1])
        A[i][i + 1] = x[i + 1] - x[i]
    print(A)
    print()

    b = np.zeros(size)
    for i in range(1, size - 1):
        b[i] = (3 * (y[i + 1] - y[i]) / (x[i + 1] - x[i])) - (3 * (y[i] - y[i - 1]) / (x[i] - x[i - 1]))
    print(b)
    print()

    x = np.linalg.solve(A, b)
    print(x)

x_1 = [3.6, 3.8, 3.9]
y_1 = [1.675, 1.436, 1.318]
x_test_1 = 3.7
print(neville(x_1, y_1, x_test_1))
print()

x_2 = [7.2, 7.4, 7.5, 7.6]
y_2 = [23.5492, 25.3913, 26.8224, 27.4589]
newton_forward(x_2, y_2)
print()

question_3(x_2, y_2, 7.3)
print()

x_4 = [3.6, 3.8, 3.9]
y_4 = [1.675, 1.436, 1.318]
dy_4 = [-1.195, -1.188, -1.182]
hermite(x_4, y_4, dy_4)
print()

x_5 = [2, 5, 8, 10]
y_5 = [3, 5, 7, 9]
cubic_spline_interpolation(x_5, y_5)