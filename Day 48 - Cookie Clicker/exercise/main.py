# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-02

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 48 - Cookie Clicker

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Start Chrome Driver
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

url = "https://www.python.org"
driver.get(url)


# Find Upcoming Events on Python.Org page
def find_upcoming_events(input_driver):
    event_times = driver.find_elements_by_css_selector("div.event-widget li time")
    times = []
    for i in event_times:
        # 10 first characters of time string (YYYY-MM-DD)
        time = i.get_attribute("datetime")[0:10]
        times.append(time)

    event_names = driver.find_elements_by_css_selector("div.event-widget li a")
    names = []
    for i in event_names:
        name = i.text
        names.append(name)

    event_times_and_names = dict(zip(times, names))
    print(event_times_and_names)
    return driver


driver = find_upcoming_events(driver)

# Stop Chrome Driver
driver.quit()
