# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-09

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 52 - Instagram Follower Bot Account

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

WAIT_TIME = 5

class InstagramBot:
    def __init__(self, input_user, input_password, input_account_to_follow):
        # Start Chrome Driver
        self.url = "https://www.instagram.com/"
        self.url_account_to_follow = self.url + input_account_to_follow
        self.s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.maximize_window()
        self.user = input_user
        self.password = input_password
        self.account_to_follow = input_account_to_follow

    def login(self):
        # Login into Instagram
        self.driver.get(self.url)
        print("Going to " + self.url)
        time.sleep(WAIT_TIME)

        # Instagram Classes
        do_not_save_class = "sqdOP.yWX7d.y3zKF"
        do_not_notify_class = "aOOlW.HoLwm"

        # Fill username and password
        username_box = self.driver.find_element(By.NAME, "username")
        username_box.send_keys(self.user)
        print("Typing username")
        time.sleep(WAIT_TIME)
        password_box = self.driver.find_element(By.NAME, "password")
        password_box.send_keys(self.password)
        print("Typing password")
        time.sleep(WAIT_TIME)
        password_box.send_keys(Keys.RETURN)
        time.sleep(WAIT_TIME)

        # Do not save login information
        do_not_save_button = self.driver.find_element(By.CLASS_NAME, do_not_save_class)
        do_not_save_button.click()
        print("Do not save login information")
        time.sleep(WAIT_TIME)

        # Do not send notifications
        do_not_notify_button = self.driver.find_element(By.CLASS_NAME, do_not_notify_class)
        do_not_notify_button.click()
        print("Do not send notifications")
        time.sleep(WAIT_TIME)

    def find_followers(self):
        # Instagram Classes
        followers_xpath = "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div"
        scroll_down_xpath = "/html/body/div[6]/div/div/div/div[2]"  # this is the div for the pop-up frame and can be inspected

        # Go to account to follow
        self.driver.get(self.url_account_to_follow)
        print("Going to " + self.url_account_to_follow)
        time.sleep(WAIT_TIME)

        # Click on followers
        followers_button = self.driver.find_element(By.XPATH, followers_xpath)
        followers_button.click()
        print("Looking at the followers")
        time.sleep(WAIT_TIME)

        # Scroll down as much as possible
        modal = self.driver.find_element(By.XPATH, scroll_down_xpath)
        for i in range(10):
            try:
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                time.sleep(WAIT_TIME)
            except NoSuchElementException:
                pass

    def follow_the_followers(self):
        # Instagram Classes
        follow_buttons_css = "li button"
        cancel_xpath = "/html/body/div[5]/div/div/div/div[3]/button[2]"

        # Follow the followers
        print("Following the followers")
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, follow_buttons_css)
        for i in follow_buttons:
            try:
                i.click()
                time.sleep(WAIT_TIME)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, cancel_xpath)
                cancel_button.click()

        print("Done following!")
