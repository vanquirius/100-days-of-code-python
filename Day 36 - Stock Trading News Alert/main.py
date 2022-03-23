# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-21

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 36 - Stock Trading News Alert

import requests
from datetime import datetime
from twilio.rest import Client

STOCK = "VT"
COMPANY_NAME = "Vanguard Total World Stock Index ETF"
DELTA_WARNING = (5 / 100)

# API keys for Alpha Vantage and Twilio
alpha_vantage_api_key = "######"
news_api_key = "######"
account_sid = "######"
auth_token = "######"
twilio_phone_number = "######"
to_phone_number = "######"

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
    print("Yesterday price: " + str(yesterday_closing_price))

    day_before_yesterday_data = data_list[1]
    day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
    print("Day before yesterday price: " + str(day_before_yesterday_closing_price))

    delta_stock_price = (float(yesterday_closing_price) / float(day_before_yesterday_closing_price) - 1)
    return delta_stock_price


# get_stock_data()

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
    articles = []
    for i in range(0, 2):
        add_article = ""
        try:
            add_article = data[i]["title"]
        except IndexError:
            pass
        articles.append(add_article)
    print(articles)
    return articles


get_news()

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

# if abs(delta_stock_price) > DELTA_WARNING:
#    print("Variation above " + str(DELTA_WARNING * 100) + "% - Get News")

# else:
#    print("Variation below " + str(DELTA_WARNING * 100) + "% - Do not get news")

#    return 0


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
