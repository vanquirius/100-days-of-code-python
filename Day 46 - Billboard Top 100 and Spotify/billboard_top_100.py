# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-21

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 46 - Top 100 Billboard and Spotify

from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas


class BillboardTop100:

    def __init__(self):
        self.user_date = None
        self.user_year = None
        self.list_type = None
        self.soup = None
        self.songs = []
        self.artists = []

    # Get a date from user
    def get_date_from_user(self, input_date):
        if input_date is None:
            self.user_date = input("Please enter a date in the YYYY-MM-DD format:")
            date_format = "%Y-%m-%d"
            # checking if format matches the date
            res = True
            # using try-except to check for truth value
            try:
                res = bool(datetime.strptime(self.user_date, date_format))
            except ValueError:
                print("Wrong format")
                self.get_date_from_user()
        else:
            self.user_date = input_date
        self.user_year = self.user_date.split("-")[0]
        return self.user_date

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
            artist = i.find_next("span").text.strip()
            self.artists.append(artist)
        # Remove unwanted data
        self.songs[:] = [i for i in self.songs if "Songwriter(s):" not in i]
        self.songs[:] = [i for i in self.songs if "Producer(s):" not in i]
        self.songs[:] = [i for i in self.songs if "Imprint/Promotion Label:" not in i]
        self.songs[:] = [i for i in self.songs if "Gains in Weekly Performance" not in i]
        self.songs[:] = [i for i in self.songs if "Additional Awards" not in i]
        self.songs[:] = [i for i in self.songs if
                         "Silk Sonic Bring the Funk, Perform Entire Debut Album at Las Vegas Residency Launch" not in i]

        self.artists[:] = [i for i in self.artists if "Share Chart on Twitter" not in i]
        self.artists[:] = [i for i in self.artists if "facebook" not in i]
        self.artists[:] = [i for i in self.artists if "Send us a tip" not in i]
        self.artists[:] = [i for i in self.artists if "Sign Up" not in i]
        self.artists[:] = [i for i in self.artists if "Plus Icon" not in i]
        self.artists[:] = [i for i in self.artists if "Last Week" not in i]
        # Only top 100 elements
        self.songs = self.songs[0:100]
        self.artists = self.artists[0:100]
        zipped = list(zip(self.songs, self.artists))
        df = pandas.DataFrame(zipped, columns=['song', 'artist'])
        artist_songs_dict = df.to_dict(orient="records")
        print("Track list from Billboard on " + str(self.user_date) + ":")
        return artist_songs_dict, self.user_year
