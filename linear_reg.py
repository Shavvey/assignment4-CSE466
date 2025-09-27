from util import Point


class LinearReg:
    """Class that represents a linear regression of a dataset"""

    m: float
    b: float

    def __init__(self, m: float, b: float):
        """Create linear regression model given slope (`m`) and y-int (`b`)"""
        self.m = m
        self.b = b

    def predict(self, x: float) -> float:
        """Get prediction from given x value"""
        return (self.m * x) + self.b

    def mse(self, points: list[Point]) -> float:
        """Return the mean-square-error (mse) given x-y points"""
        error = 0.00
        for point in points:
            pred = self.predict(point.x)
            actual = point.y
            error += (actual - pred) ** 2
        # normalize error based on number of points
        n = len(points)
        error /= n
        return error
