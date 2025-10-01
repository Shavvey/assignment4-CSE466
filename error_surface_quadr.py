import matplotlib.pyplot as plt
from quad_reg import QuadReg
import util as util
import numpy as np
from matplotlib import cm


def plot_full_mse(file: str, samples: int, interval: tuple[int, int]):
    C = 3
    aas = np.linspace(interval[0], interval[1], samples)
    bs = np.linspace(interval[0], interval[1], samples)
    points = util.get_points(file)
    fig = plt.figure()
    ax1 = fig.add_subplot(121, projection="3d")
    # create 2D mesh given our sampling points
    X, Y = np.meshgrid(aas, bs)
    Z = np.empty((samples, samples))
    min = [X[0], Y[0], 1 << 32]
    for i, a in enumerate(aas):
        for j, b in enumerate(bs):
            qr = QuadReg(a, b, C)
            mse = qr.mse(points)
            error = mse
            # find minimum error among tested models
            if min[2] > error:
                min[0] = a
                min[1] = b
                min[2] = error
            Z[j][i] = error
    print(min)
    ax1.plot_surface(X, Y, Z, cmap=cm.get_cmap("coolwarm"))
    ax1.set_xlabel("Slope (m)")
    ax1.set_ylabel("Y-intercept (b)")
    ax1.set_zlabel("Error (mse)")
    ax2 = fig.add_subplot(122, projection="3d")
    # apply the log-scale
    Z = 10 * np.log10(Z)
    ax2.plot_surface(X, Y, Z, cmap=cm.get_cmap("coolwarm"))
    ax2.set_xlabel("Slope (m)")
    ax2.set_ylabel("Y-intercept (b)")
    ax2.set_zlabel("Error (mse, log scale)")
    plt.show()


def plot_fhalf_mse(file: str, samples: int, interval: tuple[int, int]):
    C = 3
    aas = np.linspace(interval[0], interval[1], samples)
    bs = np.linspace(interval[0], interval[1], samples)
    points = util.get_points(file)
    points = points[0 : len(points) // 2]
    fig = plt.figure()
    ax1 = fig.add_subplot(121, projection="3d")
    # create 2D mesh given our sampling points
    X, Y = np.meshgrid(aas, bs)
    Z = np.empty((samples, samples))
    min = [X[0], Y[0], 1 << 32]
    for i, a in enumerate(aas):
        for j, b in enumerate(bs):
            qr = QuadReg(a, b, C)
            mse = qr.mse(points)
            error = mse
            # find minimum error among tested models
            if min[2] > error:
                min[0] = a
                min[1] = b
                min[2] = error
            Z[j][i] = error
    print(min)
    ax1.plot_surface(X, Y, Z, cmap=cm.get_cmap("coolwarm"))
    ax1.set_xlabel("Slope (m)")
    ax1.set_ylabel("Y-intercept (b)")
    ax1.set_zlabel("Error (mse)")
    ax2 = fig.add_subplot(122, projection="3d")
    # apply the log-scale
    Z = 10 * np.log10(Z)
    ax2.plot_surface(X, Y, Z, cmap=cm.get_cmap("coolwarm"))
    ax2.set_xlabel("Slope (m)")
    ax2.set_ylabel("Y-intercept (b)")
    ax2.set_zlabel("Error (mse, log scale)")
    plt.show()


def plot_lhalf_mse(file: str, samples: int, interval: tuple[int, int]):
    C = 3
    aas = np.linspace(interval[0], interval[1], samples)
    bs = np.linspace(interval[0], interval[1], samples)
    points = util.get_points(file)
    points = points[len(points) // 2:]
    fig = plt.figure()
    ax1 = fig.add_subplot(121, projection="3d")
    # create 2D mesh given our sampling points
    X, Y = np.meshgrid(aas, bs)
    Z = np.empty((samples, samples))
    min = [X[0], Y[0], 1 << 32]
    for i, a in enumerate(aas):
        for j, b in enumerate(bs):
            qr = QuadReg(a, b, C)
            mse = qr.mse(points)
            error = mse
            # find minimum error among tested models
            if min[2] > error:
                min[0] = a
                min[1] = b
                min[2] = error
            Z[j][i] = error
    print(min)
    ax1.plot_surface(X, Y, Z, cmap=cm.get_cmap("coolwarm"))
    ax1.set_xlabel("Slope (m)")
    ax1.set_ylabel("Y-intercept (b)")
    ax1.set_zlabel("Error (mse)")
    ax2 = fig.add_subplot(122, projection="3d")
    # apply the log-scale
    Z = 10 * np.log10(Z)
    ax2.plot_surface(X, Y, Z, cmap=cm.get_cmap("coolwarm"))
    ax2.set_xlabel("Slope (m)")
    ax2.set_ylabel("Y-intercept (b)")
    ax2.set_zlabel("Error (mse, log scale)")
    plt.show()
