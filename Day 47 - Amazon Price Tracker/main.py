# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-27

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 47 - Amazon Price Tracker

import requests
import lxml
from bs4 import BeautifulSoup
from send_email import SendEmail
import os

# Set as 1 to choose SendGrid over SMTP
sendgrid_enabled = 1

# E-Mail server settings
smtp_server = "smtp.gmail.com"  # if using SMTP
smtp_port = "587"  # if using SMTP

# Credentials
from_email = os.getenv("from_email")
sendGridToken = os.getenv("sendGridToken")  # If using SendGrid
email_password = os.getenv("email_password")  # If using SMTP
to_email = from_email

sendemail = SendEmail(from_email, smtp_server, smtp_port, email_password, sendGridToken)

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
    price_get = input_soup.find(class_="a-offscreen").get_text()
    price_without_currency = price_get.split("$")[1]
    price_as_float = float(price_without_currency)
    return price_as_float


price = parse_price(soup)
print("Price: " + str(price))


def notify_price(input_price):
    subject = "Good price offer found on Amazon"
    message = "Price is now at " + str(input_price) + "!"
    content = message
    send_msg = ("Subject:" + str(subject) + "\n\n" + str(content)).encode('utf-8')

    if sendgrid_enabled == 1:
        sendemail.send_grid_email(to_email, subject, content)
    else:
        sendemail.send_smtp_email(to_email, send_msg)


if price < target_price:
    notify_price(price)
    print("E-Mail notification sent!")
