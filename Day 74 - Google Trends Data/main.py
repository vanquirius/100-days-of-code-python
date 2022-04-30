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
bitcoin_price_df = pandas.read_csv("data/Daily Bitcoin Price.csv")
tesla_search_df = pandas.read_csv("data/TESLA Search Trend vs Price.csv")
ue_benefit_search_2004_19_df = pandas.read_csv("data/UE Benefits Search vs UE Rate 2004-19.csv")
ue_benefit_search_2004_19_df = pandas.read_csv("data/UE Benefits Search vs UE Rate 2004-20.csv")