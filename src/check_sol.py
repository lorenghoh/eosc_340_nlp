import pandas as pd
import numpy as np

import lib_csv
import lib_nlp
import lib_util

_cs = lib_nlp.cosine_sim

# Find terminal size
w_, _ = lib_util.get_terminal_size()

def check_sol(sol):
    df = lib_csv.read_csv('../data/a1_q8.csv')
    df.columns = ['name', 'id', 'answer']
    
    sol_col = pd.DataFrame({
                    'name': ['Solution'], 
                    'id':[f'{0:08d}'], 
                    'answer':[sol]
                })
    df = pd.concat([sol_col, df], ignore_index=True)
    scores = _cs(df.answer)[0]
    scores[0] = 0 # Ignore solution
    x = np.where(scores > 0.3)[0]
    
    for i in range(len(x)):
        print(f"Similiarity score: {scores[x[i]]:.3f}\n")
        lib_util.print_row(df.iloc[x[i]])
        print('=' * w_, '\n')
    print(f"Found {len(x)} (possible) cases")

# TODO: Input solution as argument
if __name__ == '__main__':
    # solution = 'a greater increase in pCH4 is required for the same radiative forcing when the pCH4 is higher' # a4_q3
    # solution = 'larger in Central Asia because there is more solar radiation closer to the equator, so changing the ice area by in Central Asia will reflect more radiation than changing the ice area by in Antarctica' # a4_q9_1
    # solution = ' larger in Central Asia because Central Asia is warmer and more variable ice cover than Antarctica, which is permanently frozen' # a4_q9_2
    # solution = 'Heat transport by the Hadley Circulation and ocean currents prevents the temperature of the equatorial Pacific from increasing without limit' # a4_q10
    solution = 'The semi-empirical approach estimates future sea level rise based on historical relationships between sea level rise, temperature, and radiative forcing, making an assumption that these relationships can be extrapolated into the future. model the various physical processes that cause sea level to rise and add them up'
    check_sol(solution)