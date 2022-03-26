# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-25

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 40 - Flight Club

import requests

SHEETY_USERS_ENDPOINT = "https://api.sheety.co/######/flightDeals/users"
sheety_api_key = "######"
headers = {"Authorization": "Bearer " + sheety_api_key}

class Enroll:

    def get_user_data(self):
        # Get data from sheety
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=headers)
        self.user_data = response.json()
        print(self.user_data)
        return self.user_data

    def add_new_user(self):
        # Get data from user
        self.first_name = input("What is your first name:")
        self.last_name = input("What is your last name:")
        def ask_email():
            email1 = input("Please enter your E-Mail:")
            email2 = input("Confirm your E-Mail:")
            if email1 == email2:
                return email1
            else:
                ask_email()
        self.email = ask_email()
        print("Thanks, you are in the club!")

        # Upload data to sheety
        sheet_inputs = {
            "user": {
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.email
            }
        }
        response = requests.post(url=SHEETY_USERS_ENDPOINT, json=sheet_inputs, headers=headers)
        print(response)
        print(response.text)
        self.upload_data = response.json()
        return self.first_name, self.last_name, self.email, self.upload_data