# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-01-30

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 15 - Coffee Machine

# Data provided by the exercise

# print comments
verbose = 1

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Prompt user by asking "What would you like?"

def capture_user_input():
    # Prompt user for input
    raw_user_input = input("What would you like? (expresso, latte, cappuccino)")
    # Validate user input
    if raw_user_input not in ("expresso", "latte", "cappuccino", "off", "report"):
        print("Invalid option. Please choose again between expresso, latte and cappuccino.")
        raw_user_input = capture_user_input()
    else:
        print("You chose " + raw_user_input + "!")
        return raw_user_input


# TODO 2: Turn off Coffee Machine by entering "off"
# TODO 3: Print report
# TODO 4: Check resources sufficient?
# TODO 5: Process coins
# TODO 6: Check transaction successful?
# TODO 7: Make Coffee

# Runtime
if verbose == 1:
    print(resources)
user_input = capture_user_input()
