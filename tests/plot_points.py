from matplotlib import pyplot as plt
import util as util
import numpy as np


def plot_points_lr(file: str):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # get the points from the file
    points = util.get_points(file)
    # sort the points in ascending order of x-coord
    points = sorted(points, key = lambda p : p.x)
    xs = [p.x for p in points]
    ys = [p.y for p in points]
    ax.scatter(xs, ys, color="g")
    m, b = np.polyfit(xs, ys, 1)
    lys = [m * x + b for x in xs]
    ax.plot(xs, lys, "k--")
    ax.set_title(f"Dataset with m = {m:.2f} and b = {b:.2f} fitted line")
    plt.show()


def plot_points_qr(file: str):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # get the points from the file
    points = util.get_points(file)
    # sort the points in ascending order of x-coord
    points = sorted(points, key = lambda p : p.x)
    xs = [p.x for p in points]
    ys = [p.y for p in points]

    ax.scatter(xs, ys, color="g")
    a, b, c = np.polyfit(xs, ys, 2)
    lys = [(a * (x**2) + b * x + c) for x in xs]
    ax.plot(xs, lys)
    ax.set_title(f"Dataset with a={a:.2f}, b={b:.2f}, c={c:.2f} fitted line")
    plt.show()
