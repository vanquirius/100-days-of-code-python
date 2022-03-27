# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-27

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 47 - Amazon Price Tracker

import requests
import lxml
from bs4 import BeautifulSoup
import send_email

# Credentials for E-Mail
my_email = "######"
my_password = "######" # If using SMPT
sendGridToken = "######"  # if using Send Grid

target_price = 75

# URL of Product
url = "https://www.amazon.com/XOSS-Computer-Speedometer-Waterproof-Bluetooth/dp/B07XDSPXR4/ref=sr_1_1?qid=1648414926"

# Get data from URL
def get_data_from_url():
    url = "https://www.amazon.com/XOSS-Computer-Speedometer-Waterproof-Bluetooth/dp/B07XDSPXR4/ref=sr_1_1?qid=1648414926"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    response = requests.get(url, headers=headers)
    webpage = response.content
    soup = BeautifulSoup(webpage, "lxml")
    return soup

soup = get_data_from_url()

def parse_price(input_soup):
    price = input_soup.find(class_="a-offscreen").get_text()
    price_without_currency = price.split("$")[1]
    price_as_float = float(price_without_currency)
    return price_as_float

price = parse_price(soup)
print("Price: " + str(price))

def notify_price(input_price):
    subject = "Good price offer found on Amazon"
    message = "Price is now at " + str(input_price) + "!"
    content = message
    send_msg = ("Subject:" + str(subject) + "\n\n" + str(content)).encode('utf-8')

    if send_email.sendgrid_enabled == 1:
        send_email.send_grid_email(input_mail_subject=subject, input_send_msg=content, input_to_email=my_email,
                                   input_my_email=my_email, input_sendGridToken=sendGridToken)
    else:
        send_email.send_email(input_to_email=my_email, input_send_msg=send_msg, input_my_email=my_email,
                              input_my_password=my_password)

if price < target_price:
    notify_price(price)
    print("E-Mail notification sent!")