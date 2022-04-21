# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-17

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 64 - Top 10 Movies Website

import requests
import os

TMDB_V3_API_KEY = os.getenv("TMDB_V3_API_KEY")
TMDB_V3_ENDPOINT = "https://api.themoviedb.org/3/"
TMDB_V3_ENDPOINT_DATA = TMDB_V3_ENDPOINT + "search/movie"
TMDB_V3_ENDPOINT_DETAILS = TMDB_V3_ENDPOINT + "movie/"


class MovieSearch:

    def __init__(self, movie_name):
        self.movie_name = movie_name

    def get_movie_data(self):
        # Get data from TMDB
        headers = {
            "Content-Type": "application/json;charset=utf-8"
        }
        params = {
            "api_key": TMDB_V3_API_KEY,
            "query": self.movie_name,
            "language": "en-US"
        }
        response = requests.get(url=TMDB_V3_ENDPOINT_DATA, headers=headers, params=params)
        results = response.json()["results"]
        return results

class MovieDetails:

    def __init__(self, movie_id):
        self.movie_id = movie_id


    def get_movie_details(self):
        # Get details from TMDB
        headers = {
            "Content-Type": "application/json;charset=utf-8"
        }
        params = {
            "api_key": TMDB_V3_API_KEY,
            "language": "en-US"
        }
        movie_url = TMDB_V3_ENDPOINT_DETAILS + str(self.movie_id)
        response = requests.get(url=movie_url, headers=headers, params=params)
        results = response.json()
        return results