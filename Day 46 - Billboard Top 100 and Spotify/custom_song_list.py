# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-21

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 46 - Top 100 Billboard and Spotify

import pandas

# Constants
DATAFILE = "input_songs.csv"


class CustomSongList:

    def import_data(self):
        df = pandas.read_csv(DATAFILE)
        artist_songs_dict = df.to_dict(orient="records")
        return artist_songs_dict
