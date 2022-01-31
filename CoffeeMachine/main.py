# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-01-30

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 15 - Coffee Machine

# print debug (must be 1 to print)
verbose = 0

class colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    ENDC = '\033[m'

# Data provided by the exercise

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
    raw_user_input = input(colors.BLUE + "What would you like? (expresso, latte, cappuccino)" + colors.ENDC)
    # Validate user input
    if raw_user_input not in ("expresso", "latte", "cappuccino", "off", "report"):
        print(colors.RED + "Invalid option. Please choose again between expresso, latte and cappuccino." + colors.ENDC)
        raw_user_input = capture_user_input()
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
    enough_resources = 1
    if input_resources.get("water") < water:
        print("Sorry, there is not enough water.")
        enough_resources = 0
    if input_resources.get("milk") < milk:
        print("Sorry, there is not enough milk.")
        enough_resources = 0
    if input_resources.get("coffee") < coffee:
        print("Sorry, there is not enough coffee.")
        enough_resources = 0
    if enough_resources == 1 and verbose == 1:
        print("Resources are enough.")
    return enough_resources

# Requirement 5: Process Coins
def process_coins():
  def collect_quarters():
      quarters = 0
      try:
          quarters = int(input("How many quarters?"))
      except:
          collect_quarters()
      if quarters is None:
        quarters = 0
      if quarters < 0:
        collect_quarters()
      return quarters
  quarters = collect_quarters()

  def collect_dimes():
      dimes = 0
      try:
          dimes = int(input("How many dimes?"))
      except:
          collect_dimes()
      if dimes is None:
        dimes = 0
      if dimes < 0:
        collect_dimes()
      return dimes
  dimes = collect_dimes()

  def collect_nickels():
      nickels = 0
      try:
          nickels = int(input("How many nickels?"))
      except:
          collect_nickels()
      if nickels is None:
        nickels = 0
      if nickels < 0:
        collect_nickels()
      return nickels
  nickels = collect_nickels()

  def collect_pennies():
      pennies = 0
      try:
          pennies = int(input("How many pennies?"))
      except:
          collect_pennies()
      if pennies is None:
        pennies = 0
      if pennies < 0:
        collect_pennies()
      return pennies
  pennies = collect_pennies()

  deposit = round(quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01,2)

  if verbose == 1:
    print("Deposited value is $" + str(deposit))

  return deposit

# Requirement 6: Check transaction successful
def check_transaction(input_user_input, input_menu, input_deposit):
  # Get cost from menu
  cost = input_menu.get(input_user_input).get("cost")
  # Validate cost
  if cost < 0 or cost is None:
      raise ValueError("Invalid cost in menu, please verify.")
  if verbose == 1:
    print("Cost is : $" + str(cost))
  # Process transaction
  transaction_success = 1
  if cost == input_deposit:
    if verbose == 1:
      print("Cost and deposit are the same, no change given.")
      change = 0
  elif cost > input_deposit:
    transaction_success = 0
    print("Sorry, that is not enough money. Money refunded.")
  else:
    change = round(input_deposit - cost, 2)
    print("Change of $" + str(change) + " given out.")
  
  return cost, transaction_success

# Requirement 7: Make Coffee
def make_drink(input_user_input):
  print("Here is your " + input_user_input + ". Enjoy!")

# Runtime
print(colors.GREEN + "Coffee Machine" + colors.ENDC)

if verbose == 1:
    print("Running Coffee Machine program with verbose output")
    print("Available resources")
    print(resources)
    print("Money: $" + str(money))

while(True):
  user_input = capture_user_input()
  if user_input == "off":
      turn_off_coffee_machine()
  if user_input == "report":
      generate_report(resources, money)
  if user_input in ("expresso", "latte", "cappuccino"):
      enough_resources = check_resources_sufficient(MENU, resources, user_input)
      if enough_resources == 1:
        deposit = process_coins()
        money_add, transaction_success = check_transaction(user_input, MENU, deposit)
        money = money + money_add
        if transaction_success == 1:
          make_drink(user_input)