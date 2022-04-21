# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-10

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 50 - Auto Tinder Swiping Bot

# We are using undetected_chromedriver to be able to login into Google Accounts without being called out as a bot
import undetected_chromedriver as uc
import time

from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
import random
import os

TINDER_USER = os.getenv("TINDER_USER")
TINDER_PASSWORD = os.getenv("TINDER_PASSWORD")

WAIT_TIME = 10
WAIT_TIME_SHORT = 4

# Settings
google_url = "https://accounts.google.com/servicelogin"
tinder_url = "https://tinder.com/"
user = TINDER_USER
password = TINDER_PASSWORD

# Tinder and Google Classes
login_xpath = "//*[text()='Log in']"
login_google_xpath = "/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[1]/div/button"
username_class = "whsOnd.zHQkBf"
password_class = "whsOnd.zHQkBf"  # Same, but here for flexibility if anything changes in the future
next_button_class = "VfPpkd-vQzf8d"
allow_location_xpath = "/html/body/div[2]/div/div/div/div/div[3]/button[1]/span"
notification_xpath = '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]'
like_xpath = "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span/svg/path"
dislike_xpath = "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button/span/span/svg"
profile_xpath = "/html/body/div[1]/div/div[1]/div/aside/div/a/div/div"
logout_xpath = "/html/body/div[1]/div/div[1]/div/aside/nav/div/div/div/div/div/div/div[20]/div/div/div/div"
confirm_logout_xpath = "/html/body/div[2]/div/div/div[2]/button[1]"
accept_cookies_xpath = "/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/span"

# Start Chrome Driver
if __name__ == '__main__':
    chrome_options = uc.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 1,
        "profile.default_content_setting_values.geolocation": 1,
    })

    driver = uc.Chrome(options=chrome_options)
    driver.maximize_window()

    # Login to Google
    driver.get(google_url)
    print("Going to " + google_url)
    time.sleep(WAIT_TIME_SHORT)

    username_box = driver.find_element(By.CLASS_NAME, username_class)
    username_box.send_keys(user)
    print("Typing username")
    next_button = driver.find_element(By.CLASS_NAME, next_button_class)
    next_button.click()
    time.sleep(WAIT_TIME_SHORT)
    password_box = driver.find_element(By.CLASS_NAME, password_class)
    password_box.send_keys(password)
    print("Typing password")
    time.sleep(WAIT_TIME_SHORT)
    next_button = driver.find_element(By.CLASS_NAME, next_button_class)
    next_button.click()
    time.sleep(WAIT_TIME_SHORT)

    # Login into Tinder
    driver.get(tinder_url)
    print("Going to " + tinder_url)
    time.sleep(WAIT_TIME)

    # Accept cookies
    print("Accepting cookies")
    login_button = driver.find_element(By.XPATH, accept_cookies_xpath)
    login_button.click()
    time.sleep(WAIT_TIME_SHORT)

    # Click on login button, then login with Google
    print("Logging in into Tinder")
    login_button = driver.find_element(By.XPATH, login_xpath)
    login_button.click()
    time.sleep(WAIT_TIME)
    login_with_google_button = driver.find_element(By.XPATH, login_google_xpath)
    login_with_google_button.click()
    time.sleep(WAIT_TIME)

    # Allow location to be shared
    try:
        allow_location_button = driver.find_element(By.XPATH, allow_location_xpath)
        allow_location_button.click()
        print("Allowing location to be shared")
        time.sleep(WAIT_TIME)
        try:
            # Click on pop up to accept
            driver.switch_to().alert().accept()  # switchTo depending on the version
            time.sleep(WAIT_TIME)
        except TypeError:
            pass
    except NoSuchElementException:
        pass

    # Notification button
    try:
        notification_button = driver.find_element(By.XPATH, notification_xpath)
        notification_button.click()
        print("Pressed notification button")
    except NoSuchElementException:
        pass

    # Randomly like of dislike (loop of count_profiles profiles)
    count_profiles = 10
    for i in range(1, 10):
        throw_dice = random.randint(1, 3)
        if throw_dice == 1:
            try:
                choice_xpath = like_xpath
                print("Clicking like")
            # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
            except ElementClickInterceptedException:
                try:
                    match_popup = driver.find_element_by_css_selector(".itsAMatch a")
                    match_popup.click()
                # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
                except NoSuchElementException:
                    time.sleep(WAIT_TIME)
        else:
            choice_xpath = dislike_xpath
            print("Clicking dislike")
        choice_button = driver.find_element(By.XPATH, choice_xpath)
        choice_button.click()
        time.sleep(WAIT_TIME)

    # Log out
    profile_button = driver.find_element(By.XPATH, profile_xpath)
    profile_button.click()
    time.sleep(WAIT_TIME)

    logout_button = driver.find_element(By.XPATH, logout_xpath)
    logout_button.click()
    time.sleep(WAIT_TIME)

    confirm_logout_xpath = driver.find_element(By.XPATH, logout_xpath)
    confirm_logout_xpath.click()
