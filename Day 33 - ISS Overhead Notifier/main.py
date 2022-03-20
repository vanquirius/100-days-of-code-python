# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-19

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 33 - ISS Over Head Notifier

import requests
from datetime import datetime
import smtplib
import time

# Coordinates for São Paulo, SP, Brazil
MY_LAT = -23.550520
MY_LONG = -46.633308
TOLERANCE = 5

# Credentials
my_email = "######"
my_password = "######"

# E-Mail server settings
smtp_server = "smtp.gmail.com"
smtp_port = "587"


# Connect and send
def send_email(input_smtp_server=smtp_server, input_smtp_port=smtp_port, input_my_email=my_email,
               input_my_password=my_password, input_to_email="", input_send_msg=""):
    with smtplib.SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=input_to_email, msg=input_send_msg)


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

    # Your position is within +5 or -5 degrees of the ISS position.


def check_if_dark():
    # Get sunrise and sunset times
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Compare to current time
    time_now = datetime.now()
    time_now_hour = int(time_now.hour)
    if time_now_hour >= sunset:
        if time_now_hour <= sunrise or time_now_hour in (21, 22, 23):
            # Dark
            print("Right now it is dark")
            return True
        else:
            # Bright
            print("Right now it is bright")
            return False


def notify_iss_overhead():
    dark = check_if_dark()
    iss_latitude, iss_longitude = get_iss_position()
    # check if it is dark
    if dark is True:
        # check if latitude in range
        if (iss_latitude > MY_LAT - TOLERANCE) and (iss_latitude < MY_LAT + TOLERANCE):
            # check if longitude in range
            if (iss_longitude > MY_LONG - TOLERANCE) and (iss_longitude < MY_LONG + TOLERANCE):
                print("ISS is overhead")
                send_email(input_to_email=my_email, input_send_msg="Subject:ISS is overhead")
                return True

    print("ISS is not overhead")
    return False

# Loop
while True:
    notify_iss_overhead()
    print("----------------------------------")
    print("Waiting 60 seconds to query again.")
    print("----------------------------------")
    time.sleep(60)

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
