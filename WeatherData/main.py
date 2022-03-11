# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-10

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 25 - Weather Data

import csv
import pandas

def read_weather_csv():
    # Open weather_data.csv and store values
    with open("weather_data.csv", mode="r") as f:
        weather_data = csv.reader(f)
        # Skip first row
        next(weather_data)
        temperatures = []
        print("Weather Data:")
        for i in weather_data:
            print(i)
            # Make a list with temperatures
            new_temperature = int(i[1])
            temperatures.append(new_temperature)
        print("Temperature list:")
        print(temperatures)

        return weather_data

def celsius_to_fahrenheit(input_temperature):
    fahrenheit = input_temperature * (9/5) + 32
    return fahrenheit

def read_weather_pandas():
    # Open weather_data.csv
    df = pandas.read_csv("weather_data.csv")
    # Print values
    print(df)
    # Print temperatures
    print(df["temp"])
    # Create dictionary
    df_dict = df.to_dict()
    print(df_dict)
    # Create list
    df_list = df["temp"].to_list()
    print(df_list)
    # Average temperature
    print("Average temperature:")
    print(round(df["temp"].mean(),1))
    # Maximum temperature
    print("Maximum temperature:")
    print(round(df["temp"].max(),1))
    # Get data from row
    print("Monday data:")
    print((df[df.day == "Monday"]))
    # Data at maximum temperature
    print("Data at maximum temperature:")
    print(df.loc[df["temp"].idxmax()])
    # Get day on monday
    monday = df[df.day == "Monday"]
    print("Monday condition:")
    print(monday.condition)
    # Convert Celsius to Fahrenheit
    fahrenheit_temp = celsius_to_fahrenheit(monday.temp)
    print("In Fahrenheit:")
    print(fahrenheit_temp)

def create_df():
    # Create a dataframe from stratch
    data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }

    df = pandas.DataFrame(data_dict)
    print(df)
    df.to_csv("new_data.csv")

read_weather_pandas()
create_df()
