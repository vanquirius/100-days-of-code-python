# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-18

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 32 - Automated Birthday Wisher - Exercise

import smtplib
import datetime as dt
import pandas
import random
import os

# Constants
DATAFILE = "quotes.txt"

# Credentials
my_email = os.getenv("my_email")
my_password = os.getenv("my_password")
to_email = os.getenv("to_email")

# E-Mail server settings
smtp_server = "smtp.gmail.com"
smtp_port = "587"

# Connect and send
def send_email(input_smtp_server, input_smtp_port, input_my_email, input_my_password, input_to_email, input_send_msg):
    with smtplib.SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=send_msg)

def random_quote():
    # Import data
    df = pandas.read_csv(DATAFILE)
    quote_list = df.values.tolist()
    current_quote = random.choice(quote_list)
    print(current_quote[0])
    return current_quote[0]

now = dt.datetime.now()
weekday = now.weekday()
# 0 == Monday, 1 == Tuesday, 2 == Wednesday, 3 == Thursday, 4 == Friday ...
if weekday == 4:
    print("Weekday matches, sending motivational quote...")
    # Content
    subject = "Motivational quote of the day"
    message = random_quote()
    send_msg = "Subject:" + subject + "\n\n" + message
    # Send E-Mail
    send_email(smtp_server, smtp_port, my_email, my_password, to_email, send_msg)