from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up Firefox WebDriver
driver = webdriver.Firefox()

try:
    # Step 1: Open the login page
    driver.get("https://abrarragib.github.io/")  # Replace with actual URL
    driver.maximize_window()
    
    # Step 2: Locate and enter username
    username_field = driver.find_element(By.ID, "username")  # Update with actual element ID
    username_field.send_keys("testuser")  # Replace with valid username
    
    # Step 3: Locate and enter password
    password_field = driver.find_element(By.ID, "password")  # Update with actual element ID
    password_field.send_keys("testpassword")  # Replace with valid password
    
    # Step 4: Click the login button
    login_button = driver.find_element(By.ID, "loginBtn")  # Update with actual element ID
    login_button.click()
    
    # Step 5: Wait and verify redirection to dashboard
    time.sleep(3)  # Wait for page load
    expected_url = "https://example.com/dashboard"  # Update with actual expected URL
    assert driver.current_url == expected_url, "Login Failed!"
    
    print("Test Passed: Login Successful")

    # --- SCROLLING FIX ---

    # Method 1: Scroll to Bottom of Page
    print("Scrolling to the bottom of the page...")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Pause for better visibility

    # Method 2: Scroll to a Specific Element (Uncomment if needed)
    # element = driver.find_element(By.ID, "targetElementID")  # Replace with actual element ID
    # driver.execute_script("arguments[0].scrollIntoView();", element)
    # time.sleep(2)

    # Method 3: Scroll Using the PAGE_DOWN Key
    print("Scrolling down using PAGE_DOWN key...")
    body = driver.find_element(By.TAG_NAME, "body")
    for _ in range(3):  # Adjust range for more scrolling
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

    print("Scrolling completed.")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    # Step 7: Close the browser
    time.sleep(2)
    driver.quit()
 