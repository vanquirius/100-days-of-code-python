# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-25

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 40 - Flight Club

from twilio.rest import Client


def send_sms(input_account_sid, input_auth_token, input_twilio_phone_number, input_to_phone_number, input_message):
    client = Client(input_account_sid, input_auth_token)

    message = client.messages \
        .create(
        body=input_message,
        from_=input_twilio_phone_number,
        to=input_to_phone_number
    )

    print(message.sid)
    print(message.status)
