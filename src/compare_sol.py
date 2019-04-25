import pandas as pd
import numpy as np

import lib_csv
import lib_nlp
import lib_util

_cs = lib_nlp.cosine_sim

# Find terminal size
w_, _ = lib_util.get_terminal_size()

def compare_sol():
    df = lib_csv.read_csv('../data/test.csv')
    df.columns = ['name', 'id', 'answer']
    
    scores = _cs(df.answer)
    im_ = np.identity(len(df))

    # Ignore identity matrix and search
    scores[im_ == 1] = 0
    x, y = np.where(scores > 0.5)

    # Remove mirrored pairs
    _df = pd.DataFrame({'x':x, 'y':y})
    _df = pd.DataFrame(np.sort(_df, axis=1), columns=['x', 'y'])
    _df = lib_util.reset_index(_df.drop_duplicates())

    x, y = _df.values.T

    for i in range(len(x)):
        print(f'Similiarity score: {scores[x[i], y[i]]:.3f}\n')

        lib_util.print_row(df.iloc[x[i]])
        lib_util.print_row(df.iloc[y[i]])
        
        print('=' * w_, '\n')

    print(f"Found {len(x)} (possible) cases")

# TODO: Input solution as argument
if __name__ == '__main__':
    compare_sol()