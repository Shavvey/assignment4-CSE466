import pandas as pd
from pandas.core.api import DataFrame

DATA_FILES = ["data/table1.html", "data/table2.html"]


def get_table(file: str) -> DataFrame:
    table = pd.read_html(file)
    # NOTE: we only expect one table per file
    # which is why we're just returning the first dataframe
    return table[0]


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


def get_points(file: str) -> list[Point]:
    table = get_table(file)
    points: list[Point] = []
    for _, row in table.iterrows():
        point = Point(row.at[0], row.at[1])
        points.append(point)
    return points
