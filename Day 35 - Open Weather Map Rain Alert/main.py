# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-20

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 35 - Open Weather Map Rain Alert

import requests
from datetime import datetime
import time

# Coordinates for São Paulo, SP, Brazil
MY_LAT = -23.550520
MY_LONG = -46.633308

def get_iss_position():
    # Get ISS latitude and longitude
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print("ISS Latitude: " + str(iss_latitude))
    print("ISS Longitude: " + str(iss_longitude))
    return iss_latitude, iss_longitude