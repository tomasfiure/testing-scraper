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
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def scrape_data(url):
    # Dynamically find Chromium binary
    chromium_path = shutil.which("chromium") or shutil.which("chromium-browser")

    if not chromium_path:
        raise FileNotFoundError("Chromium binary not found. Make sure Chromium is installed.")

    # Set Chrome options
    options = Options()
    options.add_argument('--headless')  # Required for Cloud Run
    options.add_argument('--no-sandbox')  # Required for Chrome to work in container
    options.add_argument('--disable-dev-shm-usage')  # Prevent /dev/shm errors
    options.binary_location = chromium_path

    # Dynamically install ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Navigate to the URL
        driver.get(url)

        # Extract the page title as an example
        title = driver.title
        return {"title": title}
    finally:
        driver.quit()

