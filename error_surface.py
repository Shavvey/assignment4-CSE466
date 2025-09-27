import matplotlib as mp
from linear_reg import LinearReg
import util as util
import numpy as np
import numpy.typing as npt


def plot_mse(file: str):
    """Given list of points from file (`data/table1.html` for example), 
    get surface plot of mse"""
    # 100 different potential slopes
    ms = np.linspace(-4, 4, 100)
    # 100 different potential y-ints
    bs = np.linspace(-4, 4, 100)
    models: list[LinearReg] = []
    # create all potential linear regression models
    for i in enumerate(ms):
        lr = LinearReg(ms[i], bs[i])
        models.append(lr)
    points = util.get_points(file)
    errors = np.array([], dtype=np.float32)
     
    
