import matplotlib.pyplot as plt
import numpy as np


def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


def median_filter(x, k=3):
    k2 = (k - 1) // 2
    y = np.zeros((len(x), k), dtype=x.dtype)
    y[:, k2] = x
    for i in range(k2):
        j = k2 - i
        y[j:, i] = x[:-j]
        y[:j, i] = x[0]
        y[:-j, -(i + 1)] = x[j:]
        y[-j:, -(i + 1)] = x[-1]
    return np.median(y, axis=1)


xaxis = np.arange(0.0, 200.0, 1)
wave = np.array(list(map(lambda t: 2 * np.sin(2 * np.pi * t / 50 + .6 * np.pi), xaxis)))

plt.plot(xaxis, wave)
plt.show()


def gauss_dist():
    noise = np.random.normal(0, 1, 200)

    plt.plot(xaxis, wave + noise)
    plt.title("Gauss")
    plt.show()

    plt.plot(xaxis[1:199], moving_average(wave + noise))
    plt.title("Gauss + Moving average")
    plt.show()

    plt.plot(xaxis, median_filter(wave + noise))
    plt.title("Gauss + Median filter")
    plt.show()


def uniform_dist():
    noise = np.random.uniform(0, 1, 200)
    plt.plot(xaxis, wave + noise)
    plt.title("Uniform dist")
    plt.show()

    plt.plot(xaxis[1:199], moving_average(wave + noise))
    plt.title("Uniform dist + Moving average")
    plt.show()

    plt.plot(xaxis, median_filter(wave + noise))
    plt.title("Uniform dist + Median filter")
    plt.show()


def salt_and_pepper():
    noise = np.random.choice([-1, 0, 1], 200, p=[0.05, 0.9, 0.05])

    plt.plot(xaxis, wave + noise)
    plt.title("Salt & Pepper")
    plt.show()

    plt.plot(xaxis[1:199], moving_average(wave + noise))
    plt.title("Salt & Pepper + Moving average")
    plt.show()

    plt.plot(xaxis, median_filter(wave + noise))
    plt.title("Salt & Pepper + Median filter")
    plt.show()

gauss_dist()
uniform_dist()
salt_and_pepper()