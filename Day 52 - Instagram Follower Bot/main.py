# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-09

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 52 - Instagram Follower Bot Account

INSTAGRAM_USER = "######"
INSTAGRAM_PASSWORD = "######"
ACCOUNT_TO_FOLLOW = "harvard_business_review"  # just an example

from instagram_follower_bot import InstagramBot

# Instantiate bot
bot = InstagramBot(INSTAGRAM_USER, INSTAGRAM_PASSWORD, ACCOUNT_TO_FOLLOW)

# Follow the followers
bot.login()
bot.find_followers()
bot.follow_the_followers()