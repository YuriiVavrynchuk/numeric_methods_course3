import math
import numpy as np


def main() -> None:
    """
    Main script with the algorithm step-by-step implementation
    """

    x_initial = np.array([1, 1])

    x_old = x_initial.copy()
    relative_percentage_deviation = 1e-5

    jacoby_matrix = calculate_jacoby_matrix(x_initial)
    inverse_jacoby_matrix = inverse_matrix(jacoby_matrix)

    function_vector = get_function_vector(x_initial)
    x = x_initial - np.matmul(inverse_jacoby_matrix, function_vector)

    while not get_convergence_state(x, x_old, relative_percentage_deviation):
        function_vector = get_function_vector(x)
        x_old = x
        x = x_old - np.matmul(inverse_jacoby_matrix, function_vector)

    print(f"Solutions are: {x}")
    print(f"First equation value: {function1(x)}")
    print(f"Second equation value: {function2(x)}")


def get_convergence_state(x: np.ndarray, x_old: np.ndarray, relative_percentage_deviation: float) -> bool:
    """
    :param x: current X-vector values
    :param x_old: previous X-vector values
    :param relative_percentage_deviation: relative percentage deviation
    :return: statement which describes convergence truth
    """

    convergence_state = True

    for x_element, x_old_element in zip(x, x_old):
        if abs((x_element - x_old_element) / x_element) * 100 < relative_percentage_deviation:
            continue
        else:
            convergence_state = False

    return convergence_state


def inverse_matrix(matrix: np.ndarray) -> np.ndarray:
    """
    :param matrix: input matrix
    :return: inverted matrix
    """

    matrix_copy = matrix.copy()
    e_matrix = np.eye(len(matrix_copy))

    # Forward operation.
    for i in range(len(matrix_copy)):

        # Swap columns with max main element.
        max_coefficient = np.argmax(matrix_copy[i][i:])
        matrix_copy[:, [i, max_coefficient + i]] = matrix_copy[:, [max_coefficient + i, i]]
        e_matrix[:, [i, max_coefficient + i]] = e_matrix[:, [max_coefficient + i, i]]
        e_matrix[i] = e_matrix[i] / matrix_copy[i][i]
        matrix_copy[i] = matrix_copy[i] / matrix_copy[i][i]

        for j in range(i + 1, len(matrix_copy)):
            first_element_divider = matrix_copy[j][i]
            e_matrix[j] = e_matrix[j] - (e_matrix[i] * first_element_divider)
            matrix_copy[j] = matrix_copy[j] - (matrix_copy[i] * first_element_divider)

    # Backward operation.
    for i in reversed(range(len(matrix_copy))):

        e_matrix[i] = e_matrix[i] / matrix_copy[i][i]
        matrix_copy[i] = matrix_copy[i] / matrix_copy[i][i]

        for j in reversed(range(0, i)):
            first_element_divider = matrix_copy[j][i]
            e_matrix[j] = e_matrix[j] - (e_matrix[i] * first_element_divider)
            matrix_copy[j] = matrix_copy[j] - (matrix_copy[i] * first_element_divider)

    return e_matrix


def get_function_vector(arguments: np.ndarray) -> np.ndarray:
    """
    :param arguments: input arguments vector
    :return: output results vector
    """

    return np.array([function1(arguments), function2(arguments)])


def function1(arguments: np.ndarray) -> float:
    """
    :param arguments: input arguments vector
    :return: output result value
    """

    x1 = arguments[0]
    x2 = arguments[1]

    return math.pow(math.pow(x1, 2) - math.pow(x2, 2), 2) / 4 - math.pow(x1 * x2, 2) + 0.5 - x1


def function2(arguments: np.ndarray) -> float:
    """
    :param arguments: input arguments vector
    :return: output result value
    """

    x1 = arguments[0]
    x2 = arguments[1]

    return x1 * x2 * (math.pow(x1, 2) - math.pow(x2, 2)) + 0.5 - x2


def calculate_jacoby_matrix(arguments: np.ndarray) -> np.ndarray:
    """
    :param arguments: input arguments vector
    :return: output jacoby matrix(according to the function1 and function2 equations)
    """

    x1 = arguments[0]
    x2 = arguments[1]
    element_0_0 = math.pow(x1, 3) - 3 * x1 * math.pow(x2, 2) - 1
    element_0_1 = math.pow(x2, 3) - 3 * math.pow(x1, 2) * x2
    element_1_0 = 3 * math.pow(x1, 2) * x2 - math.pow(x2, 3)
    element_1_1 = math.pow(x1, 3) - 3 * x1 * math.pow(x2, 2) - 1
    return np.array([[element_0_0, element_0_1], [element_1_0, element_1_1]])


if __name__ == '__main__':
    main()
