import numpy as np


def main():
    coefficients = np.loadtxt("data/coefficients.txt", dtype=float, delimiter=" ")
    solutions = np.loadtxt("data/solutions.txt", dtype=float, delimiter=" ")

    coefficients_copy = coefficients.copy()
    solutions_copy = solutions.copy()

    if len(coefficients) != len(solutions):
        raise Exception("Equations and solutions have different sizes.")

    if coefficients.shape[1] > solutions.shape[0]:
        raise Exception("Unknowns number is more than solution number.\n"
                        "System cannot be resolved!")

    unordered_roots = [0 for _ in range(coefficients.shape[1])]
    roots_number = len(unordered_roots)
    order = np.arange(0, roots_number)

    # Algorithm implementation.

    # Forward operation.
    for i in range(len(coefficients)):

        # Swap columns with max main element.
        max_coefficient = np.argmax(coefficients[i][i:])
        coefficients[:, [i, max_coefficient + i]] = coefficients[:, [max_coefficient + i, i]]
        order[i], order[max_coefficient + i] = order[max_coefficient + i], order[i]

        try:
            solutions[i] = solutions[i] / coefficients[i][i]
            coefficients[i] = coefficients[i] / coefficients[i][i]
        except ZeroDivisionError:
            if solutions[i] == 0:
                np.delete(coefficients, i, axis=0)
            else:
                raise Exception("System has no roots!")

        for j in range(i + 1, len(coefficients)):
            first_element_divider = coefficients[j][i]
            coefficients[j] = coefficients[j] - (coefficients[i] * first_element_divider)
            solutions[j] = solutions[j] - (solutions[i] * first_element_divider)

    # Backward operation.
    unordered_roots[roots_number - 1] = solutions[roots_number - 1] / coefficients[roots_number - 1][roots_number - 1]
    for i in reversed(range(roots_number - 1)):
        unordered_roots[i] = (
                solutions[i] - np.sum([unordered_roots[j] * coefficients[i][j] for j in range(i, roots_number)]))

    ordered_roots = [0 for _ in range(coefficients.shape[1])]
    for i in range(len(unordered_roots)):
        ordered_roots[order[i]] = unordered_roots[i]

    # Validation.
    resulting_solutions = np.matmul(coefficients_copy, ordered_roots)

    print("Roots are:")
    print(ordered_roots)

    print("Input solutions was:")
    print(solutions_copy)

    print("Resulting solutions are:")
    print(resulting_solutions)

    print("Average deviation:")
    differences = np.subtract(resulting_solutions, solutions_copy)
    print(np.std(differences))


if __name__ == '__main__':
    main()
