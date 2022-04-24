# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-24

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 71 - Data Exploration with Pandas

import pandas

# pandas.set_option("display.max_columns", None)
pandas.options.display.float_format = '{:,.2f}'.format
# Import data
df = pandas.read_csv('salaries_by_college_major.csv')
# Drop "not a number" values - in this case the last row
df = df.dropna()

# Highest starting salary
print("Highest Starting Median Salary:")
print(df['Starting Median Salary'].max())
print(df['Undergraduate Major'].loc[df['Starting Median Salary'].idxmax()])

# Highest mid-career salary
print("\nHighest Mid-Career Median Salary:")
print(df['Mid-Career Median Salary'].max())
print(df['Undergraduate Major'].loc[df['Mid-Career Median Salary'].idxmax()])

# Lowest starting salary
print("\nLowest Starting Median Salary:")
print(df['Starting Median Salary'].min())
print(df['Undergraduate Major'].loc[df['Starting Median Salary'].idxmin()])

# Lowest mid-career salary
print("\nLowest Mid-Career Median Salary:")
print(df['Mid-Career Median Salary'].min())
print(df['Undergraduate Major'].loc[df['Mid-Career Median Salary'].idxmin()])

# How much can people expect to gain with lowest mid-career salary
print("How much people can expect to earn:")
print(df.loc[df['Mid-Career Median Salary'].idxmin()])

# Add column of difference between 10% and 90% percentile
spread_col = df['Mid-Career 90th Percentile Salary'] - df['Mid-Career 10th Percentile Salary']
df.insert(1, 'Spread', spread_col)
df = df.sort_values('Spread')
print(df[['Undergraduate Major', 'Spread']].head())

# Top 5 degrees with the highest values in the 90th percentile
print("\nTop 5 degrees with the highest values in the 90th percentile:")
df = df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
print(df.head(n=5))

# Degrees with the greatest spread in salaries
print("\nDegrees with the greatest spread in salaries:")
df = df.sort_values('Spread', ascending=False)
print(df.head(n=5))

# Mean salary by group
print("\nMean salary by group:")
print(df.groupby('Group').mean())