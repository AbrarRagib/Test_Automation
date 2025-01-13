from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Debug logs
print("Starting Selenium script...")

# Path to your ChromeDriver
driver_path = r"C:\Users\User\Desktop\Selenium_Py\chromedriver.exe"

if not os.path.exists(driver_path):
    raise FileNotFoundError(f"ChromeDriver not found at {driver_path}. Check the path!")

# Set up the Chrome WebDriver
try:
    print("Setting up Chrome WebDriver...")
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    print("Chrome WebDriver initialized successfully!")

    # Maximize the browser window
    print("Maximizing browser window...")
    driver.maximize_window()

except Exception as e:
    print(f"Error initializing Chrome WebDriver: {e}")
    raise

try:
    # Open Google
    print("Opening Google...")
    driver.get("https://www.google.com")

    # Locate the search box
    print("Locating search box...")
    search_box = driver.find_element(By.NAME, "q")
    print("Search box located!")

    # Type in the search term
    print("Typing search term...")
    search_box.send_keys("https://www.daraz.com.bd")
    search_box.send_keys(Keys.RETURN)

    # Wait for the results to load
    print("Waiting for results to load...")
    time.sleep(5)

    # Locate and click the first search result
    print("Clicking the first search result...")
    first_link = driver.find_element(By.XPATH, "(//h3)[1]/..")
    first_link.click()

    # Wait for the page to load
    time.sleep(5)

     # Locate the search box
    print("Locating search box...")
    search_box = driver.find_element(By.NAME, "q")  # Replace "q" with the actual `name` or `id` of the search box
    print("Search box located!")

    # Type the search term
    search_term = "iPhone 15"
    print(f"Typing search term: '{search_term}'")
    search_box.send_keys(search_term)

    # Simulate pressing Enter (or locate and click the search button)
    print("Initiating search...")
    search_box.send_keys(Keys.RETURN)  # Alternatively, you can locate and click a search button:
    # search_button = driver.find_element(By.XPATH, '//button[@type="submit"]')  # Example XPATH
    # search_button.click()

    # Wait for results to load
    time.sleep(5)

    # Click the first product link
    print("https://www.daraz.com.bd/products/iphone-15-pro-max-256gb512gb1tb-usa-lla-smartphone-i323700897.html")
    first_product_link.click()

    # # Scroll the webpage
    # print("Scrolling through the webpage...")
    # for i in range(5):  # Adjust the range for more or fewer scrolls
    #     driver.execute_script("window.scrollBy(0, 500);")  # Scroll down by 500 pixels
    #     time.sleep(1)  # Pause between scrolls for a smoother effect

    # Pause to observe the browser before closing
    print("Finished scrolling. Closing the browser...")
    time.sleep(2)

finally:
    # Close the browser
    print("Closing the browser...")
    driver.quit()


