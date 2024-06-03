import pandas as pd

def get_col(filename:str, colname:str):
    df = pd.read_csv(filename)
    col_data = df[colname]
    return col_data


