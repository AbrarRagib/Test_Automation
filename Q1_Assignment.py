import os
import time
import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

def get_google_suggestions(keyword, driver):
    """
    Searches a keyword on Google and extracts the longest and shortest autocomplete suggestions.
    """
    driver.get("https://www.google.com")

    try:
        # Wait for search box to appear
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys(keyword)

        # Wait for suggestions
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ul[role='listbox'] li span"))
        )

        # Extract suggestions
        suggestions = driver.find_elements(By.CSS_SELECTOR, "ul[role='listbox'] li span")
        options = [s.text for s in suggestions if s.text.strip()]

        if options:
            longest = max(options, key=len)
            shortest = min(options, key=len)
        else:
            longest = shortest = "No Suggestions"

    except Exception as e:
        print(f"Error fetching suggestions for '{keyword}': {e}")
        longest = shortest = "Error"

    return longest, shortest

def main():
    """
    Reads an Excel file, searches Google for keyword suggestions, and updates the Excel file with results.
    """
    # Path to the Excel file (Update this based on your file location)
    excel_file = r"C:\Users\User\Desktop\Selenium_Py\sample.xlsx"

    # Verify file exists
    if not os.path.exists(excel_file):
        print(f"Error: File not found at {excel_file}")
        return

    try:
        # Read all sheets from the Excel file
        df_dict = pd.read_excel(excel_file, sheet_name=None, engine="openpyxl")
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return

    # Get today's day
    today = datetime.datetime.today().strftime("%A")  # e.g., "Monday"

    # Check if today's sheet exists
    if today not in df_dict:
        print(f"No sheet found for {today}")
        return

    df = df_dict[today]  # Load today's sheet

    if df.empty:
        print("The sheet is empty, no keywords to process.")
        return

    # Initialize Selenium WebDriver
    options = Options()
    options.headless = False  # Set to True for headless mode (No GUI)
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

    results = []
    
    try:
        for index, row in df.iterrows():
            if len(row) < 2 or pd.isna(row.iloc[1]):  # Ensure there's a keyword
                print(f"Skipping row {index}: No valid keyword found.")
                continue
            
            keyword = str(row.iloc[1]).strip()
            print(f"Searching for: {keyword}")
            longest, shortest = get_google_suggestions(keyword, driver)
            results.append([keyword, longest, shortest])

    except Exception as e:
        print(f"Error during Selenium automation: {e}")

    finally:
        driver.quit()  # Ensure the browser is closed

    if results:
        # Save results back to the Excel file
        with pd.ExcelWriter(excel_file, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            result_df = pd.DataFrame(results, columns=["Keyword", "Longest Option", "Shortest Option"])
            result_df.to_excel(writer, sheet_name=today, index=False)

        print(f"Process completed. Results saved to {excel_file}")

if __name__ == "__main__":
    main()
