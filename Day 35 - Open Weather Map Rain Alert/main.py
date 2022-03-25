# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-20

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 35 - Open Weather Map Rain Alert

import requests
import twilio_sms

# Coordinates for São Paulo, SP, Brazil
MY_LAT = -23.550520
MY_LONG = -46.633308

# API Keys for Open Weather Maps and Twilio
owp_api_key = "######"
account_sid = "######"
auth_token = "######"
twilio_phone_number = "######"
to_phone_number = "######"


def get_owp_onecallapi():
    # Call One Call API from Open Weather Maps
    parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": owp_api_key,
        "units": "metric",
        "exclude": "current,minutely,daily"
    }

    response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
    # print("Response code: " + str(response.status_code))
    response.raise_for_status()
    data = response.json()

    # Check if we have a weather code of less than 700 in the next 12 hours
    bad_weather = False
    for i in range(0, 11):
        code = data["hourly"][i]["weather"][0]["id"]
        if code < 700:
            bad_weather = True

    # Print "bring an umbrella" if there is bad weather ahead
    if bad_weather:
        message = "Bad weather! Bring an umbrella"
        print(message)
        twilio_sms.send_sms(account_sid, auth_token, twilio_phone_number, to_phone_number, message)
    else:
        print("Weather is good!")


get_owp_onecallapi()
