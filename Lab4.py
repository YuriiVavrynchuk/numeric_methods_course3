import math
from typing import Callable


def main() -> None:
    """
    Main script with the algorithm step-by-step implementation
    """
    integration_ranges = (0, 1)
    number_of_divisions = 30
    print(f"Trapeze integral:{get_trapeze_integral(integration_ranges, function, number_of_divisions)}")
    print(f"Analytics integral:{get_analytics_integral(integration_ranges, primary_function)}")
    pass


def get_analytics_integral(integration_ranges: tuple, primary: Callable) -> float:
    """
    Returns analytics integral in the certain ranges
    :param integration_ranges: ranges where analytics integral is being to be calculated
    :param primary: primary function for analytics integral calculation
    :return: value of analytics integral
    """
    a = integration_ranges[0]
    b = integration_ranges[1]
    return primary(b) - primary(a)


def get_trapeze_integral(integration_ranges: tuple, function_to_integrate: Callable, divisions_number: int) -> float:
    """
    Returns trapeze integral in the certain ranges
    :param integration_ranges: ranges where trapeze integral is being to be calculated
    :param function_to_integrate: function to calculate
    :param divisions_number: number of divisions for trapeze method
    :return: value of trapeze integral
    """
    a = integration_ranges[0]
    b = integration_ranges[1]

    integral_sum = 0
    integration_step = (b - a) / divisions_number

    fa = function_to_integrate(a)
    fb = function_to_integrate(b)

    x = a + integration_step

    for _ in range(divisions_number - 1):
        integral_sum += function_to_integrate(x)
        x += integration_step

    return integration_step * ((fa + fb) / 2 + integral_sum)


def function(x: float) -> float:
    """
    Returns function value according to the argument
    :param x: argument
    :return: function value
    """
    return 1 / (4 + math.pow(x, 2))


def primary_function(x: float) -> float:
    """
    Returns primary function for the integral calculation
    :param x: argument
    :return: primary value
    """
    return 0.5 * math.atan(x / 2)


if __name__ == '__main__':
    main()
