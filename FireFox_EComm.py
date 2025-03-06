from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up Firefox WebDriver
driver = webdriver.Firefox()

try:
    # Open SauceDemo website
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Find the username input field and enter a value
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")

    # Find the password field and enter a value
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")

    # Find the login button and click it
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Wait for some time to observe the result
    time.sleep(5)

    # Verify login success by checking if the products page is displayed
    if "inventory" in driver.current_url:
        print("Login Test Passed!")
    else:
        print("Login Test Failed!")

finally:
    # Close the browser
    driver.quit()
