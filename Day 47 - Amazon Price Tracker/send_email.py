# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-16

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 47 - Amazon Price Tracker

import smtplib
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class SendEmail:
    def __init__(self, from_email, smtp_server, smtp_port, password, sendGridToken):
        self.from_email = from_email
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.password = password
        self.sendGridToken = sendGridToken

    # Send E-Mail via SendGrid
    def send_grid_email(self, to_email, mail_subject, send_msg):
        message = Mail(
            from_email=self.from_email,
            to_emails=to_email,
            subject=str(mail_subject),
            html_content=str(send_msg).encode("utf_8").decode("unicode_escape")
        )
        try:
            sg = SendGridAPIClient(self.sendGridToken)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)

    # Send E-Mail via SMTP
    def send_smtp_email(self, to_email, send_msg):
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as connection:
            connection.starttls()
            connection.login(self.from_email, self.password)
            connection.sendmail(self.from_email, to_email, send_msg)