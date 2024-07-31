import pandas as pd

ew_ls_pf_df = pd.read_csv('EW_LS_pf_df.csv')

def get_cumulative_ret(df):

    df = df.apply(pd.to_numeric, errors='coerce')

    df = df.sort_index()
    df = df.add(1)
    df = df.cumprod()
    df = df - 1
    return df

cumulative_return = get_cumulative_ret(ew_ls_pf_df)

ls_cumulative_return = cumulative_return['ls'].iloc[-1]

print(f'The cumulative portfolio return of the total volatility long-short portfolio over the whole sample period: {ls_cumulative_return}')

#test