# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-10

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 25 - Squirrel Census Data

import pandas

# How many gray, black and cinnamon squirrels
def import_census_data():
    datasource = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
    fields = ['Primary Fur Color']
    df = pandas.read_csv(datasource, usecols=fields)
    print("Imported data:")
    print(df)
    return df

def count_export_data(input_df):
    df = input_df.groupby(['Primary Fur Color'])['Primary Fur Color'].count()
    print("Data count:")
    print(df)
    df.to_csv("squirrel_count.csv")


# Create CSV with color count
df = import_census_data()
count_export_data(df)
