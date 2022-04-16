# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-16

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 36 - Stock Trading News Alert

import requests
from datetime import datetime
from twilio_sms import SendSMS
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
DELTA_WARNING = (1 / 100)

# API keys for Alpha Vantage
alpha_vantage_api_key = os.getenv("alpha_vantage_api_key")
news_api_key = os.getenv("news_api_key")

# Account, token and phone number for Twilio
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
twilio_phone_number = os.getenv("twilio_phone_number")
twilio_sms = SendSMS(account_sid, auth_token, twilio_phone_number)

# Send SMS to this phone number
to_phone_number = os.getenv("to_phone_number")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stock_data():
    # Call Alpha Vantage API to get stock data
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": alpha_vantage_api_key
    }

    response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()
    data = response.json()

    # Filter out data
    data = data["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]
    yesterday_data = data_list[0]
    yesterday_closing_price = yesterday_data["4. close"]
    print("D-1 price: " + str(yesterday_closing_price))

    day_before_yesterday_data = data_list[1]
    day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
    print("D-2 price: " + str(day_before_yesterday_closing_price))

    delta_stock_price = (float(yesterday_closing_price) / float(day_before_yesterday_closing_price) - 1)
    return delta_stock_price


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

def get_news():
    # Today in Japanese data format
    today = datetime.today().strftime('%Y-%m-%d')

    # Call News API to get the news
    parameters = {
        "q": COMPANY_NAME,
        "from": today,
        "sortBy": "published",
        "apiKey": news_api_key
    }

    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()
    data = response.json()

    # Filter out data
    data = data["articles"]
    data = data[:3]
    return data


## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

def check_delta_and_alert():
    delta_stock_price = get_stock_data()
    if abs(delta_stock_price) > DELTA_WARNING:
        print("Variation above " + str(DELTA_WARNING * 100) + "% - Get News")
        articles = get_news()
        formatted_articles = [f"Title: {i['title']}. \nBrief: {i['description']}" for i in articles]
        print(formatted_articles)
        # Set sign for SMS
        sign = "🔺"
        if delta_stock_price < 0:
            sign = "🔻"
        for i in formatted_articles:
            message = str(STOCK) + ":" + str(sign) + str(round(abs(delta_stock_price) * 100, 1)) + "%\n" + i
            twilio_sms.send_sms(to_phone_number, message)
    else:
        print("Variation below " + str(DELTA_WARNING * 100) + "% - Do not get news")

check_delta_and_alert()