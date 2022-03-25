# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-24

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 38 - Exercise Tracking Google Sheets

import requests

nutritionix_app_id = "######"
nutritionix_api_key = "######"
my_gender = "male"
my_weight_kg = 86.0
my_height_cm = 172.5
my_age = 36

nutritionix_url = "https://trackapi.nutritionix.com/v2/"

# Get exercise stats for plain user input
def get_exercise_stats():
    nutritionix_endpoint = nutritionix_url + "natural/exercise"
    print(nutritionix_endpoint)
    parameters = {
        "query": input("What was the exercise?"),
        "gender": my_gender,
        "weight_kg": my_weight_kg,
        "height_cm": my_height_cm,
        "age": my_age
    }
    headers = {
        "x-app-id": nutritionix_app_id,
        "x-app-key": nutritionix_api_key
    }
    response = requests.post(url=nutritionix_endpoint, json=parameters, headers=headers)
    print(response)
    print(response.text)
    data = response.json()

get_exercise_stats()