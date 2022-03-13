# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-02-05

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 16 - Coffee Machine OOP version

# print debug (must be 1 to print)
verbose = 0

class colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    ENDC = '\033[m'

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects
menulist = Menu()
latte = menulist.find_drink("latte")
espresso = menulist.find_drink("espresso")
cappuccino = menulist.find_drink("cappuccino")
coffeemachine = CoffeeMaker()
moneycontrol = MoneyMachine()


# Requirement 1: Prompt user by asking "What would you like?"
def capture_user_input(input_menulist):
    # Get list of available items
    availableitems = input_menulist.get_items()
    # Prompt user for input
    raw_user_input = input(colors.BLUE + "What would you like? (" + availableitems + ")" + colors.ENDC)
    # Validate user input
    if raw_user_input not in ("espresso", "latte", "cappuccino", "off", "report"):
        print(colors.RED + "Invalid option. Please choose again." + colors.ENDC)
        raw_user_input = capture_user_input(input_menulist)
    elif raw_user_input in ("off", "report"):
        if verbose == 1:
          print("You chose the hidden option: " + raw_user_input + "!")
    else:
        if verbose == 1:
          print("You chose " + raw_user_input + "!")
    return raw_user_input

# Requirement 2: Turn off Coffee Machine
def turn_off_coffee_machine():
    print(colors.RED + "Turning off Coffee Machine...")
    # Stops running program
    exit()

# Requirement 3: Print report
def generate_report(input_coffeemachine, input_moneycontrol):
  coffeemachine.report()
  moneycontrol.report()

# Requirement 4: Check if resources are sufficient
def check_resources_sufficient(input_latte, input_espresso, input_cappuccino, input_coffeemachine, input_user_input):
  enough_resources = False
  if input_user_input == "latte":
    enough_resources = input_coffeemachine.is_resource_sufficient(input_latte)
  if input_user_input == "espresso":
    enough_resources = input_coffeemachine.is_resource_sufficient(input_espresso)
  if input_user_input == "cappuccino":
    enough_resources = input_coffeemachine.is_resource_sufficient(input_cappuccino)  
  if verbose == 1:
    print("Enough resources:")
    print(enough_resources)
  return enough_resources

# Requirement 5: Process Coins
# Requirement 6: Check transaction successful
def process_payment(input_latte, input_espresso, input_cappuccino, input_moneycontrol, input_user_input):
  if input_user_input == "latte":
    cost = input_latte.cost
  if input_user_input == "espresso":
    cost = input_espresso.cost
  if input_user_input == "cappuccino":
    cost = input_cappuccino.cost
  payment = input_moneycontrol.make_payment(cost)
  return payment


#def check_transaction(input_user_input, input_menu, input_deposit):

# Requirement 7: Make Coffee
#def make_drink(input_user_input, input_menu, input_resources):

# Runtime
print(colors.GREEN + "Coffee Machine" + colors.ENDC)

if verbose == 1:
    print("Running Coffee Machine program with verbose output")

while(True):
  user_input = capture_user_input(menulist)
  if user_input == "off":
      turn_off_coffee_machine()
  if user_input == "report":
      generate_report(coffeemachine, moneycontrol)
  if user_input in ("espresso", "latte", "cappuccino"):
      enough_resources = check_resources_sufficient(latte, espresso, cappuccino, coffeemachine, user_input)
      if enough_resources == True:
        payment = process_payment(latte, espresso, cappuccino, moneycontrol, user_input)
        if payment == True:
          if user_input == "latte":
            coffeemachine.make_coffee(latte)
          if user_input == "espresso":
            coffeemachine.make_coffee(espresso)
          if user_input == "cappuccino":
            coffeemachine.make_coffee(cappuccino)