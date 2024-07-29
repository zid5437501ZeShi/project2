import pandas as pd

# Load the CSV file
vol_ret_mrg_df = pd.read_csv('/project2/Vol_Ret_mrg_df.csv')

# Convert the Year_Month column to datetime format
vol_ret_mrg_df['Year_Month'] = pd.to_datetime(vol_ret_mrg_df['Year_Month'], format='%Y-%m').dt.to_period('M')

# Filter for the year 2008
df_2008 = vol_ret_mrg_df[vol_ret_mrg_df['Year_Month'].dt.year == 2008]

# Extract the volatility data for V for 2008
v_vol_2008 = df_2008['v_vol']

# Calculate the average monthly total volatility for V for the year 2008
v_avg_monthly_vol_2008 = v_vol_2008.mean()

# Filter for the year 2018
df_2018 = vol_ret_mrg_df[vol_ret_mrg_df['Year_Month'].dt.year == 2018]

# Extract the volatility data for V for 2018
v_vol_2018 = df_2018['v_vol']

# Calculate the average monthly total volatility for V for the year 2018
v_avg_monthly_vol_2018 = v_vol_2018.mean()

# Calculate the ratio of the average volatility in 2008 to that in 2018
volatility_ratio = v_avg_monthly_vol_2008 / v_avg_monthly_vol_2018

# Round the ratio to 1 decimal place
volatility_ratio_rounded = round(volatility_ratio, 1)

# Print the result
print(f"The ratio of the average monthly total volatility for stock 'V' in 2008 to that in 2018 is {volatility_ratio_rounded}.")

# Set the Q6_ANSWER
Q6_ANSWER = volatility_ratio_rounded
Q6_ANSWER
