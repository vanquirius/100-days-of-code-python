# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-18

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 32 - Automated Birthday Wisher

import smtplib
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Set as 1 to choose Send Grid over SMTP
sendgrid_enabled = 1

# E-Mail server settings
smtp_server = "smtp.gmail.com"  # if using SMTP
smtp_port = "587"  # if using SMTP


# Connect and send
def send_email(input_smtp_server=smtp_server, input_smtp_port=smtp_port, input_my_email=".",
               input_my_password=".", input_to_email="", input_send_msg=""):
    with smtplib.SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=input_my_email, password=input_my_password)
        connection.sendmail(from_addr=input_my_email, to_addrs=input_to_email, msg=input_send_msg)


def send_grid_email(input_mail_subject, input_send_msg, input_to_email, input_my_email, input_sendGridToken):
    message = Mail(
        from_email=input_my_email,
        to_emails=input_to_email,
        subject=str(input_mail_subject),
        html_content=str(input_send_msg).encode("utf_8").decode("unicode_escape")
    )
    try:
        sg = SendGridAPIClient(input_sendGridToken)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
