from math import sin, pi, pow
import matplotlib.pylab

U_max = 100
f = 50
R1 = 5
R2 = 4
R3 = 7
R4 = 2
C1 = 0.0003
C2 = 0.00015
final_time = 0.2
step = 0.0000001


def u1(t):
    return U_max * sin(2 * pi * f * t)


differential_equations = [
    lambda x, t:
        (1 / C1) * ((R3 * (u1(t) - x[0]) + R2 * (u1(t) - x[0] - x[1])) / (R2 * R3 + R1 * (R2 + R3))),
    lambda x, t:
        (1 / C2) * (((u1(t) - x[0] - x[1]) / R3) - (R1 * R3 * (u1(t) - x[0]) + R1 * R2 * (u1(t) - x[0] - x[1])) /
                    (R2 * pow(R3, 2) + R1 * R3 * (R2 + R3)) - x[1] / R4),
]


def find_plot():
    current_time = 0
    result = []
    x = [0, 0]
    while current_time < final_time:
        previous = []
        for i in range(len(x)):
            previous.append(x[i] + step * differential_equations[i](x, current_time))
        for i in range(len(x)):
            x[i] += step * differential_equations[i](previous, current_time)
        result.append(x[1])
        current_time += step
    return result


def build_graph(times, result):
    matplotlib.pylab.plot(times, result)
    matplotlib.pylab.ylabel('U2')
    matplotlib.pylab.xlabel('current_time')
    matplotlib.pylab.savefig("data/lab5_U2.png")


def main():
    times = [step * i for i in range(int(final_time / step))]
    result = find_plot()
    build_graph(times, result)


if __name__ == '__main__':
    main()
