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
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def scrape_data(url):
    # Manually set Chromium and ChromeDriver paths
    chromium_path = "/usr/bin/chromium"
    chromedriver_path = "/usr/bin/chromedriver"

    # Ensure the paths agree with your environment
    if not os.path.exists(chromium_path):
        raise FileNotFoundError(f"Chromium binary not found at {chromium_path}.")
    if not os.path.exists(chromedriver_path):
        raise FileNotFoundError(f"ChromeDriver binary not found at {chromedriver_path}.")

    # Set Chrome options
    options = Options()
    options.add_argument('--headless')  # Required for running in a server environment
    options.add_argument('--no-sandbox')  # Required for running as root in Docker
    options.add_argument('--disable-dev-shm-usage')  # Prevent shared memory issues
    options.binary_location = chromium_path

    # Use the manually set path for ChromeDriver
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Navigate to the URL
        driver.get(url)

        # Extract the page title as an example
        title = driver.title
        return {"title": title}
    finally:
        driver.quit()



