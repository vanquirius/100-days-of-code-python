# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-24

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 73 - Aggregate Merge LEGO Dataset

import pandas
import matplotlib.pyplot as plt

# Import data
colors_df = pandas.read_csv("data/colors.csv")
sets_df = pandas.read_csv("data/sets.csv")
themes_df = pandas.read_csv("data/themes.csv")

# Unique colors
print("Unique colors:")
print(colors_df["name"].nunique())

# Transparent
print("\nTransparent colors:")
print(colors_df["is_trans"].value_counts())

# In which year were the first LEGO sets released and what were these sets called?
print("\nYear first LEGO sets:")
print(sets_df['year'].min())
print(sets_df['name'].loc[sets_df['year'].idxmin()])

# How many products did the LEGO company sell in their first year of operation?
print("\nHow many products did LEGO sell in their first year:")
print(sets_df["name"][sets_df['year'] == sets_df['year'].min()].count())

# What are the top 5 LEGO sets with the number of parts?
print("\nTop 5 LEGO sets with most parts:")
sets_df = sets_df.sort_values(by=['num_parts'], ascending=False)
print(sets_df["name"].head(5))

# Course
sets_by_year = sets_df.groupby('year').count()
print(sets_by_year['set_num'].head())

# Number of Themes per Calendar Year
print("\nThemes by year:")
themes_by_year = sets_df.groupby('year').agg({'theme_id': pandas.Series.nunique})
print(themes_by_year)

# Plotting
# ax1 = plt.gca() # get current axes
# ax2 = ax1.twinx()

# ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='green')
# ax1.set_xlabel("Year")
# ax1.set_ylabel("Number of sets", color='green')
# ax2.plot(themes_by_year.index[:-2], themes_by_year.theme_id[:-2], color='blue')
# ax2.set_ylabel("Number of themes", color='blue')
# plt.show()

# Create a Pandas Series called parts_per_set that has the year as the index and contains the average number of parts
# per LEGO set in that year.

parts_per_set = sets_df.groupby('year').agg({'num_parts': pandas.Series.mean})
print(parts_per_set)

# plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
# plt.show()

# Number of Sets per LEGO Theme
print("\nNumber of sets per LEGO Theme:")
set_theme_count = sets_df["theme_id"].value_counts()
print(set_theme_count[:5])

set_theme_count = pandas.DataFrame({'id':set_theme_count.index, 'set_count': set_theme_count.values})
print(set_theme_count.head())
merged_df = pandas.merge(set_theme_count, themes_df, on='id')
print(merged_df)

plt.figure(figsize=(14, 8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.bar(merged_df.name[:10], merged_df.set_count[:10])
plt.show()