# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-27

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 48 - Cookie Clicker

from selenium import webdriver

# Path for Selenium Chrome Driver
chrome_driver_path = "######\\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get()

driver.quit()