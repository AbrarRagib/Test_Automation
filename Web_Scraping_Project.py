from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
query = "laptop"
driver.get(f"https://www.amazon.com/s?k={query}&ref=nav_bb_sb")


driver.close()
