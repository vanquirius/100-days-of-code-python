# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-24

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 72 - Data Visualization with Matplotlib

import pandas
import matplotlib.pyplot as plt

# Import data
header = ["DATE", "TAG", "POSTS"]
df = pandas.read_csv("QueryResults.csv", names=header, skiprows=1)
df["DATE"] = pandas.to_datetime(df["DATE"])

# Rows and columns
rows, columns = df.shape
print("Rows: " + str(rows))
print("Columns: " + str(columns))

# First 5 rows and last 5 rows
print("\nFirst five rows:")
print(df.head(5))
print("\nLast five rows:")
print(df.tail(5))

# Count values per column
print("\nValues per column:")
print(df.count())

# Language with most posts
print("\nLanguage with most posts:")
most_posts_df = df.groupby('TAG').sum('POSTS').sort_values('POSTS', ascending=False)
print(most_posts_df)

# How many months of posts per language
print("\nMonths of posts per language")
months_of_posts_df = df.groupby('TAG').count()
print(months_of_posts_df)

# Pivoted table
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
print("\nPivoted Table:")
# Replace NaN with 0
reshaped_df.fillna(0, inplace=True)
print(reshaped_df)

# Matplotlib
roll_df = reshaped_df.rolling(window=6).mean()
plt.figure(figsize=(16, 10))
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
plt.plot(roll_df.index, roll_df['python'])  # Python
plt.plot(roll_df.index, roll_df['java'])  # Java
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)
plt.legend(fontsize=16)
plt.show()