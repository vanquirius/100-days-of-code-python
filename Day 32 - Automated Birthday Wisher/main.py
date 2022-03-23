# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-18

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 32 - Automated Birthday Wisher

##################### Extra Hard Starting Project ######################

import smtplib
from datetime import datetime
import pandas
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Constants
DATAFILE = "birthdays.csv"
cc_email = "######"
# Set as 1 to choose Send Grid over SMTP
SENDGRID_ENABLED = 1

# Credentials
my_email = "######"
my_password = "######"  # if using SMTP
sendGridToken = "######"  # if using Send Grid

# E-Mail server settings
smtp_server = "smtp.gmail.com"  # if using SMTP
smtp_port = "587"  # if using SMTP


# Connect and send
def send_email(input_smtp_server=smtp_server, input_smtp_port=smtp_port, input_my_email=my_email,
               input_my_password=my_password, input_to_email="", input_send_msg=""):
    with smtplib.SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=input_to_email, msg=input_send_msg)


def send_grid_email(input_mail_subject, input_send_msg, input_to_email, input_my_email):
    message = Mail(
        from_email=input_my_email,
        to_emails=input_to_email,
        subject=str(input_mail_subject),
        html_content=str(input_send_msg).encode("utf_8").decode("unicode_escape")
    )
    try:
        sg = SendGridAPIClient(sendGridToken)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)


def select_birthday():
    # 1. Update the birthdays.csv
    df = pandas.read_csv(DATAFILE)
    birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

    # 2. Check if today matches a birthday in the birthdays.csv
    today = datetime.now()
    today_tuple = (today.month, today.day)

    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    if today_tuple in birthdays_dict:
        birthday_person = birthdays_dict[today_tuple]
        # Select random letter
        letter = "letter_templates/letter_" + str(random.randint(1, 3)) + ".txt"
        with open(letter, "r", encoding="utf-8") as f:
            content = f.read()
            content = content.replace("[NAME]", birthday_person["name"])
            subject = "Feliz aniversário! Happy Birthday!"
            send_msg = ("Subject:" + str(subject) + "\n\n" + str(content)).encode('utf-8')
            address = birthday_person["email"] + "," + cc_email
            # 4. Send the letter generated in step 3 to that person's email address.
            if SENDGRID_ENABLED == 1:
                send_grid_email(input_mail_subject=subject, input_send_msg=content, input_to_email=address, input_my_email=my_email)
            else:
                send_email(input_to_email=address, input_send_msg=send_msg)


select_birthday()
