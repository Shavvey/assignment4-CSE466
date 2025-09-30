from util import Point


class QuadReg:
    """Model to represent a quadractic regression"""

    a: float
    b: float
    c: float

    def __init__(self, a: float, b: float, c: float):
        """Create quadractic regression models given `(a,b,c)` coefficients"""
        self.a = a
        self.b = b
        self.c = c

    def predict(self, x: float) -> float:
        """Get prediction for given quadractic regression model"""
        return self.a * (x**2) + self.b * (x) + self.c

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
