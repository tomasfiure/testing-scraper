# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By

# def scrape_data(url):
#     # Set Chrome options
#     options = Options()
#     options.add_argument('--headless')
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')

#     # Initialize WebDriver
#     driver = webdriver.Chrome(options=options)
    
#     try:
#         driver.get(url)
#         # Example: Extract title of the webpage
#         title = driver.title
#         return {"title": title}
#     finally:
#         driver.quit()
import os
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import subprocess
print("Chromium Version:")
print(subprocess.run(["chromium", "--version"], capture_output=True, text=True).stdout)
print("ChromeDriver Version:")
print(subprocess.run(["chromedriver", "--version"], capture_output=True, text=True).stdout)

def scrape_data(url):
    # Dynamically find Chromium binary from the environment
    chromium_path = os.getenv("CHROME_BIN") or shutil.which("chromium") or shutil.which("chromium-browser")

    if not chromium_path:
        raise FileNotFoundError("Chromium binary not found. Make sure Chromium is installed.")

    # Set Chrome options
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.binary_location = chromium_path  # Use the detected path for Chromium

    # Dynamically install ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Navigate to the URL
        driver.get(url)

        # Example: Extract the page title
        title = driver.title
        return {"title": title}
    finally:
        driver.quit()


