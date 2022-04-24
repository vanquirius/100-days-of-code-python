# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-21

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 46 - Top 100 Billboard and Spotify

from billboard_top_100 import BillboardTop100
from spotipy_search import SpotipySearch
from custom_song_list import CustomSongList


def get_billboard_top_100_data(input_date=None):
    # Search for Billboard Top 100 data
    billboard_top_100 = BillboardTop100()
    # Get date from the user in YYYY-MM-DD format
    billboard_top_100.get_date_from_user(input_date)
    # Get data from Billboard Top 100 for this date
    billboard_top_100.get_data_from_url()
    # Parse a song list from this data
    songs, user_year = billboard_top_100.parse_songs()
    return songs, user_year


def add_billboard_to_spotify(input_artist_songs_dict, input_user_year):
    # Search and include results in a Spotify playlist
    spotipy_search = SpotipySearch()
    # Authenticate Spotify user in Spotipy
    spotipy_search.spotify_authenticate()
    # Search for tracks by song name and year
    spotipy_search.spotify_generate_uri_list_artist_song(input_artist_songs_dict)
    # Create Spotify playlist
    spotipy_search.spotify_generate_playlist(input_user_year)


def add_custom_to_spotify(input_artist_songs_dict):
    # Search and include results in a Spotify playlist
    spotipy_search = SpotipySearch()
    # Authenticate Spotify user in Spotipy
    spotipy_search.spotify_authenticate()
    # Search for tracks by song name and year
    spotipy_search.spotify_generate_uri_list_artist_song(input_artist_songs_dict)
    # Create Spotify playlist
    spotipy_search.spotify_generate_playlist()


# Create a Spotify list based on Billboard Top 100 data
for i in range(1980, 2023):  # iterates from 1980 to 2022 and will create one list for each year
    date = str(i) + "-06-30"
    artist_songs_dict, user_year = get_billboard_top_100_data(date)  # if year is not provided, will ask for input
    add_billboard_to_spotify(artist_songs_dict, user_year)

# Create a Spotify list based on a custom song list (input_songs.csv)
# custom_song_list = CustomSongList()
# artist_songs_dict = custom_song_list.import_data()
# add_custom_to_spotify(artist_songs_dict)
