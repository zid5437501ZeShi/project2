import pandas as pd

vol_ret_mrg_df = pd.read_csv('Vol_Ret_mrg_df.csv')

vol_ret_mrg_df['Year_Month'] = pd.to_datetime(vol_ret_mrg_df['Year_Month'], format='%Y-%m')
tsla_2010_df = vol_ret_mrg_df[vol_ret_mrg_df['Year_Month'].dt.year == 2010]

effective_year_months = tsla_2010_df['tsla'].notnull() & tsla_2010_df['tsla_vol'].notnull()
effective_count = effective_year_months.sum()

print(f'Number of effective year-months for TSLA in 2010: {effective_count}')
