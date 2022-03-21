# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-20

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 35 - Open Weather Map Rain Alert

import requests
from twilio.rest import Client

# Coordinates for São Paulo, SP, Brazil
MY_LAT = -23.550520
MY_LONG = -46.633308

# API Keys for Open Weather Maps and Twilio
owp_api_key = "######"
account_sid = "######"
auth_token = "######"
twilio_phone_number = "######"
to_phone_number = "######"

def send_sms(input_account_sid, input_auth_token, input_twilio_phone_number, input_to_phone_number):
    client = Client(input_account_sid, input_auth_token)

    message = client.messages \
                    .create(
                         body="Bring an umbrella",
                         from_=input_twilio_phone_number,
                         to=input_to_phone_number
                     )

    print(message.sid)
    print(message.status)

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
    # print("Reponse code: " + str(response.status_code))
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
        print("Bring an umbrella")
        send_sms(account_sid, auth_token, twilio_phone_number, to_phone_number)

get_owp_onecallapi()