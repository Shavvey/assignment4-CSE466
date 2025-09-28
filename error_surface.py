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
    for i, m in enumerate(ms):
        for j, b in enumerate(bs):
            lr = LinearReg(m ,b)
            mse = lr.mse(points)
            Z[i][j] = mse
    surf = ax.plot_surface(X, Y, Z, cmap=cm.get_cmap("coolwarm"))
    m = LinearReg(-10,10)
    print(m.mse(points))
    plt.show()
