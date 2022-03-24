# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-23

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 37 - Habit Tracker

import requests
from datetime import datetime

token_input = "######"
username_input = "######"
agreetos_input = "yes"
notminor_input = "yes"

pixela_url = "https://pixe.la/v1/"
graph_id = "graph1"


# Create Pixela user
def create_user():
    pixela_endpoint = pixela_url + "users"
    print(pixela_endpoint)
    parameters = {
        "token": token_input,
        "username": username_input,
        "agreeTermsOfService": agreetos_input,
        "notMinor": notminor_input
    }
    response = requests.post(url=pixela_endpoint, json=parameters)
    print(response)
    print(response.text)


# create_user()

# Create graph
def create_graph():
    pixela_endpoint = pixela_url + "users/" + username_input + "/graphs"
    print(pixela_endpoint)
    parameters = {
        "id": graph_id,
        "name": "Cycling",
        "unit": "Km",
        "type": "float",
        "color": "sora",
    }
    headers = {
        "X-USER-TOKEN": token_input
    }
    response = requests.post(url=pixela_endpoint, json=parameters, headers=headers)
    print(response)
    print(response.text)


# create_graph()

# Add Pixel
def add_pixel():
    pixela_endpoint = pixela_url + "users/" + username_input + "/graphs/" + graph_id
    print(pixela_endpoint)
    parameters = {
        "date": datetime.today().strftime('%Y%m%d'),
        "quantity": input("How many km did you cycle?"),
    }
    headers = {
        "X-USER-TOKEN": token_input
    }
    response = requests.post(url=pixela_endpoint, json=parameters, headers=headers)
    print(response)
    print(response.text)


add_pixel()

# Update a Pixel
def update_pixel():
    pixela_endpoint = pixela_url + "users/" + username_input + "/graphs/" + graph_id + "/" + datetime.today().strftime(
        '%Y%m%d')
    print(pixela_endpoint)
    parameters = {
        "quantity": "40"
    }
    headers = {
        "X-USER-TOKEN": token_input
    }
    response = requests.put(url=pixela_endpoint, json=parameters, headers=headers)
    print(response)
    print(response.text)


# update_pixel()

# Delete a pixel
def delete_pixel():
    pixela_endpoint = pixela_url + "users/" + username_input + "/graphs/" + graph_id + "/" + datetime.today().strftime(
        '%Y%m%d')
    print(pixela_endpoint)
    headers = {
        "X-USER-TOKEN": token_input
    }
    response = requests.delete(url=pixela_endpoint, headers=headers)
    print(response)
    print(response.text)


#delete_pixel()
