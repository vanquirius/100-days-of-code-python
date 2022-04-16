# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-25

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 40 - Flight Club

import requests
from datetime import datetime
from dateutil.relativedelta import *
from flight_data import FlightData
import os

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")
city_from = "GRU"  # Guarulhos Airport - São Paulo, SP, Brazil Area


class FlightSearch:

    def get_destination_code(self, city_name):
        # Get data from Tequila
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def get_flight_price(self, city_name):
        # Get data from Tequila
        location_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": city_from,
            "fly_to": city_name,
            "dateFrom": datetime.now().strftime("%d/%m/%Y"),  # Starting today
            "dateTo": (datetime.now() + relativedelta(months=+6)).strftime("%d/%m/%Y"),  # 6 months from today
            "curr": "BRL",  # Currency = Brazilian Reais
            "nights_in_dst_from": 7,  # At least 7 days round trip
            "nights_in_dst_to": 28,  # At most 28 days round trip
            "flight_type": "round",  # Roundtrip
            "one_for_city": 1,
            "max_stopovers": 0
        }
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        try:
            data = response.json()["data"][0]
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(url=location_endpoint, headers=headers, params=query)
            try:
                data = response.json()["data"][0]
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
            except IndexError:
                print(f"No flights found for {city_name}.")
                return False



        print(f"{flight_data.destination_city}: BRL {flight_data.price}")
        return flight_data
