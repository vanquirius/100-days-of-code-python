# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-25

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 40 - Flight Club

# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from data_manager import DataManager
from flight_search import FlightSearch
from enroll import Enroll

enroll = Enroll()
data_manager = DataManager()
flight_search = FlightSearch()

# To enroll new users
# print(enroll.add_new_user())
# print(enroll.get_user_data())

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


# update_iata_code()

# Search for flights and compare to prices
def search_and_compare():
    for row in sheet_data:
        try:
            # Search flights via API
            flight_data = flight_search.get_flight_price(row["iataCode"])
            # Function returns true if flights were found; otherwise we can stop
            if flight_data:
                if flight_data.price < row["lowestPrice"]:
                    print("Offer found! " + str(row["city"]) + " R$ " + str(flight_data.price))
                    # Creates message with offers
                    from notification_manager import NotificationManager
                    notification = NotificationManager()
                    message = "Low price alert! Only R$ " + str(flight_data.price) + " to fly from " + \
                              str(flight_data.origin_airport) + " - " + str(flight_data.origin_city) + " to " + \
                              str(flight_data.destination_airport) + " - " + str(flight_data.destination_city) + \
                              ", from " + str(flight_data.out_date) + " to " + str(flight_data.return_date) + "."
                    if flight_data.stop_overs > 0:
                        message += " 1 stop in " + flight_data.via_city + "."
                    print(message)
                    # Sends message via SMS
                    notification.notify_sms(message)
                    # Sends message via E-Mail
                    notification.get_user_emails()
                    for i in notification.user_emails:
                        notification.notify_email(message, i)
                else:
                    print("No offer found")
        except TypeError:
            print("No offer found")


search_and_compare()
