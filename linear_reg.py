from util import Point


class LinerReg:
    """Class that represents a linear regression of a dataset"""

    m: float
    b: float

    def __init__(self, m: float, b: float):
        """Create linear regression model given slope (`m`) and y-int (`b`)"""
        self.m = m
        self.b = b

    def mse(self, points: list[Point]) -> float:
        """Return the mean-square-error (mse) given x-y points in `df`"""
        return 0
