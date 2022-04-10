# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-09

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 53 - SF Renting Research

GOOGLE_FORM_URL = "https://docs.google.com/forms/######"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

WAIT_TIME = 2

class GoogleFormBot:
    def __init__(self):
        # Start Chrome Driver
        self.url = GOOGLE_FORM_URL
        self.s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.maximize_window()

    def fill_form(self, input_answer1, input_answer2, input_answer3):
        # Go to form URL
        self.driver.get(self.url)
        print("Going to " + self.url)
        time.sleep(WAIT_TIME)

        # Answer questions
        question_boxes = self.driver.find_elements(By.CLASS_NAME, "whsOnd.zHQkBf")
        question_boxes[0].send_keys(input_answer1)
        question_boxes[1].send_keys(input_answer2)
        question_boxes[2].send_keys(input_answer3)
        time.sleep(WAIT_TIME)

        # Submit
        submit_button = self.driver.find_element(By.CLASS_NAME, "NPEfkd.RveJvd.snByac")
        submit_button.click()
        time.sleep(WAIT_TIME)