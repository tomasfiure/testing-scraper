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
from webdriver_manager.chrome import ChromeDriverManager

def scrape_data(url):
    # Configure Chrome options
    options = Options()
    options.add_argument("--headless")  # Required for running in a server environment
    options.add_argument("--no-sandbox")  # Required for running as root in Docker
    options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues
    options.binary_location = "/usr/bin/chromium"  # Path to Chromium binary

    # Dynamically download ChromeDriver binary at runtime
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        return {"title": driver.title}
    finally:
        driver.quit()



