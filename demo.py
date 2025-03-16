import os
import pandas as pd

# Define the file path
excel_file = r"C:\Users\User\Desktop\Selenium_Py\sample.xls"  # Ensure this is correct

# Check if the file exists before reading
if not os.path.exists(excel_file):
    print(f"Error: File not found at {excel_file}")
else:
    try:
        df_dict = pd.read_excel(excel_file, sheet_name=None, engine="xlrd")
        print("Excel file loaded successfully!")
    except Exception as e:
        print(f"Error reading Excel file: {e}")
