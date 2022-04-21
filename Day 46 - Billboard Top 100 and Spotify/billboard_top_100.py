# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-21

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 46 - Top 100 Billboard and Spotify

from datetime import datetime
import requests
from bs4 import BeautifulSoup


class BillboardTop100:

    def __init__(self):
        self.user_date = None
        self.user_year = None
        self.list_type = None
        self.soup = None
        self.songs = []

    # Get a date from user
    def get_date_from_user(self):
        self.user_date = input("Please enter a date in the YYYY-DD-MM format:")
        date_format = "%Y-%m-%d"
        # checking if format matches the date
        res = True
        # using try-except to check for truth value
        try:
            res = bool(datetime.strptime(self.user_date, date_format))
            self.user_year = self.user_date.split("-")[0]
            return self.user_date
        except ValueError:
            print("Wrong format")
            self.get_date_from_user()

    # Get data from URL
    def get_data_from_url(self):
        # Set URL for date
        billboard_base_url = "https://www.billboard.com/charts/hot-100/"
        url = billboard_base_url + self.user_date + "/"

        response = requests.get(url)
        webpage = response.text
        self.soup = BeautifulSoup(webpage, "html.parser")

    # Parse songs
    def parse_songs(self):
        # Get song titles
        songs_tag = self.soup.find_all(id="title-of-a-story", name="h3", class_="c-title")
        for i in songs_tag:
            song = i.getText()
            song = song.replace("\n", "")
            song = song.replace("\t", "")
            self.songs.append(song)
        # Remove unwanted data
        self.songs[:] = [i for i in self.songs if "Songwriter(s):" not in i]
        self.songs[:] = [i for i in self.songs if "Producer(s):" not in i]
        self.songs[:] = [i for i in self.songs if "Imprint/Promotion Label:" not in i]
        self.songs[:] = [i for i in self.songs if "Gains in Weekly Performance" not in i]
        self.songs[:] = [i for i in self.songs if "Additional Awards" not in i]
        self.songs[:] = [i for i in self.songs if
                         "Silk Sonic Bring the Funk, Perform Entire Debut Album at Las Vegas Residency Launch" not in i]
        # Only top 100 elements
        self.songs = self.songs[1:101]
        print("Song list from Billboard on " + str(self.user_date) + ":")
        print(self.songs)
        return self.songs, self.user_year
