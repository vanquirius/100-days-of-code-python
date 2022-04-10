# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-09

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 51 - Internet Speed Twitter Complaint Bot

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        # Start Chrome Driver
        self.s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.maximize_window()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        # Go to Speed Test
        self.speedtest_url = "https://www.speedtest.net/"
        self.driver.get(self.speedtest_url)
        print("Going to " + self.speedtest_url)
        time.sleep(2)
        # Click on the go button
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        print("Speed test started")
        # Countdown
        print("1.5 minute left")
        time.sleep(30)
        print("1 minute left")
        time.sleep(30)
        print("30 seconds left")
        time.sleep(30)

        # Dismiss pop-up window
        try:
            dismiss_button = self.driver.find_element(By.CLASS_NAME, "notification-dismiss.close-btn")
            dismiss_button.click()
        except:
            pass
        time.sleep(2)

        # Get results
        up_class = ".result-item-download .result-data-large.number.result-data-value"
        down_class = ".result-item-upload .result-data-large.number.result-data-value"
        self.up = self.driver.find_element(By.CSS_SELECTOR, up_class).text
        self.down = self.driver.find_element(By.CSS_SELECTOR, down_class).text
        print("Upload speed: " + str(self.up))
        print("Download speed: " + str(self.down))
        return self.up, self.down

    def tweet_at_provider(self, input_username, input_twitter_name, input_password, input_up_speed, input_down_speed, input_promised_up,
                          input_promised_down):
        # Go to Twitter
        self.twitter_url = "https://twitter.com/login"
        self.driver.get(self.twitter_url)
        print("Going to " + self.twitter_url)
        time.sleep(2)

        # Classes to use with Twitter
        username_class = "r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu"
        twitter_name_class = "r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu"
        password_class = "r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu"
        textbox_class = "public-DraftStyleDefault-block.public-DraftStyleDefault-ltr"
        tweet_button_xpath = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span"

        # Username field
        username_box = self.driver.find_element(By.CLASS_NAME, username_class)
        username_box.send_keys(input_username)
        print("Typing username")
        time.sleep(1)
        username_box.send_keys(Keys.RETURN)
        time.sleep(2)

        # Twitter name - if there is a check
        try:
            twittername_box = self.driver.find_element(By.CLASS_NAME, twitter_name_class)
            twittername_box.send_keys(input_twitter_name)
            print("Typing twitter name")
            time.sleep(1)
            twittername_box.send_keys(Keys.RETURN)
            time.sleep(2)
        except:
            pass

        # Password field
        password_box = self.driver.find_element(By.CLASS_NAME, password_class)
        password_box.send_keys(input_password)
        print("Typing password")
        time.sleep(1)
        password_box.send_keys(Keys.RETURN)
        time.sleep(2)

        # Post on twitter
        message = "@ClaroBrasil, sou um bot. Meu dono contratou pacote com " + \
            str(input_promised_down) + " megas de download e " + str(input_promised_up) + \
            " megas de upload. O SpeedTest está mostrando " + str(input_down_speed) + " megas de download e " + \
            str(input_up_speed) + " megas de upload."
        print(message)

        # Textbox
        textbox = self.driver.find_element(By.CLASS_NAME, textbox_class)
        textbox.send_keys(message)
        time.sleep(3)

        # Tweet button
        tweet_button = self.driver.find_element(By.XPATH, tweet_button_xpath)
        tweet_button.click()
        print("Posted on Twitter!")