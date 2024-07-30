import pandas as pd

ew_ls_pf_df = pd.read_csv('EW_LS_pf_df.csv')

def get_avg(df: pd.DataFrame, year):
    df['Year_Month'] = pd.to_datetime(df['Year_Month'], format='%Y-%m')
    df = df.set_index('Year_Month')
    df_year = df[df.index.year == year]
    avg_series = df_year.mean()
    return avg_series

avg_return_2019 = get_avg(ew_ls_pf_df, 2019)

lowest_volatility_quantile_avg_return = avg_return_2019.idxmin()

print(f'The average equal weighted portfolio return of the quantile with the lowest total volatility in 2019: {avg_return_2019[lowest_volatility_quantile_avg_return]}')

