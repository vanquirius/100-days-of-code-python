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
    "expresso": {
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

# Start money at $ 2.5
money = 2.5


# Requirement 1: Prompt user by asking "What would you like?"
def capture_user_input():
    # Prompt user for input
    raw_user_input = input("What would you like? (expresso, latte, cappuccino)")
    # Validate user input
    if raw_user_input not in ("expresso", "latte", "cappuccino", "off", "report"):
        print("Invalid option. Please choose again between expresso, latte and cappuccino.")
        raw_user_input = capture_user_input()
    elif raw_user_input in ("off", "report"):
        print("You chose the hidden option: " + raw_user_input + "!")
    else:
        print("You chose " + raw_user_input + "!")
    return raw_user_input


# Requirement 2: Turn off Coffee Machine
def turn_off_coffee_machine():
    print("Turning off Coffee Machine...")
    # Stops running program
    exit()


# Requirement 3: Print report
def generate_report(input_resources, input_money):
    # Validate data
    if input_resources.get("water") < 0 or input_resources.get("milk") < 0 or input_resources.get("coffee") < 0:
        raise ValueError("Invalid amount of resources in inventory, please verify.")
    # Report
    print("Water: " + str(input_resources.get("water")) + "ml")
    print("Milk: " + str(input_resources.get("milk")) + "ml")
    print("Coffee: " + str(input_resources.get("coffee")) + "gr")
    print("Money: $" + str(input_money))
    return


# Requirement 4: Check if resources are sufficient
def check_resources_sufficient(input_menu, input_resources, input_user_input):
    # Get necessary resources from menu
    water = input_menu.get(input_user_input).get("ingredients").get("water")
    if water is None:
        water = 0
    milk = input_menu.get(input_user_input).get("ingredients").get("milk")
    if milk is None:
        milk = 0
    coffee = input_menu.get(input_user_input).get("ingredients").get("coffee")
    if coffee is None:
        coffee = 0
    if verbose == 1:
        print("Necessary ingredients for " + input_user_input)
        print("Water: " + str(water) + "ml")
        print("Milk: " + str(milk) + "ml")
        print("Coffee: " + str(coffee) + "gr")
    # Validate menu
    if water < 0 or milk < 0 or coffee < 0:
        raise ValueError("Invalid amount of ingredients in menu, please verify.")
    # Check resources
    if verbose == 1:
        print("Verifying if resources are enough...")
    if input_resources.get("water") < water:
        print("Sorry, there is not enough water.")
    if input_resources.get("milk") < milk:
        print("Sorry, there is not enough milk.")
    if input_resources.get("coffee") < coffee:
        print("Sorry, there is not enough coffee.")

# Runtime
print("Coffee Machine")

if verbose == 1:
    print("Running Coffee Machine program with verbose output")
    print("Available resources")
    print(resources)
    print("Money: $" + str(money))

user_input = capture_user_input()
if user_input == "off":
    turn_off_coffee_machine()
if user_input == "report":
    generate_report(resources, money)
if user_input in ("expresso", "latte", "cappuccino"):
    check_resources_sufficient(MENU, resources, user_input)

# TODO 4: Check resources sufficient?
# TODO 5: Process coins
# TODO 6: Check transaction successful?
# TODO 7: Make Coffee
