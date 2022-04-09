# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-05

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 49 - LinkedIn Job Applier

# Credentials
login = "######"
password = "######"

# Path for Selenium Chrome Driver
chrome_driver_path = "######\\chromedriver.exe"

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time

# Start Chrome Driver
driver = webdriver.Chrome(chrome_driver_path)
driver.maximize_window()

# LinkedIn URL data
linkedin_url = "https://www.linkedin.com/"
job_search_url = "jobs/search/?"
easy_apply = "f_AL=true"  # Easy Apply
job_title = "keywords=head%20of%20product"  # Head of Product
location = "location=Orlando"  # Orlando
published_time = "f_TPR=r2592000"  # last month
experience_level = "f_E=5%2C6"  # top 2 tiers
search_url = linkedin_url + job_search_url + easy_apply + "&" + job_title + "&" + location + "&" + published_time + "&" + experience_level

# Go to LinkedIn Homepage
driver.get(linkedin_url)

# Enter credentials
time.sleep(1)
login_box = driver.find_element_by_id("session_key")
login_box.send_keys(login)
password_box = driver.find_element_by_id("session_password")
password_box.send_keys(password)
signin_button = driver.find_element_by_class_name("sign-in-form__submit-button")
signin_button.click()

# Wait 30 seconds for two-factor authentication
time.sleep(30)

# Go to job search page
driver.get(search_url)

# Get all jobs available
jobs_available = driver.find_elements_by_css_selector(".job-card-container--clickable")

for i in jobs_available:
    # Click on each job
    i.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        submit_button = driver.find_element_by_css_selector("footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        try:
            if submit_button.get_attribute("data-control-name") == "continue_unify":
                close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
                close_button.click()
                time.sleep(2)
                discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
                discard_button.click()
                print("Complex application, skipped.")
                continue
            else:
                submit_button.click()
        except StaleElementReferenceException:
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[3]/button[1]/span")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
