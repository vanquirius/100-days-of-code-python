# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-25

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 39 - Flight Deal Finder

# API keys for Twilio
account_sid = "######"
auth_token = "######"
twilio_phone_number = "######"
to_phone_number = "######"

import twilio_sms

class NotificationManager:

    def notify_sms(self, message):
        twilio_sms.send_sms(account_sid, auth_token, twilio_phone_number, to_phone_number, message)