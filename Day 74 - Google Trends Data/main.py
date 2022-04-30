# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-30

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 74 - Google Trends Data

import pandas
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Import data
bitcoin_search_df = pandas.read_csv("data/Bitcoin Search Trend.csv")
bitcoin_search_df.name = "bitcoin_search"
bitcoin_price_df = pandas.read_csv("data/Daily Bitcoin Price.csv")
bitcoin_price_df.name = "bitcoin_price"
tesla_search_df = pandas.read_csv("data/TESLA Search Trend vs Price.csv")
tesla_search_df.name = "tesla_search"
ue_benefit_search_2004_19_df = pandas.read_csv("data/UE Benefits Search vs UE Rate 2004-19.csv")
ue_benefit_search_2004_19_df.name = "ue_benefit_search_2004_19"
ue_benefit_search_2004_20_df = pandas.read_csv("data/UE Benefits Search vs UE Rate 2004-20.csv")
ue_benefit_search_2004_20_df.name = "ue_benefit_search_2004_20"

df_list = [
    bitcoin_search_df,
    bitcoin_price_df,
    tesla_search_df,
    ue_benefit_search_2004_19_df,
    ue_benefit_search_2004_19_df
]

# What are the shapes of the DataFrames?
for i in df_list:
    print("\nShape for " + str(i.name) + ": (rows, columns)")
    print(i.shape)

# How many rows & columns do they have?
# Ditto above

# What are the column names?
for i in df_list:
    print("\nColumns for " + str(i.name) + ":")
    print(i.columns)

# What is the largest number in the search data column? Try using the .describe() function.
# BTC
print("\nLargest number in search data column for Bitcoin:")
print(bitcoin_search_df['BTC_NEWS_SEARCH'].max())

# Tesla
print("\nLargest number in search data column for Tesla:")
print(tesla_search_df['TSLA_WEB_SEARCH'].max())

# What is the periodicity of the time series data (daily, weekly, monthly)?
for i in df_list:
    print("\nPeriodicity for " + str(i.name) + ":")
    print(i.columns[0])

# Can you investigate all 4 DataFrames and find if there are any missing values?
# If yes, find how many missing or NaN values there are. Then, find the row where the missing values occur.

for i in df_list:
    print("\nChecking for missing values in " + str(i.name) + ":")
    print(i.isna().values.any())
    print("Sum: " + str(i.isna().values.sum()))

# Finally, remove any rows that contain missing values.

for i in df_list:
    print("\nDropping rows with missing values in " + str(i.name) + "...")
    i.dropna(inplace=True)

# Convert any strings you find into Datetime objects. Do this for all 4 DataFrames. Double-check if your type
# conversion was successful.

for i in (bitcoin_search_df, tesla_search_df, ue_benefit_search_2004_19_df, ue_benefit_search_2004_20_df):
    i["MONTH"] = pandas.to_datetime(i["MONTH"])
    print("Converting date for " + str(i.name))
    i.columns = i.columns.str.replace("MONTH", "DATE")

print("Converting date for bitcoin price")
bitcoin_price_df["DATE"] = pandas.to_datetime(bitcoin_price_df["DATE"])

for i in df_list:
    print("Date type for " + str(i.name) + ":")
    print(type(i.DATE[0]))

# Next, we have to think about how to make our Bitcoin price and our Bitcoin search volume comparable.
# Our Bitcoin price is daily data, but our Bitcoin Search Popularity is monthly data.

bitcoin_price_monthly_df = bitcoin_price_df.resample('M', on='DATE').last()  # alternative: mean instead of last
print(bitcoin_price_monthly_df)

# Plot the Tesla stock price against the Tesla search volume using a line chart and two different axes.
# For our updated chart, let's differentiate the two lines and the axis labels using different colors.
# Try using one of the blue colour names for the search volume and a HEX code for a red colour for the stock price.

# Increase the figure size (e.g., to 14 by 8).
# Increase the font sizes for the labels and the ticks on the x-axis to 14.
# Rotate the text on the x-axis by 45 degrees.
# Add a title that reads 'Tesla Web Search vs Price'
# Make the lines on the chart thicker.
# Keep the chart looking sharp by changing the dots-per-inch or DPI value.
# Set minimum and maximum values for the y and x-axis. Hint: check out methods like set_xlim().
# Finally use plt.show() to display the chart below the cell instead of relying on the automatic notebook output.

plt.figure(figsize=(14, 8), dpi=120)
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.xlabel('Tesla Web Search vs Price', fontsize=18)

ax1 = plt.gca()  # get current axis
ax2 = ax1.twinx()
ax1.set_ylabel('TSLA Stock Price', color="red")
ax2.set_ylabel('Search Trend', color="blue")
# Set the minimum and maximum values on the axes
ax1.set_ylim([0, 600])
ax1.set_xlim([tesla_search_df.DATE.min(), tesla_search_df.DATE.max()])

ax1.plot(tesla_search_df.DATE, tesla_search_df.TSLA_USD_CLOSE, color="red", linewidth=3)
ax2.plot(tesla_search_df.DATE, tesla_search_df.TSLA_WEB_SEARCH, color="blue", linewidth=3)
plt.show()
