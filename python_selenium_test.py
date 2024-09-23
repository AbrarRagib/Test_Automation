from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to the downloaded chromedriver
driver_path = r"C:\Users\User\Desktop\Selenium_Py\chromedriver.exe"

# Use Service class to set the ChromeDriver path
service = Service(driver_path)

# Initialize ChromeDriver with the correct service
driver = webdriver.Chrome(service=service)

# Open a webpage
driver.get("https://www.google.com")


