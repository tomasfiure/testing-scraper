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
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def scrape_data(url):
    # Set Chrome options
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Dynamically install ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Navigate to the URL
        driver.get(url)

        # Example: Extract the title of the page
        title = driver.title
        return {"title": title}
    finally:
        # Close the browser
        driver.quit()
