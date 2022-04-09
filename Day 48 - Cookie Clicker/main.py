# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-05

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 48 - Cookie Clicker

# initial wait time (seconds) before attempting to upgrade/buy items
wait_time = 0.1
# Progressive increase based on price
wait_time_vs_price_dictionary = {
    50: 0.5,
    100: 1,
    1000: 10,
    10000: 20,
    100000: 30,
    1000000: 40,
    10000000: 50,
    100000000: 60,
    1000000000: 120,
    10000000000: 240
}

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time
import random

# Start Chrome Driver
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

# Go to Cookie Clicker game
url = "https://orteil.dashnet.org/cookieclicker/"
driver.get(url)
driver.maximize_window()

# Find cookie
big_cookie = driver.find_element_by_id("bigCookie")

# Timer
timeout = time.time() + wait_time
five_min = time.time() + 60 * 5  # 5 minutes


# Fix number formats - is called when units turn to millions/billions/trillions
def replace_decimals(input_number) -> int:
    output_number = str(input_number)
    if "," in output_number:
        output_number = str(input_number.replace(",", ""))
    if "million" in str(output_number):
        output_number = str(output_number).replace(" million", "")
        output_number = int(round(float(output_number) * 1000000, 0))
    if "billion" in str(output_number):
        output_number = str(output_number).replace(" billion", "")
        output_number = int(round(float(output_number) * 1000000000, 0))
    if "trillion" in str(output_number):
        output_number = str(output_number).replace(" trillion", "")
        output_number = int(round(float(output_number) * 1000000000000, 0))
    return int(output_number)


# 5 minute report - will give performance in cookies per second (cps)
report = True

while True:
    # Click on the cookie; Exception handling enabled because this action may fail eventually
    try:
        big_cookie.click()
    except:
        pass

    # Buy upgrades and store items based on timer
    if time.time() > timeout:

        # Perform affordable upgrades - all enabled elements are affordable, no need to check
        try:
            upgrades = driver.find_elements_by_css_selector("div.crate.upgrade.enabled")
            for i in upgrades:
                try:
                    i.click()
                except:
                    pass
        except NoSuchElementException:
            pass

        # Buy store items - all enabled elements are affordable, no need to check
        store_elements = driver.find_elements_by_css_selector("div.product.unlocked.enabled")
        store_prices = driver.find_elements_by_css_selector("div.product.unlocked.enabled div.content span.price")

        item_elements = []
        for i in store_elements:
            item_elements.append(i)

        item_prices = []
        for i in store_prices:
            cost = replace_decimals(i.text)
            item_prices.append(cost)

        # Create dictionary of store items and prices
        store_elements_dict = dict(zip(item_elements, item_prices))

        # Purchase a random item out of the 3 most expensive items that we can afford
        try:
            random_item, random_price = random.choice(list(store_elements_dict.items())[-3:])
            random_item.click()
        except IndexError:
            pass

        # Change wait time depending on the least expensive item out of the 3 most expensive items that we can afford
        try:
            least_expensive_price = min(item_prices[-3:])
            for (key, value) in wait_time_vs_price_dictionary:
                if least_expensive_price > key:
                    wait_time = value
                    print("Wait time: " + str(wait_time) + " seconds")
        except:
            pass

        # Add wait_time until the next check
        timeout = time.time() + wait_time

    # After 5 minutes, issue report
    if time.time() > five_min:
        if report:
            cps = driver.find_element_by_css_selector("div.focusLeft div.inset div.title")
            print(cps.text)
            report = False
            # Uncomment to stop after 5 minutes
            # break

driver.quit()
