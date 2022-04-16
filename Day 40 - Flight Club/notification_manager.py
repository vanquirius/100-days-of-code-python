# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-25

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 40 - Flight Club

import requests
import twilio_sms
import send_email
import os

# API keys for Twilio
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
twilio_phone_number = os.getenv("twilio_phone_number")
to_phone_number = os.getenv("to_phone_number")

# Credentials for E-Mail
my_email = os.getenv("my_email")
my_password = os.getenv("my_password")  # If using SMPT
sendGridToken = os.getenv("sendGridToken")  # if using Send Grid

# Sheety Credentials
SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")
sheety_api_key = os.getenv("sheety_api_key")
headers = {"Authorization": "Bearer " + sheety_api_key}


class NotificationManager:

    def __init__(self):
        self.user_emails = []

    def notify_sms(self, message):
        twilio_sms.send_sms(account_sid, auth_token, twilio_phone_number, to_phone_number, message)

    def notify_email(self, message, address=my_email):
        subject = "New flight offer found!"
        content = message
        send_msg = ("Subject:" + str(subject) + "\n\n" + str(content)).encode('utf-8')
        if send_email.sendgrid_enabled == 1:
            send_email.send_grid_email(input_mail_subject=subject, input_send_msg=content, input_to_email=address,
                                       input_my_email=my_email, input_sendGridToken=sendGridToken)
        else:
            send_email.send_email(input_to_email=address, input_send_msg=send_msg, input_my_email=my_email,
                                  input_my_password=my_password)

    def get_user_emails(self):
        # Get E-Mail list from users tab using Sheety
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=headers)
        user_data = response.json()["users"]
        for i in user_data:
            email = (i["email"])
            self.user_emails.append(email)
        print(self.user_emails)
        return self.user_emails
