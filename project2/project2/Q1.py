import pandas as pd

# Load the CSV file
dm_ret_dict_df = pd.read_csv('DM_Ret_dict.csv')

# Convert the Date column to datetime format
dm_ret_dict_df['Date'] = pd.to_datetime(dm_ret_dict_df['Date'])

# Filter for the year 2008
df_2008 = dm_ret_dict_df[dm_ret_dict_df['Date'].dt.year == 2008]

# Drop the Date column for easier aggregation
df_2008 = df_2008.drop(columns=['Date'])

# Calculate the average daily return for each stock
avg_daily_returns_2008 = df_2008.mean()

# Find the stock with the lowest average daily return
lowest_avg_return_stock = avg_daily_returns_2008.idxmin()
lowest_avg_return_value = avg_daily_returns_2008.min()

# Print the result
print(f"The stock with the lowest average daily return in 2008 is {lowest_avg_return_stock} with an average return of {lowest_avg_return_value}.")

# Set the Q1_ANSWER
Q1_ANSWER = lowest_avg_return_stock
Q1_ANSWER

11111222223333factset

