# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-26

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 45 - Beautiful Soup Web Scraping

from bs4 import BeautifulSoup

def read_website():
    with open("website.html", mode="r", encoding="utf-8") as f:
        contents = f.read()
        return contents

contents = read_website()
soup = BeautifulSoup(contents, "html.parser")
print(soup.li)