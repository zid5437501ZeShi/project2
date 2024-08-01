import pandas as pd

# Load the CSV file
vol_ret_mrg_df = pd.read_csv('Vol_Ret_mrg_df.csv')

# Convert the Year_Month column to datetime format
vol_ret_mrg_df['Year_Month'] = pd.to_datetime(vol_ret_mrg_df['Year_Month'], format='%Y-%m').dt.to_period('M')

# Filter for the year 2010
df_2010 = vol_ret_mrg_df[vol_ret_mrg_df['Year_Month'].dt.year == 2010]

# Extract the volatility data for TSLA
tsla_vol_2010 = df_2010['tsla_vol']

# Calculate the average monthly total volatility for TSLA for the year 2010
tsla_avg_monthly_vol_2010 = tsla_vol_2010.mean()

# Print the result
print(f"The average monthly total volatility for TSLA in 2010 is {tsla_avg_monthly_vol_2010}.")

# Set the Q5_ANSWER
Q5_ANSWER = tsla_avg_monthly_vol_2010
Q5_ANSWER
