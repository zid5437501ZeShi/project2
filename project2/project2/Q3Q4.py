import pandas as pd

# Load the CSV file
vol_ret_mrg_df = pd.read_csv('Vol_Ret_mrg_df.csv')

# Convert the Year_Month column to datetime format
vol_ret_mrg_df['Year_Month'] = pd.to_datetime(vol_ret_mrg_df['Year_Month'], format='%Y-%m').dt.to_period('M')

# Filter for the year 2019
df_2019 = vol_ret_mrg_df[vol_ret_mrg_df['Year_Month'].dt.year == 2019]

# Drop the Year_Month column for easier aggregation
df_2019 = df_2019.drop(columns=['Year_Month'])

# Calculate the average monthly return for each stock
avg_monthly_returns_2019 = df_2019.mean()

# Find the stock with the highest average monthly return
highest_avg_return_stock_2019 = avg_monthly_returns_2019.idxmax()
highest_avg_return_value_2019 = avg_monthly_returns_2019.max()

# Print the result
print(f"The stock with the highest average monthly return in 2019 is {highest_avg_return_stock_2019} with an average return of {highest_avg_return_value_2019}.")

# Set the Q3_ANSWER
Q3_ANSWER = highest_avg_return_stock_2019
Q3_ANSWER
