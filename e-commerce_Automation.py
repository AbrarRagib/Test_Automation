from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import requests

# Debug logs
print("Starting Selenium script...")

# Path to your ChromeDriver
driver_path = r"C:\Users\User\Desktop\Selenium_Py\chromedriver.exe"

if not os.path.exists(driver_path):
    raise FileNotFoundError(f"ChromeDriver not found at {driver_path}. Check the path!")

# 2Captcha API key
CAPTCHA_API_KEY = 'your_2captcha_api_key'  # Replace with your actual 2Captcha API key

def solve_captcha(site_key, url):
    # Send request to 2Captcha to solve CAPTCHA
    response = requests.post("http://2captcha.com/in.php", data={
        'key': CAPTCHA_API_KEY,
        'method': 'userrecaptcha',
        'googlekey': site_key,
        'pageurl': url,
    })
    request_id = response.text.split('|')[1]

    # Check the status of the CAPTCHA solving
    while True:
        response = requests.get(f"http://2captcha.com/res.php?key={CAPTCHA_API_KEY}&action=get&id={request_id}")
        if response.text.startswith('OK'):
            captcha_code = response.text.split('|')[1]
            return captcha_code
        time.sleep(5)

try:
    print("Setting up Chrome WebDriver...")
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    print("Chrome WebDriver initialized successfully!")

    print("Maximizing browser window...")
    driver.maximize_window()

    print("Opening Google...")
    driver.get("https://www.google.com")

    print("Locating search box...")
    search_box = driver.find_element(By.NAME, "q")
    print("Search box located!")

    print("Typing search term...")
    search_box.send_keys("https://www.daraz.com.bd")
    search_box.send_keys(Keys.RETURN)

    print("Waiting for results to load...")
    time.sleep(5)

    print("Clicking the first search result...")
    first_link = driver.find_element(By.XPATH, "(//h3)[1]/..")
    first_link.click()

    time.sleep(5)

    print("Checking for CAPTCHA...")
    site_key = '1,472a5a324b4fbcaafb60c736a9741229'  # Replace with the site key of the CAPTCHA
    url = driver.current_url  # Use the current page URL
    captcha_solution = solve_captcha(site_key, url)
    if captcha_solution:
        print("CAPTCHA solved, proceeding...")
        # Inject the CAPTCHA response token into the page and submit
        driver.execute_script("document.getElementById('g-recaptcha-response').innerHTML = arguments[0];", captcha_solution)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit_button"))  # Replace with the actual submit button ID
        )
        submit_button.click()

        # Wait until CAPTCHA is no longer visible
        WebDriverWait(driver, 300).until_not(
            EC.presence_of_element_located((By.ID, "captcha"))  # Replace "captcha" with the actual ID/class if needed
        )

    else:
        print("Failed to solve CAPTCHA.")

    print("No CAPTCHA detected, proceeding...")

    print("Locating search box on Daraz...")
    search_box = driver.find_element(By.NAME, "q")  # Replace with correct `name` or `id`
    print("Search box located!")

    search_term = "iPhone 15"
    print(f"Typing search term: '{search_term}'")
    search_box.send_keys(search_term)

    print("Initiating search...")
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)

    print("Clicking the first product link...")
    first_product_link = driver.find_element(By.XPATH, "(//a[contains(@href, 'iphone-15')])[1]")  # Update with correct XPath
    first_product_link.click()

    print("Finished browsing. Closing the browser...")
    time.sleep(2)

finally:
    print("Closing the browser...")
    driver.quit()
