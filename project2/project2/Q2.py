import pandas as pd

# Load the CSV file
dm_ret_dict_df = pd.read_csv('DM_Ret_dict.csv')

# Convert the Date column to datetime format
dm_ret_dict_df['Date'] = pd.to_datetime(dm_ret_dict_df['Date'])

# Filter for the year 2008
df_2008 = dm_ret_dict_df[dm_ret_dict_df['Date'].dt.year == 2008]

# Extract the returns for NVDA
nvda_returns_2008 = df_2008['nvda']

# Calculate the average daily return for NVDA for the year 2008
nvda_avg_daily_return_2008 = nvda_returns_2008.mean()

# Set the Q2_ANSWER
Q2_ANSWER = nvda_avg_daily_return_2008
print(f"The average daily return for NVDA in 2008 is {Q2_ANSWER}.")
