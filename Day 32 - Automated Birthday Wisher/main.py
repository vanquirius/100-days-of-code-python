# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-16

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 32 - Automated Birthday Wisher

from datetime import *
import pandas
import random
from send_email import SendEmail
import os

# Constants
DATAFILE = "birthdays.csv"

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


def select_birthday():
    # 1. Update the birthdays.csv
    df = pandas.read_csv(DATAFILE)
    birthdays_dict = df.to_dict(orient="records")
    print(birthdays_dict)

    # 2. Check if today matches a birthday in the birthdays.csv
    month_day = str(datetime.now().month) + "/" + str(datetime.now().day)

    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
    # actual name from birthdays.csv
    for birthday_person in birthdays_dict:
        month_day_birth = str(birthday_person['month']) + "/" + str(birthday_person['day'])
        birthday_year = birthday_person['year']
        # Select random letter
        letter = "letter_templates/letter_" + str(random.randint(1, 3)) + ".txt"
        if month_day == month_day_birth:
            with open(letter, "r", encoding="utf-8") as f:
                subject = "Feliz aniversário! Happy Birthday!"
                content = f.read()
                content = content.replace("[NAME]", birthday_person["name"])
                # send_msg is the concatenation of subject and content
                send_msg = ("Subject:" + str(subject) + "\n\n" + str(content)).encode('utf-8')
                to_email = birthday_person["email"]
                # 4. Send the letter generated in step 3 to that person's email address.
                if sendgrid_enabled == 1:
                    sendemail.send_grid_email(to_email, subject, content)
                else:
                    sendemail.send_smtp_email(to_email, send_msg)


select_birthday()
