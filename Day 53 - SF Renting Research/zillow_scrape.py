# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-09

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 53 - SF Renting Research

import requests
from bs4 import BeautifulSoup


class ZillowBot:
    def __init__(self):
        self.url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
                   "%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22" \
                   "%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C" \
                   "%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba" \
                   "%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value" \
                   "%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D" \
                   "%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A" \
                   "%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22" \
                   "%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22" \
                   "%3A12%7D "
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/99.0.4844.88 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }
        self.soup = None

    # Get data from URL
    def get_data_from_url(self):
        response = requests.get(self.url, headers=self.headers)  # Headers are needed
        webpage = response.text
        self.soup = BeautifulSoup(webpage, "html.parser")

    # Parse offers
    def parse_offers(self):
        price_offers = self.soup.find_all(name="div", class_="list-card-price")
        price_list = []
        for i in price_offers:
            price = i.getText().split()[0].replace("/mo", "").replace("+", "")
            price_list.append(price)

        addresses = self.soup.find_all(name="address", class_="list-card-addr")
        address_list = [i.get_text().split(" | ")[-1] for i in addresses]

        link_to_offers = self.soup.select(".list-card-top a")
        link_list = []
        for i in link_to_offers:
            link = i.get("href")
            if "http" not in link:
                link = "https://www.zillow.com" + link
            link_list.append(link)

        return price_list, address_list, link_list