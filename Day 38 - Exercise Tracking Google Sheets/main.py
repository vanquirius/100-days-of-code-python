# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-24

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 38 - Exercise Tracking Google Sheets

import requests
from datetime import datetime
import os

nutritionix_app_id = os.getenv("nutritionix_app_id")
nutritionix_api_key = os.getenv("nutritionix_api_key")
sheety_token = os.getenv("sheety_token")
sheety_api_key = os.getenv("sheety_api_key")

my_gender = "male"
my_weight_kg = 86.0
my_height_cm = 172.5
my_age = 36

nutritionix_url = "https://trackapi.nutritionix.com/v2/"
sheety_url = "https://api.sheety.co/"


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
    return data


# Get data already in sheety
def sheety_get_rows():
    sheety_endpoint = sheety_url + sheety_token
    headers = {"Authorization": "Bearer " + sheety_api_key}
    response = requests.get(url=sheety_endpoint, headers=headers)
    response.raise_for_status()
    data = response.json()
    print(data)


# Add data to sheety
def sheety_add_rows(input_data):
    sheety_endpoint = sheety_url + sheety_token
    headers = {"Authorization": "Bearer " + sheety_api_key}

    for i in input_data["exercises"]:
        exercise_name = i["name"].title()
        exercise_duration = i["duration_min"]
        exercise_calories = i["nf_calories"]

    sheet_inputs = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise_name,
            "duration": exercise_duration,
            "calories": exercise_calories
        }
    }
    response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=headers)
    print(response)
    print(response.text)
    data = response.json()


exercise_data = get_exercise_stats()
# sheety_get_rows()
sheety_add_rows(exercise_data)
