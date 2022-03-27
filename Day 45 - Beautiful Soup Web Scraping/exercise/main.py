# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-27

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 45 - Beautiful Soup Web Scraping

import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles_tag = soup.find_all(name="a", class_="titlelink")
articles_text = []
articles_link = []
for i in articles_tag:
    text = i.getText()
    articles_text.append(text)
    link = i.get("href")
    articles_link.append(link)
articles_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_position = articles_upvotes.index(max(articles_upvotes))

print(articles_text[max_position])
print(articles_link[max_position])
print(articles_upvotes[max_position])