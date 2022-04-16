# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-27

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 46 - Top 100 Billboard and Spotify

from datetime import datetime
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import os

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = "http://127.0.0.1:8080"


# Get a date from user
def get_date_from_user():
    user_date = input("Please enter a date in the YYYY-DD-MM format:")
    format = "%Y-%m-%d"
    # checking if format matches the date
    res = True
    # using try-except to check for truth value
    try:
        res = bool(datetime.strptime(user_date, format))
        return user_date
    except ValueError:
        print("Wrong format")
        get_date_from_user()


user_date = str(get_date_from_user())
user_year = user_date.split("-")[0]

# Set URL for date
billboard_base_url = "https://www.billboard.com/charts/hot-100/"
url = billboard_base_url + user_date + "/"


# Get data from URL
def get_data_from_url():
    response = requests.get(url)
    webpage = response.text
    soup = BeautifulSoup(webpage, "html.parser")
    return soup


soup = get_data_from_url()


# Parse songs
def parse_songs(input_soup):
    # Get song titles
    songs_tag = soup.find_all(id="title-of-a-story", name="h3", class_="c-title")
    songs = []
    for i in songs_tag:
        song = i.getText()
        song = song.replace("\n", "")
        song = song.replace("\t", "")
        songs.append(song)
    # Remove unwanted data
    songs[:] = [i for i in songs if "Songwriter(s):" not in i]
    songs[:] = [i for i in songs if "Producer(s):" not in i]
    songs[:] = [i for i in songs if "Imprint/Promotion Label:" not in i]
    songs[:] = [i for i in songs if "Gains in Weekly Performance" not in i]
    songs[:] = [i for i in songs if "Additional Awards" not in i]
    songs[:] = [i for i in songs if
                "Silk Sonic Bring the Funk, Perform Entire Debut Album at Las Vegas Residency Launch" not in i]
    # Only top 100 elements
    songs = songs[:100]

    return songs


songs = parse_songs(soup)
print("Song list from Billboard on " + str(user_date) + ":")
print(songs)


def spotify_authenticate():
    # Authenticate with Spotify
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri=SPOTIPY_REDIRECT_URI,
            client_id=SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    user_id = sp.current_user()["id"]
    return sp, user_id


sp, user_id = spotify_authenticate()


def spotify_generate_uri_list(input_sp, input_user_id, input_songs, input_user_year):
    # Search for tracks in Billboard 100 by song name and year
    song_uris = []
    for song in input_songs:
        result = input_sp.search(q=f"track:{song} year:{input_user_year}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")
    return song_uris


song_uris = spotify_generate_uri_list(sp, user_id, songs, user_year)
print("Song tracks from Spotify:")
print(song_uris)


def spotify_generate_playlist(input_sp, input_user_id, input_song_uris, input_user_year):
    # Generate a playlist in Spotify from song tracks that were found
    playlist = input_sp.user_playlist_create(user=input_user_id, name=f"{input_user_year} Billboard 100", public=False)
    sp.playlist_add_items(playlist_id=playlist["id"], items=input_song_uris)
    return playlist


playlist = spotify_generate_playlist(sp, user_id, song_uris, user_year)
print(playlist)
