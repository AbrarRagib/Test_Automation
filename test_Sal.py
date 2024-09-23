from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your ChromeDriver
driver_path = r"C:\Users\User\Desktop\Selenium_Py\chromedriver.exe"

# Set up the Chrome WebDriver
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open Google
    driver.get("https://www.google.com")
    
    # Locate the search box using its name attribute value
    search_box = driver.find_element(By.NAME, "q")
    
    # Type in the search term
    search_box.send_keys("Selenium WebDriver")
    
    # Press Enter
    search_box.send_keys(Keys.RETURN)
    
    # Wait for the results to load
    time.sleep(3)
    
    # Print the title of the results page
    print(driver.title)

finally:
    # Close the browser
    driver.quit()
