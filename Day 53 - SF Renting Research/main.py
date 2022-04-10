# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-09

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 53 - SF Renting Research

from zillow_scrape import ZillowBot
from google_form import GoogleFormBot

# Scrape data
zillow_bot = ZillowBot()
zillow_bot.get_data_from_url()
price_list, address_list, link_list = zillow_bot.parse_offers()

# Fill data to Google Forms
google_bot = GoogleFormBot()
for i in range(0, len(price_list)):
    google_bot.fill_form(price_list[i], address_list[i], link_list[i])