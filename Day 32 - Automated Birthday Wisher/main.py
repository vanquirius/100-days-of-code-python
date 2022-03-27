# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-18

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 32 - Automated Birthday Wisher

##################### Extra Hard Starting Project ######################

from datetime import *
import pandas
import random
import send_email

# Constants
DATAFILE = "birthdays.csv"
cc_email = "######"

# Credentials
my_email = "######@gmail.com"
my_password = "######" # If using SMPT
sendGridToken = "######"  # if using Send Grid


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
                content = f.read()
                content = content.replace("[NAME]", birthday_person["name"])
                subject = "Feliz aniversário! Happy Birthday!"
                send_msg = ("Subject:" + str(subject) + "\n\n" + str(content)).encode('utf-8')
                address = birthday_person["email"] + "," + cc_email
                # 4. Send the letter generated in step 3 to that person's email address.
                if send_email.sendgrid_enabled == 1:
                    send_email.send_grid_email(input_mail_subject=subject, input_send_msg=content, input_to_email=address,
                                               input_my_email=my_email, input_sendGridToken=sendGridToken)
                else:
                    send_email.send_email(input_to_email=address, input_send_msg=send_msg, input_my_email=my_email,
                                          input_my_password=my_password)


select_birthday()
