import math


def input_function(x):
    return math.log(x) + math.sin(x / 4)


def input_function_derivative(x):
    return 1 / x + 1 / 4 * math.cos(x / 4)


def main(fn, x_range, step):
    eps = 0.00001

    a = x_range[0]
    b = x_range[0] + step

    if math.fabs(fn(b)) > math.fabs(fn(a)) and fn(a) * fn(b) > 0:
        step = -step
    b = a + step

    while fn(a) * fn(b) > 0:
        a = b
        b = a + step

    x = (a + b) / 2

    while math.fabs(fn(x)) < eps:
        if fn(x) * fn(a) > 0:
            a = x
        else:
            b = x
        x = (a + b) / 2

    return x


if __name__ == '__main__':
    x_range = (0.1, 3)
    h = 0.001

    root = main(input_function, x_range, h)
    print(root)
    print(input_function(root))
