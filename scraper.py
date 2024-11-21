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
import stat
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def set_chromedriver_executable_permissions(driver_path):
    """
    Ensures the ChromeDriver binary has executable permissions.
    """
    st = os.stat(driver_path)
    os.chmod(driver_path, st.st_mode | stat.S_IEXEC)

def scrape_data(url):
    """
    Scrapes the given URL using Selenium with dynamically downloaded ChromeDriver.
    """
    # Path to Chromium binary
    chromium_path = "/usr/bin/chromium"

    # Verify Chromium binary exists
    # if not os.path.exists(chromium_path):
    #     raise FileNotFoundError(f"Chromium binary not found at {chromium_path}.")

    # Configure Chrome options
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")  # Required for running as root in Docker
    options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues
    options.binary_location = chromium_path

    # Dynamically download ChromeDriver and ensure it is executable
    chromedriver_path = ChromeDriverManager().install()
    set_chromedriver_executable_permissions(chromedriver_path)

    # Initialize WebDriver
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
        
# def scrape_data(url):
#     # Configure Chrome options
#     options = Options()
#     options.add_argument("--headless")  # Required for running in a server environment
#     options.add_argument("--no-sandbox")  # Required for running as root in Docker
#     options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues
#     options.binary_location = "/usr/bin/chromium"  # Path to Chromium binary

#     # Dynamically download ChromeDriver binary at runtime
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=options)

#     try:
#         driver.get(url)
#         return {"title": driver.title}
#     finally:
#         driver.quit()
    



