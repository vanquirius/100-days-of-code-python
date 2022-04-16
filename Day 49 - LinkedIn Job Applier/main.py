# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-09

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 49 - LinkedIn Job Applier

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time
import os

# Credentials
login = os.getenv("login")
password = os.getenv("password")

# Start Chrome Driver
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

# LinkedIn URL data
linkedin_url = "https://www.linkedin.com/"
job_search_url = "jobs/search/?"
easy_apply = "f_AL=true"  # Easy Apply - this has to be enabled for this program
job_title = "keywords=head%20of%20product"  # Head of Product
location = "location=Orlando"  # Orlando
published_time = "f_TPR=r2592000"  # last month
experience_level = "f_E=5%2C6"  # top 2 tiers
search_url = linkedin_url + job_search_url + easy_apply + "&" + job_title + "&" + location + "&" + published_time + "&" + experience_level

# Go to LinkedIn Homepage
driver.get(linkedin_url)
print("Going to " + linkedin_url)

# Enter credentials in the login page
time.sleep(2)
login_box = driver.find_element(By.ID, "session_key")
login_box.send_keys(login)
password_box = driver.find_element(By.ID, "session_password")
password_box.send_keys(password)
signin_button = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button")
signin_button.click()
print("Credentials provided")

# Wait 30 seconds for two-factor authentication
time.sleep(30)
print("Assuming two-factor authentication was successful")

# Go to job search page
driver.get(search_url)
time.sleep(2)
print("Looking for job list")

# Get all jobs available
jobs_available = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable .job-card-container__link")
print("Obtaining job list")

# Application routine for jobs available
for i in jobs_available:
    # Click on each job
    i.click()
    print("Clicked on job from job list")
    time.sleep(2)

    # Click on Easy Apply
    easy_apply_button = driver.find_element(By.CSS_SELECTOR, "div.jobs-apply-button--top-card span.artdeco-button__text")
    easy_apply_button.click()
    print("Clicked on Easy Apply")
    time.sleep(2)

    # Try to press on next/review/submit button 5 times
    for i in range(1, 5):
        try:
            print("Trying to click next/review/submit")
            next_button = driver.find_element(By.CSS_SELECTOR, "div.display-flex span.artdeco-button__text")
            time.sleep(2)
        except:
            pass

time.sleep(5)
driver.quit()
