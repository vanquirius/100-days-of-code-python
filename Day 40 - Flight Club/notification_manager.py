# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-25

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 40 - Flight Club

import requests
from send_email import SendEmail
from twilio_sms import SendSMS
import os

# Account, token and phone number for Twilio
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
twilio_phone_number = os.getenv("twilio_phone_number")
twilio_sms = SendSMS(account_sid, auth_token, twilio_phone_number)

# Send SMS to this phone number
to_phone_number = os.getenv("to_phone_number")

# Set as 1 to choose SendGrid over SMTP
sendgrid_enabled = 1

# E-Mail server settings
smtp_server = "smtp.gmail.com"  # if using SMTP
smtp_port = "587"  # if using SMTP

# Credentials
from_email = os.getenv("from_email")
sendGridToken = os.getenv("sendGridToken")  # If using SendGrid
email_password = os.getenv("email_password")  # If using SMTP

sendemail = SendEmail(from_email, smtp_server, smtp_port, email_password, sendGridToken)

# Sheety Credentials
SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")
sheety_api_key = os.getenv("sheety_api_key")
headers = {"Authorization": "Bearer " + sheety_api_key}


class NotificationManager:

    def __init__(self):
        self.user_emails = []

    def notify_sms(self, message):
        twilio_sms.send_sms(to_phone_number, message)

    def notify_email(self, message, to_email):
        subject = "New flight offer found!"
        content = message
        send_msg = ("Subject:" + str(subject) + "\n\n" + str(content)).encode('utf-8')
        if sendgrid_enabled == 1:
            sendemail.send_grid_email(to_email, subject, content)
        else:
            sendemail.send_smtp_email(to_email, send_msg)

    def get_user_emails(self):
        # Get E-Mail list from users tab using Sheety
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=headers)
        user_data = response.json()["users"]
        for i in user_data:
            email = (i["email"])
            self.user_emails.append(email)
        print(self.user_emails)
        return self.user_emails
