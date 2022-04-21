# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-21

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 46 - Top 100 Billboard and Spotify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import os

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = "http://127.0.0.1:8080"


class SpotipySearch:
    def __init__(self):
        self.user_id = None
        self.sp = None
        self.song_uris = []
        self.songs = None
        self.user_year = None

    def spotify_authenticate(self):
        # Authenticate with Spotify
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri=SPOTIPY_REDIRECT_URI,
                client_id=SPOTIPY_CLIENT_ID,
                client_secret=SPOTIPY_CLIENT_SECRET,
                show_dialog=True,
                cache_path="token.txt"
            )
        )
        self.user_id = self.sp.current_user()["id"]

    def spotify_generate_uri_list(self, songs, year):
        # Search for tracks by song name and year
        self.songs = songs
        self.user_year = year
        for song in self.songs:
            print(f"track:{song} year:{self.user_year}")
            result = self.sp.search(q=f"track:{song} year:{self.user_year}", type="track")
            try:
                uri = result["tracks"]["items"][0]["uri"]
                self.song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")
        print("Song tracks from Spotify:")
        print(self.song_uris)

    def spotify_generate_uri_list_artist_song(self, artist_songs_dict):
        # Search for tracks by song name and year
        for track in artist_songs_dict:
            song = track["song"]
            artist = track["artist"]
            print(f"track:{song} artist:{artist}")
            result = self.sp.search(q=f"track:{song} artist:{artist}", type="track")
            try:
                uri = result["tracks"]["items"][0]["uri"]
                self.song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")
        print("Song tracks from Spotify:")
        print(self.song_uris)

    def spotify_generate_playlist(self):
        # Generate a playlist in Spotify from song tracks that were found
        if self.user_year is None:
            self.user_year = "Custom Playlist"
        playlist = self.sp.user_playlist_create(user=self.user_id, name=f"{self.user_year}",
                                                public=False)
        self.sp.playlist_add_items(playlist_id=playlist["id"], items=self.song_uris)
        print(playlist)
