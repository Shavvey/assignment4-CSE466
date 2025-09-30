from matplotlib import pyplot as plt
import util as util
import numpy as np

def plot_points(file: str):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # get the points from the file
    points = util.get_points(file)
    xs = [p.x for p in points]
    ys = [p.y for p in points]
    ax.scatter(xs, ys, color='g')
    m,b =  np.polyfit(xs, ys, 1)
    lys = [m*x + b for x in xs]
    ax.plot(xs, lys, 'k--')
    ax.set_title(f"Dataset with m = {m:.2f} and b = {b:.2f} fitted line")
    plt.show()
