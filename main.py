from pandas import DataFrame
import pandas as pd
import read_tables as rd

def main():
    tables: list[DataFrame] = []
    for file in rd.DATA_FILES:
        table = rd.get_table(file)
        tables.append(table)

    
if __name__ == "__main__":
    main()
