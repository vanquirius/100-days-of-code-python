# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-02

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 48 - Cookie Clicker

from selenium import webdriver

# Path for Selenium Chrome Driver
chrome_driver_path = "D:\\Users\\Marcelo\\Documents\\Code\\chromedriver.exe"

# Fake credentials to test
first_name = "abc"
last_name = "efg"
email = "abc@efg.com"

# Start Chrome Driver
driver = webdriver.Chrome(chrome_driver_path)

url = "https://secure-retreat-92358.herokuapp.com/"
driver.get(url)

# First name field
first_name_field = driver.find_element_by_name("fName")
first_name_field.send_keys(first_name)

# Last name field
last_name_field = driver.find_element_by_name("lName")
last_name_field.send_keys(last_name)

# E-mail field
email_field = driver.find_element_by_name("email")
email_field.send_keys(email)

# Send button
send_button = driver.find_element_by_css_selector("form button")
send_button.click()

# Stop Chrome Driver
#driver.quit()
