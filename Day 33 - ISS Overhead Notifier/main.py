# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-16

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 33 - ISS Over Head Notifier

import requests
from datetime import datetime
import time
import os
from send_email import SendEmail

# Coordinates for São Paulo, SP, Brazil
MY_LAT = -23.550520
MY_LONG = -46.633308
TOLERANCE = 5

# Set as 1 to choose SendGrid over SMTP
sendgrid_enabled = 1

# E-Mail server settings
smtp_server = "smtp.gmail.com"  # if using SMTP
smtp_port = "587"  # if using SMTP

# Credentials
from_email = os.getenv("from_email")
sendGridToken = os.getenv("sendGridToken")  # If using SendGrid
email_password = os.getenv("email_password")  # If using SMTP
to_email = from_email  # Send e-mail to yourself

sendemail = SendEmail(from_email, smtp_server, smtp_port, email_password, sendGridToken)


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

    response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
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
            print("Right now it is not dark")
            return False
    else:
        # Bright
        print("Right now it is not dark")
        return False


def notify_iss_overhead():
    dark = check_if_dark()
    iss_latitude, iss_longitude = get_iss_position()
    # check if it is dark
    if dark is True:
        print("It is dark")
        # check if latitude in range
        if (iss_latitude > MY_LAT - TOLERANCE) and (iss_latitude < MY_LAT + TOLERANCE):
            print("My latitude in range of ISS")
            # check if longitude in range
            if (iss_longitude > MY_LONG - TOLERANCE) and (iss_longitude < MY_LONG + TOLERANCE):
                print("My longitude in range of ISS")
                subject = "ISS is overhead"
                content = subject
                # send_msg is the concatenation of subject and content
                send_msg = ("Subject:" + str(subject) + "\n\n" + str(content)).encode('utf-8')
                print(subject)
                if sendgrid_enabled == 1:
                    sendemail.send_grid_email(to_email, subject, content)
                else:
                    sendemail.send_smtp_email(to_email, send_msg)
                return True
            else:
                print("My longitude not in range of ISS")
        else:
            print("My latitude not in range of ISS")
    else:
        print("It is not dark, skipping check")

    print("ISS is not overhead or it is not dark")
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
