import pandas as pd
import shutil

import lib_csv
import lib_nlp
import lib_util

_cs = lib_nlp.cosine_sim

# Find terminal size
w_, _ = shutil.get_terminal_size((80, 20))

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

    for i in range(1, len(df)):
        if scores[i] > 0.3:
            print(f'Similiarity score: {scores[i]:.3f}\n')
            lib_util.print_row(df.iloc[i])
            print('=' * w_, '\n')

# TODO: Input solution as argument
if __name__ == '__main__':
    # solution = 'a greater increase in pCH4 is required for the same radiative forcing when the pCH4 is higher' # a4_q3
    # solution = 'larger in Central Asia because there is more solar radiation closer to the equator, so changing the ice area by in Central Asia will reflect more radiation than changing the ice area by in Antarctica' # a4_q9_1
    # solution = ' larger in Central Asia because Central Asia is warmer and more variable ice cover than Antarctica, which is permanently frozen' # a4_q9_2
    # solution = 'Heat transport by the Hadley Circulation and ocean currents prevents the temperature of the equatorial Pacific from increasing without limit' # a4_q10
    solution = 'the time scale of change more closely matches funding cycles and human lifetimes'
    check_sol(solution)