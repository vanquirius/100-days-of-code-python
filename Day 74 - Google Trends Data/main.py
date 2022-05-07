# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-30

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 74 - Google Trends Data

import pandas
import matplotlib.pyplot as plt

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
    i["ORIGINAL_DATE"] = pandas.to_datetime(i["MONTH"])
    i["MONTH"] = pandas.to_datetime(i["MONTH"])
    print("Converting date for " + str(i.name))
    i.columns = i.columns.str.replace("MONTH", "DATE")
    i.columns = i.columns.str.replace("ORIGINAL_DATE", "MONTH")

print("Converting date for bitcoin price")
bitcoin_price_df["DATE"] = pandas.to_datetime(bitcoin_price_df["DATE"])

for i in df_list:
    print("Date type for " + str(i.name) + ":")
    print(type(i.DATE[0]))

# Next, we have to think about how to make our Bitcoin price and our Bitcoin search volume comparable.
# Our Bitcoin price is daily data, but our Bitcoin Search Popularity is monthly data.

bitcoin_price_monthly_df = bitcoin_price_df.resample('M', on='DATE').last()  # alternative: mean instead of last

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
# plt.show()

# Modify the chart title to read 'Bitcoin News Search vs Resampled Price'
# Change the y-axis label to 'BTC Price'
# Change the y- and x-axis limits to improve the appearance
# Investigate the linestyles to make the BTC closing price a dashed line
# Investigate the marker types to make the search datapoints little circles
# Were big increases in searches for Bitcoin accompanied by big increases in the price?

plt.figure(figsize=(14, 8), dpi=120)

plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('BTC Price', color='#F08F2E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)

ax1.set_ylim(bottom=0, top=15000)
ax1.set_xlim([bitcoin_price_monthly_df.index.min(), bitcoin_price_monthly_df.index.max()])

# Experiment with the linestyle and markers
ax1.plot(bitcoin_price_monthly_df.index, bitcoin_price_monthly_df.CLOSE,
         color='#F08F2E', linewidth=3, linestyle='--')
ax2.plot(bitcoin_price_monthly_df.index, bitcoin_search_df.BTC_NEWS_SEARCH,
         color='skyblue', linewidth=3, marker='o')

# plt.show()

# Plot the search for "unemployment benefits" against the official unemployment rate.
# Change the title to: Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate
# Change the y-axis label to: FRED U/E Rate
# Change the axis limits
# Add a grey grid to the chart to better see the years and the U/E rate values. Use dashed lines for the line style.
# Can you discern any seasonality in the searches? Is there a pattern?

plt.figure(figsize=(14, 8), dpi=120)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)

ax1.set_ylim(bottom=3, top=10.5)
ax1.set_xlim([ue_benefit_search_2004_19_df.MONTH.min(), ue_benefit_search_2004_19_df.MONTH.max()])

# Show the grid lines as dark grey lines
ax1.grid(color='grey', linestyle='--')

# Change the dataset used
ax1.plot(ue_benefit_search_2004_19_df.MONTH, ue_benefit_search_2004_19_df.UNRATE,
         color='purple', linewidth=3, linestyle='--')
ax2.plot(ue_benefit_search_2004_19_df.MONTH, ue_benefit_search_2004_19_df.UE_BENEFITS_WEB_SEARCH,
         color='skyblue', linewidth=3)

# plt.show()

# Challenge
# Calculate the 3-month or 6-month rolling average for the web searches. Plot the 6-month rolling average
# search data against the actual unemployment. What do you see? Which line moves first? Hint: Take a look at our
# prior lesson on Programming Languages where we smoothed out time-series data.

plt.figure(figsize=(14, 8), dpi=120)
plt.title('Rolling Monthly US "Unemployment Benefits" Web Searches vs UNRATE', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)

ax1.set_ylim(bottom=3, top=10.5)
ax1.set_xlim([ue_benefit_search_2004_19_df.MONTH[0], ue_benefit_search_2004_19_df.MONTH.max()])

# Calculate the rolling average over a 6 month window
roll_df = ue_benefit_search_2004_19_df[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()

ax1.plot(ue_benefit_search_2004_19_df.MONTH, roll_df.UNRATE, 'purple', linewidth=3, linestyle='-.')
ax2.plot(ue_benefit_search_2004_19_df.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)

# plt.show()

# Challenge
# Read the data in the 'UE Benefits Search vs UE Rate 2004-20.csv' into a DataFrame. Convert the MONTH
# column to Pandas Datetime objects and then plot the chart. What do you see?

plt.figure(figsize=(14, 8), dpi=120)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
plt.title('Monthly US "Unemployment Benefits" Web Search vs UNRATE incl 2020', fontsize=18)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)

ax1.set_xlim([ue_benefit_search_2004_20_df.MONTH.min(), ue_benefit_search_2004_20_df.MONTH.max()])

ax1.plot(ue_benefit_search_2004_20_df.MONTH, ue_benefit_search_2004_20_df.UNRATE, 'purple', linewidth=3)
ax2.plot(ue_benefit_search_2004_20_df.MONTH, ue_benefit_search_2004_20_df.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)

plt.show()