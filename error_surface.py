import matplotlib.pyplot as plt
from linear_reg import LinearReg
import util as util
import numpy as np
from matplotlib import cm


def plot_mse(file: str, samples: int, interval: tuple[int, int]):
    """Given list of points from file (`data/table1.html` for example),
    get surface plot of mse"""
    ms = np.linspace(interval[0], interval[1], samples)
    bs = np.linspace(interval[0], interval[1], samples)
    points = util.get_points(file)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    # create 2D mesh given our sampling points
    X, Y = np.meshgrid(ms, bs)
    Z = np.empty((samples, samples))
    min = [X[0], Y[0], 1 << 32]
    for i, m in enumerate(ms):
        for j, b in enumerate(bs):
            lr = LinearReg(m, b)
            mse = lr.mse(points)
            error = 20 * np.log10(mse)
            if min[2] > error:
                min[0] = m
                min[1] = b
                min[2] = error
            Z[j][i] = error
    print(min)
    surf = ax.plot_surface(X, Y, Z, cmap=cm.get_cmap("coolwarm"))
    print(LinearReg(7.7,-3.5).mse(points))
    ax.set_xlabel("Slope (m)")
    ax.set_ylabel("Y-intercept (b)")
    ax.set_zlabel("Error (mse)")
    plt.show()
