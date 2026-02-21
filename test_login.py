from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os

screenshot_folder = "Screenshots"
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

driver = webdriver.Chrome()
print("Browser Opened ✅")

driver.get("https://practicetestautomation.com/practice-test-login/")
print("Navigating to login page ✅")
time.sleep(2)

driver.save_screenshot(os.path.join(screenshot_folder, "home.png"))

try:
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    print("Clicking Login button ✅")

    time.sleep(3)
    driver.save_screenshot(os.path.join(screenshot_folder, "after_login.png"))

    print("Test Passed ✅")

except NoSuchElementException:
    print("Test Failed ❌ Element not found")
    driver.save_screenshot(os.path.join(screenshot_folder, "error.png"))

finally:
    driver.quit()
    print("Browser Closed ✅")