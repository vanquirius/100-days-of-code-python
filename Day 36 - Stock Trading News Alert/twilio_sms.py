# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-16

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 36 - Stock Trading News Alert

from twilio.rest import Client


class SendSMS:
    def __init__(self, account_sid, auth_token, twilio_phone_number):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.twilio_phone_number = twilio_phone_number

    def send_sms(self, to_phone_number, message):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages \
            .create(
            body=message,
            from_=self.twilio_phone_number,
            to=to_phone_number
        )

        print(message.sid)
        print(message.status)
