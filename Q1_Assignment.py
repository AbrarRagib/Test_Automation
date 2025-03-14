import time
import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

def get_google_suggestions(keyword, driver):
    driver.get("https://www.google.com")
    time.sleep(2)
    
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(keyword)
    time.sleep(2)  # Wait for autocomplete suggestions
    
    suggestions = driver.find_elements(By.CSS_SELECTOR, "ul[role='listbox'] li span")
    
    options = [s.text for s in suggestions if s.text.strip()]
    if options:
        longest = max(options, key=len)
        shortest = min(options, key=len)
    else:
        longest = shortest = "No Suggestions"
    
    return longest, shortest

def main():
    # Load the Excel file
    excel_file = "sample.xlsx"  # Change this to your actual file path
    df_dict = pd.read_excel(excel_file, sheet_name=None)
    
    # Get today's day
    today = datetime.datetime.today().strftime("%A")  # e.g., "Monday"
    
    # Check if today's sheet exists
    if today not in df_dict:
        print(f"No sheet found for {today}")
        return
    
    df = df_dict[today]  # Load today's sheet
    
    # Initialize Selenium WebDriver
    options = Options()
    options.headless = False  # Set to True for headless mode
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    
    # Process keywords
    results = []
    for index, row in df.iterrows():
        keyword = row.iloc[1]  # Assuming keyword is in the second column
        print(f"Searching for: {keyword}")
        longest, shortest = get_google_suggestions(keyword, driver)
        results.append([keyword, longest, shortest])
    
    driver.quit()
    
    # Save results back to the Excel file
    result_df = pd.DataFrame(results, columns=["Keyword", "Longest Option", "Shortest Option"])
    with pd.ExcelWriter(excel_file, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
        result_df.to_excel(writer, sheet_name=today, index=False)
    
    print("Process completed. Results saved to Excel.")

if __name__ == "__main__":
    main()
