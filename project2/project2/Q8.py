import pandas as pd

ew_ls_pf_df = pd.read_csv('EW_LS_pf_df.csv')

rows, columns = ew_ls_pf_df.shape

print(f'{rows}rows,{columns}columns')
