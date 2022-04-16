# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-25

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 39 - Flight Deal Finder

from twilio_sms import SendSMS
import os

# Account, token and phone number for Twilio
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
twilio_phone_number = os.getenv("twilio_phone_number")
twilio_sms = SendSMS(account_sid, auth_token, twilio_phone_number)

# Send SMS to this phone number
to_phone_number = os.getenv("to_phone_number")


class NotificationManager:

    def notify_sms(self, message):
        twilio_sms.send_sms(to_phone_number, message)
