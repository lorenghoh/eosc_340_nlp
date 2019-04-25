'''
Assume the following convention:
    0: Name
    1: Student ID
    2: Answers

and merge rest of the columns
'''

import pandas as pd
import pyarrow.parquet as pq

def read_csv(file_name):
    df = pd.read_csv(
            file_name,
            skiprows=1,
            header=None,
        )

    for item in df.columns[3:]:
        df[2] = df[2] + df[item]
        df = df.drop(columns=item)
    df = df.dropna().reset_index()
    return df.drop('index', axis='columns')

def read_df():
    pass

def write_df():
    pass

if __name__ == '__main__':
    read_csv('../data/a1_q8.csv')