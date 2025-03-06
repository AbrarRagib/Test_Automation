from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up Firefox WebDriver
driver = webdriver.Firefox()

try:
    # Open the website
    driver.get("https://quiet-empanada-dd7f3d.netlify.app/training")
    driver.maximize_window()

    # Wait for elements to load
    time.sleep(2)

    # Fill out the form fields
    driver.find_element(By.ID, "firstName").send_keys("John")  # First Name
    driver.find_element(By.ID, "lastName").send_keys("Doe")    # Last Name
    driver.find_element(By.ID, "email").send_keys("johndoe@example.com")  # Email
    driver.find_element(By.ID, "phone").send_keys("1234567890")  # Phone Number
    driver.find_element(By.ID, "dateOfBirth").send_keys("01/15/1995")  # Date of Birth (MM/DD/YYYY format)

    # Submit the form (modify XPath if needed)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Wait for response or confirmation message
    time.sleep(3)

finally:
    # Close the browser
    driver.quit()
