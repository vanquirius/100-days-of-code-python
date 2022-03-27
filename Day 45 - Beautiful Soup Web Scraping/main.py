# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-27

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 45 - Beautiful Soup Web Scraping

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

# Get data from URL
response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

# Parse titles
titles_tag = soup.find_all(name="h3", class_="title")
movies = []
for i in titles_tag:
    movie = i.getText()
    movies.append(movie)
#print(movies)
#movies.split()