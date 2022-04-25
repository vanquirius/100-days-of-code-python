# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-24

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 73 - Aggregate Merge LEGO Dataset

import pandas

# Import data
colors_df = pandas.read_csv("data/colors.csv")
sets_df = pandas.read_csv("data/sets.csv")
themes_df = pandas.read_csv("data/themes.csv")

# Unique colors
print("Unique colors:")
print(colors_df["name"].nunique())

# Transparent
print("Transparent colors:")
print(colors_df["is_trans"].value_counts())

# In which year were the first LEGO sets released and what were these sets called?
print("Year first LEGO sets:")
print(sets_df['year'].min())
print(sets_df['name'].loc[sets_df['year'].idxmin()])


# How many different products did the LEGO company sell in their first year of operation?

# What are the top 5 LEGO sets with the most number of parts?