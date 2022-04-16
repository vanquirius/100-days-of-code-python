# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-09

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 51 - Internet Speed Twitter Complaint Bot

from internet_speed_twitter_bot import InternetSpeedTwitterBot
import os

PROMISED_DOWN = 500
PROMISED_UP = 35
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_NAME = os.getenv("TWITTER_NAME")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

# Instantiate bot
bot = InternetSpeedTwitterBot()

# Get up/down speeds
up_speed, down_speed = bot.get_internet_speed()

# Post on Twitter
bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_NAME, TWITTER_PASSWORD, down_speed, up_speed, PROMISED_UP, PROMISED_DOWN)