import pandas as pd
from pandas.core.api import DataFrame

DATA_FILES = ["data/table1.html", "data/table2.html"]


def get_table(file: str) -> DataFrame:
    table = pd.read_html(file)
    # NOTE: we only expect one table per file
    # which is why we're just returning the first dataframe
    return table[0]
