# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-25

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 39 - Flight Deal Finder

# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_destination_data()
print("Sheet data:")
print(sheet_data)


#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.
def update_iata_code():
    if sheet_data[0]["iataCode"] == "":
        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_code(row["city"])
        print(f"sheet_data:\n {sheet_data}")

        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()
        print("IATA codes updated.")
        return


update_iata_code()

# Search for flights and compare to prices
def search_and_compare():
    for row in sheet_data:
        try:
            price, out_date, return_date = flight_search.get_flight_price(row["iataCode"])
            if price < row["lowestPrice"]:
                print("Offer found! " + str(row["city"]) + " R$ " + str(price))
                from notification_manager import NotificationManager
                notification = NotificationManager()
                message = "Low price alert! Only R$ " + str(price) + " to fly from São Paulo to " + str(row["city"]) + \
                          ", from " + str(out_date) + " to " + str(return_date) + "."
                notification.notify_sms(message)
            else:
                print("No offer found")
        except TypeError:
            print("No offer found")

search_and_compare()
